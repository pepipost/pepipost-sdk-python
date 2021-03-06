# -*- coding: utf-8 -*-

"""
    pepipost

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Attachments(object):

    """Implementation of the 'Attachments' model.

    Attachments

    Attributes:
        content (string): Base64 encoded value of the attached file
        name (string): filename of attachments

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "content":'content',
        "name":'name'
    }

    def __init__(self,
                 content=None,
                 name=None):
        """Constructor for the Attachments class"""

        # Initialize members of the class
        self.content = content
        self.name = name


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
        content = dictionary.get('content')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(content,
                   name)


