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
from phagesdb_client.api.host_genera_api import HostGeneraApi  # noqa: E501
from phagesdb_client.rest import ApiException


class TestHostGeneraApi(unittest.TestCase):
    """HostGeneraApi unit test stubs"""

    def setUp(self):
        self.api = phagesdb_client.api.host_genera_api.HostGeneraApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_host_genera_list(self):
        """Test case for host_genera_list

        Host Genus Information  # noqa: E501
        """
        pass

    def test_host_genera_phagelist_list(self):
        """Test case for host_genera_phagelist_list

        Phages by Genus  # noqa: E501
        """
        pass

    def test_host_genera_read(self):
        """Test case for host_genera_read

        Host Genus Information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
