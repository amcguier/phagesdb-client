# phagesdb_client.TemperatePhagesApi

All URIs are relative to *https://phagesdb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temperate_phages_list**](TemperatePhagesApi.md#temperate_phages_list) | **GET** /api/temperate_phages/ | Sequenced Temperate Phages


# **temperate_phages_list**
> temperate_phages_list(page=page, page_size=page_size)

Sequenced Temperate Phages

Sequenced Temperate Phages  Get detailed information about phages that have been sequenced and placed in a cluster which generally contains temperate phages.

### Example
```python
from __future__ import print_function
import time
import phagesdb_client
from phagesdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phagesdb_client.TemperatePhagesApi()
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # Sequenced Temperate Phages
    api_instance.temperate_phages_list(page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling TemperatePhagesApi->temperate_phages_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

