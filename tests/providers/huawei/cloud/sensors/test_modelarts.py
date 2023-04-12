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

from airflow.providers.huawei.cloud.sensors.modelarts import (
    ModelArtsDatasetSensor,
    ModelArtsDatasetVersionSensor,
    ModelArtsModelSensor,
    ModelArtsServiceJobSensor,
    ModelArtsTrainingJobSensor
)

MODELARTS_SENSOR_STRING = "airflow.providers.huawei.cloud.sensors.modelarts.{}"
MOCK_DATASET_ID = "test-dataset"
MOCK_VERSION_ID = "test-version"
MOCK_TRAINING_JOB_ID = "test-training-job"
MOCK_MODEL_ID = "test-model"
MOCK_PROJECT_ID = "test-project"
MOCK_SERVICE_ID = "test-service"
MOCK_CONN_ID = "huaweicloud_default"
MOCK_TASK_ID = "test-modelarts-operator"
MOCK_WORKSPACE = "workspace-id"
MOCK_REGION = "region"

MOCK_DATASET_RESPONSE = {
    "datasets": [
        {
            "dataset_id": MOCK_DATASET_ID,
            "status": 1,
        }
    ]
}

MOCK_DATASET_VERSION_SUCCESS_RESPONSE = {
    "versions": [
        {
            "version_id": MOCK_VERSION_ID,
            "status": 1,
        }
    ]
}

MOCK_DATASET_VERSION_OTHER_RESPONSE = {
    "versions": [
        {
            "version_id": MOCK_VERSION_ID,
            "status": 3,
        }
    ]
}

MOCK_TRAINING_JOB_COMPLETED_RESPONSE = {
    "status": {
        "phase": "Completed",
    }
}

MOCK_TRAINING_JOB_OTHER_RESPONSE = {
    "status": {
        "phase": "Not Completed",
    }
}

MOCK_SERVICE_RUNNING_RESPONSE = {
    "status": "running",
}

MOCK_SERVICE_OTHER_RESPONSE = {
    "status": "unknown",
}

MOCK_MODEL_PUBLISHED_RESPONSE = {
    "model_status" : "published",
}


class TestModelArtsDatasetSensor(unittest.TestCase):
    def setUp(self):
        self.dataset_sensor = ModelArtsDatasetSensor(
            task_id=MOCK_TASK_ID,
            dataset_id=MOCK_DATASET_ID,
            project_id=MOCK_PROJECT_ID,
            huaweicloud_conn_id=MOCK_CONN_ID,
            region=MOCK_REGION,
        )

    @mock.patch(MODELARTS_SENSOR_STRING.format("ModelArtsHook"))
    def test_get_hook(self, mock_service):
        self.dataset_sensor.get_hook()
        mock_service.assert_called_once_with(
            huaweicloud_conn_id=MOCK_CONN_ID, project_id=MOCK_PROJECT_ID, region=MOCK_REGION
        )

    @mock.patch(
        MODELARTS_SENSOR_STRING.format("ModelArtsDatasetSensor.get_hook"), new_callable=PropertyMock
    )
    def test_poke_dataset_sensor(self, mock_service):
        # Given
        mock_service.return_value.list_dataset.return_value = MOCK_DATASET_RESPONSE

        # When
        res = self.dataset_sensor.poke(None)

        # Then
        assert res is True
        mock_service.return_value.list_dataset.assert_called_once

class TestModelArtsDatasetVersionSensor(unittest.TestCase):
    def setUp(self):
        self.dataset_version_sensor = ModelArtsDatasetVersionSensor(
            task_id=MOCK_TASK_ID,
            dataset_id=MOCK_DATASET_ID,
            version_id=MOCK_VERSION_ID,
            project_id=MOCK_PROJECT_ID,
            huaweicloud_conn_id=MOCK_CONN_ID,
            region=MOCK_REGION,
        )

    @mock.patch(MODELARTS_SENSOR_STRING.format("ModelArtsHook"))
    def test_get_hook(self, mock_service):
        self.dataset_version_sensor.get_hook()
        mock_service.assert_called_once_with(
            huaweicloud_conn_id=MOCK_CONN_ID, project_id=MOCK_PROJECT_ID, region=MOCK_REGION
        )

    @mock.patch(
        MODELARTS_SENSOR_STRING.format("ModelArtsDatasetVersionSensor.get_hook"), new_callable=PropertyMock
    )
    def test_poke_dataset_version_sensor_success(self, mock_service):
        # Given
        mock_service.return_value.list_dataset_version.return_value = MOCK_DATASET_VERSION_SUCCESS_RESPONSE

        # When
        res = self.dataset_version_sensor.poke(None)

        # Then
        assert res is True
        mock_service.return_value.list_dataset_version.assert_called_once_with(
            dataset_id=MOCK_DATASET_ID
        )

    @mock.patch(
        MODELARTS_SENSOR_STRING.format("ModelArtsDatasetVersionSensor.get_hook"), new_callable=PropertyMock
    )
    def test_poke_dataset_version_sensor_other(self, mock_service):
        # Given
        mock_service.return_value.list_dataset_version.return_value = MOCK_DATASET_VERSION_OTHER_RESPONSE

        # When
        res = self.dataset_version_sensor.poke(None)

        # Then
        assert res is False
        mock_service.return_value.list_dataset_version.assert_called_once_with(
            dataset_id=MOCK_DATASET_ID
        )

class TestModelArtsTrainingJobSensor(unittest.TestCase):
    def setUp(self):
        self.training_job = ModelArtsTrainingJobSensor(
            task_id=MOCK_TASK_ID,
            training_job_id= MOCK_TRAINING_JOB_ID,
            project_id=MOCK_PROJECT_ID,
            huaweicloud_conn_id=MOCK_CONN_ID,
            region=MOCK_REGION,
        )

    @mock.patch(MODELARTS_SENSOR_STRING.format("ModelArtsHook"))
    def test_get_hook(self, mock_service):
        self.training_job.get_hook()
        mock_service.assert_called_once_with(
            huaweicloud_conn_id=MOCK_CONN_ID, project_id=MOCK_PROJECT_ID, region=MOCK_REGION
        )

    @mock.patch(
        MODELARTS_SENSOR_STRING.format("ModelArtsTrainingJobSensor.get_hook"), new_callable=PropertyMock
    )
    def test_poke_training_job_completed(self, mock_service):
        # Given
        mock_service.return_value.list_training_job.return_value = MOCK_TRAINING_JOB_COMPLETED_RESPONSE

        # When
        res = self.training_job.poke(None)

        # Then
        assert res is True
        mock_service.return_value.list_training_job.assert_called_once_with(
            training_job_id=MOCK_TRAINING_JOB_ID
        )

    @mock.patch(
        MODELARTS_SENSOR_STRING.format("ModelArtsTrainingJobSensor.get_hook"), new_callable=PropertyMock
    )
    def test_poke_training_job_other(self, mock_service):
        # Given
        mock_service.return_value.list_training_job.return_value = MOCK_TRAINING_JOB_OTHER_RESPONSE

        # When
        res = self.training_job.poke(None)

        # Then
        assert res is False
        mock_service.return_value.list_training_job.assert_called_once_with(
            training_job_id=MOCK_TRAINING_JOB_ID
        )

class TestModelArtsServiceJobSensor(unittest.TestCase):
    def setUp(self):
        self.service_job = ModelArtsServiceJobSensor(
            task_id=MOCK_TASK_ID,
            service_id= MOCK_SERVICE_ID,
            project_id=MOCK_PROJECT_ID,
            huaweicloud_conn_id=MOCK_CONN_ID,
            region=MOCK_REGION,
        )

    @mock.patch(MODELARTS_SENSOR_STRING.format("ModelArtsHook"))
    def test_get_hook(self, mock_service):
        self.service_job.get_hook()
        mock_service.assert_called_once_with(
            huaweicloud_conn_id=MOCK_CONN_ID, project_id=MOCK_PROJECT_ID, region=MOCK_REGION
        )

    @mock.patch(
        MODELARTS_SENSOR_STRING.format("ModelArtsServiceJobSensor.get_hook"), new_callable=PropertyMock
    )
    def test_poke_service_job_running(self, mock_service):
        # Given
        mock_service.return_value.show_service.return_value = MOCK_SERVICE_RUNNING_RESPONSE

        # When
        res = self.service_job.poke(None)

        # Then
        assert res is True
        mock_service.return_value.show_service.assert_called_once_with(
            service_id=MOCK_SERVICE_ID
        )

    @mock.patch(
        MODELARTS_SENSOR_STRING.format("ModelArtsServiceJobSensor.get_hook"), new_callable=PropertyMock
    )
    def test_poke_service_job_other(self, mock_service):
        # Given
        mock_service.return_value.show_service.return_value = MOCK_SERVICE_OTHER_RESPONSE

        # When
        res = self.service_job.poke(None)

        # Then
        assert res is False
        mock_service.return_value.show_service.assert_called_once_with(
            service_id=MOCK_SERVICE_ID
        )

class TestModelArtsModelSensor(unittest.TestCase):
    def setUp(self):
        self.model_sensor = ModelArtsModelSensor(
            task_id=MOCK_TASK_ID,
            model_id= MOCK_MODEL_ID,
            project_id=MOCK_PROJECT_ID,
            huaweicloud_conn_id=MOCK_CONN_ID,
            region=MOCK_REGION,
        )

    @mock.patch(MODELARTS_SENSOR_STRING.format("ModelArtsHook"))
    def test_get_hook(self, mock_service):
        self.model_sensor.get_hook()
        mock_service.assert_called_once_with(
            huaweicloud_conn_id=MOCK_CONN_ID, project_id=MOCK_PROJECT_ID, region=MOCK_REGION
        )

    @mock.patch(
        MODELARTS_SENSOR_STRING.format("ModelArtsModelSensor.get_hook"), new_callable=PropertyMock
    )
    def test_poke_model_sensor_published(self, mock_service):
        # Given
        mock_service.return_value.show_model.return_value = MOCK_MODEL_PUBLISHED_RESPONSE

        # When
        res = self.model_sensor.poke(None)

        # Then
        assert res is True
        mock_service.return_value.show_model.assert_called_once_with(
            model_id=MOCK_MODEL_ID
        )

class mock_node:
    def __init__(self, job_name, status):
        self.job_name = job_name
        self.status = status
