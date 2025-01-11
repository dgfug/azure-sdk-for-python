# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
import sys
from typing import Any, Callable, Dict, IO, Literal, Optional, Type, TypeVar, Union

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ...operations._append_blob_operations import (
    build_append_block_from_url_request,
    build_append_block_request,
    build_create_request,
    build_seal_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AppendBlobOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.blob.aio.AzureBlobStorage`'s
        :attr:`append_blob` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def create(  # pylint: disable=inconsistent-return-statements
        self,
        content_length: int,
        timeout: Optional[int] = None,
        metadata: Optional[Dict[str, str]] = None,
        request_id_parameter: Optional[str] = None,
        blob_tags_string: Optional[str] = None,
        immutability_policy_expiry: Optional[datetime.datetime] = None,
        immutability_policy_mode: Optional[Union[str, _models.BlobImmutabilityPolicyMode]] = None,
        legal_hold: Optional[bool] = None,
        blob_http_headers: Optional[_models.BlobHTTPHeaders] = None,
        lease_access_conditions: Optional[_models.LeaseAccessConditions] = None,
        cpk_info: Optional[_models.CpkInfo] = None,
        cpk_scope_info: Optional[_models.CpkScopeInfo] = None,
        modified_access_conditions: Optional[_models.ModifiedAccessConditions] = None,
        **kwargs: Any
    ) -> None:
        # pylint: disable=line-too-long
        """The Create Append Blob operation creates a new append blob.

        :param content_length: The length of the request. Required.
        :type content_length: int
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://learn.microsoft.com/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param metadata: Optional. Specifies a user-defined name-value pair associated with the blob.
         If no name-value pairs are specified, the operation will copy the metadata from the source blob
         or file to the destination blob. If one or more name-value pairs are specified, the destination
         blob is created with the specified metadata, and metadata is not copied from the source blob or
         file. Note that beginning with version 2009-09-19, metadata names must adhere to the naming
         rules for C# identifiers. See Naming and Referencing Containers, Blobs, and Metadata for more
         information. Default value is None.
        :type metadata: dict[str, str]
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param blob_tags_string: Optional.  Used to set blob tags in various blob operations. Default
         value is None.
        :type blob_tags_string: str
        :param immutability_policy_expiry: Specifies the date time when the blobs immutability policy
         is set to expire. Default value is None.
        :type immutability_policy_expiry: ~datetime.datetime
        :param immutability_policy_mode: Specifies the immutability policy mode to set on the blob.
         Known values are: "Mutable", "Unlocked", and "Locked". Default value is None.
        :type immutability_policy_mode: str or ~azure.storage.blob.models.BlobImmutabilityPolicyMode
        :param legal_hold: Specified if a legal hold should be set on the blob. Default value is None.
        :type legal_hold: bool
        :param blob_http_headers: Parameter group. Default value is None.
        :type blob_http_headers: ~azure.storage.blob.models.BlobHTTPHeaders
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.blob.models.CpkInfo
        :param cpk_scope_info: Parameter group. Default value is None.
        :type cpk_scope_info: ~azure.storage.blob.models.CpkScopeInfo
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {  # pylint: disable=unsubscriptable-object
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        blob_type: Literal["AppendBlob"] = kwargs.pop("blob_type", _headers.pop("x-ms-blob-type", "AppendBlob"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _blob_content_type = None
        _blob_content_encoding = None
        _blob_content_language = None
        _blob_content_md5 = None
        _blob_cache_control = None
        _lease_id = None
        _blob_content_disposition = None
        _encryption_key = None
        _encryption_key_sha256 = None
        _encryption_algorithm = None
        _encryption_scope = None
        _if_modified_since = None
        _if_unmodified_since = None
        _if_match = None
        _if_none_match = None
        _if_tags = None
        if blob_http_headers is not None:
            _blob_cache_control = blob_http_headers.blob_cache_control
            _blob_content_disposition = blob_http_headers.blob_content_disposition
            _blob_content_encoding = blob_http_headers.blob_content_encoding
            _blob_content_language = blob_http_headers.blob_content_language
            _blob_content_md5 = blob_http_headers.blob_content_md5
            _blob_content_type = blob_http_headers.blob_content_type
        if lease_access_conditions is not None:
            _lease_id = lease_access_conditions.lease_id
        if cpk_info is not None:
            _encryption_algorithm = cpk_info.encryption_algorithm
            _encryption_key = cpk_info.encryption_key
            _encryption_key_sha256 = cpk_info.encryption_key_sha256
        if cpk_scope_info is not None:
            _encryption_scope = cpk_scope_info.encryption_scope
        if modified_access_conditions is not None:
            _if_match = modified_access_conditions.if_match
            _if_modified_since = modified_access_conditions.if_modified_since
            _if_none_match = modified_access_conditions.if_none_match
            _if_tags = modified_access_conditions.if_tags
            _if_unmodified_since = modified_access_conditions.if_unmodified_since

        _request = build_create_request(
            url=self._config.url,
            content_length=content_length,
            timeout=timeout,
            blob_content_type=_blob_content_type,
            blob_content_encoding=_blob_content_encoding,
            blob_content_language=_blob_content_language,
            blob_content_md5=_blob_content_md5,
            blob_cache_control=_blob_cache_control,
            metadata=metadata,
            lease_id=_lease_id,
            blob_content_disposition=_blob_content_disposition,
            encryption_key=_encryption_key,
            encryption_key_sha256=_encryption_key_sha256,
            encryption_algorithm=_encryption_algorithm,
            encryption_scope=_encryption_scope,
            if_modified_since=_if_modified_since,
            if_unmodified_since=_if_unmodified_since,
            if_match=_if_match,
            if_none_match=_if_none_match,
            if_tags=_if_tags,
            request_id_parameter=request_id_parameter,
            blob_tags_string=blob_tags_string,
            immutability_policy_expiry=immutability_policy_expiry,
            immutability_policy_mode=immutability_policy_mode,
            legal_hold=legal_hold,
            blob_type=blob_type,
            version=self._config.version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))
        response_headers["Last-Modified"] = self._deserialize("rfc-1123", response.headers.get("Last-Modified"))
        response_headers["Content-MD5"] = self._deserialize("bytearray", response.headers.get("Content-MD5"))
        response_headers["x-ms-client-request-id"] = self._deserialize(
            "str", response.headers.get("x-ms-client-request-id")
        )
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["x-ms-version-id"] = self._deserialize("str", response.headers.get("x-ms-version-id"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))
        response_headers["x-ms-request-server-encrypted"] = self._deserialize(
            "bool", response.headers.get("x-ms-request-server-encrypted")
        )
        response_headers["x-ms-encryption-key-sha256"] = self._deserialize(
            "str", response.headers.get("x-ms-encryption-key-sha256")
        )
        response_headers["x-ms-encryption-scope"] = self._deserialize(
            "str", response.headers.get("x-ms-encryption-scope")
        )

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    @distributed_trace_async
    async def append_block(  # pylint: disable=inconsistent-return-statements
        self,
        content_length: int,
        body: IO[bytes],
        timeout: Optional[int] = None,
        transactional_content_md5: Optional[bytes] = None,
        transactional_content_crc64: Optional[bytes] = None,
        request_id_parameter: Optional[str] = None,
        structured_body_type: Optional[str] = None,
        structured_content_length: Optional[int] = None,
        lease_access_conditions: Optional[_models.LeaseAccessConditions] = None,
        append_position_access_conditions: Optional[_models.AppendPositionAccessConditions] = None,
        cpk_info: Optional[_models.CpkInfo] = None,
        cpk_scope_info: Optional[_models.CpkScopeInfo] = None,
        modified_access_conditions: Optional[_models.ModifiedAccessConditions] = None,
        **kwargs: Any
    ) -> None:
        # pylint: disable=line-too-long
        """The Append Block operation commits a new block of data to the end of an existing append blob.
        The Append Block operation is permitted only if the blob was created with x-ms-blob-type set to
        AppendBlob. Append Block is supported only on version 2015-02-21 version or later.

        :param content_length: The length of the request. Required.
        :type content_length: int
        :param body: Initial data. Required.
        :type body: IO[bytes]
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://learn.microsoft.com/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param transactional_content_md5: Specify the transactional md5 for the body, to be validated
         by the service. Default value is None.
        :type transactional_content_md5: bytes
        :param transactional_content_crc64: Specify the transactional crc64 for the body, to be
         validated by the service. Default value is None.
        :type transactional_content_crc64: bytes
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param structured_body_type: Required if the request body is a structured message. Specifies
         the message schema version and properties. Default value is None.
        :type structured_body_type: str
        :param structured_content_length: Required if the request body is a structured message.
         Specifies the length of the blob/file content inside the message body. Will always be smaller
         than Content-Length. Default value is None.
        :type structured_content_length: int
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param append_position_access_conditions: Parameter group. Default value is None.
        :type append_position_access_conditions:
         ~azure.storage.blob.models.AppendPositionAccessConditions
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.blob.models.CpkInfo
        :param cpk_scope_info: Parameter group. Default value is None.
        :type cpk_scope_info: ~azure.storage.blob.models.CpkScopeInfo
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {  # pylint: disable=unsubscriptable-object
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        comp: Literal["appendblock"] = kwargs.pop("comp", _params.pop("comp", "appendblock"))
        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/octet-stream"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _lease_id = None
        _max_size = None
        _append_position = None
        _encryption_key = None
        _encryption_key_sha256 = None
        _encryption_algorithm = None
        _encryption_scope = None
        _if_modified_since = None
        _if_unmodified_since = None
        _if_match = None
        _if_none_match = None
        _if_tags = None
        if lease_access_conditions is not None:
            _lease_id = lease_access_conditions.lease_id
        if append_position_access_conditions is not None:
            _append_position = append_position_access_conditions.append_position
            _max_size = append_position_access_conditions.max_size
        if cpk_info is not None:
            _encryption_algorithm = cpk_info.encryption_algorithm
            _encryption_key = cpk_info.encryption_key
            _encryption_key_sha256 = cpk_info.encryption_key_sha256
        if cpk_scope_info is not None:
            _encryption_scope = cpk_scope_info.encryption_scope
        if modified_access_conditions is not None:
            _if_match = modified_access_conditions.if_match
            _if_modified_since = modified_access_conditions.if_modified_since
            _if_none_match = modified_access_conditions.if_none_match
            _if_tags = modified_access_conditions.if_tags
            _if_unmodified_since = modified_access_conditions.if_unmodified_since
        _content = body

        _request = build_append_block_request(
            url=self._config.url,
            content_length=content_length,
            timeout=timeout,
            transactional_content_md5=transactional_content_md5,
            transactional_content_crc64=transactional_content_crc64,
            lease_id=_lease_id,
            max_size=_max_size,
            append_position=_append_position,
            encryption_key=_encryption_key,
            encryption_key_sha256=_encryption_key_sha256,
            encryption_algorithm=_encryption_algorithm,
            encryption_scope=_encryption_scope,
            if_modified_since=_if_modified_since,
            if_unmodified_since=_if_unmodified_since,
            if_match=_if_match,
            if_none_match=_if_none_match,
            if_tags=_if_tags,
            request_id_parameter=request_id_parameter,
            structured_body_type=structured_body_type,
            structured_content_length=structured_content_length,
            comp=comp,
            content_type=content_type,
            version=self._config.version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))
        response_headers["Last-Modified"] = self._deserialize("rfc-1123", response.headers.get("Last-Modified"))
        response_headers["Content-MD5"] = self._deserialize("bytearray", response.headers.get("Content-MD5"))
        response_headers["x-ms-content-crc64"] = self._deserialize(
            "bytearray", response.headers.get("x-ms-content-crc64")
        )
        response_headers["x-ms-client-request-id"] = self._deserialize(
            "str", response.headers.get("x-ms-client-request-id")
        )
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))
        response_headers["x-ms-blob-append-offset"] = self._deserialize(
            "str", response.headers.get("x-ms-blob-append-offset")
        )
        response_headers["x-ms-blob-committed-block-count"] = self._deserialize(
            "int", response.headers.get("x-ms-blob-committed-block-count")
        )
        response_headers["x-ms-request-server-encrypted"] = self._deserialize(
            "bool", response.headers.get("x-ms-request-server-encrypted")
        )
        response_headers["x-ms-encryption-key-sha256"] = self._deserialize(
            "str", response.headers.get("x-ms-encryption-key-sha256")
        )
        response_headers["x-ms-encryption-scope"] = self._deserialize(
            "str", response.headers.get("x-ms-encryption-scope")
        )
        response_headers["x-ms-structured-body"] = self._deserialize(
            "str", response.headers.get("x-ms-structured-body")
        )

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    @distributed_trace_async
    async def append_block_from_url(  # pylint: disable=inconsistent-return-statements
        self,
        source_url: str,
        content_length: int,
        source_range: Optional[str] = None,
        source_content_md5: Optional[bytes] = None,
        source_contentcrc64: Optional[bytes] = None,
        timeout: Optional[int] = None,
        transactional_content_md5: Optional[bytes] = None,
        request_id_parameter: Optional[str] = None,
        copy_source_authorization: Optional[str] = None,
        cpk_info: Optional[_models.CpkInfo] = None,
        cpk_scope_info: Optional[_models.CpkScopeInfo] = None,
        lease_access_conditions: Optional[_models.LeaseAccessConditions] = None,
        append_position_access_conditions: Optional[_models.AppendPositionAccessConditions] = None,
        modified_access_conditions: Optional[_models.ModifiedAccessConditions] = None,
        source_modified_access_conditions: Optional[_models.SourceModifiedAccessConditions] = None,
        **kwargs: Any
    ) -> None:
        # pylint: disable=line-too-long
        """The Append Block operation commits a new block of data to the end of an existing append blob
        where the contents are read from a source url. The Append Block operation is permitted only if
        the blob was created with x-ms-blob-type set to AppendBlob. Append Block is supported only on
        version 2015-02-21 version or later.

        :param source_url: Specify a URL to the copy source. Required.
        :type source_url: str
        :param content_length: The length of the request. Required.
        :type content_length: int
        :param source_range: Bytes of source data in the specified range. Default value is None.
        :type source_range: str
        :param source_content_md5: Specify the md5 calculated for the range of bytes that must be read
         from the copy source. Default value is None.
        :type source_content_md5: bytes
        :param source_contentcrc64: Specify the crc64 calculated for the range of bytes that must be
         read from the copy source. Default value is None.
        :type source_contentcrc64: bytes
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://learn.microsoft.com/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param transactional_content_md5: Specify the transactional md5 for the body, to be validated
         by the service. Default value is None.
        :type transactional_content_md5: bytes
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param copy_source_authorization: Only Bearer type is supported. Credentials should be a valid
         OAuth access token to copy source. Default value is None.
        :type copy_source_authorization: str
        :param cpk_info: Parameter group. Default value is None.
        :type cpk_info: ~azure.storage.blob.models.CpkInfo
        :param cpk_scope_info: Parameter group. Default value is None.
        :type cpk_scope_info: ~azure.storage.blob.models.CpkScopeInfo
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param append_position_access_conditions: Parameter group. Default value is None.
        :type append_position_access_conditions:
         ~azure.storage.blob.models.AppendPositionAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :param source_modified_access_conditions: Parameter group. Default value is None.
        :type source_modified_access_conditions:
         ~azure.storage.blob.models.SourceModifiedAccessConditions
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {  # pylint: disable=unsubscriptable-object
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        comp: Literal["appendblock"] = kwargs.pop("comp", _params.pop("comp", "appendblock"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _encryption_key = None
        _encryption_key_sha256 = None
        _encryption_algorithm = None
        _encryption_scope = None
        _lease_id = None
        _max_size = None
        _append_position = None
        _if_modified_since = None
        _if_unmodified_since = None
        _if_match = None
        _if_none_match = None
        _if_tags = None
        _source_if_modified_since = None
        _source_if_unmodified_since = None
        _source_if_match = None
        _source_if_none_match = None
        if cpk_info is not None:
            _encryption_algorithm = cpk_info.encryption_algorithm
            _encryption_key = cpk_info.encryption_key
            _encryption_key_sha256 = cpk_info.encryption_key_sha256
        if cpk_scope_info is not None:
            _encryption_scope = cpk_scope_info.encryption_scope
        if lease_access_conditions is not None:
            _lease_id = lease_access_conditions.lease_id
        if append_position_access_conditions is not None:
            _append_position = append_position_access_conditions.append_position
            _max_size = append_position_access_conditions.max_size
        if modified_access_conditions is not None:
            _if_match = modified_access_conditions.if_match
            _if_modified_since = modified_access_conditions.if_modified_since
            _if_none_match = modified_access_conditions.if_none_match
            _if_tags = modified_access_conditions.if_tags
            _if_unmodified_since = modified_access_conditions.if_unmodified_since
        if source_modified_access_conditions is not None:
            _source_if_match = source_modified_access_conditions.source_if_match
            _source_if_modified_since = source_modified_access_conditions.source_if_modified_since
            _source_if_none_match = source_modified_access_conditions.source_if_none_match
            _source_if_unmodified_since = source_modified_access_conditions.source_if_unmodified_since

        _request = build_append_block_from_url_request(
            url=self._config.url,
            source_url=source_url,
            content_length=content_length,
            source_range=source_range,
            source_content_md5=source_content_md5,
            source_contentcrc64=source_contentcrc64,
            timeout=timeout,
            transactional_content_md5=transactional_content_md5,
            encryption_key=_encryption_key,
            encryption_key_sha256=_encryption_key_sha256,
            encryption_algorithm=_encryption_algorithm,
            encryption_scope=_encryption_scope,
            lease_id=_lease_id,
            max_size=_max_size,
            append_position=_append_position,
            if_modified_since=_if_modified_since,
            if_unmodified_since=_if_unmodified_since,
            if_match=_if_match,
            if_none_match=_if_none_match,
            if_tags=_if_tags,
            source_if_modified_since=_source_if_modified_since,
            source_if_unmodified_since=_source_if_unmodified_since,
            source_if_match=_source_if_match,
            source_if_none_match=_source_if_none_match,
            request_id_parameter=request_id_parameter,
            copy_source_authorization=copy_source_authorization,
            comp=comp,
            version=self._config.version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))
        response_headers["Last-Modified"] = self._deserialize("rfc-1123", response.headers.get("Last-Modified"))
        response_headers["Content-MD5"] = self._deserialize("bytearray", response.headers.get("Content-MD5"))
        response_headers["x-ms-content-crc64"] = self._deserialize(
            "bytearray", response.headers.get("x-ms-content-crc64")
        )
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))
        response_headers["x-ms-blob-append-offset"] = self._deserialize(
            "str", response.headers.get("x-ms-blob-append-offset")
        )
        response_headers["x-ms-blob-committed-block-count"] = self._deserialize(
            "int", response.headers.get("x-ms-blob-committed-block-count")
        )
        response_headers["x-ms-encryption-key-sha256"] = self._deserialize(
            "str", response.headers.get("x-ms-encryption-key-sha256")
        )
        response_headers["x-ms-encryption-scope"] = self._deserialize(
            "str", response.headers.get("x-ms-encryption-scope")
        )
        response_headers["x-ms-request-server-encrypted"] = self._deserialize(
            "bool", response.headers.get("x-ms-request-server-encrypted")
        )

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    @distributed_trace_async
    async def seal(  # pylint: disable=inconsistent-return-statements
        self,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        lease_access_conditions: Optional[_models.LeaseAccessConditions] = None,
        modified_access_conditions: Optional[_models.ModifiedAccessConditions] = None,
        append_position_access_conditions: Optional[_models.AppendPositionAccessConditions] = None,
        **kwargs: Any
    ) -> None:
        # pylint: disable=line-too-long
        """The Seal operation seals the Append Blob to make it read-only. Seal is supported only on
        version 2019-12-12 version or later.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://learn.microsoft.com/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param lease_access_conditions: Parameter group. Default value is None.
        :type lease_access_conditions: ~azure.storage.blob.models.LeaseAccessConditions
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.blob.models.ModifiedAccessConditions
        :param append_position_access_conditions: Parameter group. Default value is None.
        :type append_position_access_conditions:
         ~azure.storage.blob.models.AppendPositionAccessConditions
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {  # pylint: disable=unsubscriptable-object
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        comp: Literal["seal"] = kwargs.pop("comp", _params.pop("comp", "seal"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _lease_id = None
        _if_modified_since = None
        _if_unmodified_since = None
        _if_match = None
        _if_none_match = None
        _append_position = None
        if lease_access_conditions is not None:
            _lease_id = lease_access_conditions.lease_id
        if modified_access_conditions is not None:
            _if_match = modified_access_conditions.if_match
            _if_modified_since = modified_access_conditions.if_modified_since
            _if_none_match = modified_access_conditions.if_none_match
            _if_unmodified_since = modified_access_conditions.if_unmodified_since
        if append_position_access_conditions is not None:
            _append_position = append_position_access_conditions.append_position

        _request = build_seal_request(
            url=self._config.url,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            lease_id=_lease_id,
            if_modified_since=_if_modified_since,
            if_unmodified_since=_if_unmodified_since,
            if_match=_if_match,
            if_none_match=_if_none_match,
            append_position=_append_position,
            comp=comp,
            version=self._config.version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))
        response_headers["Last-Modified"] = self._deserialize("rfc-1123", response.headers.get("Last-Modified"))
        response_headers["x-ms-client-request-id"] = self._deserialize(
            "str", response.headers.get("x-ms-client-request-id")
        )
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))
        response_headers["x-ms-blob-sealed"] = self._deserialize("bool", response.headers.get("x-ms-blob-sealed"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore
