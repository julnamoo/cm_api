# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import json
import unittest
from cm_api.endpoints.clusters import *
from cm_api.endpoints.services import *
from cm_api.endpoints.types import *
from cm_api_tests import utils

class TestYarn(unittest.TestCase):

  def test_get_yarn_applications(self):
    resource = utils.MockResource(self)
    service = ApiService(resource, name="bar")

    time = datetime.datetime.now()

    resource.expect("GET", "/cm/service/yarnApplications",
    retdata={ 'applications': [], 'warnings' : [] },
    params={ 'from':time.isoformat(), 'to':time.isoformat(), \
        'filter':'', 'limit':100, 'offset':0 })
    resp = service.get_yarn_applications(time, time)
    self.assertEquals(0, len(resp.applications))

  def test_kill_application(self):
    resource = utils.MockResource(self)
    service = ApiService(resource, name="bar")

    resource.expect("POST", "/cm/service/yarnApplications/randomId/kill",
        retdata={ 'warning' : 'test' })
    resp = service.kill_yarn_application('randomId')
    self.assertEquals('test', resp.warning)

