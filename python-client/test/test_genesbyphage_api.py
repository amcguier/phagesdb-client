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
from phagesdb_client.api.genesbyphage_api import GenesbyphageApi  # noqa: E501
from phagesdb_client.rest import ApiException


class TestGenesbyphageApi(unittest.TestCase):
    """GenesbyphageApi unit test stubs"""

    def setUp(self):
        self.api = phagesdb_client.api.genesbyphage_api.GenesbyphageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_genesbyphage_read(self):
        """Test case for genesbyphage_read

        Genes from one Phage  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
