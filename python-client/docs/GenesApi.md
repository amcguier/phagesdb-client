# phagesdb_client.GenesApi

All URIs are relative to *https://phagesdb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**genes_list**](GenesApi.md#genes_list) | **GET** /api/genes/ | Phamerator Gene Information
[**genes_read**](GenesApi.md#genes_read) | **GET** /api/genes/{GeneID}/ | Phamerator Gene Information


# **genes_list**
> genes_list(page=page, page_size=page_size)

Phamerator Gene Information

Phamerator Gene Information  Get information on all or any genes found in Phamerator's Actino_Draft database.

### Example
```python
from __future__ import print_function
import time
import phagesdb_client
from phagesdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phagesdb_client.GenesApi()
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # Phamerator Gene Information
    api_instance.genes_list(page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling GenesApi->genes_list: %s\n" % e)
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

# **genes_read**
> genes_read(gene_id)

Phamerator Gene Information

Phamerator Gene Information  Get information on all or any genes found in Phamerator's Actino_Draft database.

### Example
```python
from __future__ import print_function
import time
import phagesdb_client
from phagesdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phagesdb_client.GenesApi()
gene_id = 'gene_id_example' # str | A unique value identifying this pham gene.

try:
    # Phamerator Gene Information
    api_instance.genes_read(gene_id)
except ApiException as e:
    print("Exception when calling GenesApi->genes_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**| A unique value identifying this pham gene. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

