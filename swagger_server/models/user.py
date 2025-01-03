# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None, phone_number: str=None, membership_date: date=None):  # noqa: E501
        """User - a model defined in Swagger

        :param id: The id of this User.  # noqa: E501
        :type id: str
        :param name: The name of this User.  # noqa: E501
        :type name: str
        :param phone_number: The phone_number of this User.  # noqa: E501
        :type phone_number: str
        :param membership_date: The membership_date of this User.  # noqa: E501
        :type membership_date: date
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'phone_number': str,
            'membership_date': date
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'phone_number': 'phoneNumber',
            'membership_date': 'membershipDate'
        }
        self._id = id
        self._name = name
        self._phone_number = phone_number
        self._membership_date = membership_date

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this User.

        Unique identifier for the user  # noqa: E501

        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this User.

        Unique identifier for the user  # noqa: E501

        :param id: The id of this User.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this User.

        Full name of the user  # noqa: E501

        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this User.

        Full name of the user  # noqa: E501

        :param name: The name of this User.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def phone_number(self) -> str:
        """Gets the phone_number of this User.

        User's phoneNumber  # noqa: E501

        :return: The phone_number of this User.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str):
        """Sets the phone_number of this User.

        User's phoneNumber  # noqa: E501

        :param phone_number: The phone_number of this User.
        :type phone_number: str
        """
        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def membership_date(self) -> date:
        """Gets the membership_date of this User.

        Date when the user registered  # noqa: E501

        :return: The membership_date of this User.
        :rtype: date
        """
        return self._membership_date

    @membership_date.setter
    def membership_date(self, membership_date: date):
        """Sets the membership_date of this User.

        Date when the user registered  # noqa: E501

        :param membership_date: The membership_date of this User.
        :type membership_date: date
        """

        self._membership_date = membership_date
