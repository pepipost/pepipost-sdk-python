# -*- coding: utf-8 -*-

"""
    pepipost

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdaterecurringCredisofsubaccount(object):

    """Implementation of the 'UpdaterecurringCredisofsubaccount' model.

    Setrecurringcreditddetails modal

    Attributes:
        username (string): The username of the subaccount
        recurring_credit (int): The amount to be added periodically
        timeperiod (TimeperiodEnum): The periodic \n\nAllowed values 
            \"daily\", \"weekly\", \"monhtly\"
        start_date (string): The date from which the credit allocation will
            commence
        end_date (string): The last date of credit allocation
        status (string): Flag to enable or disable the recurring credit
            allocation

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "username":'username',
        "recurring_credit":'recurring_credit',
        "timeperiod":'timeperiod',
        "start_date":'start_date',
        "end_date":'end_date',
        "status":'status'
    }

    def __init__(self,
                 username=None,
                 recurring_credit=None,
                 timeperiod=None,
                 start_date=None,
                 end_date=None,
                 status=None):
        """Constructor for the UpdaterecurringCredisofsubaccount class"""

        # Initialize members of the class
        self.username = username
        self.recurring_credit = recurring_credit
        self.timeperiod = timeperiod
        self.start_date = start_date
        self.end_date = end_date
        self.status = status


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
        username = dictionary.get('username')
        recurring_credit = dictionary.get('recurring_credit')
        timeperiod = dictionary.get('timeperiod')
        start_date = dictionary.get('start_date')
        end_date = dictionary.get('end_date')
        status = dictionary.get('status')

        # Return an object of this model
        return cls(username,
                   recurring_credit,
                   timeperiod,
                   start_date,
                   end_date,
                   status)


