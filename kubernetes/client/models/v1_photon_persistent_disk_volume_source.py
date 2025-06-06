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


class V1PhotonPersistentDiskVolumeSource(object):
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
        'fs_type': 'str',
        'pd_id': 'str'
    }

    attribute_map = {
        'fs_type': 'fsType',
        'pd_id': 'pdID'
    }

    def __init__(self, fs_type=None, pd_id=None, local_vars_configuration=None):  # noqa: E501
        """V1PhotonPersistentDiskVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fs_type = None
        self._pd_id = None
        self.discriminator = None

        if fs_type is not None:
            self.fs_type = fs_type
        self.pd_id = pd_id

    @property
    def fs_type(self):
        """Gets the fs_type of this V1PhotonPersistentDiskVolumeSource.  # noqa: E501

        fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.  # noqa: E501

        :return: The fs_type of this V1PhotonPersistentDiskVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this V1PhotonPersistentDiskVolumeSource.

        fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.  # noqa: E501

        :param fs_type: The fs_type of this V1PhotonPersistentDiskVolumeSource.  # noqa: E501
        :type: str
        """

        self._fs_type = fs_type

    @property
    def pd_id(self):
        """Gets the pd_id of this V1PhotonPersistentDiskVolumeSource.  # noqa: E501

        pdID is the ID that identifies Photon Controller persistent disk  # noqa: E501

        :return: The pd_id of this V1PhotonPersistentDiskVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._pd_id

    @pd_id.setter
    def pd_id(self, pd_id):
        """Sets the pd_id of this V1PhotonPersistentDiskVolumeSource.

        pdID is the ID that identifies Photon Controller persistent disk  # noqa: E501

        :param pd_id: The pd_id of this V1PhotonPersistentDiskVolumeSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pd_id is None:  # noqa: E501
            raise ValueError("Invalid value for `pd_id`, must not be `None`")  # noqa: E501

        self._pd_id = pd_id

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
        if not isinstance(other, V1PhotonPersistentDiskVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PhotonPersistentDiskVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
