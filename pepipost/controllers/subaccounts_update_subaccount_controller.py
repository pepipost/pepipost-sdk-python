# -*- coding: utf-8 -*-

"""
    pepipost

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from pepipost.api_helper import APIHelper
from pepipost.configuration import Configuration
from pepipost.controllers.base_controller import BaseController
from pepipost.http.auth.custom_header_auth import CustomHeaderAuth
from pepipost.exceptions.api_exception import APIException

class SubaccountsUpdateSubaccountController(BaseController):

    """A Controller to access Endpoints in the pepipost API."""


    def create_subaccounts_update_subaccount_post(self,
                                                  body):
        """Does a POST request to /subaccounts/updateSubaccount.

        lets you update credentials and credit type of a subaccount.

        Args:
            body (Updatesubaccount): Update sub account

        Returns:
            object: Response from the API. API Response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/subaccounts/updateSubaccount'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('API Response', _context)
        elif _context.response.status_code == 401:
            raise APIException('API Response', _context)
        elif _context.response.status_code == 403:
            raise APIException('API Response', _context)
        elif _context.response.status_code == 405:
            raise APIException('Invalid input', _context)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
