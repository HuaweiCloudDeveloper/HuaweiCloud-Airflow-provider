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

from typing import TYPE_CHECKING, Any, Sequence

if TYPE_CHECKING:
    from airflow.utils.context import Context

from airflow.compat.functools import cached_property
from airflow.exceptions import AirflowException
from airflow.sensors.base import BaseSensorOperator
from airflow.providers.huawei.cloud.hooks.mrs import MRSHook


class MRSShowClusterStateSensor(BaseSensorOperator):
    """
    Sensor for checking the state of an MRS cluster.

    :param cluster_id: The cluster ID.
    :param target_status: The cluster status desired.

        - starting: The cluster is being started.
        - running: The cluster is running.
        - terminated: The cluster has been deleted.
        - failed: The cluster is failed.
        - abnormal: The cluster is abnormal.
        - terminating: The cluster is being deleted.
        - frozen: The cluster is frozen.
        - scaling-out: The cluster is being scaled out.
        - scaling-in: The cluster is being scaled in.
    :param region: The MRS region.
    :param project_id: Project ID.
    :param huaweicloud_conn_id: The Airflow connection used for MRS credentials.
        If this is None or empty then the default obs behaviour is used. If
        running Airflow in a distributed manner and huaweicloud_conn_id is None or
        empty, then default obs configuration would be used (and must be
        maintained on each worker node).
    """
    FAILURE_STATES = ("failed", "abnormal")

    template_fields: Sequence[str] = ("cluster_id",)
    template_ext: Sequence[str] = ()
    ui_color = "#66c3ff"

    def __init__(
        self,
        *,
        cluster_id: str,
        target_status: str = "running",
        region: str | None = None,
        project_id: str | None = None,
        huaweicloud_conn_id: str = "huaweicloud_default",
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cluster_id = cluster_id
        self.target_status = target_status
        self.region = region
        self.project_id = project_id
        self.huaweicloud_conn_id = huaweicloud_conn_id

    def poke(self, context: Context) -> bool:
        state = self.get_hook.show_cluster_details(cluster_id=self.cluster_id).cluster.cluster_state
        self.log.info("Poking for status : %s for cluster %s. Now cluster status: %s",
                      self.target_status, self.cluster_id, state)
        if state in self.FAILURE_STATES:
            self.log.error(f"MRS sensor cluster({self.cluster_id}) failed.")
            raise AirflowException("MRS sensor failed")
        return state == self.target_status

    @cached_property
    def get_hook(self) -> MRSHook:
        """Create and return a MRSHook"""
        return MRSHook(
            huaweicloud_conn_id=self.huaweicloud_conn_id, project_id=self.project_id, region=self.region
        )

