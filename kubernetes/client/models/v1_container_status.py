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


class V1ContainerStatus(object):
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
        'allocated_resources': 'dict(str, str)',
        'allocated_resources_status': 'list[V1ResourceStatus]',
        'container_id': 'str',
        'image': 'str',
        'image_id': 'str',
        'last_state': 'V1ContainerState',
        'name': 'str',
        'ready': 'bool',
        'resources': 'V1ResourceRequirements',
        'restart_count': 'int',
        'started': 'bool',
        'state': 'V1ContainerState',
        'stop_signal': 'str',
        'user': 'V1ContainerUser',
        'volume_mounts': 'list[V1VolumeMountStatus]'
    }

    attribute_map = {
        'allocated_resources': 'allocatedResources',
        'allocated_resources_status': 'allocatedResourcesStatus',
        'container_id': 'containerID',
        'image': 'image',
        'image_id': 'imageID',
        'last_state': 'lastState',
        'name': 'name',
        'ready': 'ready',
        'resources': 'resources',
        'restart_count': 'restartCount',
        'started': 'started',
        'state': 'state',
        'stop_signal': 'stopSignal',
        'user': 'user',
        'volume_mounts': 'volumeMounts'
    }

    def __init__(self, allocated_resources=None, allocated_resources_status=None, container_id=None, image=None, image_id=None, last_state=None, name=None, ready=None, resources=None, restart_count=None, started=None, state=None, stop_signal=None, user=None, volume_mounts=None, local_vars_configuration=None):  # noqa: E501
        """V1ContainerStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allocated_resources = None
        self._allocated_resources_status = None
        self._container_id = None
        self._image = None
        self._image_id = None
        self._last_state = None
        self._name = None
        self._ready = None
        self._resources = None
        self._restart_count = None
        self._started = None
        self._state = None
        self._stop_signal = None
        self._user = None
        self._volume_mounts = None
        self.discriminator = None

        if allocated_resources is not None:
            self.allocated_resources = allocated_resources
        if allocated_resources_status is not None:
            self.allocated_resources_status = allocated_resources_status
        if container_id is not None:
            self.container_id = container_id
        self.image = image
        self.image_id = image_id
        if last_state is not None:
            self.last_state = last_state
        self.name = name
        self.ready = ready
        if resources is not None:
            self.resources = resources
        self.restart_count = restart_count
        if started is not None:
            self.started = started
        if state is not None:
            self.state = state
        if stop_signal is not None:
            self.stop_signal = stop_signal
        if user is not None:
            self.user = user
        if volume_mounts is not None:
            self.volume_mounts = volume_mounts

    @property
    def allocated_resources(self):
        """Gets the allocated_resources of this V1ContainerStatus.  # noqa: E501

        AllocatedResources represents the compute resources allocated for this container by the node. Kubelet sets this value to Container.Resources.Requests upon successful pod admission and after successfully admitting desired pod resize.  # noqa: E501

        :return: The allocated_resources of this V1ContainerStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._allocated_resources

    @allocated_resources.setter
    def allocated_resources(self, allocated_resources):
        """Sets the allocated_resources of this V1ContainerStatus.

        AllocatedResources represents the compute resources allocated for this container by the node. Kubelet sets this value to Container.Resources.Requests upon successful pod admission and after successfully admitting desired pod resize.  # noqa: E501

        :param allocated_resources: The allocated_resources of this V1ContainerStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._allocated_resources = allocated_resources

    @property
    def allocated_resources_status(self):
        """Gets the allocated_resources_status of this V1ContainerStatus.  # noqa: E501

        AllocatedResourcesStatus represents the status of various resources allocated for this Pod.  # noqa: E501

        :return: The allocated_resources_status of this V1ContainerStatus.  # noqa: E501
        :rtype: list[V1ResourceStatus]
        """
        return self._allocated_resources_status

    @allocated_resources_status.setter
    def allocated_resources_status(self, allocated_resources_status):
        """Sets the allocated_resources_status of this V1ContainerStatus.

        AllocatedResourcesStatus represents the status of various resources allocated for this Pod.  # noqa: E501

        :param allocated_resources_status: The allocated_resources_status of this V1ContainerStatus.  # noqa: E501
        :type: list[V1ResourceStatus]
        """

        self._allocated_resources_status = allocated_resources_status

    @property
    def container_id(self):
        """Gets the container_id of this V1ContainerStatus.  # noqa: E501

        ContainerID is the ID of the container in the format '<type>://<container_id>'. Where type is a container runtime identifier, returned from Version call of CRI API (for example \"containerd\").  # noqa: E501

        :return: The container_id of this V1ContainerStatus.  # noqa: E501
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this V1ContainerStatus.

        ContainerID is the ID of the container in the format '<type>://<container_id>'. Where type is a container runtime identifier, returned from Version call of CRI API (for example \"containerd\").  # noqa: E501

        :param container_id: The container_id of this V1ContainerStatus.  # noqa: E501
        :type: str
        """

        self._container_id = container_id

    @property
    def image(self):
        """Gets the image of this V1ContainerStatus.  # noqa: E501

        Image is the name of container image that the container is running. The container image may not match the image used in the PodSpec, as it may have been resolved by the runtime. More info: https://kubernetes.io/docs/concepts/containers/images.  # noqa: E501

        :return: The image of this V1ContainerStatus.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this V1ContainerStatus.

        Image is the name of container image that the container is running. The container image may not match the image used in the PodSpec, as it may have been resolved by the runtime. More info: https://kubernetes.io/docs/concepts/containers/images.  # noqa: E501

        :param image: The image of this V1ContainerStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and image is None:  # noqa: E501
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def image_id(self):
        """Gets the image_id of this V1ContainerStatus.  # noqa: E501

        ImageID is the image ID of the container's image. The image ID may not match the image ID of the image used in the PodSpec, as it may have been resolved by the runtime.  # noqa: E501

        :return: The image_id of this V1ContainerStatus.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this V1ContainerStatus.

        ImageID is the image ID of the container's image. The image ID may not match the image ID of the image used in the PodSpec, as it may have been resolved by the runtime.  # noqa: E501

        :param image_id: The image_id of this V1ContainerStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and image_id is None:  # noqa: E501
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def last_state(self):
        """Gets the last_state of this V1ContainerStatus.  # noqa: E501


        :return: The last_state of this V1ContainerStatus.  # noqa: E501
        :rtype: V1ContainerState
        """
        return self._last_state

    @last_state.setter
    def last_state(self, last_state):
        """Sets the last_state of this V1ContainerStatus.


        :param last_state: The last_state of this V1ContainerStatus.  # noqa: E501
        :type: V1ContainerState
        """

        self._last_state = last_state

    @property
    def name(self):
        """Gets the name of this V1ContainerStatus.  # noqa: E501

        Name is a DNS_LABEL representing the unique name of the container. Each container in a pod must have a unique name across all container types. Cannot be updated.  # noqa: E501

        :return: The name of this V1ContainerStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1ContainerStatus.

        Name is a DNS_LABEL representing the unique name of the container. Each container in a pod must have a unique name across all container types. Cannot be updated.  # noqa: E501

        :param name: The name of this V1ContainerStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def ready(self):
        """Gets the ready of this V1ContainerStatus.  # noqa: E501

        Ready specifies whether the container is currently passing its readiness check. The value will change as readiness probes keep executing. If no readiness probes are specified, this field defaults to true once the container is fully started (see Started field).  The value is typically used to determine whether a container is ready to accept traffic.  # noqa: E501

        :return: The ready of this V1ContainerStatus.  # noqa: E501
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this V1ContainerStatus.

        Ready specifies whether the container is currently passing its readiness check. The value will change as readiness probes keep executing. If no readiness probes are specified, this field defaults to true once the container is fully started (see Started field).  The value is typically used to determine whether a container is ready to accept traffic.  # noqa: E501

        :param ready: The ready of this V1ContainerStatus.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and ready is None:  # noqa: E501
            raise ValueError("Invalid value for `ready`, must not be `None`")  # noqa: E501

        self._ready = ready

    @property
    def resources(self):
        """Gets the resources of this V1ContainerStatus.  # noqa: E501


        :return: The resources of this V1ContainerStatus.  # noqa: E501
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this V1ContainerStatus.


        :param resources: The resources of this V1ContainerStatus.  # noqa: E501
        :type: V1ResourceRequirements
        """

        self._resources = resources

    @property
    def restart_count(self):
        """Gets the restart_count of this V1ContainerStatus.  # noqa: E501

        RestartCount holds the number of times the container has been restarted. Kubelet makes an effort to always increment the value, but there are cases when the state may be lost due to node restarts and then the value may be reset to 0. The value is never negative.  # noqa: E501

        :return: The restart_count of this V1ContainerStatus.  # noqa: E501
        :rtype: int
        """
        return self._restart_count

    @restart_count.setter
    def restart_count(self, restart_count):
        """Sets the restart_count of this V1ContainerStatus.

        RestartCount holds the number of times the container has been restarted. Kubelet makes an effort to always increment the value, but there are cases when the state may be lost due to node restarts and then the value may be reset to 0. The value is never negative.  # noqa: E501

        :param restart_count: The restart_count of this V1ContainerStatus.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and restart_count is None:  # noqa: E501
            raise ValueError("Invalid value for `restart_count`, must not be `None`")  # noqa: E501

        self._restart_count = restart_count

    @property
    def started(self):
        """Gets the started of this V1ContainerStatus.  # noqa: E501

        Started indicates whether the container has finished its postStart lifecycle hook and passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. In both cases, startup probes will run again. Is always true when no startupProbe is defined and container is running and has passed the postStart lifecycle hook. The null value must be treated the same as false.  # noqa: E501

        :return: The started of this V1ContainerStatus.  # noqa: E501
        :rtype: bool
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this V1ContainerStatus.

        Started indicates whether the container has finished its postStart lifecycle hook and passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. In both cases, startup probes will run again. Is always true when no startupProbe is defined and container is running and has passed the postStart lifecycle hook. The null value must be treated the same as false.  # noqa: E501

        :param started: The started of this V1ContainerStatus.  # noqa: E501
        :type: bool
        """

        self._started = started

    @property
    def state(self):
        """Gets the state of this V1ContainerStatus.  # noqa: E501


        :return: The state of this V1ContainerStatus.  # noqa: E501
        :rtype: V1ContainerState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this V1ContainerStatus.


        :param state: The state of this V1ContainerStatus.  # noqa: E501
        :type: V1ContainerState
        """

        self._state = state

    @property
    def stop_signal(self):
        """Gets the stop_signal of this V1ContainerStatus.  # noqa: E501

        StopSignal reports the effective stop signal for this container  # noqa: E501

        :return: The stop_signal of this V1ContainerStatus.  # noqa: E501
        :rtype: str
        """
        return self._stop_signal

    @stop_signal.setter
    def stop_signal(self, stop_signal):
        """Sets the stop_signal of this V1ContainerStatus.

        StopSignal reports the effective stop signal for this container  # noqa: E501

        :param stop_signal: The stop_signal of this V1ContainerStatus.  # noqa: E501
        :type: str
        """

        self._stop_signal = stop_signal

    @property
    def user(self):
        """Gets the user of this V1ContainerStatus.  # noqa: E501


        :return: The user of this V1ContainerStatus.  # noqa: E501
        :rtype: V1ContainerUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this V1ContainerStatus.


        :param user: The user of this V1ContainerStatus.  # noqa: E501
        :type: V1ContainerUser
        """

        self._user = user

    @property
    def volume_mounts(self):
        """Gets the volume_mounts of this V1ContainerStatus.  # noqa: E501

        Status of volume mounts.  # noqa: E501

        :return: The volume_mounts of this V1ContainerStatus.  # noqa: E501
        :rtype: list[V1VolumeMountStatus]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts):
        """Sets the volume_mounts of this V1ContainerStatus.

        Status of volume mounts.  # noqa: E501

        :param volume_mounts: The volume_mounts of this V1ContainerStatus.  # noqa: E501
        :type: list[V1VolumeMountStatus]
        """

        self._volume_mounts = volume_mounts

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
        if not isinstance(other, V1ContainerStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ContainerStatus):
            return True

        return self.to_dict() != other.to_dict()
