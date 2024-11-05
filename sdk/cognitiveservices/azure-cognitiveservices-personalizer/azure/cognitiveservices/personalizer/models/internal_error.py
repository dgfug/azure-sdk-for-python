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


class InternalError(Model):
    """An object containing more specific information than the parent object about
    the error.

    :param code: Detailed error code.
    :type code: str
    :param innererror: The error object.
    :type innererror:
     ~azure.cognitiveservices.personalizer.models.InternalError
    """

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "innererror": {"key": "innererror", "type": "InternalError"},
    }

    def __init__(self, **kwargs):
        super(InternalError, self).__init__(**kwargs)
        self.code = kwargs.get("code", None)
        self.innererror = kwargs.get("innererror", None)
