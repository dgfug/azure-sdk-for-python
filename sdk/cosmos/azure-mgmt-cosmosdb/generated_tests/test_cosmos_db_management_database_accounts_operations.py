# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.cosmosdb import CosmosDBManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCosmosDBManagementDatabaseAccountsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(CosmosDBManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.database_accounts.get(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-11-15",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update(self, resource_group):
        response = self.client.database_accounts.begin_update(
            resource_group_name=resource_group.name,
            account_name="str",
            update_parameters={
                "analyticalStorageConfiguration": {"schemaType": "str"},
                "apiProperties": {"serverVersion": "str"},
                "backupPolicy": "backup_policy",
                "capabilities": [{"name": "str"}],
                "capacity": {"totalThroughputLimit": 0},
                "connectorOffer": "str",
                "consistencyPolicy": {
                    "defaultConsistencyLevel": "str",
                    "maxIntervalInSeconds": 0,
                    "maxStalenessPrefix": 0,
                },
                "cors": [
                    {
                        "allowedOrigins": "str",
                        "allowedHeaders": "str",
                        "allowedMethods": "str",
                        "exposedHeaders": "str",
                        "maxAgeInSeconds": 0,
                    }
                ],
                "customerManagedKeyStatus": "str",
                "defaultIdentity": "str",
                "disableKeyBasedMetadataWriteAccess": bool,
                "disableLocalAuth": bool,
                "enableAnalyticalStorage": bool,
                "enableAutomaticFailover": bool,
                "enableBurstCapacity": bool,
                "enableCassandraConnector": bool,
                "enableFreeTier": bool,
                "enableMultipleWriteLocations": bool,
                "enablePartitionMerge": bool,
                "enablePerRegionPerPartitionAutoscale": bool,
                "identity": {
                    "principalId": "str",
                    "tenantId": "str",
                    "type": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "ipRules": [{"ipAddressOrRange": "str"}],
                "isVirtualNetworkFilterEnabled": bool,
                "keyVaultKeyUri": "str",
                "keysMetadata": {
                    "primaryMasterKey": {"generationTime": "2020-02-20 00:00:00"},
                    "primaryReadonlyMasterKey": {"generationTime": "2020-02-20 00:00:00"},
                    "secondaryMasterKey": {"generationTime": "2020-02-20 00:00:00"},
                    "secondaryReadonlyMasterKey": {"generationTime": "2020-02-20 00:00:00"},
                },
                "location": "str",
                "locations": [
                    {
                        "documentEndpoint": "str",
                        "failoverPriority": 0,
                        "id": "str",
                        "isZoneRedundant": bool,
                        "locationName": "str",
                        "provisioningState": "str",
                    }
                ],
                "minimalTlsVersion": "str",
                "networkAclBypass": "str",
                "networkAclBypassResourceIds": ["str"],
                "publicNetworkAccess": "str",
                "tags": {"str": "str"},
                "virtualNetworkRules": [{"id": "str", "ignoreMissingVNetServiceEndpoint": bool}],
            },
            api_version="2024-11-15",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.database_accounts.begin_create_or_update(
            resource_group_name=resource_group.name,
            account_name="str",
            create_update_parameters={
                "databaseAccountOfferType": "Standard",
                "locations": [
                    {
                        "documentEndpoint": "str",
                        "failoverPriority": 0,
                        "id": "str",
                        "isZoneRedundant": bool,
                        "locationName": "str",
                        "provisioningState": "str",
                    }
                ],
                "analyticalStorageConfiguration": {"schemaType": "str"},
                "apiProperties": {"serverVersion": "str"},
                "backupPolicy": "backup_policy",
                "capabilities": [{"name": "str"}],
                "capacity": {"totalThroughputLimit": 0},
                "connectorOffer": "str",
                "consistencyPolicy": {
                    "defaultConsistencyLevel": "str",
                    "maxIntervalInSeconds": 0,
                    "maxStalenessPrefix": 0,
                },
                "cors": [
                    {
                        "allowedOrigins": "str",
                        "allowedHeaders": "str",
                        "allowedMethods": "str",
                        "exposedHeaders": "str",
                        "maxAgeInSeconds": 0,
                    }
                ],
                "createMode": "Default",
                "customerManagedKeyStatus": "str",
                "defaultIdentity": "str",
                "disableKeyBasedMetadataWriteAccess": bool,
                "disableLocalAuth": bool,
                "enableAnalyticalStorage": bool,
                "enableAutomaticFailover": bool,
                "enableBurstCapacity": bool,
                "enableCassandraConnector": bool,
                "enableFreeTier": bool,
                "enableMultipleWriteLocations": bool,
                "enablePartitionMerge": bool,
                "enablePerRegionPerPartitionAutoscale": bool,
                "id": "str",
                "identity": {
                    "principalId": "str",
                    "tenantId": "str",
                    "type": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "ipRules": [{"ipAddressOrRange": "str"}],
                "isVirtualNetworkFilterEnabled": bool,
                "keyVaultKeyUri": "str",
                "keysMetadata": {
                    "primaryMasterKey": {"generationTime": "2020-02-20 00:00:00"},
                    "primaryReadonlyMasterKey": {"generationTime": "2020-02-20 00:00:00"},
                    "secondaryMasterKey": {"generationTime": "2020-02-20 00:00:00"},
                    "secondaryReadonlyMasterKey": {"generationTime": "2020-02-20 00:00:00"},
                },
                "kind": "str",
                "location": "str",
                "minimalTlsVersion": "str",
                "name": "str",
                "networkAclBypass": "str",
                "networkAclBypassResourceIds": ["str"],
                "publicNetworkAccess": "str",
                "restoreParameters": {
                    "databasesToRestore": [{"collectionNames": ["str"], "databaseName": "str"}],
                    "gremlinDatabasesToRestore": [{"databaseName": "str", "graphNames": ["str"]}],
                    "restoreMode": "str",
                    "restoreSource": "str",
                    "restoreTimestampInUtc": "2020-02-20 00:00:00",
                    "restoreWithTtlDisabled": bool,
                    "tablesToRestore": ["str"],
                },
                "tags": {"str": "str"},
                "type": "str",
                "virtualNetworkRules": [{"id": "str", "ignoreMissingVNetServiceEndpoint": bool}],
            },
            api_version="2024-11-15",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.database_accounts.begin_delete(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-11-15",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_failover_priority_change(self, resource_group):
        response = self.client.database_accounts.begin_failover_priority_change(
            resource_group_name=resource_group.name,
            account_name="str",
            failover_parameters={"failoverPolicies": [{"failoverPriority": 0, "id": "str", "locationName": "str"}]},
            api_version="2024-11-15",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.database_accounts.list(
            api_version="2024-11-15",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_resource_group(self, resource_group):
        response = self.client.database_accounts.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-11-15",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_keys(self, resource_group):
        response = self.client.database_accounts.list_keys(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-11-15",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_connection_strings(self, resource_group):
        response = self.client.database_accounts.list_connection_strings(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-11-15",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_offline_region(self, resource_group):
        response = self.client.database_accounts.begin_offline_region(
            resource_group_name=resource_group.name,
            account_name="str",
            region_parameter_for_offline={"region": "str"},
            api_version="2024-11-15",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_online_region(self, resource_group):
        response = self.client.database_accounts.begin_online_region(
            resource_group_name=resource_group.name,
            account_name="str",
            region_parameter_for_online={"region": "str"},
            api_version="2024-11-15",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get_read_only_keys(self, resource_group):
        response = self.client.database_accounts.get_read_only_keys(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-11-15",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_read_only_keys(self, resource_group):
        response = self.client.database_accounts.list_read_only_keys(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-11-15",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_regenerate_key(self, resource_group):
        response = self.client.database_accounts.begin_regenerate_key(
            resource_group_name=resource_group.name,
            account_name="str",
            key_to_regenerate={"keyKind": "str"},
            api_version="2024-11-15",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_check_name_exists(self, resource_group):
        response = self.client.database_accounts.check_name_exists(
            account_name="str",
            api_version="2024-11-15",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_metrics(self, resource_group):
        response = self.client.database_accounts.list_metrics(
            resource_group_name=resource_group.name,
            account_name="str",
            filter="str",
            api_version="2024-11-15",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_usages(self, resource_group):
        response = self.client.database_accounts.list_usages(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-11-15",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_metric_definitions(self, resource_group):
        response = self.client.database_accounts.list_metric_definitions(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-11-15",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
