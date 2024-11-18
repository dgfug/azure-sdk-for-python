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
class TestCosmosDBManagementDatabaseOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(CosmosDBManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_metrics(self, resource_group):
        response = self.client.database.list_metrics(
            resource_group_name=resource_group.name,
            account_name="str",
            database_rid="str",
            filter="str",
            api_version="2024-11-15",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_usages(self, resource_group):
        response = self.client.database.list_usages(
            resource_group_name=resource_group.name,
            account_name="str",
            database_rid="str",
            api_version="2024-11-15",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_metric_definitions(self, resource_group):
        response = self.client.database.list_metric_definitions(
            resource_group_name=resource_group.name,
            account_name="str",
            database_rid="str",
            api_version="2024-11-15",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
