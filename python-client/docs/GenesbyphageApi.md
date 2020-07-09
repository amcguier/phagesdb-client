# swagger_client.GenesbyphageApi

All URIs are relative to *https://phagesdb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**genesbyphage_read**](GenesbyphageApi.md#genesbyphage_read) | **GET** /api/genesbyphage/{name}/ | Genes from one Phage


# **genesbyphage_read**
> genesbyphage_read(name)

Genes from one Phage

Genes from one Phage  Get all genes from a particular phage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenesbyphageApi()
name = 'name_example' # str | 

try:
    # Genes from one Phage
    api_instance.genesbyphage_read(name)
except ApiException as e:
    print("Exception when calling GenesbyphageApi->genesbyphage_read: %s\n" % e)
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

