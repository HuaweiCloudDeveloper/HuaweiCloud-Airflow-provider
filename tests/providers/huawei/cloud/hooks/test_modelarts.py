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

from airflow.providers.huawei.cloud.hooks.modelarts import ModelArtsHook
from tests.providers.huawei.cloud.utils.hw_mock import default_mock_constants, mock_huawei_cloud_default

MODELARTS_STRING = "airflow.providers.huawei.cloud.hooks.modelarts.{}"


class TestModelArtsHook(unittest.TestCase):
    def setUp(self):
        with mock.patch(
            MODELARTS_STRING.format("ModelArtsHook.__init__"),
            new=mock_huawei_cloud_default,
        ):
            self.hook = ModelArtsHook()

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.create_dataset"))
    def test_create_dataset(self, create_dataset):
        data_sources= []
        work_path= "str"
        work_path_type= 0
        data_format= "str"
        dataset_name= "str"
        dataset_type= 0
        description= "desc"
        import_annotations= False
        import_data= False
        label_format= {}
        labels= []
        managed= False
        schema= []
        workforce_information= {}
        workspace_id= "0"
        self.hook.create_dataset(
            data_sources,
            work_path,
            work_path_type,
            data_format,
            dataset_name,
            dataset_type,
            description,
            import_annotations,
            import_data,
            label_format,
            labels,
            managed,
            schema,
            workforce_information,
            workspace_id,
        )
        create_dataset.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.create_dataset_version"))
    def create_dataset_version(self, create_dataset_version):
        dataset_id= "dataset-id"
        clear_hard_property= False
        description= "description"
        export_images= False
        remove_sample_usage= False
        train_evaluate_sample_ratio= "train_evaluate_sample_ratio"
        version_format= "version_format"
        version_name= "version_name"
        with_column_header= False
        self.hook.create_dataset_version(
            dataset_id,
            clear_hard_property,
            description,
            export_images,
            remove_sample_usage,
            train_evaluate_sample_ratio,
            version_format,
            version_name,
            with_column_header,
        )
        create_dataset_version.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.update_dataset"))
    def test_update_dataset(self, update_dataset):
        dataset_id= "dataset_id",
        add_labels= [],
        current_version_id= "current_version_id",
        dataset_name= " dataset_name",
        delete_labels= [],
        description= "description",
        update_labels= []
        self.hook.update_dataset(
            dataset_id,
            add_labels,
            current_version_id,
            dataset_name,
            delete_labels,
            description,
            update_labels
        )
        update_dataset.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.delete_dataset_version"))
    def test_delete_dataset_version(self, delete_dataset_version):
        dataset_id= "dataset_id",
        version_id= "version_id"
        self.hook.delete_dataset_version(
            dataset_id,
            version_id
        )
        delete_dataset_version.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.delete_dataset"))
    def test_delete_dataset(self, delete_dataset):
        dataset_id= "dataset_id"
        self.hook.delete_dataset(
            dataset_id
        )
        delete_dataset.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.create_algorithm"))
    def test_create_algorithm(self, create_algorithm):
        metadata= {},
        job_config= {},
        resource_requirements= [],
        advanced_config= {}
        self.hook.create_algorithm(
            metadata,
            job_config,
            resource_requirements,
            advanced_config
        )
        create_algorithm.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.change_algorithm"))
    def test_change_algorithm(self, change_algorithm):
        algorithm_id= "algorithm_id",
        metadata= {},
        job_config= {},
        resource_requirements= [],
        advanced_config= {}
        self.hook.change_algorithm(
            algorithm_id,
            metadata,
            job_config,
            resource_requirements,
            advanced_config
        )
        change_algorithm.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.delete_algorithm"))
    def test_delete_algorithm(self, delete_algorithm):
        algorithm_id= "algorithm_id"
        self.hook.delete_algorithm(
            algorithm_id
        )
        delete_algorithm.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.create_training_job"))
    def test_create_training_job(self, create_training_job):
        kind= "kind",
        metadata= {},
        algorithm= {},
        tasks= [],
        spec= {}
        self.hook.create_training_job(
            kind,
            metadata,
            algorithm,
            tasks,
            spec
        )
        create_training_job.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.delete_training_job"))
    def test_delete_training_job(self, delete_training_job):
        training_job_id= "job_id"
        self.hook.delete_training_job(
            training_job_id
        )
        delete_training_job.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.stop_training_job"))
    def test_stop_training_job(self, stop_training_job):
        training_job_id= "job_id"
        action_type= "action_type"
        self.hook.stop_training_job(
            training_job_id,
            action_type
        )
        stop_training_job.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.create_service"))
    def test_create_service(self, create_service):
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
        additional_properties= {}
        self.hook.create_service(
            infer_type,
            service_name,
            workspace_id,
            schedule,
            cluster_id,
            pool_name,
            vpc_id,
            description,
            security_group_id,
            subnet_network_id,
            config,
            additional_properties
        )
        create_service.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.delete_service"))
    def test_delete_service(self, delete_service):
        service_id= "service_id"
        self.hook.delete_service(
            service_id
        )
        delete_service.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.update_service"))
    def test_update_service(self, update_service):
        service_id= "service_id",
        schedule= [],
        description= "description",
        config= [],
        status= "status",
        additional_properties= {}
        self.hook.update_service(
            service_id,
            schedule,
            description,
            config,
            status,
            additional_properties
        )
        update_service.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.create_model"))
    def test_create_model(self, create_model):
        model_version= str,
        source_location= str,
        model_type= str,
        model_name= str,
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
        input_params= []
        self.hook.create_model(
            model_version,
            source_location,
            model_type,
            model_name,
            model_docs,
            template,
            source_job_version,
            source_copy,
            initial_config,
            execution_code,
            source_job_id,
            output_params,
            description,
            runtime,
            model_metrics,
            source_type,
            dependencies,
            workspace_id,
            model_algorithm,
            apis,
            install_type,
            input_params
        )
        create_model.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.delete_model"))
    def test_delete_model(self, delete_model):
        model_id= "model_id"
        self.hook.delete_model(
            model_id
        )
        delete_model.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.list_dataset"))
    def test_list_dataset(self, list_dataset):
        self.hook.list_dataset()
        list_dataset.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.list_dataset_version"))
    def test_list_dataset_version(self, list_dataset_version):
        dataset_id= "dataset_id"
        self.hook.list_dataset_version(
            dataset_id
        )
        list_dataset_version.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.list_training_job"))
    def test_list_training_job(self, list_training_job):
        self.hook.list_training_job()
        list_training_job.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.show_service"))
    def test_show_service(self, show_service):
        service_id= "service_id"
        self.hook.show_service(
            service_id
        )
        show_service.assert_called_once

    @mock.patch(MODELARTS_STRING.format("ModelArtsHook.show_model"))
    def test_show_model(self, show_model):
        model_id= "model_id"
        self.hook.show_model(
            model_id
        )
        show_model.assert_called_once


