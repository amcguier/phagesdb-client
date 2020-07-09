# swagger_client.GenbankupdatedApi

All URIs are relative to *https://phagesdb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**genbankupdated_read**](GenbankupdatedApi.md#genbankupdated_read) | **GET** /api/genbankupdated/{year}/{month}/{day}/ | Phages by Genbank File update date


# **genbankupdated_read**
> genbankupdated_read(year, month, day)

Phages by Genbank File update date

Phages by Genbank File update date  Get detailed information about all phages whose QCed Genbank files have changed since a certain date

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GenbankupdatedApi()
year = 'year_example' # str | 
month = 'month_example' # str | 
day = 'day_example' # str | 

try:
    # Phages by Genbank File update date
    api_instance.genbankupdated_read(year, month, day)
except ApiException as e:
    print("Exception when calling GenbankupdatedApi->genbankupdated_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  | 
 **month** | **str**|  | 
 **day** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

