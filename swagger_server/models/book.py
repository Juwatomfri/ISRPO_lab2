# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Book(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, title: str=None, author: str=None, isbn: str=None, publication_year: int=None, copies_available: int=None):  # noqa: E501
        """Book - a model defined in Swagger

        :param id: The id of this Book.  # noqa: E501
        :type id: str
        :param title: The title of this Book.  # noqa: E501
        :type title: str
        :param author: The author of this Book.  # noqa: E501
        :type author: str
        :param isbn: The isbn of this Book.  # noqa: E501
        :type isbn: str
        :param publication_year: The publication_year of this Book.  # noqa: E501
        :type publication_year: int
        :param copies_available: The copies_available of this Book.  # noqa: E501
        :type copies_available: int
        """
        self.swagger_types = {
            'id': str,
            'title': str,
            'author': str,
            'isbn': str,
            'publication_year': int,
            'copies_available': int
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'author': 'author',
            'isbn': 'isbn',
            'publication_year': 'publicationYear',
            'copies_available': 'copiesAvailable'
        }
        self._id = id
        self._title = title
        self._author = author
        self._isbn = isbn
        self._publication_year = publication_year
        self._copies_available = copies_available

    @classmethod
    def from_dict(cls, dikt) -> 'Book':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Book of this Book.  # noqa: E501
        :rtype: Book
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Book.

        Unique identifier for the book  # noqa: E501

        :return: The id of this Book.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Book.

        Unique identifier for the book  # noqa: E501

        :param id: The id of this Book.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self) -> str:
        """Gets the title of this Book.

        Title of the book  # noqa: E501

        :return: The title of this Book.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Book.

        Title of the book  # noqa: E501

        :param title: The title of this Book.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def author(self) -> str:
        """Gets the author of this Book.

        Author of the book  # noqa: E501

        :return: The author of this Book.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author: str):
        """Sets the author of this Book.

        Author of the book  # noqa: E501

        :param author: The author of this Book.
        :type author: str
        """
        if author is None:
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501

        self._author = author

    @property
    def isbn(self) -> str:
        """Gets the isbn of this Book.

        ISBN number of the book  # noqa: E501

        :return: The isbn of this Book.
        :rtype: str
        """
        return self._isbn

    @isbn.setter
    def isbn(self, isbn: str):
        """Sets the isbn of this Book.

        ISBN number of the book  # noqa: E501

        :param isbn: The isbn of this Book.
        :type isbn: str
        """
        if isbn is None:
            raise ValueError("Invalid value for `isbn`, must not be `None`")  # noqa: E501

        self._isbn = isbn

    @property
    def publication_year(self) -> int:
        """Gets the publication_year of this Book.

        Year the book was published  # noqa: E501

        :return: The publication_year of this Book.
        :rtype: int
        """
        return self._publication_year

    @publication_year.setter
    def publication_year(self, publication_year: int):
        """Sets the publication_year of this Book.

        Year the book was published  # noqa: E501

        :param publication_year: The publication_year of this Book.
        :type publication_year: int
        """

        self._publication_year = publication_year

    @property
    def copies_available(self) -> int:
        """Gets the copies_available of this Book.

        Number of copies available for loan  # noqa: E501

        :return: The copies_available of this Book.
        :rtype: int
        """
        return self._copies_available

    @copies_available.setter
    def copies_available(self, copies_available: int):
        """Sets the copies_available of this Book.

        Number of copies available for loan  # noqa: E501

        :param copies_available: The copies_available of this Book.
        :type copies_available: int
        """
        if copies_available is None:
            raise ValueError("Invalid value for `copies_available`, must not be `None`")  # noqa: E501

        self._copies_available = copies_available