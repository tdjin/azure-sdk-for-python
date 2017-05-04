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


class ServicePlacementPolicyDescription(Model):
    """Describes the policy to be used for placement of a Service Fabric service.

    :param Type: Polymorphic Discriminator
    :type Type: str
    """ 

    _validation = {
        'Type': {'required': True},
    }

    _attribute_map = {
        'Type': {'key': 'Type', 'type': 'str'},
    }

    _subtype_map = {
        'Type': {'InvalidDomain': 'ServicePlacementInvalidDomainPolicyDescription', 'NonPartiallyPlaceService': 'ServicePlacementNonPartiallyPlaceServicePolicyDescription', 'PreferPrimaryDomain': 'ServicePlacementPreferPrimaryDomainPolicyDescription', 'RequireDomain': 'ServicePlacementRequiredDomainPolicyDescription', 'RequireDomainDistribution': 'ServicePlacementRequireDomainDistributionPolicyDescription'}
    }

    def __init__(self):
        self.Type = None
