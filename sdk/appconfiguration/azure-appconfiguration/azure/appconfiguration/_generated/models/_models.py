# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=useless-super-delegation

import datetime
from typing import Any, Dict, List, Mapping, Optional, TYPE_CHECKING, Union, overload

from azure.core.exceptions import ODataV4Format

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import models as _models


class Error(_model_base.Model):
    """Azure App Configuration error object.

    :ivar type: The type of the error.
    :vartype type: str
    :ivar title: A brief summary of the error.
    :vartype title: str
    :ivar name: The name of the parameter that resulted in the error.
    :vartype name: str
    :ivar detail: A detailed description of the error.
    :vartype detail: str
    :ivar status: The HTTP status code that the error maps to.
    :vartype status: int
    """

    type: Optional[str] = rest_field()
    """The type of the error."""
    title: Optional[str] = rest_field()
    """A brief summary of the error."""
    name: Optional[str] = rest_field()
    """The name of the parameter that resulted in the error."""
    detail: Optional[str] = rest_field()
    """A detailed description of the error."""
    status: Optional[int] = rest_field()
    """The HTTP status code that the error maps to."""

    @overload
    def __init__(
        self,
        *,
        type: Optional[str] = None,
        title: Optional[str] = None,
        name: Optional[str] = None,
        detail: Optional[str] = None,
        status: Optional[int] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Key(_model_base.Model):
    """Keys serve as identifiers for key-values and are used to store and retrieve corresponding
    values.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar name: The name of the key. Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read"])
    """The name of the key. Required."""


class KeyValue(_model_base.Model):
    """A key-value pair representing application settings.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar key: The key of the key-value. Required.
    :vartype key: str
    :ivar label: The label the key-value belongs to.
    :vartype label: str
    :ivar content_type: The content type of the value stored within the key-value.
    :vartype content_type: str
    :ivar value: The value of the key-value.
    :vartype value: str
    :ivar last_modified: A date representing the last time the key-value was modified.
    :vartype last_modified: ~datetime.datetime
    :ivar tags: The tags of the key-value.
    :vartype tags: dict[str, str]
    :ivar locked: Indicates whether the key-value is locked.
    :vartype locked: bool
    :ivar etag: A value representing the current state of the resource.
    :vartype etag: str
    """

    key: str = rest_field(visibility=["read"])
    """The key of the key-value. Required."""
    label: Optional[str] = rest_field()
    """The label the key-value belongs to."""
    content_type: Optional[str] = rest_field()
    """The content type of the value stored within the key-value."""
    value: Optional[str] = rest_field()
    """The value of the key-value."""
    last_modified: Optional[datetime.datetime] = rest_field(format="rfc3339")
    """A date representing the last time the key-value was modified."""
    tags: Optional[Dict[str, str]] = rest_field()
    """The tags of the key-value."""
    locked: Optional[bool] = rest_field()
    """Indicates whether the key-value is locked."""
    etag: Optional[str] = rest_field()
    """A value representing the current state of the resource."""

    @overload
    def __init__(
        self,
        *,
        label: Optional[str] = None,
        content_type: Optional[str] = None,
        value: Optional[str] = None,
        last_modified: Optional[datetime.datetime] = None,
        tags: Optional[Dict[str, str]] = None,
        locked: Optional[bool] = None,
        etag: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class KeyValueFilter(_model_base.Model):
    """Enables filtering of key-values. Syntax reference:
    https://aka.ms/azconfig/docs/restapisnapshots.


    :ivar key: Filters key-values by their key field. Required.
    :vartype key: str
    :ivar label: Filters key-values by their label field.
    :vartype label: str
    :ivar tags: Filters key-values by their tags field.
    :vartype tags: list[str]
    """

    key: str = rest_field()
    """Filters key-values by their key field. Required."""
    label: Optional[str] = rest_field()
    """Filters key-values by their label field."""
    tags: Optional[List[str]] = rest_field()
    """Filters key-values by their tags field."""

    @overload
    def __init__(
        self,
        *,
        key: str,
        label: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Label(_model_base.Model):
    """Labels are used to group key-values.

    :ivar name: The name of the label.
    :vartype name: str
    """

    name: Optional[str] = rest_field()
    """The name of the label."""

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class OperationDetails(_model_base.Model):
    """Details of a long running operation.


    :ivar id: The unique id of the operation. Required.
    :vartype id: str
    :ivar status: The current status of the operation. Required. Known values are: "NotStarted",
     "Running", "Succeeded", "Failed", and "Canceled".
    :vartype status: str or ~azure.appconfiguration.models.OperationState
    :ivar error: An error, available when the status is ``Failed``\\ , describing why the operation
     failed.
    :vartype error: ~azure.core.ODataV4Format
    """

    id: str = rest_field()
    """The unique id of the operation. Required."""
    status: Union[str, "_models.OperationState"] = rest_field()
    """The current status of the operation. Required. Known values are: \"NotStarted\", \"Running\",
     \"Succeeded\", \"Failed\", and \"Canceled\"."""
    error: Optional[ODataV4Format] = rest_field()
    """An error, available when the status is ``Failed``\ , describing why the operation
     failed."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        status: Union[str, "_models.OperationState"],
        error: Optional[ODataV4Format] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Snapshot(_model_base.Model):
    """A snapshot is a named, immutable subset of an App Configuration store's key-values.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar name: The name of the snapshot. Required.
    :vartype name: str
    :ivar status: The current status of the snapshot. Known values are: "provisioning", "ready",
     "archived", and "failed".
    :vartype status: str or ~azure.appconfiguration.models.SnapshotStatus
    :ivar filters: A list of filters used to filter the key-values included in the snapshot.
     Required.
    :vartype filters: list[~azure.appconfiguration.models.KeyValueFilter]
    :ivar composition_type: The composition type describes how the key-values within the snapshot
     are
     composed. The 'key' composition type ensures there are no two key-values
     containing the same key. The 'key_label' composition type ensures there are no
     two key-values containing the same key and label. Known values are: "key" and "key_label".
    :vartype composition_type: str or ~azure.appconfiguration.models.SnapshotComposition
    :ivar created: The time that the snapshot was created.
    :vartype created: ~datetime.datetime
    :ivar expires: The time that the snapshot will expire.
    :vartype expires: ~datetime.datetime
    :ivar retention_period: The amount of time, in seconds, that a snapshot will remain in the
     archived
     state before expiring. This property is only writable during the creation of a
     snapshot. If not specified, the default lifetime of key-value revisions will be
     used.
    :vartype retention_period: int
    :ivar size: The size in bytes of the snapshot.
    :vartype size: int
    :ivar items_count: The amount of key-values in the snapshot.
    :vartype items_count: int
    :ivar tags: The tags of the snapshot.
    :vartype tags: dict[str, str]
    :ivar etag: A value representing the current state of the snapshot.
    :vartype etag: str
    """

    name: str = rest_field(visibility=["read"])
    """The name of the snapshot. Required."""
    status: Optional[Union[str, "_models.SnapshotStatus"]] = rest_field(visibility=["read"])
    """The current status of the snapshot. Known values are: \"provisioning\", \"ready\",
     \"archived\", and \"failed\"."""
    filters: List["_models.KeyValueFilter"] = rest_field()
    """A list of filters used to filter the key-values included in the snapshot. Required."""
    composition_type: Optional[Union[str, "_models.SnapshotComposition"]] = rest_field()
    """The composition type describes how the key-values within the snapshot are
     composed. The 'key' composition type ensures there are no two key-values
     containing the same key. The 'key_label' composition type ensures there are no
     two key-values containing the same key and label. Known values are: \"key\" and \"key_label\"."""
    created: Optional[datetime.datetime] = rest_field(visibility=["read"], format="rfc3339")
    """The time that the snapshot was created."""
    expires: Optional[datetime.datetime] = rest_field(visibility=["read"], format="rfc3339")
    """The time that the snapshot will expire."""
    retention_period: Optional[int] = rest_field()
    """The amount of time, in seconds, that a snapshot will remain in the archived
     state before expiring. This property is only writable during the creation of a
     snapshot. If not specified, the default lifetime of key-value revisions will be
     used."""
    size: Optional[int] = rest_field(visibility=["read"])
    """The size in bytes of the snapshot."""
    items_count: Optional[int] = rest_field(visibility=["read"])
    """The amount of key-values in the snapshot."""
    tags: Optional[Dict[str, str]] = rest_field()
    """The tags of the snapshot."""
    etag: Optional[str] = rest_field(visibility=["read"])
    """A value representing the current state of the snapshot."""

    @overload
    def __init__(
        self,
        *,
        filters: List["_models.KeyValueFilter"],
        composition_type: Optional[Union[str, "_models.SnapshotComposition"]] = None,
        retention_period: Optional[int] = None,
        tags: Optional[Dict[str, str]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SnapshotUpdateParameters(_model_base.Model):
    """Parameters used to update a snapshot.

    :ivar status: The desired status of the snapshot. Known values are: "provisioning", "ready",
     "archived", and "failed".
    :vartype status: str or ~azure.appconfiguration.models.SnapshotStatus
    """

    status: Optional[Union[str, "_models.SnapshotStatus"]] = rest_field()
    """The desired status of the snapshot. Known values are: \"provisioning\", \"ready\",
     \"archived\", and \"failed\"."""

    @overload
    def __init__(
        self,
        *,
        status: Optional[Union[str, "_models.SnapshotStatus"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
