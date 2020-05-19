# -*- coding: utf-8 -*-

"""
    pepipost

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pepipost.models.attachments
import pepipost.models.email_struct

class Personalizations(object):

    """Implementation of the 'Personalizations' model.

    Personalizations

    Attributes:
        attributes (object): Dynamic attributes
        headers (object): Dynamic headers attributes
        attachments (list of Attachments): Attachments to individuals
            recipient
        to (list of EmailStruct): To email-address
        cc (list of EmailStruct): CC email-address
        bcc (list of EmailStruct): Bcc email-addresses
        token_to (string): token to which is json string
        token_cc (string): token cc which is json string
        token_bcc (string): token bcc which is json string

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "to":'to',
        "attributes":'attributes',
        "headers":'headers',
        "attachments":'attachments',
        "cc":'cc',
        "bcc":'bcc',
        "token_to":'token_to',
        "token_cc":'token_cc',
        "token_bcc":'token_bcc'
    }

    def __init__(self,
                 to=None,
                 attributes=None,
                 headers=None,
                 attachments=None,
                 cc=None,
                 bcc=None,
                 token_to=None,
                 token_cc=None,
                 token_bcc=None):
        """Constructor for the Personalizations class"""

        # Initialize members of the class
        self.attributes = attributes
        self.headers = headers
        self.attachments = attachments
        self.to = to
        self.cc = cc
        self.bcc = bcc
        self.token_to = token_to
        self.token_cc = token_cc
        self.token_bcc = token_bcc


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
        to = None
        if dictionary.get('to') != None:
            to = list()
            for structure in dictionary.get('to'):
                to.append(pepipost.models.email_struct.EmailStruct.from_dictionary(structure))
        attributes = dictionary.get('attributes')
        headers = dictionary.get('headers')
        attachments = None
        if dictionary.get('attachments') != None:
            attachments = list()
            for structure in dictionary.get('attachments'):
                attachments.append(pepipost.models.attachments.Attachments.from_dictionary(structure))
        cc = None
        if dictionary.get('cc') != None:
            cc = list()
            for structure in dictionary.get('cc'):
                cc.append(pepipost.models.email_struct.EmailStruct.from_dictionary(structure))
        bcc = None
        if dictionary.get('bcc') != None:
            bcc = list()
            for structure in dictionary.get('bcc'):
                bcc.append(pepipost.models.email_struct.EmailStruct.from_dictionary(structure))
        token_to = dictionary.get('token_to')
        token_cc = dictionary.get('token_cc')
        token_bcc = dictionary.get('token_bcc')

        # Return an object of this model
        return cls(to,
                   attributes,
                   headers,
                   attachments,
                   cc,
                   bcc,
                   token_to,
                   token_cc,
                   token_bcc)


