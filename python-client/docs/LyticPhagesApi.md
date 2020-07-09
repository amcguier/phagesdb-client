# swagger_client.LyticPhagesApi

All URIs are relative to *https://phagesdb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lytic_phages_list**](LyticPhagesApi.md#lytic_phages_list) | **GET** /api/lytic_phages/ | Sequenced Lytic Phages


# **lytic_phages_list**
> lytic_phages_list(page=page, page_size=page_size)

Sequenced Lytic Phages

Sequenced Lytic Phages  Get detailed information about phages that have been sequenced and placed in a cluster which generally contains lytic phages (those which cannot form lysogens).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LyticPhagesApi()
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # Sequenced Lytic Phages
    api_instance.lytic_phages_list(page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling LyticPhagesApi->lytic_phages_list: %s\n" % e)
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

