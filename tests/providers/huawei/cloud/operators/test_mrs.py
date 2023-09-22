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

from unittest import TestCase, mock

from airflow.providers.huawei.cloud.operators.mrs import (
    MRSCreateClusterOperator,
    MRSCreateClusterRunJobOperator,
    MRSDeleteClusterOperator,
)

MOCK_TASK_ID = "test-mrs-operator"
MOCK_MRS_CONN_ID = "mock_mrs_conn_default"
MOCK_REGION = "mock_region"
MOCK_PROJECT_ID = "mock_project_id"
MOCK_CLUSTER_ID = "b2645baf-91e9-4afe-92a4-0e7738b587ad3"

MOCK_CLUSTER_VERSION = "MRS 3.1.5"
MOCK_CLUSTER_NAME = "mrs_airflow"
MOCK_CLUSTER_TYPE = "ANALYSIS"
MOCK_SAFE_MODE = "SIMPLE"
MOCK_MANAGER_ADMIN_PASSWORD = "mock_manager_admin_password"
MOCK_LOGIN_MODE = "PASSWORD"
MOCK_VPC_NAME = "mock_vpc_name"
MOCK_SUBNET_ID = "8beae632-aec2-vr59-vr35-saf214f4fe56"
MOCK_COMPONENTS = "mock_components"
MOCK_AVAILABILITY_ZONE = "ap-southeast-3b"
MOCK_NODE_GROUPS = [mock.MagicMock(spec=dict)]
MOCK_IS_DEC_PROJECT = False
MOCK_CHARGE_INFO = mock.MagicMock(spec=dict)
MOCK_SUBNET_NAME = "mock_subnet_name"
MOCK_EXTERNAL_DATASOURCES = [mock.MagicMock(spec=dict)]
MOCK_SECURITY_GROUPS_ID = "mock_security_groups_id"
MOCK_AUTO_CREATE_DEFAULT_SECURITY_GROUP = True
MOCK_NODE_ROOT_PASSWORD = "mock_node_root_password"
MOCK_NODE_KEYPAIR_NAME = "mock_node_keypair_name"
MOCK_ENTERPRISE_PROJECT_ID = "mock_enterprise_project_id"
MOCK_EIP_ADDRESS = "mock_eip_address"
MOCK_EIP_ID = "mock_eip_id"
MOCK_MRS_ECS_DEFAULT_AGENCY = "mock_mrs_ecs_default_agency"
MOCK_TEMPLATE_ID = "mock_template_id"
MOCK_TAGS = [{'key': 'creator', 'value': 'airflow'}, {'key': 'create_time', 'value': '20230918'}]
MOCK_LOG_COLLECTION = 1
MOCK_BOOTSTRAP_SCRIPTS = [mock.MagicMock(spec=dict)]
MOCK_LOG_URI = "mock_log_uri"
MOCK_COMPONENT_CONFIGS = [mock.MagicMock(spec=dict)]
MOCK_STEPS = [mock.MagicMock(spec=dict)]
MOCK_DELETE_WHEN_NO_STEPS = False

MOCK_CONTEXT = mock.Mock()


class TestMRSCreateClusterOperator(TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.mrs.MRSHook")
    def test_execute(self, mock_hook):
        operator = MRSCreateClusterOperator(
            cluster_version=MOCK_CLUSTER_VERSION,
            cluster_name=MOCK_CLUSTER_NAME,
            cluster_type=MOCK_CLUSTER_TYPE,
            safe_mode=MOCK_SAFE_MODE,
            manager_admin_password=MOCK_MANAGER_ADMIN_PASSWORD,
            login_mode=MOCK_LOGIN_MODE,
            vpc_name=MOCK_VPC_NAME,
            subnet_id=MOCK_SUBNET_ID,
            components=MOCK_COMPONENTS,
            availability_zone=MOCK_AVAILABILITY_ZONE,
            node_groups=MOCK_NODE_GROUPS,
            is_dec_project=MOCK_IS_DEC_PROJECT,
            subnet_name=MOCK_SUBNET_NAME,
            external_datasources=MOCK_EXTERNAL_DATASOURCES,
            security_groups_id=MOCK_SECURITY_GROUPS_ID,
            auto_create_default_security_group=MOCK_AUTO_CREATE_DEFAULT_SECURITY_GROUP,
            node_root_password=MOCK_NODE_ROOT_PASSWORD,
            node_keypair_name=MOCK_NODE_KEYPAIR_NAME,
            enterprise_project_id=MOCK_ENTERPRISE_PROJECT_ID,
            eip_address=MOCK_EIP_ADDRESS,
            eip_id=MOCK_EIP_ID,
            mrs_ecs_default_agency=MOCK_MRS_ECS_DEFAULT_AGENCY,
            template_id=MOCK_TEMPLATE_ID,
            tags=MOCK_TAGS,
            log_collection=MOCK_LOG_COLLECTION,
            bootstrap_scripts=MOCK_BOOTSTRAP_SCRIPTS,
            log_uri=MOCK_LOG_URI,
            component_configs=MOCK_COMPONENT_CONFIGS,
            task_id=MOCK_TASK_ID,
            project_id=MOCK_PROJECT_ID,
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MRS_CONN_ID,
        )

        operator.execute(MOCK_CONTEXT)

        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MRS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.create_cluster.assert_called_once_with(
            charge_info=None,
            is_dec_project=MOCK_IS_DEC_PROJECT,
            cluster_version=MOCK_CLUSTER_VERSION,
            cluster_name=MOCK_CLUSTER_NAME,
            cluster_type=MOCK_CLUSTER_TYPE,
            safe_mode=MOCK_SAFE_MODE,
            manager_admin_password=MOCK_MANAGER_ADMIN_PASSWORD,
            login_mode=MOCK_LOGIN_MODE,
            vpc_name=MOCK_VPC_NAME,
            subnet_id=MOCK_SUBNET_ID,
            components=MOCK_COMPONENTS,
            availability_zone=MOCK_AVAILABILITY_ZONE,
            node_groups=MOCK_NODE_GROUPS,
            subnet_name=MOCK_SUBNET_NAME,
            external_datasources=MOCK_EXTERNAL_DATASOURCES,
            security_groups_id=MOCK_SECURITY_GROUPS_ID,
            auto_create_default_security_group=MOCK_AUTO_CREATE_DEFAULT_SECURITY_GROUP,
            node_root_password=MOCK_NODE_ROOT_PASSWORD,
            node_keypair_name=MOCK_NODE_KEYPAIR_NAME,
            enterprise_project_id=MOCK_ENTERPRISE_PROJECT_ID,
            eip_address=MOCK_EIP_ADDRESS,
            eip_id=MOCK_EIP_ID,
            mrs_ecs_default_agency=MOCK_MRS_ECS_DEFAULT_AGENCY,
            template_id=MOCK_TEMPLATE_ID,
            tags=MOCK_TAGS,
            log_collection=MOCK_LOG_COLLECTION,
            bootstrap_scripts=MOCK_BOOTSTRAP_SCRIPTS,
            log_uri=MOCK_LOG_URI,
            component_configs=MOCK_COMPONENT_CONFIGS,
        )


class TestMRSCreateClusterRunJobOperator(TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.mrs.MRSHook")
    def test_execute(self, mock_hook):
        operator = MRSCreateClusterRunJobOperator(
            steps=MOCK_STEPS,
            delete_when_no_steps=MOCK_DELETE_WHEN_NO_STEPS,
            cluster_version=MOCK_CLUSTER_VERSION,
            cluster_name=MOCK_CLUSTER_NAME,
            cluster_type=MOCK_CLUSTER_TYPE,
            safe_mode=MOCK_SAFE_MODE,
            manager_admin_password=MOCK_MANAGER_ADMIN_PASSWORD,
            login_mode=MOCK_LOGIN_MODE,
            vpc_name=MOCK_VPC_NAME,
            subnet_id=MOCK_SUBNET_ID,
            components=MOCK_COMPONENTS,
            availability_zone=MOCK_AVAILABILITY_ZONE,
            node_groups=MOCK_NODE_GROUPS,
            is_dec_project=MOCK_IS_DEC_PROJECT,
            subnet_name=MOCK_SUBNET_NAME,
            external_datasources=MOCK_EXTERNAL_DATASOURCES,
            security_groups_id=MOCK_SECURITY_GROUPS_ID,
            auto_create_default_security_group=MOCK_AUTO_CREATE_DEFAULT_SECURITY_GROUP,
            node_root_password=MOCK_NODE_ROOT_PASSWORD,
            node_keypair_name=MOCK_NODE_KEYPAIR_NAME,
            enterprise_project_id=MOCK_ENTERPRISE_PROJECT_ID,
            eip_address=MOCK_EIP_ADDRESS,
            eip_id=MOCK_EIP_ID,
            mrs_ecs_default_agency=MOCK_MRS_ECS_DEFAULT_AGENCY,
            template_id=MOCK_TEMPLATE_ID,
            tags=MOCK_TAGS,
            log_collection=MOCK_LOG_COLLECTION,
            bootstrap_scripts=MOCK_BOOTSTRAP_SCRIPTS,
            log_uri=MOCK_LOG_URI,
            component_configs=MOCK_COMPONENT_CONFIGS,
            task_id=MOCK_TASK_ID,
            project_id=MOCK_PROJECT_ID,
            region=MOCK_REGION,
            huaweicloud_conn_id=MOCK_MRS_CONN_ID,
        )

        operator.execute(MOCK_CONTEXT)

        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MRS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )
        mock_hook.return_value.create_cluster_run_job.assert_called_once_with(
            steps=MOCK_STEPS,
            charge_info=None,
            delete_when_no_steps=MOCK_DELETE_WHEN_NO_STEPS,
            cluster_version=MOCK_CLUSTER_VERSION,
            cluster_name=MOCK_CLUSTER_NAME,
            cluster_type=MOCK_CLUSTER_TYPE,
            safe_mode=MOCK_SAFE_MODE,
            manager_admin_password=MOCK_MANAGER_ADMIN_PASSWORD,
            login_mode=MOCK_LOGIN_MODE,
            vpc_name=MOCK_VPC_NAME,
            subnet_id=MOCK_SUBNET_ID,
            components=MOCK_COMPONENTS,
            availability_zone=MOCK_AVAILABILITY_ZONE,
            node_groups=MOCK_NODE_GROUPS,
            is_dec_project=MOCK_IS_DEC_PROJECT,
            subnet_name=MOCK_SUBNET_NAME,
            external_datasources=MOCK_EXTERNAL_DATASOURCES,
            security_groups_id=MOCK_SECURITY_GROUPS_ID,
            auto_create_default_security_group=MOCK_AUTO_CREATE_DEFAULT_SECURITY_GROUP,
            node_root_password=MOCK_NODE_ROOT_PASSWORD,
            node_keypair_name=MOCK_NODE_KEYPAIR_NAME,
            enterprise_project_id=MOCK_ENTERPRISE_PROJECT_ID,
            eip_address=MOCK_EIP_ADDRESS,
            eip_id=MOCK_EIP_ID,
            mrs_ecs_default_agency=MOCK_MRS_ECS_DEFAULT_AGENCY,
            template_id=MOCK_TEMPLATE_ID,
            tags=MOCK_TAGS,
            log_collection=MOCK_LOG_COLLECTION,
            bootstrap_scripts=MOCK_BOOTSTRAP_SCRIPTS,
            log_uri=MOCK_LOG_URI,
            component_configs=MOCK_COMPONENT_CONFIGS,
        )


class TestMRSDeleteClusterOperator(TestCase):
    @mock.patch("airflow.providers.huawei.cloud.operators.mrs.MRSHook")
    def test_execute(self, mock_hook):
        operator = MRSDeleteClusterOperator(
            task_id=MOCK_TASK_ID,
            cluster_id=MOCK_CLUSTER_ID,
            region=MOCK_REGION,
            project_id=MOCK_PROJECT_ID,
            huaweicloud_conn_id=MOCK_MRS_CONN_ID,
        )

        operator.execute(MOCK_CONTEXT)

        mock_hook.assert_called_once_with(
            huaweicloud_conn_id=MOCK_MRS_CONN_ID, region=MOCK_REGION, project_id=MOCK_PROJECT_ID
        )

        mock_hook.return_value.delete_cluster.assert_called_once_with(cluster_id=MOCK_CLUSTER_ID)
