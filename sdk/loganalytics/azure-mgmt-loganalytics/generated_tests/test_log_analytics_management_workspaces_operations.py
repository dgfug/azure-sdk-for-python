# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.loganalytics import LogAnalyticsManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestLogAnalyticsManagementWorkspacesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(LogAnalyticsManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.workspaces.list(
            api_version="2022-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_resource_group(self, resource_group):
        response = self.client.workspaces.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2022-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.workspaces.begin_create_or_update(
            resource_group_name=resource_group.name,
            workspace_name="str",
            parameters={
                "location": "str",
                "createdDate": "str",
                "customerId": "str",
                "defaultDataCollectionRuleResourceId": "str",
                "etag": "str",
                "features": {
                    "clusterResourceId": "str",
                    "disableLocalAuth": bool,
                    "enableDataExport": bool,
                    "enableLogAccessUsingOnlyResourcePermissions": bool,
                    "immediatePurgeDataOn30Days": bool,
                },
                "forceCmkForQuery": bool,
                "id": "str",
                "identity": {
                    "type": "str",
                    "principalId": "str",
                    "tenantId": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "modifiedDate": "str",
                "name": "str",
                "privateLinkScopedResources": [{"resourceId": "str", "scopeId": "str"}],
                "provisioningState": "str",
                "publicNetworkAccessForIngestion": "Enabled",
                "publicNetworkAccessForQuery": "Enabled",
                "retentionInDays": 0,
                "sku": {"name": "str", "capacityReservationLevel": 0, "lastSkuUpdate": "str"},
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tags": {"str": "str"},
                "type": "str",
                "workspaceCapping": {"dailyQuotaGb": 0.0, "dataIngestionStatus": "str", "quotaNextResetTime": "str"},
            },
            api_version="2022-10-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.workspaces.begin_delete(
            resource_group_name=resource_group.name,
            workspace_name="str",
            api_version="2022-10-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.workspaces.get(
            resource_group_name=resource_group.name,
            workspace_name="str",
            api_version="2022-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_update(self, resource_group):
        response = self.client.workspaces.update(
            resource_group_name=resource_group.name,
            workspace_name="str",
            parameters={
                "createdDate": "str",
                "customerId": "str",
                "defaultDataCollectionRuleResourceId": "str",
                "etag": "str",
                "features": {
                    "clusterResourceId": "str",
                    "disableLocalAuth": bool,
                    "enableDataExport": bool,
                    "enableLogAccessUsingOnlyResourcePermissions": bool,
                    "immediatePurgeDataOn30Days": bool,
                },
                "forceCmkForQuery": bool,
                "id": "str",
                "identity": {
                    "type": "str",
                    "principalId": "str",
                    "tenantId": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "modifiedDate": "str",
                "name": "str",
                "privateLinkScopedResources": [{"resourceId": "str", "scopeId": "str"}],
                "provisioningState": "str",
                "publicNetworkAccessForIngestion": "Enabled",
                "publicNetworkAccessForQuery": "Enabled",
                "retentionInDays": 0,
                "sku": {"name": "str", "capacityReservationLevel": 0, "lastSkuUpdate": "str"},
                "tags": {"str": "str"},
                "type": "str",
                "workspaceCapping": {"dailyQuotaGb": 0.0, "dataIngestionStatus": "str", "quotaNextResetTime": "str"},
            },
            api_version="2022-10-01",
        )

        # please add some check logic here by yourself
        # ...
