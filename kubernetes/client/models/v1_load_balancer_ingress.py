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


class V1LoadBalancerIngress(object):
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
        'hostname': 'str',
        'ip': 'str',
        'ip_mode': 'str',
        'ports': 'list[V1PortStatus]'
    }

    attribute_map = {
        'hostname': 'hostname',
        'ip': 'ip',
        'ip_mode': 'ipMode',
        'ports': 'ports'
    }

    def __init__(self, hostname=None, ip=None, ip_mode=None, ports=None, local_vars_configuration=None):  # noqa: E501
        """V1LoadBalancerIngress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hostname = None
        self._ip = None
        self._ip_mode = None
        self._ports = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        if ip is not None:
            self.ip = ip
        if ip_mode is not None:
            self.ip_mode = ip_mode
        if ports is not None:
            self.ports = ports

    @property
    def hostname(self):
        """Gets the hostname of this V1LoadBalancerIngress.  # noqa: E501

        Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers)  # noqa: E501

        :return: The hostname of this V1LoadBalancerIngress.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this V1LoadBalancerIngress.

        Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers)  # noqa: E501

        :param hostname: The hostname of this V1LoadBalancerIngress.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def ip(self):
        """Gets the ip of this V1LoadBalancerIngress.  # noqa: E501

        IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers)  # noqa: E501

        :return: The ip of this V1LoadBalancerIngress.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this V1LoadBalancerIngress.

        IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers)  # noqa: E501

        :param ip: The ip of this V1LoadBalancerIngress.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def ip_mode(self):
        """Gets the ip_mode of this V1LoadBalancerIngress.  # noqa: E501

        IPMode specifies how the load-balancer IP behaves, and may only be specified when the ip field is specified. Setting this to \"VIP\" indicates that traffic is delivered to the node with the destination set to the load-balancer's IP and port. Setting this to \"Proxy\" indicates that traffic is delivered to the node or pod with the destination set to the node's IP and node port or the pod's IP and port. Service implementations may use this information to adjust traffic routing.  # noqa: E501

        :return: The ip_mode of this V1LoadBalancerIngress.  # noqa: E501
        :rtype: str
        """
        return self._ip_mode

    @ip_mode.setter
    def ip_mode(self, ip_mode):
        """Sets the ip_mode of this V1LoadBalancerIngress.

        IPMode specifies how the load-balancer IP behaves, and may only be specified when the ip field is specified. Setting this to \"VIP\" indicates that traffic is delivered to the node with the destination set to the load-balancer's IP and port. Setting this to \"Proxy\" indicates that traffic is delivered to the node or pod with the destination set to the node's IP and node port or the pod's IP and port. Service implementations may use this information to adjust traffic routing.  # noqa: E501

        :param ip_mode: The ip_mode of this V1LoadBalancerIngress.  # noqa: E501
        :type: str
        """

        self._ip_mode = ip_mode

    @property
    def ports(self):
        """Gets the ports of this V1LoadBalancerIngress.  # noqa: E501

        Ports is a list of records of service ports If used, every port defined in the service should have an entry in it  # noqa: E501

        :return: The ports of this V1LoadBalancerIngress.  # noqa: E501
        :rtype: list[V1PortStatus]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this V1LoadBalancerIngress.

        Ports is a list of records of service ports If used, every port defined in the service should have an entry in it  # noqa: E501

        :param ports: The ports of this V1LoadBalancerIngress.  # noqa: E501
        :type: list[V1PortStatus]
        """

        self._ports = ports

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
        if not isinstance(other, V1LoadBalancerIngress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1LoadBalancerIngress):
            return True

        return self.to_dict() != other.to_dict()
