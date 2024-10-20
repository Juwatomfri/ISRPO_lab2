# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.book import Book  # noqa: E501
from swagger_server.models.book_input import BookInput  # noqa: E501
from swagger_server.models.loan import Loan  # noqa: E501
from swagger_server.models.loan_input import LoanInput  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_input import UserInput  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_books_get(self):
        """Test case for books_get

        Get a list of books
        """
        response = self.client.open(
            '/v1/books',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_id_delete(self):
        """Test case for books_id_delete

        Delete a book
        """
        response = self.client.open(
            '/v1/books/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_id_get(self):
        """Test case for books_id_get

        Get a book by ID
        """
        response = self.client.open(
            '/v1/books/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_id_put(self):
        """Test case for books_id_put

        Update a book
        """
        body = BookInput()
        response = self.client.open(
            '/v1/books/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_post(self):
        """Test case for books_post

        Add a new book
        """
        body = BookInput()
        response = self.client.open(
            '/v1/books',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rental_get(self):
        """Test case for rental_get

        Get a list of rental
        """
        response = self.client.open(
            '/v1/rental',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rental_id_delete(self):
        """Test case for rental_id_delete

        Delete a loan
        """
        response = self.client.open(
            '/v1/rental/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rental_id_get(self):
        """Test case for rental_id_get

        Get a loan by ID
        """
        response = self.client.open(
            '/v1/rental/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rental_id_put(self):
        """Test case for rental_id_put

        Update a loan
        """
        body = LoanInput()
        response = self.client.open(
            '/v1/rental/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rental_post(self):
        """Test case for rental_post

        Create a new loan
        """
        body = LoanInput()
        response = self.client.open(
            '/v1/rental',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_get(self):
        """Test case for users_get

        Get a list of users
        """
        response = self.client.open(
            '/v1/users',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_id_delete(self):
        """Test case for users_id_delete

        Delete a user
        """
        response = self.client.open(
            '/v1/users/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_id_get(self):
        """Test case for users_id_get

        Get a user by ID
        """
        response = self.client.open(
            '/v1/users/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_id_put(self):
        """Test case for users_id_put

        Update a user
        """
        body = UserInput()
        response = self.client.open(
            '/v1/users/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_post(self):
        """Test case for users_post

        Register a new user
        """
        body = UserInput()
        response = self.client.open(
            '/v1/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
