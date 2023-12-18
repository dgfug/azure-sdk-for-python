# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar, Union

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._cluster_versions_operations import (
    build_get_by_environment_request,
    build_get_request,
    build_list_by_environment_request,
    build_list_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ClusterVersionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.servicefabric.aio.ServiceFabricManagementClient`'s
        :attr:`cluster_versions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(self, location: str, cluster_version: str, **kwargs: Any) -> _models.ClusterCodeVersionsListResult:
        """Gets information about a Service Fabric cluster code version available in the specified
        location.

        Gets information about an available Service Fabric cluster code version.

        :param location: The location for the cluster code versions. This is different from cluster
         location. Required.
        :type location: str
        :param cluster_version: The cluster code version. Required.
        :type cluster_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ClusterCodeVersionsListResult or the result of cls(response)
        :rtype: ~azure.mgmt.servicefabric.models.ClusterCodeVersionsListResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ClusterCodeVersionsListResult] = kwargs.pop("cls", None)

        request = build_get_request(
            location=location,
            cluster_version=cluster_version,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorModel, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ClusterCodeVersionsListResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/clusterVersions/{clusterVersion}"
    }

    @distributed_trace_async
    async def get_by_environment(
        self,
        location: str,
        environment: Union[str, _models.ClusterVersionsEnvironment],
        cluster_version: str,
        **kwargs: Any
    ) -> _models.ClusterCodeVersionsListResult:
        """Gets information about a Service Fabric cluster code version available for the specified
        environment.

        Gets information about an available Service Fabric cluster code version by environment.

        :param location: The location for the cluster code versions. This is different from cluster
         location. Required.
        :type location: str
        :param environment: The operating system of the cluster. The default means all. Known values
         are: "Windows" and "Linux". Required.
        :type environment: str or ~azure.mgmt.servicefabric.models.ClusterVersionsEnvironment
        :param cluster_version: The cluster code version. Required.
        :type cluster_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ClusterCodeVersionsListResult or the result of cls(response)
        :rtype: ~azure.mgmt.servicefabric.models.ClusterCodeVersionsListResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ClusterCodeVersionsListResult] = kwargs.pop("cls", None)

        request = build_get_by_environment_request(
            location=location,
            environment=environment,
            cluster_version=cluster_version,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_by_environment.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorModel, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ClusterCodeVersionsListResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_environment.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/environments/{environment}/clusterVersions/{clusterVersion}"
    }

    @distributed_trace_async
    async def list(self, location: str, **kwargs: Any) -> _models.ClusterCodeVersionsListResult:
        """Gets the list of Service Fabric cluster code versions available for the specified location.

        Gets all available code versions for Service Fabric cluster resources by location.

        :param location: The location for the cluster code versions. This is different from cluster
         location. Required.
        :type location: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ClusterCodeVersionsListResult or the result of cls(response)
        :rtype: ~azure.mgmt.servicefabric.models.ClusterCodeVersionsListResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ClusterCodeVersionsListResult] = kwargs.pop("cls", None)

        request = build_list_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorModel, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ClusterCodeVersionsListResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/clusterVersions"
    }

    @distributed_trace_async
    async def list_by_environment(
        self, location: str, environment: Union[str, _models.ClusterVersionsEnvironment], **kwargs: Any
    ) -> _models.ClusterCodeVersionsListResult:
        """Gets the list of Service Fabric cluster code versions available for the specified environment.

        Gets all available code versions for Service Fabric cluster resources by environment.

        :param location: The location for the cluster code versions. This is different from cluster
         location. Required.
        :type location: str
        :param environment: The operating system of the cluster. The default means all. Known values
         are: "Windows" and "Linux". Required.
        :type environment: str or ~azure.mgmt.servicefabric.models.ClusterVersionsEnvironment
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ClusterCodeVersionsListResult or the result of cls(response)
        :rtype: ~azure.mgmt.servicefabric.models.ClusterCodeVersionsListResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ClusterCodeVersionsListResult] = kwargs.pop("cls", None)

        request = build_list_by_environment_request(
            location=location,
            environment=environment,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list_by_environment.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorModel, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ClusterCodeVersionsListResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_by_environment.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/environments/{environment}/clusterVersions"
    }
