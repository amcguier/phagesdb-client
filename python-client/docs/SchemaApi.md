# phagesdb_client.SchemaApi

All URIs are relative to *https://phagesdb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schema_list**](SchemaApi.md#schema_list) | **GET** /api/schema/ | 


# **schema_list**
> schema_list()



### Example
```python
from __future__ import print_function
import time
import phagesdb_client
from phagesdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phagesdb_client.SchemaApi()

try:
    api_instance.schema_list()
except ApiException as e:
    print("Exception when calling SchemaApi->schema_list: %s\n" % e)
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

