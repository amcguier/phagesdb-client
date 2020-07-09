# swagger_client.InstitutionsApi

All URIs are relative to *https://phagesdb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**institutions_list**](InstitutionsApi.md#institutions_list) | **GET** /api/institutions/ | Institution Information
[**institutions_read**](InstitutionsApi.md#institutions_read) | **GET** /api/institutions/{institution_code}/ | Institution Information


# **institutions_list**
> institutions_list()

Institution Information

Institution Information  Get basic information on all or any institutions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstitutionsApi()

try:
    # Institution Information
    api_instance.institutions_list()
except ApiException as e:
    print("Exception when calling InstitutionsApi->institutions_list: %s\n" % e)
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

# **institutions_read**
> institutions_read(institution_code)

Institution Information

Institution Information  Get basic information on all or any institutions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstitutionsApi()
institution_code = 'institution_code_example' # str | A unique value identifying this institution.

try:
    # Institution Information
    api_instance.institutions_read(institution_code)
except ApiException as e:
    print("Exception when calling InstitutionsApi->institutions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_code** | **str**| A unique value identifying this institution. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

