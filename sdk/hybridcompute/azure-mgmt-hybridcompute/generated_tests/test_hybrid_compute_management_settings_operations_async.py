# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.hybridcompute.aio import HybridComputeManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestHybridComputeManagementSettingsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(HybridComputeManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.settings.get(
            resource_group_name=resource_group.name,
            base_provider="str",
            base_resource_type="str",
            base_resource_name="str",
            settings_resource_name="str",
            api_version="2024-07-31-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_update(self, resource_group):
        response = await self.client.settings.update(
            resource_group_name=resource_group.name,
            base_provider="str",
            base_resource_type="str",
            base_resource_name="str",
            settings_resource_name="str",
            parameters={
                "gatewayResourceId": "str",
                "id": "str",
                "name": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tenantId": "str",
                "type": "str",
            },
            api_version="2024-07-31-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_patch(self, resource_group):
        response = await self.client.settings.patch(
            resource_group_name=resource_group.name,
            base_provider="str",
            base_resource_type="str",
            base_resource_name="str",
            settings_resource_name="str",
            parameters={
                "gatewayResourceId": "str",
                "id": "str",
                "name": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tenantId": "str",
                "type": "str",
            },
            api_version="2024-07-31-preview",
        )

        # please add some check logic here by yourself
        # ...
