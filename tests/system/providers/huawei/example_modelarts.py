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

from datetime import datetime

from airflow import DAG
from airflow.providers.huawei.cloud.operators.modelarts import (
    ModelArtsCreateAlgorithmOperator,
    ModelArtsCreateModelOperator,
    ModelArtsChangeAlgorithmOperator,
    ModelArtsCreateDatasetOperator,
    ModelArtsCreateServiceOperator,
    ModelArtsCreateTrainingJobOperator,
    ModelArtsDeleteAlgorithmOperator,
    ModelArtsDeleteDatasetVersionOperator,
    ModelArtsDeleteModelOperator,
    ModelArtsDeleteServiceOperator,
    ModelArtsDeleteTrainingJobOperator,
    ModelArtsStopTrainingJobOperator,
    ModelArtsUpdateDatasetOperator,
    ModelArtsUpdateServiceOperator
)

from airflow.providers.huawei.cloud.sensors.modelarts import (
    ModelArtsDatasetSensor,
    ModelArtsDatasetVersionSensor,
    ModelArtsTrainingJobSensor,
    ModelArtsServiceJobSensor,
    ModelArtsModelSensor
)

project_id = "ea31ff23328a4d6bbcca820076f7c606"
job_name = "job_name"
workspace = "workspace-id"
body = {"jobParams": [{"name": "param1", "value": "value1"}]}


with DAG(
    "modelarts",
    description="Huawei Cloud ModelArts",
    start_date=datetime(2022, 10, 29),
    catchup=False,
    render_template_as_native_obj=True,
) as dag:

    # [START howto_operator_modelarts_create_algorithm]
    create_algorithm = ModelArtsCreateAlgorithmOperator(
        task_id="create_algorithm",
        job_config={
            "code_dir": "/modelarts-airflow/mnist_code/",
            "boot_file": "/modelarts-airflow/mnist_code/train_mnist_tf.py",
            "parameters_customization": True,
            "inputs": [
                {
                    "name": "data_url",
                    "description": "Input Source1",
                    "access_method": "parameter"
                }
            ],
            "outputs": [
                {
                    "name": "train_url",
                    "description": "Output Data1",
                    "access_method": "parameter",
                    "prefetch_to_local": False
                }
            ],
            "engine": {
                "engine_id": "tensorflow-cp36-1.8.0",
                "engine_name": "TensorFlow",
                "engine_version": "TF-1.8.0-python3.6",
                "tags": [
                    {
                        "key": "enableHeteroLearner",
                        "value": "True"
                    },
                    {
                        "key": "enableHeteroWorker",
                        "value": "True"
                    }
                ],
                "v1_compatible": True,
                "run_user": "",
                "image_info": {
                    "cpu_image_url": "modelarts-job-dev-image/tensorflow-cpu-cp36:1.8.0",
                    "gpu_image_url": "modelarts-job-dev-image/tensorflow-gpu-cuda9-cp36:1.8.0",
                    "image_version": "3.1.0"
                },
                "image_source": False
            }
        },
        metadata={
            "name": "algorithm-013",
            "workspace_id": "0"
        }
    )
    # [END howto_operator_modelarts_create_algorithm]

    # [START howto_operator_modelarts_create_model]
    create_model = ModelArtsCreateModelOperator(
        task_id="create_model",
        model_version="0.0.1",
        source_location="https://modelarts-airflow.obs.ap-southeast-3.myhuaweicloud.com/mnist_model",
        model_type="TensorFlow",
        model_name="model-test005",
        runtime="python2.7",
        source_job_id="sorce_job_id",
        execution_code="/modelarts-airflow/mnist_model/model/customize_service.py",
        install_type=["real-time"]

    )
    # [END howto_operator_modelarts_create_model]

    # [START howto_operator_modelarts_change_algorithm]
    change_algorithm = ModelArtsChangeAlgorithmOperator(
        task_id="change_algorithm",
        algorithm_id="algorithm_id",
        metadata={
            "name": "algorithm-013",
            "description": "87n description"
        },
        job_config={
            "code_dir": "/modelarts-airflow/mnist_code/",
            "boot_file": "/modelarts-airflow/mnist_code/train_mnist_tf.py",
            "parameters_customization": True,
            "inputs": [
                {
                    "name": "data_url",
                    "description": "Input Source1",
                    "access_method": "parameter"
                }
            ],
            "outputs": [
                {
                    "name": "train_url",
                    "description": "Output Data1",
                    "access_method": "parameter",
                    "prefetch_to_local": False
                }
            ],
            "engine": {
                "engine_id": "tensorflow-cp36-1.8.0",
                "engine_name": "TensorFlow",
                "engine_version": "TF-1.8.0-python3.6",
                "tags": [
                    {
                        "key": "enableHeteroLearner",
                        "value": "True"
                    },
                    {
                        "key": "enableHeteroWorker",
                        "value": "True"
                    }
                ],
                "v1_compatible": True,
                "run_user": "",
                "image_info": {
                    "cpu_image_url": "modelarts-job-dev-image/tensorflow-cpu-cp36:1.8.0",
                    "gpu_image_url": "modelarts-job-dev-image/tensorflow-gpu-cuda9-cp36:1.8.0",
                    "image_version": "3.1.0"
                },
                "image_source": False
            }
        }

    )
    # [END howto_operator_modelarts_change_algorithm]

    # [START howto_operator_modelarts_create_dataset]
    create_dataset = ModelArtsCreateDatasetOperator(
        task_id="create_dataset",
        data_sources=[{
            "data_type": 0,
            "data_path": "/airflow-bucket/modelarts/"
        }],
        work_path="/airflow-bucket/modelarts-output/",
        work_path_type=0,
        dataset_name="dataset-test005",
        dataset_type=0
    )
    # [END howto_operator_modelarts_create_dataset]

    # [START howto_operator_modelarts_create_service]
    create_service = ModelArtsCreateServiceOperator(
        task_id = "create_service",
        infer_type="real-time",
        service_name="service-test005",
        config=[
            {
                "specification": "modelarts.vm.cpu.2u",
                "model_id": "model_id",
                "instance_count": 1
            }
        ]
    )
    # [END howto_operator_modelarts_create_service]

    # [START howto_operator_modelarts_create_training_job]
    ModelArtsCreateTrainingJobOperator(
        task_id="create_training_job",
        kind="job",
        metadata={
            "name": "algorithm-013",
            "workspace_id": "0",
            "description": "description",
            "annotations": {
                "job_template": "Template DL",
                "key_task": "worker"
            }
        },
        algorithm={
            "id": "algorithm_id",
            "code_dir": "/modelarts-airflow/mnist_code/",
            "boot_file": "/modelarts-airflow/mnist_code/train_mnist_tf.py",
            "inputs": [
                {
                    "name": "data_url",
                    "remote": {
                        "obs": {
                            "obs_url": "/modelarts-airflow/mnist_dataset/"
                        }
                    }
                }
            ],
            "outputs": [
                {
                    "name": "train_url",
                    "remote": {
                        "obs": {
                            "obs_url": "/modelarts-airflow/mnist_model/"
                        }
                    }
                }
            ],
            "engine": {
                "engine_id": "tensorflow-cp36-1.8.0",
                "engine_name": "TensorFlow",
                "engine_version": "TF-1.8.0-python3.6"
            }
        },
        spec={
            "resource": {
                "flavor_id": "modelarts.vm.gpu.v100NV32",
                "node_count": 1
            }
        }
    )
    # [END howto_operator_modelarts_create_training_job]

    # [START howto_operator_modelarts_delete_algorithm]
    delete_algorithm = ModelArtsDeleteAlgorithmOperator(
        algorithm_id="algorithm_id",
        task_id="delete_algorithm"
    )
    # [END howto_operator_modelarts_delete_algorithm]

    # [START howto_operator_modelarts_delete_dataset_version]
    delete_dataset_version = ModelArtsDeleteDatasetVersionOperator(
        task_id="delete_dataset_version",
        dataset_id="dataset_id",
        version_id="version_id"
    )
    # [END howto_operator_modelarts_delete_dataset_version]

    # [START howto_operator_modelarts_delete_model]
    delete_model = ModelArtsDeleteModelOperator(
        model_id="model_id",
        task_id="delete_model"
    )
    # [END howto_operator_modelarts_delete_model]

    # [START howto_operator_modelarts_delete_service]
    delete_service = ModelArtsDeleteServiceOperator(
        task_id="delete_service",
        service_id="service_id"
    )
    # [END howto_operator_modelarts_delete_service]

    # [START howto_operator_modelarts_delete_training_job]
    delete_training_job = ModelArtsDeleteTrainingJobOperator(
        trigger_rule="none_skipped",
        task_id="delete_training_job",
        training_job_id="training_job_id",
    )
    # [END howto_operator_modelarts_delete_training_job]

    # [START howto_operator_modelarts_stop_training_job]
    stop_training_job = ModelArtsStopTrainingJobOperator(
        task_id="stop_training_job",
        training_job_id="training_job_id",
        action_type = "terminate"
    )
    # [END howto_operator_modelarts_stop_training_job]

    # [START howto_operator_modelarts_update_dataset]
    update_dataset = ModelArtsUpdateDatasetOperator(
        task_id="update_dataset",
        dataset_id="dataset_id",
        description="dataset description",
        add_labels=[
            {
                "name": "Label5"
            }
        ]
    )
    # [END howto_operator_modelarts_update_dataset]

    # [START howto_operator_modelarts_update_service]
    update_service = ModelArtsUpdateServiceOperator(
        task_id="update_service",
        service_id="service_id",
        description="description",
    )
    # [END howto_operator_modelarts_update_service]

    # [START howto_sensor_modelarts_dataset_status]
    dataset_sensor = ModelArtsDatasetSensor (
        task_id="dataset_sensor",
        dataset_id="dataset_id"
    )
    # [END howto_sensor_modelarts_dataset_status]

    # [START howto_sensor_modelarts_dataset_version_status]
    dataset_version_sensor = ModelArtsDatasetVersionSensor (
        task_id="dataset_version_sensor",
        dataset_id="dataset_id",
        version_id="version_id"
    )
    # [END howto_sensor_modelarts_dataset_version_status]

    # [START howto_sensor_modelarts_training_job_status]
    training_job_sensor = ModelArtsTrainingJobSensor(
        task_id="training_job_sensor",
        training_job_id="training_job_id"
    )
    # [END howto_sensor_modelarts_training_job_status]

    # [START howto_sensor_modelarts_service_job_status]
    service_job_sensor = ModelArtsServiceJobSensor(
        task_id="service_job_sensor",
        service_id="service_id"
    )
    # [END howto_sensor_modelarts_service_job_status]

    # [START howto_sensor_modelarts_model_status]
    model_sensor = ModelArtsModelSensor(
        task_id="model_sensor",
        model_id="model_id"
    )
    # [END howto_sensor_modelarts_model_status]


from tests.system.utils import get_test_run  # noqa: E402

# Needed to run the example DAG with pytest (see: tests/system/README.md#run_via_pytest)
test_run = get_test_run(dag)
