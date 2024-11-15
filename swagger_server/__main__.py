#!/usr/bin/env python3

import connexion
from flask import Flask, Response, request
from prometheus_client import Counter, Histogram, generate_latest
import time
from swagger_server import encoder

# Инициализация метрик
REQUEST_COUNT = Counter('request_count', 'Количество запросов', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Время обработки запроса', ['method', 'endpoint'])

# Создаем приложение с использованием connexion
app = connexion.App(__name__, specification_dir='./swagger/')

# Инициализация Flask (будет доступен через app.app)
flask_app = app.app

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
    
    return response

# Эндпоинт для метрик
@flask_app.route('/v1/ui/metrics', methods=['GET'])
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

# Пример маршрута для демонстрации
@flask_app.route('/api/example')
def example():
    return {"message": "Hello, World!"}

def main():
    # Настройка Swagger через connexion
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Library App API'}, pythonic_params=True)

    # Запуск сервера
    app.run(port=8080)


if __name__ == '__main__':
    print(flask_app.url_map)  # Проверка зарегистрированных маршрутов
    main()
