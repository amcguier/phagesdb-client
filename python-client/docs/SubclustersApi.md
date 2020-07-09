# swagger_client.SubclustersApi

All URIs are relative to *https://phagesdb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subclusters_list**](SubclustersApi.md#subclusters_list) | **GET** /api/subclusters/ | Subcluster Information
[**subclusters_phagelist_list**](SubclustersApi.md#subclusters_phagelist_list) | **GET** /api/subclusters/{subcluster}/phagelist/ | Phages by Subcluster
[**subclusters_read**](SubclustersApi.md#subclusters_read) | **GET** /api/subclusters/{subcluster}/ | Subcluster Information


# **subclusters_list**
> subclusters_list()

Subcluster Information

Subcluster Information  Get information on all or any subluster, including its set of phages.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubclustersApi()

try:
    # Subcluster Information
    api_instance.subclusters_list()
except ApiException as e:
    print("Exception when calling SubclustersApi->subclusters_list: %s\n" % e)
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

# **subclusters_phagelist_list**
> subclusters_phagelist_list(subcluster, page=page, page_size=page_size)

Phages by Subcluster

Phages by Subcluster  Get detailed information about all phages in a given subcluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubclustersApi()
subcluster = 'subcluster_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # Phages by Subcluster
    api_instance.subclusters_phagelist_list(subcluster, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling SubclustersApi->subclusters_phagelist_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subcluster** | **str**|  | 
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

# **subclusters_read**
> subclusters_read(subcluster)

Subcluster Information

Subcluster Information  Get information on all or any subluster, including its set of phages.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubclustersApi()
subcluster = 'subcluster_example' # str | 

try:
    # Subcluster Information
    api_instance.subclusters_read(subcluster)
except ApiException as e:
    print("Exception when calling SubclustersApi->subclusters_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subcluster** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

