# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.redis import RedisManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRedisManagementLinkedServerOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(RedisManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_linked_server_begin_create(self, resource_group):
        response = self.client.linked_server.begin_create(
            resource_group_name=resource_group.name,
            name="str",
            linked_server_name="str",
            parameters={
                "linkedRedisCacheId": "str",
                "linkedRedisCacheLocation": "str",
                "serverRole": "str",
                "geoReplicatedPrimaryHostName": "str",
                "primaryHostName": "str",
            },
            api_version="2024-11-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_linked_server_begin_delete(self, resource_group):
        response = self.client.linked_server.begin_delete(
            resource_group_name=resource_group.name,
            name="str",
            linked_server_name="str",
            api_version="2024-11-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_linked_server_get(self, resource_group):
        response = self.client.linked_server.get(
            resource_group_name=resource_group.name,
            name="str",
            linked_server_name="str",
            api_version="2024-11-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_linked_server_list(self, resource_group):
        response = self.client.linked_server.list(
            resource_group_name=resource_group.name,
            name="str",
            api_version="2024-11-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
