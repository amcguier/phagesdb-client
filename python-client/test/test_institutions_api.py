# coding: utf-8

"""
    PhagesDB API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import phagesdb_client
from phagesdb_client.api.institutions_api import InstitutionsApi  # noqa: E501
from phagesdb_client.rest import ApiException


class TestInstitutionsApi(unittest.TestCase):
    """InstitutionsApi unit test stubs"""

    def setUp(self):
        self.api = phagesdb_client.api.institutions_api.InstitutionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_institutions_list(self):
        """Test case for institutions_list

        Institution Information  # noqa: E501
        """
        pass

    def test_institutions_read(self):
        """Test case for institutions_read

        Institution Information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
