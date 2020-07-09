# phagesdb_client.PhagesApi

All URIs are relative to *https://phagesdb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**phages_list**](PhagesApi.md#phages_list) | **GET** /api/phages/ | Detailed Phage Information
[**phages_read**](PhagesApi.md#phages_read) | **GET** /api/phages/{phage_name}/ | Detailed Phage Information


# **phages_list**
> phages_list(page=page, page_size=page_size)

Detailed Phage Information

Detailed Phage Information  Access detailed information about all phages, or about a particular phage (given its name).

### Example
```python
from __future__ import print_function
import time
import phagesdb_client
from phagesdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phagesdb_client.PhagesApi()
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # Detailed Phage Information
    api_instance.phages_list(page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling PhagesApi->phages_list: %s\n" % e)
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

# **phages_read**
> phages_read(phage_name)

Detailed Phage Information

Detailed Phage Information  Access detailed information about all phages, or about a particular phage (given its name).

### Example
```python
from __future__ import print_function
import time
import phagesdb_client
from phagesdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phagesdb_client.PhagesApi()
phage_name = 'phage_name_example' # str | 

try:
    # Detailed Phage Information
    api_instance.phages_read(phage_name)
except ApiException as e:
    print("Exception when calling PhagesApi->phages_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phage_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

