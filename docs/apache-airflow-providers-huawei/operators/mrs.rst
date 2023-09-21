 .. Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

 ..   http://www.apache.org/licenses/LICENSE-2.0

 .. Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.

==========================
Huawei Cloud MRS Operators
==========================

`MapReduce Service (MRS) <https://support.huaweicloud.com/intl/en-us/mrs/>`__ is provided on Huawei Cloud for you to
manage Hadoop-based components. With MRS, you can deploy a Hadoop cluster with a few clicks. MRS provides
enterprise-level big data clusters on the cloud. Tenants can fully control clusters and easily run big data components
such as Storm, Hadoop, Spark, HBase, and Kafka. MRS is fully compatible with open source APIs, and incorporates
advantages of Huawei Cloud computing and storage and big data industry experience to provide customers with a full-stack
big data platform featuring high performance, low cost, flexibility, and ease-of-use. In addition, the platform can be
customized based on service requirements to help enterprises quickly build a massive data processing system and
discover new value points and business opportunities by analyzing and mining massive amounts of data in real time
or in non-real time.

 - :class:`~airflow.providers.huawei.cloud.operators.mrs.MRSCreateClusterOperator`
 - :class:`~airflow.providers.huawei.cloud.operators.mrs.MRSCreateClusterRunJobOperator`
 - :class:`~airflow.providers.huawei.cloud.operators.mrs.MRSDeleteClusterOperator`
 - :class:`~airflow.providers.huawei.cloud.sensors.mrs.MRSShowClusterStateSensor`


Operators
---------

Create a Huawei Cloud MRS cluster
=================================

To create a Huawei Cloud MRS Cluster with the specified parameters you can use.
:class:`~airflow.providers.huawei.cloud.operators.mrs.MRSCreateClusterOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_mrs.py
    :language: python
    :dedent: 4
    :start-after: [START howto_operator_mrs_create_cluster]
    :end-before: [END howto_operator_mrs_create_cluster]

Create a Huawei Cloud MRS cluster and run job
=============================================

To create a Huawei Cloud MRS Cluster, run job list, and delete the cluster.
:class:`~airflow.providers.huawei.cloud.operators.mrs.MRSCreateClusterRunJobOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_mrs.py
    :language: python
    :dedent: 4
    :start-after: [START howto_operator_mrs_create_cluster_run_job_delete_cluster]
    :end-before: [END howto_operator_mrs_create_cluster_run_job_delete_cluster]

.. _howto/operator: DWSDeleteClusterSnapshotOperator:

Delete a Huawei Cloud MRS cluster snapshot
===========================================

To delete a Huawei Cloud MRS cluster snapshot with cluster id.
:class:`~airflow.providers.huawei.cloud.operators.mrs.MRSDeleteClusterOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_mrs.py
    :language: python
    :dedent: 4
    :start-after: [START howto_operator_mrs_delete_cluster]
    :end-before: [END howto_operator_mrs_delete_cluster]

Sensors
-------

Waits for an MRS cluster to reach a specific status
===================================================

To wait for a MRS cluster to reach a specific status.
:class:`~airflow.providers.huawei.cloud.sensors.mrs.MRSShowClusterStateSensor`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_mrs.py
    :language: python
    :dedent: 4
    :start-after: [START howto_sensor_mrs_wait_cluster_running]
    :end-before: [END howto_sensor_mrs_wait_cluster_running]

