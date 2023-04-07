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

from airflow.providers.huawei.cloud.operators.modelarts import (
    ModelArtsCreateDatasetOperator,
    ModelArtsCreateModelOperator,
    ModelArtsUpdateDatasetOperator,
    ModelArtsDeleteDatasetVersionOperator,
    ModelArtsCreateAlgorithmOperator,
    ModelArtsDeleteAlgorithmOperator,
    ModelArtsChangeAlgorithmOperator,
    ModelArtsCreateServiceOperator,
    ModelArtsDeleteServiceOperator,
    ModelArtsUpdateServiceOperator,
    ModelArtsCreateTrainingJobOperator,
    ModelArtsDeleteTrainingJobOperator,
    ModelArtsStopTrainingJobOperator,
    ModelArtsDeleteModelOperator,
    ModelArtsDeleteDatasetOperator,
    ModelArtsCreateDatasetVersionOperator
)

MOCK_TASK_ID = "test-modelarts-operator"
MOCK_REGION = "mock_region"
MOCK_MODELARTS_CONN_ID = "mock_cdm_conn_default"
MOCK_PROJECT_ID = "mock_project_id"


class TestModelArtsCreateDatasetOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsCreateDatasetOperator(
            task_id=MOCK_TASK_ID,
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
            data_sources=[],
            work_path="str",
            work_path_type=0,
            data_format="str",
            dataset_name="str",
            dataset_type=0,
            description="desc",
            import_annotations=False,
            import_data=False,
            label_format={},
            labels=[],
            managed=False,
            schema=[],
            workforce_information={},
            workspace_id="0"
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.create_dataset.assert_called_once_with(
            data_sources=[],
            work_path="str",
            work_path_type=0,
            data_format="str",
            dataset_name="str",
            dataset_type=0,
            description="desc",
            import_annotations=False,
            import_data=False,
            label_format={},
            labels=[],
            managed=False,
            schema=[],
            workforce_information={},
            workspace_id="0"
        )


class TestModelArtsUpdateDatasetOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsUpdateDatasetOperator(
            task_id=MOCK_TASK_ID,
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
            dataset_id="dataset_id",
            add_labels=[],
            current_version_id="current_version_id",
            dataset_name=" dataset_name",
            delete_labels=[],
            description="description",
            update_labels=[]
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.update_dataset.assert_called_once_with(
            dataset_id="dataset_id",
            add_labels=[],
            current_version_id="current_version_id",
            dataset_name=" dataset_name",
            delete_labels=[],
            description="description",
            update_labels=[]
        )

class TestModelArtsDeleteDatasetOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsDeleteDatasetOperator(
            task_id=MOCK_TASK_ID,
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
            dataset_id="dataset_id",
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.delete_dataset.assert_called_once_with(
            dataset_id="dataset_id",
        )


