# phagesdb_client.HostGeneraApi

All URIs are relative to *https://phagesdb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_genera_list**](HostGeneraApi.md#host_genera_list) | **GET** /api/host_genera/ | Host Genus Information
[**host_genera_phagelist_list**](HostGeneraApi.md#host_genera_phagelist_list) | **GET** /api/host_genera/{id}/phagelist/ | Phages by Genus
[**host_genera_read**](HostGeneraApi.md#host_genera_read) | **GET** /api/host_genera/{id}/ | Host Genus Information


# **host_genera_list**
> host_genera_list()

Host Genus Information

Host Genus Information  Get information on all or any host genus.

### Example
```python
from __future__ import print_function
import time
import phagesdb_client
from phagesdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phagesdb_client.HostGeneraApi()

try:
    # Host Genus Information
    api_instance.host_genera_list()
except ApiException as e:
    print("Exception when calling HostGeneraApi->host_genera_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_genera_phagelist_list**
> host_genera_phagelist_list(id, page=page, page_size=page_size)

Phages by Genus

Phages by Genus  Get detailed information about all phages in a given genus.

### Example
```python
from __future__ import print_function
import time
import phagesdb_client
from phagesdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phagesdb_client.HostGeneraApi()
id = 'id_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # Phages by Genus
    api_instance.host_genera_phagelist_list(id, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling HostGeneraApi->host_genera_phagelist_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **host_genera_read**
> host_genera_read(id)

Host Genus Information

Host Genus Information  Get information on all or any host genus.

### Example
```python
from __future__ import print_function
import time
import phagesdb_client
from phagesdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phagesdb_client.HostGeneraApi()
id = 56 # int | A unique integer value identifying this genus.

try:
    # Host Genus Information
    api_instance.host_genera_read(id)
except ApiException as e:
    print("Exception when calling HostGeneraApi->host_genera_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this genus. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

