
# Getting Started with Swagger Petstore

## Introduction

This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.

Find out more about Swagger: [http://swagger.io](http://swagger.io)

## Install the Package

The package is compatible with Python versions `3 >=3.7, <= 3.11`.
Install the package from PyPi using the following pip command:

```python
pip install petstore-sdk==1.0.0
```

You can also view the package at:
https://pypi.python.org/pypi/petstore-sdk/1.0.0

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/hamzashoukat94/petstore-sdk/tree/1.0.0/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `o_auth_client_id` | `str` | OAuth 2 Client ID |
| `o_auth_redirect_uri` | `str` | OAuth 2 Redirection endpoint or Callback Uri |
| `o_auth_token` | `OAuthToken` | Object for storing information about the OAuth token |
| `o_auth_scopes` | `OAuthScopeEnum` |  |

The API client can be initialized as follows:

```python
from swaggerpetstore.swaggerpetstore_client import SwaggerpetstoreClient
from swaggerpetstore.configuration import Environment

client = SwaggerpetstoreClient(
    o_auth_client_id='OAuthClientId',
    o_auth_redirect_uri='OAuthRedirectUri',
    o_auth_scopes=[OAuthScopeEnum.READPETS, OAuthScopeEnum.WRITEPETS]
)
```

## Authorization

This API uses `OAuth 2 Implicit Grant`.

## Implicit Grant

Your application must obtain user authorization before it can execute an endpoint call incase this SDK chooses to use *OAuth 2.0 Implicit Grant* to obtain a user's consent to perform an API request on user's behalf. This authorization includes the following steps

This process requires the presence of a client-side JavaScript code on the redirect URI page to receive the *access token* after the consent step is completed.

### 1\. Obtain user consent

To obtain user's consent, you must redirect the user to the authorization page. The `get_authorization_url()` method creates the URL to the authorization page. You must have initialized the client with scopes for which you need permission to access.

```python
auth_url = client.auth_managers['global'].get_authorization_url()
```

### 2\. Handle the OAuth server response

Once the user responds to the consent request, the OAuth 2.0 server responds to your application's access request by redirecting the user to the redirect URI specified set in `Configuration`.

The redirect URI will receive the *access token* as the `token` argument in the URL fragment.

```
https://example.com/oauth/callback#token=XXXXXXXXXXXXXXXXXXXXXXXXX
```

The access token must be extracted by the client-side JavaScript code. The access token can be used to authorize any further endpoint calls by the JavaScript code.

### Scopes

Scopes enable your application to only request access to the resources it needs while enabling users to control the amount of access they grant to your application. Available scopes are defined in the `OAuthScopeEnum` enumeration.

| Scope Name | Description |
|  --- | --- |
| `READPETS` | read your pets |
| `WRITEPETS` | modify pets in your account |

## List of APIs

* [Pet](https://www.github.com/hamzashoukat94/petstore-sdk/tree/1.0.0/doc/controllers/pet.md)
* [Store](https://www.github.com/hamzashoukat94/petstore-sdk/tree/1.0.0/doc/controllers/store.md)
* [User](https://www.github.com/hamzashoukat94/petstore-sdk/tree/1.0.0/doc/controllers/user.md)

## Classes Documentation

* [Utility Classes](https://www.github.com/hamzashoukat94/petstore-sdk/tree/1.0.0/doc/utility-classes.md)
* [HttpResponse](https://www.github.com/hamzashoukat94/petstore-sdk/tree/1.0.0/doc/http-response.md)
* [HttpRequest](https://www.github.com/hamzashoukat94/petstore-sdk/tree/1.0.0/doc/http-request.md)

