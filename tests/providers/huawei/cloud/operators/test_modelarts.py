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

class TestModelArtsCreateDatasetVersionOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsCreateDatasetVersionOperator(
            task_id=MOCK_TASK_ID,
            dataset_id= "dataset_id",
            clear_hard_property= False,
            description= "description",
            export_images= False,
            remove_sample_usage= False,
            train_evaluate_sample_ratio= "train_evaluate_sample_ratio",
            version_format= "version_format",
            version_name= "version_name",
            with_column_header= False,
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.create_dataset_version.assert_called_once_with(
            dataset_id= "dataset_id",
            clear_hard_property= False,
            description= "description",
            export_images= False,
            remove_sample_usage= False,
            train_evaluate_sample_ratio= "train_evaluate_sample_ratio",
            version_format= "version_format",
            version_name= "version_name",
            with_column_header= False,
        )


class TestModelArtsDeleteDatasetVersionOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsDeleteDatasetVersionOperator(
            task_id=MOCK_TASK_ID,
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
            dataset_id= "dataset_id",
            version_id= "version_id"
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.delete_dataset_version.assert_called_once_with(
            dataset_id= "dataset_id",
            version_id= "version_id"
        )

class TestModelArtsCreateAlgorithmOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsCreateAlgorithmOperator(
            task_id=MOCK_TASK_ID,
            metadata= {},
            job_config= {},
            resource_requirements= [],
            advanced_config= {},
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.create_algorithm.assert_called_once_with(
            metadata= {},
            job_config= {},
            resource_requirements= [],
            advanced_config= {}
        )

class TestModelArtsChangeAlgorithmOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsChangeAlgorithmOperator(
            task_id=MOCK_TASK_ID,
            algorithm_id= "algorithm_id",
            metadata= {},
            job_config= {},
            resource_requirements= [],
            advanced_config= {},
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.change_algorithm.assert_called_once_with(
            algorithm_id= "algorithm_id",
            metadata= {},
            job_config= {},
            resource_requirements= [],
            advanced_config= {}
        )

class TestModelArtsDeleteAlgorithmOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsDeleteAlgorithmOperator(
            task_id=MOCK_TASK_ID,
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
            algorithm_id= "algorithm_id"
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.delete_algorithm.assert_called_once_with(
            algorithm_id= "algorithm_id"
        )


class TestModelArtsCreateTrainingJobOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsCreateTrainingJobOperator(
            task_id=MOCK_TASK_ID,
            kind= "kind",
            metadata= {},
            algorithm= {},
            tasks= [],
            spec= {},
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.create_training_job.assert_called_once_with(
            kind= "kind",
            metadata= {},
            algorithm= {},
            tasks= [],
            spec= {},
        )

class TestModelArtsDeleteTrainingJobOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsDeleteTrainingJobOperator(
            task_id=MOCK_TASK_ID,
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
            training_job_id= "training_job_id",
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.delete_training_job.assert_called_once_with(
            training_job_id= "training_job_id",
        )

class TestModelArtsStopTrainingJobOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsStopTrainingJobOperator(
            task_id=MOCK_TASK_ID,
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
            training_job_id= "training_job_id",
            action_type= "action_type",
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.stop_training_job.assert_called_once_with(
            training_job_id= "training_job_id",
            action_type= "action_type",
        )


class TestModelArtsCreateServiceOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsCreateServiceOperator(
            task_id=MOCK_TASK_ID,
            infer_type= "infer_type",
            service_name= "service_name",
            workspace_id= "workspace_id",
            schedule= [],
            cluster_id= "cluster_id",
            pool_name= "pool_name",
            vpc_id= "vpc_id",
            description= "description",
            security_group_id= "security_group_id",
            subnet_network_id= "subnet_network_id",
            config= [],
            additional_properties= {},
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.create_service.assert_called_once_with(
            infer_type= "infer_type",
            service_name= "service_name",
            workspace_id= "workspace_id",
            schedule= [],
            cluster_id= "cluster_id",
            pool_name= "pool_name",
            vpc_id= "vpc_id",
            description= "description",
            security_group_id= "security_group_id",
            subnet_network_id= "subnet_network_id",
            config= [],
            additional_properties= {},
        )

class TestModelArtsDeleteServiceOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsDeleteServiceOperator(
            task_id=MOCK_TASK_ID,
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
            service_id= "service_id",
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.delete_service.assert_called_once_with(
            service_id= "service_id",
        )

class TestModelArtsUpdateServiceOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsUpdateServiceOperator(
            task_id=MOCK_TASK_ID,
            service_id= "service_id",
            schedule= [],
            description= "description",
            config= [],
            status= "status",
            additional_properties= {},
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.update_service.assert_called_once_with(
            service_id= "service_id",
            schedule= [],
            description= "description",
            config= [],
            status= "status",
            additional_properties= {},
        )


class TestModelArtsCreateModelOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsCreateModelOperator(
            task_id=MOCK_TASK_ID,
            model_version= "model_version",
            source_location= "source_location",
            model_type= "model_type",
            model_name= "model_name",
            model_docs= [],
            template= {},
            source_job_version= "source_job_version",
            source_copy= "source_copy",
            initial_config= "initial_config",
            execution_code= "execution_code",
            source_job_id= "source_job_id",
            output_params= [],
            description= "description",
            runtime= "runtime",
            model_metrics= "model_metrics",
            source_type= "source_type",
            dependencies= [],
            workspace_id= "workspace_id",
            model_algorithm= "model_algorithm",
            apis= [],
            install_type= [],
            input_params= [],
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.create_model.assert_called_once_with(
            model_version= "model_version",
            source_location= "source_location",
            model_type= "model_type",
            model_name= "model_name",
            model_docs= [],
            template= {},
            source_job_version= "source_job_version",
            source_copy= "source_copy",
            initial_config= "initial_config",
            execution_code= "execution_code",
            source_job_id= "source_job_id",
            output_params= [],
            description= "description",
            runtime= "runtime",
            model_metrics= "model_metrics",
            source_type= "source_type",
            dependencies= [],
            workspace_id= "workspace_id",
            model_algorithm= "model_algorithm",
            apis= [],
            install_type= [],
            input_params= [],
        )


class TestModelArtsDeleteModelOperator(unittest.TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.modelarts.ModelArtsHook")
    def test_execute(self, mock_hook):
        operator = ModelArtsDeleteModelOperator(
            task_id=MOCK_TASK_ID,
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID,
            project_id=MOCK_PROJECT_ID,
            model_id= "model_id",
        )
        operator.execute(None)
        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MODELARTS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.delete_model.assert_called_once_with(
            model_id= "model_id",
        )
