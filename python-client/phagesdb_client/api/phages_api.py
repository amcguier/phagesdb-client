# coding: utf-8

"""
    PhagesDB API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from phagesdb_client.api_client import ApiClient


class PhagesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def phages_list(self, **kwargs):  # noqa: E501
        """Detailed Phage Information  # noqa: E501

        Detailed Phage Information  Access detailed information about all phages, or about a particular phage (given its name).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.phages_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: A page number within the paginated result set.
        :param int page_size: Number of results to return per page.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.phages_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.phages_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def phages_list_with_http_info(self, **kwargs):  # noqa: E501
        """Detailed Phage Information  # noqa: E501

        Detailed Phage Information  Access detailed information about all phages, or about a particular phage (given its name).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.phages_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: A page number within the paginated result set.
        :param int page_size: Number of results to return per page.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method phages_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/phages/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def phages_read(self, phage_name, **kwargs):  # noqa: E501
        """Detailed Phage Information  # noqa: E501

        Detailed Phage Information  Access detailed information about all phages, or about a particular phage (given its name).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.phages_read(phage_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str phage_name:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.phages_read_with_http_info(phage_name, **kwargs)  # noqa: E501
        else:
            (data) = self.phages_read_with_http_info(phage_name, **kwargs)  # noqa: E501
            return data

    def phages_read_with_http_info(self, phage_name, **kwargs):  # noqa: E501
        """Detailed Phage Information  # noqa: E501

        Detailed Phage Information  Access detailed information about all phages, or about a particular phage (given its name).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.phages_read_with_http_info(phage_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str phage_name:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phage_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method phages_read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'phage_name' is set
        if ('phage_name' not in params or
                params['phage_name'] is None):
            raise ValueError("Missing the required parameter `phage_name` when calling `phages_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'phage_name' in params:
            path_params['phage_name'] = params['phage_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/phages/{phage_name}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
