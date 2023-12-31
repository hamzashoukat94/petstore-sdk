# -*- coding: utf-8 -*-

"""
swaggerpetstore

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from swaggerpetstore.configuration import Configuration
from swaggerpetstore.controllers.base_controller import BaseController
from swaggerpetstore.configuration import Environment
from swaggerpetstore.http.auth.o_auth_2 import OAuth2
from swaggerpetstore.controllers.pet_controller import PetController
from swaggerpetstore.controllers.store_controller import StoreController
from swaggerpetstore.controllers.user_controller import UserController


class SwaggerpetstoreClient(object):

    @LazyProperty
    def pet(self):
        return PetController(self.global_configuration)

    @LazyProperty
    def store(self):
        return StoreController(self.global_configuration)

    @LazyProperty
    def user(self):
        return UserController(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
                 retry_methods=['GET', 'PUT'],
                 environment=Environment.PRODUCTION,
                 o_auth_client_id='TODO: Replace',
                 o_auth_redirect_uri='TODO: Replace', o_auth_token=None,
                 o_auth_scopes=None, config=None):
        if config is None:
            self.config = Configuration(
                                         http_client_instance=http_client_instance,
                                         override_http_client_configuration=override_http_client_configuration,
                                         http_call_back=http_call_back,
                                         timeout=timeout,
                                         max_retries=max_retries,
                                         backoff_factor=backoff_factor,
                                         retry_statuses=retry_statuses,
                                         retry_methods=retry_methods,
                                         environment=environment,
                                         o_auth_client_id=o_auth_client_id,
                                         o_auth_redirect_uri=o_auth_redirect_uri,
                                         o_auth_token=o_auth_token,
                                         o_auth_scopes=o_auth_scopes)
        else:
            self.config = config

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseController.user_agent(), BaseController.user_agent_parameters())
        self.initialize_auth_managers(self.global_configuration)

        self.global_configuration = self.global_configuration.auth_managers(self.auth_managers)

    def initialize_auth_managers(self, global_config):
        http_client_config = global_config.get_http_client_configuration()
        self.auth_managers = { key: None for key in ['global']}
        self.auth_managers['global'] = OAuth2(http_client_config.o_auth_client_id, http_client_config.o_auth_redirect_uri, http_client_config.o_auth_token, global_config, http_client_config.o_auth_scopes)
        return self.auth_managers
