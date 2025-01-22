# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.quota import QuotaMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestQuotaMgmtGroupQuotaLimitsRequestOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(QuotaMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_group_quota_limits_request_begin_update(self, resource_group):
        response = self.client.group_quota_limits_request.begin_update(
            management_group_id="str",
            group_quota_name="str",
            resource_provider_name="str",
            location="str",
            api_version="2024-12-18-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_group_quota_limits_request_get(self, resource_group):
        response = self.client.group_quota_limits_request.get(
            management_group_id="str",
            group_quota_name="str",
            request_id_parameter="str",
            api_version="2024-12-18-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_group_quota_limits_request_list(self, resource_group):
        response = self.client.group_quota_limits_request.list(
            management_group_id="str",
            group_quota_name="str",
            resource_provider_name="str",
            filter="str",
            api_version="2024-12-18-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
