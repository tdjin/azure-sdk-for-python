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

from .contractual_rules_attribution import ContractualRulesAttribution


class ContractualRulesLicenseAttribution(ContractualRulesAttribution):
    """Defines a contractual rule for license attribution.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar target_property_name: The name of the field that the rule applies
     to.
    :vartype target_property_name: str
    :param _type: Polymorphic Discriminator
    :type _type: str
    :ivar must_be_close_to_content: A Boolean value that determines whether
     the contents of the rule must be placed in close proximity to the field
     that the rule applies to. If true, the contents must be placed in close
     proximity. If false, or this field does not exist, the contents may be
     placed at the caller's discretion.
    :vartype must_be_close_to_content: bool
    :ivar license: The license under which the content may be used.
    :vartype license: :class:`License <entitysearch2.models.License>`
    :ivar license_notice: The license to display next to the targeted field.
    :vartype license_notice: str
    """

    _validation = {
        'target_property_name': {'readonly': True},
        '_type': {'required': True},
        'must_be_close_to_content': {'readonly': True},
        'license': {'readonly': True},
        'license_notice': {'readonly': True},
    }

    _attribute_map = {
        'target_property_name': {'key': 'targetPropertyName', 'type': 'str'},
        '_type': {'key': '_type', 'type': 'str'},
        'must_be_close_to_content': {'key': 'mustBeCloseToContent', 'type': 'bool'},
        'license': {'key': 'license', 'type': 'License'},
        'license_notice': {'key': 'licenseNotice', 'type': 'str'},
    }

    def __init__(self):
        super(ContractualRulesLicenseAttribution, self).__init__()
        self.license = None
        self.license_notice = None
        self._type = 'ContractualRules/LicenseAttribution'
