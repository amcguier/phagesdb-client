# swagger_client.HostStrainsApi

All URIs are relative to *https://phagesdb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_strains_list**](HostStrainsApi.md#host_strains_list) | **GET** /api/host_strains/ | Host Strain Information
[**host_strains_phagelist_list**](HostStrainsApi.md#host_strains_phagelist_list) | **GET** /api/host_strains/{id}/phagelist/ | Phages by Strain
[**host_strains_read**](HostStrainsApi.md#host_strains_read) | **GET** /api/host_strains/{id}/ | Host Strain Information


# **host_strains_list**
> host_strains_list()

Host Strain Information

Host Strain Information  Get information on all or any host strain.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostStrainsApi()

try:
    # Host Strain Information
    api_instance.host_strains_list()
except ApiException as e:
    print("Exception when calling HostStrainsApi->host_strains_list: %s\n" % e)
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

# **host_strains_phagelist_list**
> host_strains_phagelist_list(id, page=page, page_size=page_size)

Phages by Strain

Phages by Strain  Get detailed information about all phages in a given strain.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostStrainsApi()
id = 'id_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # Phages by Strain
    api_instance.host_strains_phagelist_list(id, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling HostStrainsApi->host_strains_phagelist_list: %s\n" % e)
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

# **host_strains_read**
> host_strains_read(id)

Host Strain Information

Host Strain Information  Get information on all or any host strain.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostStrainsApi()
id = 56 # int | A unique integer value identifying this Host strain.

try:
    # Host Strain Information
    api_instance.host_strains_read(id)
except ApiException as e:
    print("Exception when calling HostStrainsApi->host_strains_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Host strain. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

