# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.33
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1beta2DeviceAttribute(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'bool': 'bool',
        'int': 'int',
        'string': 'str',
        'version': 'str'
    }

    attribute_map = {
        'bool': 'bool',
        'int': 'int',
        'string': 'string',
        'version': 'version'
    }

    def __init__(self, bool=None, int=None, string=None, version=None, local_vars_configuration=None):  # noqa: E501
        """V1beta2DeviceAttribute - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bool = None
        self._int = None
        self._string = None
        self._version = None
        self.discriminator = None

        if bool is not None:
            self.bool = bool
        if int is not None:
            self.int = int
        if string is not None:
            self.string = string
        if version is not None:
            self.version = version

    @property
    def bool(self):
        """Gets the bool of this V1beta2DeviceAttribute.  # noqa: E501

        BoolValue is a true/false value.  # noqa: E501

        :return: The bool of this V1beta2DeviceAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._bool

    @bool.setter
    def bool(self, bool):
        """Sets the bool of this V1beta2DeviceAttribute.

        BoolValue is a true/false value.  # noqa: E501

        :param bool: The bool of this V1beta2DeviceAttribute.  # noqa: E501
        :type: bool
        """

        self._bool = bool

    @property
    def int(self):
        """Gets the int of this V1beta2DeviceAttribute.  # noqa: E501

        IntValue is a number.  # noqa: E501

        :return: The int of this V1beta2DeviceAttribute.  # noqa: E501
        :rtype: int
        """
        return self._int

    @int.setter
    def int(self, int):
        """Sets the int of this V1beta2DeviceAttribute.

        IntValue is a number.  # noqa: E501

        :param int: The int of this V1beta2DeviceAttribute.  # noqa: E501
        :type: int
        """

        self._int = int

    @property
    def string(self):
        """Gets the string of this V1beta2DeviceAttribute.  # noqa: E501

        StringValue is a string. Must not be longer than 64 characters.  # noqa: E501

        :return: The string of this V1beta2DeviceAttribute.  # noqa: E501
        :rtype: str
        """
        return self._string

    @string.setter
    def string(self, string):
        """Sets the string of this V1beta2DeviceAttribute.

        StringValue is a string. Must not be longer than 64 characters.  # noqa: E501

        :param string: The string of this V1beta2DeviceAttribute.  # noqa: E501
        :type: str
        """

        self._string = string

    @property
    def version(self):
        """Gets the version of this V1beta2DeviceAttribute.  # noqa: E501

        VersionValue is a semantic version according to semver.org spec 2.0.0. Must not be longer than 64 characters.  # noqa: E501

        :return: The version of this V1beta2DeviceAttribute.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1beta2DeviceAttribute.

        VersionValue is a semantic version according to semver.org spec 2.0.0. Must not be longer than 64 characters.  # noqa: E501

        :param version: The version of this V1beta2DeviceAttribute.  # noqa: E501
        :type: str
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta2DeviceAttribute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta2DeviceAttribute):
            return True

        return self.to_dict() != other.to_dict()
