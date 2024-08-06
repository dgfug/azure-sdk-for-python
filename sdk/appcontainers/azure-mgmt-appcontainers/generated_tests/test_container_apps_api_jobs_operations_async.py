# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.appcontainers.aio import ContainerAppsAPIClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestContainerAppsAPIJobsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ContainerAppsAPIClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_detectors(self, resource_group):
        response = self.client.jobs.list_detectors(
            resource_group_name=resource_group.name,
            job_name="str",
            api_version="2024-03-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get_detector(self, resource_group):
        response = await self.client.jobs.get_detector(
            resource_group_name=resource_group.name,
            job_name="str",
            detector_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_proxy_get(self, resource_group):
        response = await self.client.jobs.proxy_get(
            resource_group_name=resource_group.name,
            job_name="str",
            api_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_subscription(self, resource_group):
        response = self.client.jobs.list_by_subscription(
            api_version="2024-03-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_resource_group(self, resource_group):
        response = self.client.jobs.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-03-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.jobs.get(
            resource_group_name=resource_group.name,
            job_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.jobs.begin_create_or_update(
                resource_group_name=resource_group.name,
                job_name="str",
                job_envelope={
                    "location": "str",
                    "configuration": {
                        "replicaTimeout": 0,
                        "triggerType": "Manual",
                        "eventTriggerConfig": {
                            "parallelism": 0,
                            "replicaCompletionCount": 0,
                            "scale": {
                                "maxExecutions": 100,
                                "minExecutions": 0,
                                "pollingInterval": 0,
                                "rules": [
                                    {
                                        "auth": [{"secretRef": "str", "triggerParameter": "str"}],
                                        "metadata": {},
                                        "name": "str",
                                        "type": "str",
                                    }
                                ],
                            },
                        },
                        "manualTriggerConfig": {"parallelism": 0, "replicaCompletionCount": 0},
                        "registries": [
                            {"identity": "str", "passwordSecretRef": "str", "server": "str", "username": "str"}
                        ],
                        "replicaRetryLimit": 0,
                        "scheduleTriggerConfig": {
                            "cronExpression": "str",
                            "parallelism": 0,
                            "replicaCompletionCount": 0,
                        },
                        "secrets": [{"identity": "str", "keyVaultUrl": "str", "name": "str", "value": "str"}],
                    },
                    "environmentId": "str",
                    "eventStreamEndpoint": "str",
                    "id": "str",
                    "identity": {
                        "type": "str",
                        "principalId": "str",
                        "tenantId": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "name": "str",
                    "outboundIpAddresses": ["str"],
                    "provisioningState": "str",
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "tags": {"str": "str"},
                    "template": {
                        "containers": [
                            {
                                "args": ["str"],
                                "command": ["str"],
                                "env": [{"name": "str", "secretRef": "str", "value": "str"}],
                                "image": "str",
                                "name": "str",
                                "probes": [
                                    {
                                        "failureThreshold": 0,
                                        "httpGet": {
                                            "port": 0,
                                            "host": "str",
                                            "httpHeaders": [{"name": "str", "value": "str"}],
                                            "path": "str",
                                            "scheme": "str",
                                        },
                                        "initialDelaySeconds": 0,
                                        "periodSeconds": 0,
                                        "successThreshold": 0,
                                        "tcpSocket": {"port": 0, "host": "str"},
                                        "terminationGracePeriodSeconds": 0,
                                        "timeoutSeconds": 0,
                                        "type": "str",
                                    }
                                ],
                                "resources": {"cpu": 0.0, "ephemeralStorage": "str", "memory": "str"},
                                "volumeMounts": [{"mountPath": "str", "subPath": "str", "volumeName": "str"}],
                            }
                        ],
                        "initContainers": [
                            {
                                "args": ["str"],
                                "command": ["str"],
                                "env": [{"name": "str", "secretRef": "str", "value": "str"}],
                                "image": "str",
                                "name": "str",
                                "resources": {"cpu": 0.0, "ephemeralStorage": "str", "memory": "str"},
                                "volumeMounts": [{"mountPath": "str", "subPath": "str", "volumeName": "str"}],
                            }
                        ],
                        "volumes": [
                            {
                                "mountOptions": "str",
                                "name": "str",
                                "secrets": [{"path": "str", "secretRef": "str"}],
                                "storageName": "str",
                                "storageType": "str",
                            }
                        ],
                    },
                    "type": "str",
                    "workloadProfileName": "str",
                },
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.jobs.begin_delete(
                resource_group_name=resource_group.name,
                job_name="str",
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_update(self, resource_group):
        response = await (
            await self.client.jobs.begin_update(
                resource_group_name=resource_group.name,
                job_name="str",
                job_envelope={
                    "identity": {
                        "type": "str",
                        "principalId": "str",
                        "tenantId": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "properties": {
                        "configuration": {
                            "replicaTimeout": 0,
                            "triggerType": "Manual",
                            "eventTriggerConfig": {
                                "parallelism": 0,
                                "replicaCompletionCount": 0,
                                "scale": {
                                    "maxExecutions": 100,
                                    "minExecutions": 0,
                                    "pollingInterval": 0,
                                    "rules": [
                                        {
                                            "auth": [{"secretRef": "str", "triggerParameter": "str"}],
                                            "metadata": {},
                                            "name": "str",
                                            "type": "str",
                                        }
                                    ],
                                },
                            },
                            "manualTriggerConfig": {"parallelism": 0, "replicaCompletionCount": 0},
                            "registries": [
                                {"identity": "str", "passwordSecretRef": "str", "server": "str", "username": "str"}
                            ],
                            "replicaRetryLimit": 0,
                            "scheduleTriggerConfig": {
                                "cronExpression": "str",
                                "parallelism": 0,
                                "replicaCompletionCount": 0,
                            },
                            "secrets": [{"identity": "str", "keyVaultUrl": "str", "name": "str", "value": "str"}],
                        },
                        "environmentId": "str",
                        "eventStreamEndpoint": "str",
                        "outboundIpAddresses": ["str"],
                        "template": {
                            "containers": [
                                {
                                    "args": ["str"],
                                    "command": ["str"],
                                    "env": [{"name": "str", "secretRef": "str", "value": "str"}],
                                    "image": "str",
                                    "name": "str",
                                    "probes": [
                                        {
                                            "failureThreshold": 0,
                                            "httpGet": {
                                                "port": 0,
                                                "host": "str",
                                                "httpHeaders": [{"name": "str", "value": "str"}],
                                                "path": "str",
                                                "scheme": "str",
                                            },
                                            "initialDelaySeconds": 0,
                                            "periodSeconds": 0,
                                            "successThreshold": 0,
                                            "tcpSocket": {"port": 0, "host": "str"},
                                            "terminationGracePeriodSeconds": 0,
                                            "timeoutSeconds": 0,
                                            "type": "str",
                                        }
                                    ],
                                    "resources": {"cpu": 0.0, "ephemeralStorage": "str", "memory": "str"},
                                    "volumeMounts": [{"mountPath": "str", "subPath": "str", "volumeName": "str"}],
                                }
                            ],
                            "initContainers": [
                                {
                                    "args": ["str"],
                                    "command": ["str"],
                                    "env": [{"name": "str", "secretRef": "str", "value": "str"}],
                                    "image": "str",
                                    "name": "str",
                                    "resources": {"cpu": 0.0, "ephemeralStorage": "str", "memory": "str"},
                                    "volumeMounts": [{"mountPath": "str", "subPath": "str", "volumeName": "str"}],
                                }
                            ],
                            "volumes": [
                                {
                                    "mountOptions": "str",
                                    "name": "str",
                                    "secrets": [{"path": "str", "secretRef": "str"}],
                                    "storageName": "str",
                                    "storageType": "str",
                                }
                            ],
                        },
                    },
                    "tags": {"str": "str"},
                },
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_start(self, resource_group):
        response = await (
            await self.client.jobs.begin_start(
                resource_group_name=resource_group.name,
                job_name="str",
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_stop_execution(self, resource_group):
        response = await (
            await self.client.jobs.begin_stop_execution(
                resource_group_name=resource_group.name,
                job_name="str",
                job_execution_name="str",
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_stop_multiple_executions(self, resource_group):
        response = await (
            await self.client.jobs.begin_stop_multiple_executions(
                resource_group_name=resource_group.name,
                job_name="str",
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_secrets(self, resource_group):
        response = await self.client.jobs.list_secrets(
            resource_group_name=resource_group.name,
            job_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...
