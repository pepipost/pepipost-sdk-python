# -*- coding: utf-8 -*-

"""
    pepipost.models.attributes

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""

from ..api_helper import APIHelper
class Xheaders:

    """Implementation of the 'Attributes' model.

    TODO: type model description here.

    Attributes:
        xheaders (string): TODO: type description here.
    """

    def __init__(self,
                 xheaders):
        """Constructor for the xheaders class"""

        # Initialize members of the class
        self.xheaders = xheaders


    def get_xheaders(self):
        """Creates an instance of this model from a dictionary

        Args:
            JSON (string): A key value pair json string.

        Returns:
            dictionary : dictionary mapping of passed xheaders

        """

        if self.xheaders == "" or self.xheaders == None:
            return None

        return APIHelper.json_deserialize(self.xheaders)

