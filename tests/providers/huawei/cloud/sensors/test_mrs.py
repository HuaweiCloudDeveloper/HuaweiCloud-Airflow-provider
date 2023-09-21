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
from unittest.mock import PropertyMock

from airflow.exceptions import AirflowException
from airflow.providers.huawei.cloud.sensors.mrs import MRSShowClusterStateSensor

MRS_SENSOR_STRING = "airflow.providers.huawei.cloud.sensors.mrs.{}"
MOCK_PROJECT_ID = "test-project"
MOCK_CONN_ID = "huaweicloud_default"
MOCK_REGION = "mock_region"
MOCK_TASK_ID = "test-mrs-operator"
MOCK_CLUSTER_ID = "b2645baf-91e9-4afe-92a4-0e7738b587ad3"
MOCK_SNAPSHOT = "mock_snapshot"
MOCK_STATUS = "running"


class TestMRSShowClusterStateSensor(unittest.TestCase):
    def setUp(self) -> None:
        self.cluster_sensor = MRSShowClusterStateSensor(
            task_id=MOCK_TASK_ID,
            cluster_id=MOCK_CLUSTER_ID,
            target_status=MOCK_STATUS,
            region=MOCK_REGION,
            project_id=MOCK_PROJECT_ID,
            huaweicloud_conn_id=MOCK_CONN_ID,
        )

    @mock.patch(MRS_SENSOR_STRING.format("MRSHook"))
    def test_get_hook(self, mock_service):
        self.cluster_sensor.get_hook()
        mock_service.assert_called_once_with(
            huaweicloud_conn_id=MOCK_CONN_ID, project_id=MOCK_PROJECT_ID, region=MOCK_REGION
        )

    @mock.patch(MRS_SENSOR_STRING.format("MRSShowClusterStateSensor.get_hook"), new_callable=PropertyMock)
    def test_poke(self, mock_service):
        expect_status = "running"
        cluster = mock.Mock(cluster_state=expect_status)
        expect_resp = mock.Mock(cluster=cluster)
        mock_service.return_value.show_cluster_details.return_value = expect_resp

        if expect_status in ("failed", "abnormal"):
            with self.assertRaises(AirflowException):
                res = self.cluster_sensor.poke(None)
                self.assertEqual(expect_status == MOCK_STATUS, res)
        else:
            res = self.cluster_sensor.poke(None)
            self.assertEqual(expect_status == MOCK_STATUS, res)
