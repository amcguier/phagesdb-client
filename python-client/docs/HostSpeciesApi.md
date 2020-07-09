# swagger_client.HostSpeciesApi

All URIs are relative to *https://phagesdb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_species_list**](HostSpeciesApi.md#host_species_list) | **GET** /api/host_species/ | Host Species Information
[**host_species_phagelist_list**](HostSpeciesApi.md#host_species_phagelist_list) | **GET** /api/host_species/{id}/phagelist/ | Phages by Species
[**host_species_read**](HostSpeciesApi.md#host_species_read) | **GET** /api/host_species/{id}/ | Host Species Information


# **host_species_list**
> host_species_list()

Host Species Information

Host Species Information  Get information on all or any host species.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostSpeciesApi()

try:
    # Host Species Information
    api_instance.host_species_list()
except ApiException as e:
    print("Exception when calling HostSpeciesApi->host_species_list: %s\n" % e)
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

# **host_species_phagelist_list**
> host_species_phagelist_list(id, page=page, page_size=page_size)

Phages by Species

Phages by Species  Get detailed information about all phages in a given species.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostSpeciesApi()
id = 'id_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # Phages by Species
    api_instance.host_species_phagelist_list(id, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling HostSpeciesApi->host_species_phagelist_list: %s\n" % e)
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

# **host_species_read**
> host_species_read(id)

Host Species Information

Host Species Information  Get information on all or any host species.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostSpeciesApi()
id = 56 # int | A unique integer value identifying this Host species.

try:
    # Host Species Information
    api_instance.host_species_read(id)
except ApiException as e:
    print("Exception when calling HostSpeciesApi->host_species_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Host species. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

