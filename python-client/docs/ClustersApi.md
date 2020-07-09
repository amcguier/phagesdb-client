# phagesdb_client.ClustersApi

All URIs are relative to *https://phagesdb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clusters_list**](ClustersApi.md#clusters_list) | **GET** /api/clusters/ | Cluster Information
[**clusters_phagelist_list**](ClustersApi.md#clusters_phagelist_list) | **GET** /api/clusters/{cluster}/phagelist/ | Phages by Cluster
[**clusters_read**](ClustersApi.md#clusters_read) | **GET** /api/clusters/{cluster}/ | Cluster Information


# **clusters_list**
> clusters_list()

Cluster Information

Cluster Information  Get information on all or any Cluster, including its subclusters and phages.

### Example
```python
from __future__ import print_function
import time
import phagesdb_client
from phagesdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phagesdb_client.ClustersApi()

try:
    # Cluster Information
    api_instance.clusters_list()
except ApiException as e:
    print("Exception when calling ClustersApi->clusters_list: %s\n" % e)
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

# **clusters_phagelist_list**
> clusters_phagelist_list(cluster, page=page, page_size=page_size)

Phages by Cluster

Phages by Cluster  Get detailed information about all phages in a given cluster.

### Example
```python
from __future__ import print_function
import time
import phagesdb_client
from phagesdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phagesdb_client.ClustersApi()
cluster = 'cluster_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # Phages by Cluster
    api_instance.clusters_phagelist_list(cluster, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling ClustersApi->clusters_phagelist_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**|  | 
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

# **clusters_read**
> clusters_read(cluster)

Cluster Information

Cluster Information  Get information on all or any Cluster, including its subclusters and phages.

### Example
```python
from __future__ import print_function
import time
import phagesdb_client
from phagesdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phagesdb_client.ClustersApi()
cluster = 'cluster_example' # str | 

try:
    # Cluster Information
    api_instance.clusters_read(cluster)
except ApiException as e:
    print("Exception when calling ClustersApi->clusters_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

