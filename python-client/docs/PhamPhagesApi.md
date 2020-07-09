# swagger_client.PhamPhagesApi

All URIs are relative to *https://phagesdb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pham_phages_list**](PhamPhagesApi.md#pham_phages_list) | **GET** /api/pham_phages/ | Phamerator Phage Information
[**pham_phages_read**](PhamPhagesApi.md#pham_phages_read) | **GET** /api/pham_phages/{Name}/ | Phamerator Phage Information


# **pham_phages_list**
> pham_phages_list(page=page, page_size=page_size)

Phamerator Phage Information

Phamerator Phage Information  Get information on all or any phages found in Phamerator's Actino_Draft database, including their DNA sequence.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PhamPhagesApi()
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # Phamerator Phage Information
    api_instance.pham_phages_list(page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling PhamPhagesApi->pham_phages_list: %s\n" % e)
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

# **pham_phages_read**
> pham_phages_read(name)

Phamerator Phage Information

Phamerator Phage Information  Get information on all or any phages found in Phamerator's Actino_Draft database, including their DNA sequence.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PhamPhagesApi()
name = 'name_example' # str | 

try:
    # Phamerator Phage Information
    api_instance.pham_phages_read(name)
except ApiException as e:
    print("Exception when calling PhamPhagesApi->pham_phages_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

