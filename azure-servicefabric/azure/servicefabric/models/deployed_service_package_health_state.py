# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .entity_health_state import EntityHealthState


class DeployedServicePackageHealthState(EntityHealthState):
    """Represents the health state of a deployed service package, containing the
    entity identifier and the aggregated health state.

    :param aggregated_health_state: Possible values include: 'Invalid', 'Ok',
     'Warning', 'Error', 'Unknown'
    :type aggregated_health_state: str
    :param node_name: Name of the node on which the service package is
     deployed.
    :type node_name: str
    :param application_name: Full name of the application.
    :type application_name: str
    :param service_manifest_name: Name of the manifest describing the service
     package.
    :type service_manifest_name: str
    :param service_package_activation_id:
    :type service_package_activation_id: str
    """ 

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'node_name': {'key': 'NodeName', 'type': 'str'},
        'application_name': {'key': 'ApplicationName', 'type': 'str'},
        'service_manifest_name': {'key': 'ServiceManifestName', 'type': 'str'},
        'service_package_activation_id': {'key': 'ServicePackageActivationId', 'type': 'str'},
    }

    def __init__(self, aggregated_health_state=None, node_name=None, application_name=None, service_manifest_name=None, service_package_activation_id=None):
        super(DeployedServicePackageHealthState, self).__init__(aggregated_health_state=aggregated_health_state)
        self.node_name = node_name
        self.application_name = application_name
        self.service_manifest_name = service_manifest_name
        self.service_package_activation_id = service_package_activation_id
