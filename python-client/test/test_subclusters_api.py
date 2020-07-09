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
from phagesdb_client.api.subclusters_api import SubclustersApi  # noqa: E501
from phagesdb_client.rest import ApiException


class TestSubclustersApi(unittest.TestCase):
    """SubclustersApi unit test stubs"""

    def setUp(self):
        self.api = phagesdb_client.api.subclusters_api.SubclustersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_subclusters_list(self):
        """Test case for subclusters_list

        Subcluster Information  # noqa: E501
        """
        pass

    def test_subclusters_phagelist_list(self):
        """Test case for subclusters_phagelist_list

        Phages by Subcluster  # noqa: E501
        """
        pass

    def test_subclusters_read(self):
        """Test case for subclusters_read

        Subcluster Information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()