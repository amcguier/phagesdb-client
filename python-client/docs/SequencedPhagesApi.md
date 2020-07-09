# swagger_client.SequencedPhagesApi

All URIs are relative to *https://phagesdb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sequenced_phages_list**](SequencedPhagesApi.md#sequenced_phages_list) | **GET** /api/sequenced_phages/ | Sequenced Phages Only


# **sequenced_phages_list**
> sequenced_phages_list(page=page, page_size=page_size)

Sequenced Phages Only

Sequenced Phages Only  Get detailed information about all sequenced phages.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SequencedPhagesApi()
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # Sequenced Phages Only
    api_instance.sequenced_phages_list(page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling SequencedPhagesApi->sequenced_phages_list: %s\n" % e)
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

