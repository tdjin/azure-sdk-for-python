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


class ClusterManifest(Model):
    """Information about the cluster manifest.

    :param manifest: The contents of the cluster manifest file.
    :type manifest: str
    """ 

    _attribute_map = {
        'manifest': {'key': 'Manifest', 'type': 'str'},
    }

    def __init__(self, manifest=None):
        self.manifest = manifest
