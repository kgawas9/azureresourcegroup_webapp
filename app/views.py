from django.shortcuts import render

from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient

from django.conf import settings

# Create your views here.

def get_resource_groups():
    """Read the resource groups and return it to the main function."""
    credentials = ClientSecretCredential(
        client_id=settings.CLIENT_ID,
        tenant_id=settings.TENANT_ID,
        client_secret=settings.SECRET_KEY,
    )

    subscription_id = settings.SUBSCRIPTION_ID

    resource_client = ResourceManagementClient(credential=credentials, subscription_id=subscription_id)
    resource_groups = resource_client.resource_groups.list()

    resource_groups_list = []

    for resource_group in resource_groups:
        resource_groups_list.append(resource_group)

    return resource_groups_list

def read_resource_groups(request):
    """Read the resource group based on the given subscription id."""

    resource_groups = get_resource_groups()

    context = {
        'resource_groups': resource_groups,
    }
    return render(request, 'app/resource-groups.html', context=context)
