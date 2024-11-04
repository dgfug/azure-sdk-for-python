# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING
from typing_extensions import Self

from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient
from azure.mgmt.core.policies import ARMAutoResourceProviderRegistrationPolicy

from . import models as _models
from ._configuration import PostgreSQLManagementClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    AdministratorsOperations,
    BackupsOperations,
    CheckNameAvailabilityOperations,
    CheckNameAvailabilityWithLocationOperations,
    ConfigurationsOperations,
    DatabasesOperations,
    FirewallRulesOperations,
    FlexibleServerOperations,
    GetPrivateDnsZoneSuffixOperations,
    LocationBasedCapabilitiesOperations,
    LogFilesOperations,
    LtrBackupOperationsOperations,
    MigrationsOperations,
    Operations,
    PostgreSQLManagementClientOperationsMixin,
    PrivateEndpointConnectionOperations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    QuotaUsagesOperations,
    ReplicasOperations,
    ServerCapabilitiesOperations,
    ServerThreatProtectionSettingsOperations,
    ServersOperations,
    TuningOptionsOperations,
    VirtualEndpointsOperations,
    VirtualNetworkSubnetUsageOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class PostgreSQLManagementClient(
    PostgreSQLManagementClientOperationsMixin
):  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """The Microsoft Azure management API provides create, read, update, and delete functionality for
    Azure PostgreSQL resources including servers, databases, firewall rules, VNET rules, security
    alert policies, log files and configurations with new business model.

    :ivar administrators: AdministratorsOperations operations
    :vartype administrators:
     azure.mgmt.postgresqlflexibleservers.operations.AdministratorsOperations
    :ivar backups: BackupsOperations operations
    :vartype backups: azure.mgmt.postgresqlflexibleservers.operations.BackupsOperations
    :ivar location_based_capabilities: LocationBasedCapabilitiesOperations operations
    :vartype location_based_capabilities:
     azure.mgmt.postgresqlflexibleservers.operations.LocationBasedCapabilitiesOperations
    :ivar server_capabilities: ServerCapabilitiesOperations operations
    :vartype server_capabilities:
     azure.mgmt.postgresqlflexibleservers.operations.ServerCapabilitiesOperations
    :ivar check_name_availability: CheckNameAvailabilityOperations operations
    :vartype check_name_availability:
     azure.mgmt.postgresqlflexibleservers.operations.CheckNameAvailabilityOperations
    :ivar check_name_availability_with_location: CheckNameAvailabilityWithLocationOperations
     operations
    :vartype check_name_availability_with_location:
     azure.mgmt.postgresqlflexibleservers.operations.CheckNameAvailabilityWithLocationOperations
    :ivar configurations: ConfigurationsOperations operations
    :vartype configurations:
     azure.mgmt.postgresqlflexibleservers.operations.ConfigurationsOperations
    :ivar databases: DatabasesOperations operations
    :vartype databases: azure.mgmt.postgresqlflexibleservers.operations.DatabasesOperations
    :ivar firewall_rules: FirewallRulesOperations operations
    :vartype firewall_rules:
     azure.mgmt.postgresqlflexibleservers.operations.FirewallRulesOperations
    :ivar servers: ServersOperations operations
    :vartype servers: azure.mgmt.postgresqlflexibleservers.operations.ServersOperations
    :ivar flexible_server: FlexibleServerOperations operations
    :vartype flexible_server:
     azure.mgmt.postgresqlflexibleservers.operations.FlexibleServerOperations
    :ivar ltr_backup_operations: LtrBackupOperationsOperations operations
    :vartype ltr_backup_operations:
     azure.mgmt.postgresqlflexibleservers.operations.LtrBackupOperationsOperations
    :ivar migrations: MigrationsOperations operations
    :vartype migrations: azure.mgmt.postgresqlflexibleservers.operations.MigrationsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.postgresqlflexibleservers.operations.Operations
    :ivar get_private_dns_zone_suffix: GetPrivateDnsZoneSuffixOperations operations
    :vartype get_private_dns_zone_suffix:
     azure.mgmt.postgresqlflexibleservers.operations.GetPrivateDnsZoneSuffixOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.postgresqlflexibleservers.operations.PrivateEndpointConnectionsOperations
    :ivar private_endpoint_connection: PrivateEndpointConnectionOperations operations
    :vartype private_endpoint_connection:
     azure.mgmt.postgresqlflexibleservers.operations.PrivateEndpointConnectionOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.postgresqlflexibleservers.operations.PrivateLinkResourcesOperations
    :ivar quota_usages: QuotaUsagesOperations operations
    :vartype quota_usages: azure.mgmt.postgresqlflexibleservers.operations.QuotaUsagesOperations
    :ivar replicas: ReplicasOperations operations
    :vartype replicas: azure.mgmt.postgresqlflexibleservers.operations.ReplicasOperations
    :ivar log_files: LogFilesOperations operations
    :vartype log_files: azure.mgmt.postgresqlflexibleservers.operations.LogFilesOperations
    :ivar server_threat_protection_settings: ServerThreatProtectionSettingsOperations operations
    :vartype server_threat_protection_settings:
     azure.mgmt.postgresqlflexibleservers.operations.ServerThreatProtectionSettingsOperations
    :ivar tuning_options: TuningOptionsOperations operations
    :vartype tuning_options:
     azure.mgmt.postgresqlflexibleservers.operations.TuningOptionsOperations
    :ivar virtual_endpoints: VirtualEndpointsOperations operations
    :vartype virtual_endpoints:
     azure.mgmt.postgresqlflexibleservers.operations.VirtualEndpointsOperations
    :ivar virtual_network_subnet_usage: VirtualNetworkSubnetUsageOperations operations
    :vartype virtual_network_subnet_usage:
     azure.mgmt.postgresqlflexibleservers.operations.VirtualNetworkSubnetUsageOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. The value must be an UUID. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2024-11-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = PostgreSQLManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                ARMAutoResourceProviderRegistrationPolicy(),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, policies=_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.administrators = AdministratorsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backups = BackupsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.location_based_capabilities = LocationBasedCapabilitiesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.server_capabilities = ServerCapabilitiesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.check_name_availability = CheckNameAvailabilityOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.check_name_availability_with_location = CheckNameAvailabilityWithLocationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.configurations = ConfigurationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.databases = DatabasesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.firewall_rules = FirewallRulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.servers = ServersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.flexible_server = FlexibleServerOperations(self._client, self._config, self._serialize, self._deserialize)
        self.ltr_backup_operations = LtrBackupOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.migrations = MigrationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.get_private_dns_zone_suffix = GetPrivateDnsZoneSuffixOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_endpoint_connection = PrivateEndpointConnectionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.quota_usages = QuotaUsagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.replicas = ReplicasOperations(self._client, self._config, self._serialize, self._deserialize)
        self.log_files = LogFilesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.server_threat_protection_settings = ServerThreatProtectionSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.tuning_options = TuningOptionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.virtual_endpoints = VirtualEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_network_subnet_usage = VirtualNetworkSubnetUsageOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
