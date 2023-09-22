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

import random
from unittest import TestCase, mock

from airflow.providers.huawei.cloud.hooks.mrs import MRSHook, MrsV2Sdk, MrsV1Sdk
from tests.providers.huawei.cloud.utils.hw_mock import default_mock_constants, mock_huawei_cloud_default

MOCK_PROJECT_ID = default_mock_constants["PROJECT_ID"]
AK = default_mock_constants["AK"]
SK = default_mock_constants["SK"]
MRS_STRING = "airflow.providers.huawei.cloud.hooks.mrs.{}"
MOCK_MRS_CONN_ID = "mock_mrs_conn_default"

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
MOCK_CHARGE_INFO = {"charge_mode": "postPaid"}
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
MOCK_REGION = "ap-southeast-3"


class TestMRSHook(TestCase):
    def setUp(self):
        with mock.patch(
            MRS_STRING.format("MRSHook.__init__"),
            new=mock_huawei_cloud_default,
        ):
            self.hook = MRSHook(huaweicloud_conn_id=MOCK_MRS_CONN_ID)

    @mock.patch(MRS_STRING.format("BasicCredentials"))
    @mock.patch(MRS_STRING.format("MrsV2Sdk.MrsClient"))
    @mock.patch(MRS_STRING.format("MrsV1Sdk.MrsClient"))
    def test_get_mrs_client(self, mock_mrs_client_v1, mock_mrs_client_v2, mock_basic_credentials):
        version = random.choice(['v1', 'v2'])
        if version == 'v1':
            mock_mrs_client_v1.return_value = MrsV1Sdk.MrsClient()
        else:
            mock_mrs_client_v2.return_value = MrsV2Sdk.MrsClient()
        self.hook.get_mrs_client(version=version)

        mock_basic_credentials.assert_called_once_with(ak=AK, sk=SK, project_id=MOCK_PROJECT_ID)

    @mock.patch(MRS_STRING.format("MrsV2Sdk.CreateClusterRequest"))
    @mock.patch(MRS_STRING.format("MRSHook.get_mrs_client"))
    def test_create_cluster(self, mock_mrs_client, mock_request):
        mock_create_cluster = mock_mrs_client.return_value.create_cluster
        request_body = MrsV2Sdk.CreateClusterReqV2(
            is_dec_project=MOCK_IS_DEC_PROJECT,
            cluster_version=MOCK_CLUSTER_VERSION,
            cluster_name=MOCK_CLUSTER_NAME,
            cluster_type=MOCK_CLUSTER_TYPE,
            charge_info=MrsV2Sdk.ChargeInfo(charge_mode="postPaid"),
            region=MOCK_REGION,
            vpc_name=MOCK_VPC_NAME,
            subnet_id=MOCK_SUBNET_ID,
            subnet_name=MOCK_SUBNET_NAME,
            components=MOCK_COMPONENTS,
            external_datasources=[mock.MagicMock(spec=MrsV2Sdk.ClusterDataConnectorMap)],
            availability_zone=MOCK_AVAILABILITY_ZONE,
            security_groups_id=MOCK_SECURITY_GROUPS_ID,
            auto_create_default_security_group=MOCK_AUTO_CREATE_DEFAULT_SECURITY_GROUP,
            safe_mode=MOCK_SAFE_MODE,
            manager_admin_password=MOCK_MANAGER_ADMIN_PASSWORD,
            login_mode=MOCK_LOGIN_MODE,
            node_root_password=MOCK_NODE_ROOT_PASSWORD,
            node_keypair_name=MOCK_NODE_KEYPAIR_NAME,
            enterprise_project_id=MOCK_ENTERPRISE_PROJECT_ID,
            eip_address=MOCK_EIP_ADDRESS,
            eip_id=MOCK_EIP_ID,
            mrs_ecs_default_agency=MOCK_MRS_ECS_DEFAULT_AGENCY,
            template_id=MOCK_TEMPLATE_ID,
            tags=[MrsV2Sdk.Tag(key="creator", value="airflow"),
                  MrsV2Sdk.Tag(key="create_time", value="20230918")],
            log_collection=MOCK_LOG_COLLECTION,
            node_groups=[mock.MagicMock(spec=MrsV2Sdk.NodeGroupV2)],
            bootstrap_scripts=[mock.MagicMock(spec=MrsV2Sdk.BootstrapScript)],
            log_uri=MOCK_LOG_URI,
            component_configs=[mock.MagicMock(spec=MrsV2Sdk.ComponentConfig)],
        )
        request = mock_request(body=request_body)

        self.hook.create_cluster(
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
            charge_info=MOCK_CHARGE_INFO,
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

        mock_create_cluster.assert_called_once_with(request)

    @mock.patch(MRS_STRING.format("MrsV2Sdk.RunJobFlowRequest"))
    @mock.patch(MRS_STRING.format("MRSHook.get_mrs_client"))
    def test_create_cluster_run_job(self, mock_mrs_client, mock_request):
        mock_run_job_flow = mock_mrs_client.return_value.run_job_flow
        mock_run_job_flow.return_value = mock.Mock(cluster=mock.Mock(id=MOCK_CLUSTER_ID))
        request_body = MrsV2Sdk.RunJobFlowCommand(
            steps=[mock.MagicMock(spec=MrsV2Sdk.StepConfig)],
            delete_when_no_steps=MOCK_DELETE_WHEN_NO_STEPS,
            is_dec_project=MOCK_IS_DEC_PROJECT,
            cluster_version=MOCK_CLUSTER_VERSION,
            cluster_name=MOCK_CLUSTER_NAME,
            cluster_type=MOCK_CLUSTER_TYPE,
            charge_info=MrsV2Sdk.ChargeInfo(charge_mode="postPaid"),
            region=MOCK_REGION,
            vpc_name=MOCK_VPC_NAME,
            subnet_id=MOCK_SUBNET_ID,
            subnet_name=MOCK_SUBNET_NAME,
            components=MOCK_COMPONENTS,
            external_datasources=[mock.MagicMock(spec=MrsV2Sdk.ClusterDataConnectorMap)],
            availability_zone=MOCK_AVAILABILITY_ZONE,
            security_groups_id=MOCK_SECURITY_GROUPS_ID,
            auto_create_default_security_group=MOCK_AUTO_CREATE_DEFAULT_SECURITY_GROUP,
            safe_mode=MOCK_SAFE_MODE,
            manager_admin_password=MOCK_MANAGER_ADMIN_PASSWORD,
            login_mode=MOCK_LOGIN_MODE,
            node_root_password=MOCK_NODE_ROOT_PASSWORD,
            node_keypair_name=MOCK_NODE_KEYPAIR_NAME,
            enterprise_project_id=MOCK_ENTERPRISE_PROJECT_ID,
            eip_address=MOCK_EIP_ADDRESS,
            eip_id=MOCK_EIP_ID,
            mrs_ecs_default_agency=MOCK_MRS_ECS_DEFAULT_AGENCY,
            template_id=MOCK_TEMPLATE_ID,
            tags=[MrsV2Sdk.Tag(key="creator", value="airflow"),
                  MrsV2Sdk.Tag(key="create_time", value="20230918")],
            log_collection=MOCK_LOG_COLLECTION,
            node_groups=[mock.MagicMock(spec=MrsV2Sdk.NodeGroupV2)],
            bootstrap_scripts=[mock.MagicMock(spec=MrsV2Sdk.BootstrapScript)],
            log_uri=MOCK_LOG_URI,
            component_configs=[mock.MagicMock(spec=MrsV2Sdk.ComponentConfig)],
        )
        request = mock_request(body=request_body)

        self.hook.create_cluster_run_job(
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
            charge_info=MOCK_CHARGE_INFO,
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

        mock_run_job_flow.assert_called_once_with(request)

    @mock.patch(MRS_STRING.format("MRSHook.get_mrs_client"))
    def test_delete_cluster(self, mock_mrs_client):
        mock_delete_cluster = mock_mrs_client.return_value.delete_cluster
        request = MrsV1Sdk.DeleteClusterRequest(cluster_id=MOCK_CLUSTER_ID)

        self.hook.delete_cluster(cluster_id=MOCK_CLUSTER_ID)

        mock_delete_cluster.assert_called_once_with(request)

    @mock.patch(MRS_STRING.format("MRSHook.get_mrs_client"))
    def test_show_cluster_details(self, mock_mrs_client):
        mock_show_cluster_details = mock_mrs_client.return_value.show_cluster_details
        request = MrsV1Sdk.ShowClusterDetailsRequest(cluster_id=MOCK_CLUSTER_ID)

        self.hook.show_cluster_details(cluster_id=MOCK_CLUSTER_ID)

        mock_show_cluster_details.assert_called_once_with(request)


