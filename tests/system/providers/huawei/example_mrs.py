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
from airflow.providers.huawei.cloud.operators.mrs import (
    MRSCreateClusterOperator,
    MRSCreateClusterRunJobOperator,
    MRSDeleteClusterOperator
)
from airflow.providers.huawei.cloud.sensors.mrs import MRSShowClusterStateSensor


DAG_ID = "example_mrs"

cluster_version = "MRS 3.1.0"
cluster_name = "mrs_airflow_test"
cluster_type = "ANALYSIS"
charge_info = {'charge_mode': 'postPaid'}
region = "ap-southeast-3"
availability_zone = "ap-southeast-3b"
vpc_name = "vpc-37cd"
subnet_id = "1f8c5ca6-1f66-4096-bb00-baf175954f6e"
subnet_name = "subnet"
components = "Hadoop,Spark2x,HBase,Hive,Hue,Loader,Flink,Oozie,Ranger,Tez"
safe_mode = "KERBEROS"
manager_admin_password = "your password"
login_mode = "PASSWORD"
node_root_password = "your password"
log_collection = 1
mrs_ecs_default_agency = "MRS_ECS_DEFAULT_AGENCY"
tags = [{'key': 'tag1', 'value': '111'}, {'key': 'tag2', 'value': '222'}]
node_groups = [
    {
        'group_name': 'master_node_default_group',
        'node_num': 2,
        'node_size': 'rc3.4xlarge.4.linux.bigdata',
        'root_volume': {'type': 'SAS', 'size': 480},
        'data_volume': {'type': 'SAS', 'size': 600},
        'data_volume_count': 1
    },
    {
        'group_name': 'core_node_analysis_group',
        'node_num': 3,
        'node_size': 'rc3.4xlarge.4.linux.bigdata',
        'root_volume': {'type': 'SAS', 'size': 480},
        'data_volume': {'type': 'SAS', 'size': 600},
        'data_volume_count': 1
    },
    {
        'group_name': 'task_node_analysis_group',
        'node_num': 3,
        'node_size': 'rc3.4xlarge.4.linux.bigdata',
        'root_volume': {'type': 'SAS', 'size': 480},
        'data_volume': {'type': 'SAS', 'size': 600},
        'data_volume_count': 1,
        'auto_scaling_policy': {
            'auto_scaling_enable': True,
            'min_capacity': 0,
            'max_capacity': 1,
            'resources_plans': [{'period_type': 'daily', 'start_time': '12:00', 'end_time': '13:00',
                                 'min_capacity': 2, 'max_capacity': 3, 'effective_days': ['MONDAY']}],
            'rules': [{
                'name': 'default-expand-1',
                'description': '',
                'adjustment_type': 'scale_out',
                'cool_down_minutes': 5,
                'scaling_adjustment': '1',
                'trigger': {'metric_name': 'YARNAppRunning', 'metric_value': 100,
                            'comparison_operator': 'GTOE', 'evaluation_periods': '1'}
            }]
        }
    }
]
component_configs = [{
    'component_name': 'Hive',
    'configs': [
        {'key': 'hive.union.data.type.incompatible.enable', 'value': 'true',
         'config_file_name': 'hive-site.xml'},
        {'key': 'dfs.replication', 'value': '4', 'config_file_name': 'hdfs-site.xml'}
    ]
}]

delete_when_no_steps = True
steps = [
    {'job_execution': {'job_name': 'import_file', 'job_type': 'DistCp',
                       'arguments': ['obs://test/test.sql', '/user/hive/input']}},
    {'job_execution': {'job_name': 'hive_test', 'job_type': 'HiveScript',
                       'arguments': ['obs://test/hive/sql/HiveScript.sql']}}
]

with DAG(
    dag_id=DAG_ID,
    default_args={"huaweicloud_conn_id": "huaweicloud_default"},
    schedule="@once",
    start_date=datetime(2023, 1, 29),
    catchup=False,
    tags=["example"],
) as dag:
    # [START howto_operator_mrs_create_cluster]
    create_cluster = MRSCreateClusterOperator(
        task_id="create_cluster",
        cluster_version=cluster_version,
        cluster_name=cluster_name,
        cluster_type=cluster_type,
        vpc_name=vpc_name,
        subnet_id=subnet_id,
        subnet_name=subnet_name,
        components=components,
        availability_zone=availability_zone,
        safe_mode=safe_mode,
        manager_admin_password=manager_admin_password,
        login_mode=login_mode,
        node_root_password=node_root_password,
        mrs_ecs_default_agency=mrs_ecs_default_agency,
        tags=tags,
        node_groups=node_groups,
        component_configs=component_configs,
    )
    # [END howto_operator_mrs_create_cluster]

    # [START howto_sensor_mrs_wait_cluster_running]
    wait_cluster_running = MRSShowClusterStateSensor(
        task_id="wait_cluster_running",
        cluster_id="{{ ti.xcom_pull(task_ids='create_cluster') }}",
        target_status="running",
        poke_interval=15,
        timeout=60 * 20,
    )
    # [END howto_sensor_mrs_wait_cluster_running]

    # [START howto_operator_mrs_delete_cluster]
    delete_cluster = MRSDeleteClusterOperator(
        task_id="delete_cluster",
        cluster_id="{{ ti.xcom_pull(task_ids='create_cluster') }}",
    )
    # [END howto_operator_mrs_delete_cluster]

    # [START howto_operator_mrs_create_cluster_run_job_delete_cluster]
    create_cluster_run_job_delete_cluster = MRSCreateClusterRunJobOperator(
        task_id="create_cluster_run_job_delete_cluster",
        cluster_version=cluster_version,
        cluster_name=cluster_name,
        cluster_type=cluster_type,
        vpc_name=vpc_name,
        subnet_id=subnet_id,
        subnet_name=subnet_name,
        components=components,
        availability_zone=availability_zone,
        safe_mode=safe_mode,
        manager_admin_password=manager_admin_password,
        login_mode=login_mode,
        node_root_password=node_root_password,
        mrs_ecs_default_agency=mrs_ecs_default_agency,
        tags=tags,
        node_groups=node_groups,
        component_configs=component_configs,
        delete_when_no_steps=delete_when_no_steps,
        steps=steps,
    )
    # [END howto_operator_mrs_create_cluster_run_job_delete_cluster]

    (
        create_cluster
        >> wait_cluster_running
        >> delete_cluster
    )


from tests.system.utils import get_test_run  # noqa: E402

# Needed to run the example DAG with pytest (see: tests/system/README.md#run_via_pytest)

test_run = get_test_run(dag)
