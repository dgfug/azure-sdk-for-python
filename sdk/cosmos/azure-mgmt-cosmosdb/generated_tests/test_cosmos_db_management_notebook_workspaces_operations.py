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
class TestCosmosDBManagementNotebookWorkspacesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(CosmosDBManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_database_account(self, resource_group):
        response = self.client.notebook_workspaces.list_by_database_account(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-11-15",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.notebook_workspaces.get(
            resource_group_name=resource_group.name,
            account_name="str",
            notebook_workspace_name="str",
            api_version="2024-11-15",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.notebook_workspaces.begin_create_or_update(
            resource_group_name=resource_group.name,
            account_name="str",
            notebook_workspace_name="str",
            notebook_create_update_parameters={"id": "str", "name": "str", "type": "str"},
            api_version="2024-11-15",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.notebook_workspaces.begin_delete(
            resource_group_name=resource_group.name,
            account_name="str",
            notebook_workspace_name="str",
            api_version="2024-11-15",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_connection_info(self, resource_group):
        response = self.client.notebook_workspaces.list_connection_info(
            resource_group_name=resource_group.name,
            account_name="str",
            notebook_workspace_name="str",
            api_version="2024-11-15",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_regenerate_auth_token(self, resource_group):
        response = self.client.notebook_workspaces.begin_regenerate_auth_token(
            resource_group_name=resource_group.name,
            account_name="str",
            notebook_workspace_name="str",
            api_version="2024-11-15",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_start(self, resource_group):
        response = self.client.notebook_workspaces.begin_start(
            resource_group_name=resource_group.name,
            account_name="str",
            notebook_workspace_name="str",
            api_version="2024-11-15",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
