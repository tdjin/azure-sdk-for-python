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

from msrest.serialization import Model


class ServiceDescription(Model):
    """A ServiceDescription contains all of the information necessary to create a
    service.

    :param application_name: The application name.
    :type application_name: str
    :param service_name: The service name.
    :type service_name: str
    :param service_type_name: The service type name.
    :type service_type_name: str
    :param initialization_data: The initialization data as an array of bytes.
     Initialization data is passed to service instances or replicas when they
     are created.
    :type initialization_data: list of int
    :param partition_description: The partition description as an object.
    :type partition_description: :class:`PartitionSchemeDescription
     <azure.servicefabric.models.PartitionSchemeDescription>`
    :param placement_constraints: The placement constraints as a string.
     Placement constraints are boolean expressions on node properties and
     allow for restricting a service to particular nodes based on the service
     requirements. For example, to place a service on nodes where NodeType is
     blue specify the following: "NodeColor == blue)".
    :type placement_constraints: str
    :param correlation_scheme: The correlation scheme.
    :type correlation_scheme: list of :class:`ServiceCorrelationDescription
     <azure.servicefabric.models.ServiceCorrelationDescription>`
    :param service_load_metrics: The service load metrics.
    :type service_load_metrics: list of :class:`ServiceLoadMetricDescription
     <azure.servicefabric.models.ServiceLoadMetricDescription>`
    :param service_placement_policies: The service placement policies.
    :type service_placement_policies: list of
     :class:`ServicePlacementPolicyDescription
     <azure.servicefabric.models.ServicePlacementPolicyDescription>`
    :param default_move_cost: The move cost for the service. Possible values
     include: 'Zero', 'Low', 'Medium', 'High'
    :type default_move_cost: str
    :param is_default_move_cost_specified: Indicates if the DefaultMoveCost
     property is specified.
    :type is_default_move_cost_specified: bool
    :param service_package_activation_mode: The activation mode of service
     package to be used for a service. Possible values include:
     'SharedProcess', 'ExclusiveProcess'
    :type service_package_activation_mode: str
    :param service_dns_name: The DNS name of the service. It requires the DNS
     system service to be enabled in Service Fabric cluster.
    :type service_dns_name: str
    :param ServiceKind: Polymorphic Discriminator
    :type ServiceKind: str
    """ 

    _validation = {
        'service_name': {'required': True},
        'service_type_name': {'required': True},
        'partition_description': {'required': True},
        'ServiceKind': {'required': True},
    }

    _attribute_map = {
        'application_name': {'key': 'ApplicationName', 'type': 'str'},
        'service_name': {'key': 'ServiceName', 'type': 'str'},
        'service_type_name': {'key': 'ServiceTypeName', 'type': 'str'},
        'initialization_data': {'key': 'InitializationData', 'type': '[int]'},
        'partition_description': {'key': 'PartitionDescription', 'type': 'PartitionSchemeDescription'},
        'placement_constraints': {'key': 'PlacementConstraints', 'type': 'str'},
        'correlation_scheme': {'key': 'CorrelationScheme', 'type': '[ServiceCorrelationDescription]'},
        'service_load_metrics': {'key': 'ServiceLoadMetrics', 'type': '[ServiceLoadMetricDescription]'},
        'service_placement_policies': {'key': 'ServicePlacementPolicies', 'type': '[ServicePlacementPolicyDescription]'},
        'default_move_cost': {'key': 'DefaultMoveCost', 'type': 'str'},
        'is_default_move_cost_specified': {'key': 'IsDefaultMoveCostSpecified', 'type': 'bool'},
        'service_package_activation_mode': {'key': 'ServicePackageActivationMode', 'type': 'str'},
        'service_dns_name': {'key': 'ServiceDnsName', 'type': 'str'},
        'ServiceKind': {'key': 'ServiceKind', 'type': 'str'},
    }

    _subtype_map = {
        'ServiceKind': {'Stateful': 'StatefulServiceDescription', 'Stateless': 'StatelessServiceDescription'}
    }

    def __init__(self, service_name, service_type_name, partition_description, application_name=None, initialization_data=None, placement_constraints=None, correlation_scheme=None, service_load_metrics=None, service_placement_policies=None, default_move_cost=None, is_default_move_cost_specified=None, service_package_activation_mode=None, service_dns_name=None):
        self.application_name = application_name
        self.service_name = service_name
        self.service_type_name = service_type_name
        self.initialization_data = initialization_data
        self.partition_description = partition_description
        self.placement_constraints = placement_constraints
        self.correlation_scheme = correlation_scheme
        self.service_load_metrics = service_load_metrics
        self.service_placement_policies = service_placement_policies
        self.default_move_cost = default_move_cost
        self.is_default_move_cost_specified = is_default_move_cost_specified
        self.service_package_activation_mode = service_package_activation_mode
        self.service_dns_name = service_dns_name
        self.ServiceKind = None
