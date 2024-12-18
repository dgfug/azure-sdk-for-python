# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.deviceregistry import DeviceRegistryMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-deviceregistry
# USAGE
    python create_discovered_asset_endpoint_profile.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DeviceRegistryMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.discovered_asset_endpoint_profiles.begin_create_or_replace(
        resource_group_name="myResourceGroup",
        discovered_asset_endpoint_profile_name="my-discoveredassetendpointprofile",
        resource={
            "extendedLocation": {
                "name": "/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/myResourceGroup/providers/microsoft.extendedlocation/customlocations/location1",
                "type": "CustomLocation",
            },
            "location": "West Europe",
            "properties": {
                "additionalConfiguration": '{"foo": "bar"}',
                "discoveryId": "11111111-1111-1111-1111-111111111111",
                "endpointProfileType": "myEndpointProfileType",
                "supportedAuthenticationMethods": ["Anonymous", "Certificate", "UsernamePassword"],
                "targetAddress": "https://www.example.com/myTargetAddress",
                "version": 73766,
            },
            "tags": {"site": "building-1"},
        },
    ).result()
    print(response)


# x-ms-original-file: 2024-09-01-preview/Create_DiscoveredAssetEndpointProfile.json
if __name__ == "__main__":
    main()
