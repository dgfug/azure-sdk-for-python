# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.deviceregistry.aio import DeviceRegistryMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDeviceRegistryMgmtSchemaVersionsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DeviceRegistryMgmtClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_schema_versions_get(self, resource_group):
        response = await self.client.schema_versions.get(
            resource_group_name=resource_group.name,
            schema_registry_name="str",
            schema_name="str",
            schema_version_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_schema_versions_create_or_replace(self, resource_group):
        response = await self.client.schema_versions.create_or_replace(
            resource_group_name=resource_group.name,
            schema_registry_name="str",
            schema_name="str",
            schema_version_name="str",
            resource={
                "id": "str",
                "name": "str",
                "properties": {
                    "schemaContent": "str",
                    "description": "str",
                    "hash": "str",
                    "provisioningState": "str",
                    "uuid": "str",
                },
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_schema_versions_delete(self, resource_group):
        response = await self.client.schema_versions.delete(
            resource_group_name=resource_group.name,
            schema_registry_name="str",
            schema_name="str",
            schema_version_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_schema_versions_list_by_schema(self, resource_group):
        response = self.client.schema_versions.list_by_schema(
            resource_group_name=resource_group.name,
            schema_registry_name="str",
            schema_name="str",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
