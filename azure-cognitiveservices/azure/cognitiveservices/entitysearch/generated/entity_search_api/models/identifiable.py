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

from .response_base import ResponseBase


class Identifiable(ResponseBase):
    """Identifiable.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param _type: Polymorphic Discriminator
    :type _type: str
    :ivar id:
    :vartype id: str
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
    }

    _subtype_map = {
        '_type': {'Response': 'Response'}
    }

    def __init__(self):
        super(Identifiable, self).__init__()
        self.id = None
        self._type = 'Identifiable'
