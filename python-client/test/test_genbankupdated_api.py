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
from phagesdb_client.api.genbankupdated_api import GenbankupdatedApi  # noqa: E501
from phagesdb_client.rest import ApiException


class TestGenbankupdatedApi(unittest.TestCase):
    """GenbankupdatedApi unit test stubs"""

    def setUp(self):
        self.api = phagesdb_client.api.genbankupdated_api.GenbankupdatedApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_genbankupdated_read(self):
        """Test case for genbankupdated_read

        Phages by Genbank File update date  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()