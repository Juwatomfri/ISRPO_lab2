#!/usr/bin/env python3
import logging
from logging.handlers import HTTPHandler
import requests
import connexion
from flask import Flask, Response, request
from prometheus_client import Counter, Histogram, generate_latest
import time
from swagger_server import encoder
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
import random, time

# Конфигурация логирования для Loki
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.INFO)

# Настройка логирования для отправки в Loki
class LokiHandler(HTTPHandler):
    def __init__(self, url):
        self.url = url
        super().__init__(host='', url=url, method='POST')

    def emit(self, record):
        log_entry = self.format(record)
        payload = {
            "streams": [
                {
                    "stream": {"job": "flask-api", "level": record.levelname},
                    "values": [[str(int(time.time() * 1000000000)), log_entry]]
                }
            ]
        }
        try:
            response = requests.post(self.url, json=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            app.app.logger.error(f"Failed to send log entry to Loki: {e}")

# Указываем URL Loki для отправки логов
loki_url = "http://loki:3100/loki/api/v1/push"

# Добавляем кастомный хендлер для отправки логов в Loki
loki_handler = LokiHandler(loki_url)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
loki_handler.setFormatter(formatter)
loki_handler.setLevel(logging.INFO)
# log.addHandler(loki_handler)

# Инициализация метрик
REQUEST_COUNT = Counter('request_count', 'Количество запросов', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Время обработки запроса', ['method', 'endpoint'])

# Создаем приложение с использованием connexion
app = connexion.App(__name__, specification_dir='./swagger/')

# Инициализация Flask (будет доступен через app.app)
flask_app = app.app
flask_app.logger.addHandler(loki_handler)

# Определяем поведение перед и после запроса
@flask_app.before_request
def start_timer():
    request.start_time = time.time()

@flask_app.after_request
def record_metrics(response):
    # Запись времени обработки запроса
    latency = time.time() - request.start_time
    REQUEST_LATENCY.labels(request.method, request.path).observe(latency)
    
    # Увеличение счетчика запросов
    REQUEST_COUNT.labels(request.method, request.path).inc()
    flask_app.logger.info(f"Request {request.method} to {request.path} succeeded with status {response.status_code}")
    return response

# Эндпоинт для метрик
@flask_app.route('/v1/ui/metrics', methods=['GET'])
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

# Пример маршрута для демонстрации
@flask_app.route('/v1/ui/metrics')
def example():
    return {"message": "Hello, World!"}

# Настройка OpenTelemetry
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer_provider().get_tracer(__name__)


# Экспорт трейсов в Tempo через OTLP
otlp_exporter = OTLPSpanExporter(
    endpoint="http://tempo:4317",  # Порт и адрес контейнера Tempo
    insecure=True
)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Инструментируем Flask
FlaskInstrumentor().instrument_app(flask_app)

@app.route("/trace-example")
def trace_example():
    with tracer.start_as_current_span("example-span"):
        time.sleep(random.uniform(0.1, 0.5))
        return "Trace example!"
    
@app.route("/error")
def error_route():
    with tracer.start_as_current_span("example-span", attributes={"service.name": "flask-api"}) as span:
        try:
            # Генерация случайной ошибки
            if random.random() > 0.5:
                raise ValueError("Random error occurred")
        except Exception as e:
            span.set_status(trace.Status(trace.StatusCode.ERROR, str(e)))
            span.record_exception(e)
            return "Error occurred!", 500
    return "No error!", 200

def main():
    # Настройка Swagger через connexion
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Library App API'}, pythonic_params=True)

    # Запуск сервера
    app.run(port=8080)


if __name__ == '__main__':
    print(flask_app.url_map)  # Проверка зарегистрированных маршрутов
    main()
