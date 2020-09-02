# -*- coding: utf-8 -*-

"""
    pepipost

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class AddemailordomaintoSuppressionlist(object):

    """Implementation of the 'AddemailordomaintoSuppressionlist' model.

    Add Suppression modal

    Attributes:
        domain (string): Add the domain to be suppressed here. We will not
            deliver emails to recipients email addresses with this
            domain.<br>\nComma separate the values to suppress multiple
            domains..
        email (string): Add an email address to be suppressed here. We will
            not deliver emails to this email address.<br>\nComma separate the
            values to suppress multiple email addresses

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain":'domain',
        "email":'email'
    }

    def __init__(self,
                 domain=None,
                 email=None):
        """Constructor for the AddemailordomaintoSuppressionlist class"""

        # Initialize members of the class
        self.domain = domain
        self.email = email


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
        domain = dictionary.get('domain')
        email = dictionary.get('email')

        # Return an object of this model
        return cls(domain,
                   email)

