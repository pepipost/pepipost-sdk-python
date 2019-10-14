# -*- coding: utf-8 -*-

"""
    pepipost.models.personalizations

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
import pepipost.models.attachments

class Personalizations(object):

    """Implementation of the 'Personalizations' model.

    This consits of personlized attachments with recipient,recipient_cc,etc.

    Attributes:
        recipient (string): Emails to be passed in Apicall
        x_apiheader_cc (string): TODO: type description here.
        x_apiheader (string): TODO: type description here.
        attributes (object): TODO: type description here.
        attachments (list of Attachments): TODO: type description here.
        recipient_cc (list of string): TODO: type description here.
        recipient_bcc (list of string): TODO: type description here.
        x_headers (object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "recipient":'recipient',
        "x_apiheader_cc":'x-apiheader_cc',
        "x_apiheader":'x-apiheader',
        "attributes":'attributes',
        "attachments":'attachments',
        "recipient_cc":'recipient_cc',
        "recipient_bcc":'recipient_bcc',
        "x_headers":'x-headers'
    }

    def __init__(self,
                 recipient=None,
                 x_apiheader_cc=None,
                 x_apiheader=None,
                 attributes=None,
                 attachments=None,
                 recipient_cc=None,
                 recipient_bcc=None,
                 x_headers=None):
        """Constructor for the Personalizations class"""

        # Initialize members of the class
        self.recipient = recipient
        self.x_apiheader_cc = x_apiheader_cc
        self.x_apiheader = x_apiheader
        self.attributes = attributes
        self.attachments = attachments
        self.recipient_cc = recipient_cc
        self.recipient_bcc = recipient_bcc
        self.x_headers = x_headers


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
        recipient = dictionary.get('recipient')
        x_apiheader_cc = dictionary.get('x-apiheader_cc')
        x_apiheader = dictionary.get('x-apiheader')
        attributes = dictionary.get('attributes')
        attachments = None
        if dictionary.get('attachments') != None:
            attachments = list()
            for structure in dictionary.get('attachments'):
                attachments.append(pepipost.models.attachments.Attachments.from_dictionary(structure))
        recipient_cc = dictionary.get('recipient_cc')
        recipient_bcc = dictionary.get('recipient_bcc')
        x_headers = dictionary.get('x-headers')

        # Return an object of this model
        return cls(recipient,
                   x_apiheader_cc,
                   x_apiheader,
                   attributes,
                   attachments,
                   recipient_cc,
                   recipient_bcc,
                   x_headers)


