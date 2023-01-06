#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

import unittest
from unittest import mock


from airflow.providers.huawei.cloud.hooks.smn import SMNHook
from tests.providers.huawei.cloud.utils.smn_mock import mock_smn_hook_default_project_id
SMN_STRING = "airflow.providers.huawei.cloud.hooks.smn.{}"
MOCK_SMN_CONN_ID = "mock_smn_default"


class TestSmnHook(unittest.TestCase):
    def setUp(self):
        with mock.patch(
            SMN_STRING.format("SMNHook.__init__"),
            new=mock_smn_hook_default_project_id,
        ):
            self.hook = SMNHook(huaweicloud_conn_id=MOCK_SMN_CONN_ID)

    def test_get_default_region(self):
        assert self.hook.get_region() == "ap-southeast-3"

    def test_get_smn_client(self):
        client = self.hook.get_smn_client("project_id")
        assert client.get_credentials().ak == "AK"
        assert client.get_credentials().sk == "SK"
        assert client.get_credentials().project_id == "project_id"

    def test_get_request_body(self):
        req = self.hook.make_publish_app_message_request(
            "test_urn", {"subject": "bar"})
        assert req.body.subject == "bar"

    @mock.patch(SMN_STRING.format("SmnSdk.smn_client.SmnClient.publish_message"))
    def test_send_request(self, publish_message):
        var = self.hook.make_publish_app_message_request(
            "test_urn", {"subject": "bar"})
        self.hook.send_request("project_id", var)
        publish_message.assert_called_once_with(var)

    @mock.patch(SMN_STRING.format("SMNHook.send_request"))
    def test_publish_message(self, send_request):
        payload = {"message_structure": '{"default":"Merhaba", "sms":"Merhaba SMS", "email":"Merhaba EMail"}',
                   "tags": {"a": "1"},
                   "message": "message"}
        self.hook.send_message(project_id="example-id",
                               topic_urn="example-urn", **payload)
        send_request.assert_called_once_with("example-id",
                                             self.hook.make_publish_app_message_request("example-urn", payload))
