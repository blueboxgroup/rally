# Copyright 2014: Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from rally import consts
from rally import objects
from tests.unit import test


class EndpointTestCase(test.TestCase):

    def test_endpoint(self):
        endpoint = objects.Endpoint("url", "user", "pwd", "tenant", "admin")
        self.assertEqual(endpoint.to_dict(include_permission=True),
                         {"auth_url": "url", "username": "user",
                          "password": "pwd", "tenant_name": "tenant",
                          "region_name": None, "permission": "admin",
                          "domain_name": None,
                          "endpoint_type": consts.EndpointType.PUBLIC,
                          "project_domain_name": "Default",
                          "user_domain_name": "Default"})
