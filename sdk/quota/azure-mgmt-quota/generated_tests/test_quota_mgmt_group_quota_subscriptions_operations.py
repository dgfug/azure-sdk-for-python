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
class TestQuotaMgmtGroupQuotaSubscriptionsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(QuotaMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_group_quota_subscriptions_begin_create_or_update(self, resource_group):
        response = self.client.group_quota_subscriptions.begin_create_or_update(
            management_group_id="str",
            group_quota_name="str",
            api_version="2024-12-18-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_group_quota_subscriptions_begin_update(self, resource_group):
        response = self.client.group_quota_subscriptions.begin_update(
            management_group_id="str",
            group_quota_name="str",
            api_version="2024-12-18-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_group_quota_subscriptions_begin_delete(self, resource_group):
        response = self.client.group_quota_subscriptions.begin_delete(
            management_group_id="str",
            group_quota_name="str",
            api_version="2024-12-18-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_group_quota_subscriptions_get(self, resource_group):
        response = self.client.group_quota_subscriptions.get(
            management_group_id="str",
            group_quota_name="str",
            api_version="2024-12-18-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_group_quota_subscriptions_list(self, resource_group):
        response = self.client.group_quota_subscriptions.list(
            management_group_id="str",
            group_quota_name="str",
            api_version="2024-12-18-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
