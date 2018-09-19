# -*- coding: utf-8 -*-

"""
    pepipost.models.settings

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class Settings(object):

    """Implementation of the 'Settings' model.

    TODO: type model description here.

    Attributes:
        footer (int): TODO: type description here.
        clicktrack (int): TODO: type description here.
        opentrack (int): TODO: type description here.
        unsubscribe (int): TODO: type description here.
        bcc (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "footer":'footer',
        "clicktrack":'clicktrack',
        "opentrack":'opentrack',
        "unsubscribe":'unsubscribe',
        "bcc":'bcc'
    }

    def __init__(self,
                 footer=None,
                 clicktrack=None,
                 opentrack=None,
                 unsubscribe=None,
                 bcc=None):
        """Constructor for the Settings class"""

        # Initialize members of the class
        self.footer = footer
        self.clicktrack = clicktrack
        self.opentrack = opentrack
        self.unsubscribe = unsubscribe
        self.bcc = bcc


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        footer = dictionary.get('footer')
        clicktrack = dictionary.get('clicktrack')
        opentrack = dictionary.get('opentrack')
        unsubscribe = dictionary.get('unsubscribe')
        bcc = dictionary.get('bcc')

        # Return an object of this model
        return cls(footer,
                   clicktrack,
                   opentrack,
                   unsubscribe,
                   bcc)

