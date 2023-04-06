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

================================
Huawei Cloud ModelArts Operators
================================

Overview
--------

ModelArts is a one-stop AI platform that enables developers and data scientists of any skill level to rapidly build, train, and deploy models anywhere, from the cloud to the edge.

 - :class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsCreateDatasetOperator`
 - :class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsCreateModelOperator`
 - :class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsUpdateDatasetOperator`
 - :class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsDeleteDatasetVersionOperator`
 - :class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsCreateAlgorithmOperator`
 - :class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsDeleteAlgorithmOperator`
 - :class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsChangeAlgorithmOperator`
 - :class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsCreateServiceOperator`
 - :class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsDeleteServiceOperator`
 - :class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsUpdateServiceOperator`
 - :class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsCreateTrainingJobOperator`
 - :class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsDeleteTrainingJobOperator`
 - :class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsStopTrainingJobOperator`
 - :class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsDeleteModelOperator`


Operators
---------

Create a dataset
================

To to create a dataset you can use
:class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsCreateDatasetOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_modelarts.py
   :dedent: 4
   :language: python
   :start-after: [START howto_operator_modelarts_create_dataset]
   :end-before: [END howto_operator_modelarts_create_dataset]


Update a dataset
================

To modify basic information about a dataset such as the dataset name, description, current version, and labels you can use
:class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsUpdateDatasetOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_modelarts.py
   :dedent: 4
   :language: python
   :start-after: [START howto_operator_modelarts_update_dataset]
   :end-before: [END howto_operator_modelarts_update_dataset]

Delete a dataset version
========================

To delete a dataset labeling version you can use
:class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsDeleteDatasetVersionOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_modelarts.py
   :dedent: 4
   :language: python
   :start-after: [START howto_operator_modelarts_delete_dataset_version]
   :end-before: [END howto_operator_modelarts_delete_dataset_version]

Create an algorithm
===================

To create an algorithm you can use
:class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsCreateAlgorithmOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_modelarts.py
   :dedent: 4
   :language: python
   :start-after: [START howto_operator_modelarts_create_algorithm]
   :end-before: [END howto_operator_modelarts_create_algorithm]

Delete an algorithm
===================

To delete an algorithm you can use
:class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsDeleteAlgorithmOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_modelarts.py
   :dedent: 4
   :language: python
   :start-after: [START howto_operator_modelarts_delete_algorithm]
   :end-before: [END howto_operator_modelarts_delete_algorithm]

Change an algorithm
===================

To modify basic information about an algorithm such as the algorithm name, description, and labels you can use
:class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsChangeAlgorithmOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_modelarts.py
   :dedent: 4
   :language: python
   :start-after: [START howto_operator_modelarts_change_algorithm]
   :end-before: [END howto_operator_modelarts_change_algorithm]

Create a model
==============

To create a model you can use
:class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsCreateModelOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_modelarts.py
   :dedent: 4
   :language: python
   :start-after: [START howto_operator_modelarts_create_model]
   :end-before: [END howto_operator_modelarts_create_model]

Delete a model
==============

To delete a model you can use
:class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsDeleteModelOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_modelarts.py
   :dedent: 4
   :language: python
   :start-after: [START howto_operator_modelarts_delete_model]
   :end-before: [END howto_operator_modelarts_delete_model]

Create a service
================

To create a service you can use
:class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsCreateServiceOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_modelarts.py
   :dedent: 4
   :language: python
   :start-after: [START howto_operator_modelarts_create_service]
   :end-before: [END howto_operator_modelarts_create_service]

Delete a service
================

To delete a service you can use
:class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsDeleteServiceOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_modelarts.py
   :dedent: 4
   :language: python
   :start-after: [START howto_operator_modelarts_delete_service]
   :end-before: [END howto_operator_modelarts_delete_service]

Update a service
================

To modify basic information about a service such as the service name, description, and labels you can use
:class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsUpdateServiceOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_modelarts.py
   :dedent: 4
   :language: python
   :start-after: [START howto_operator_modelarts_update_service]
   :end-before: [END howto_operator_modelarts_update_service]

Create a training job
=====================

To create a training job you can use
:class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsCreateTrainingJobOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_modelarts.py
   :dedent: 4
   :language: python
   :start-after: [START howto_operator_modelarts_create_training_job]
   :end-before: [END howto_operator_modelarts_create_training_job]

Delete a training job
=====================

To delete a training job you can use
:class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsDeleteTrainingJobOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_modelarts.py
   :dedent: 4
   :language: python
   :start-after: [START howto_operator_modelarts_delete_training_job]
   :end-before: [END howto_operator_modelarts_delete_training_job]


Stop a training job
===================

To stop a training job you can use
:class:`~airflow.providers.huawei.cloud.operators.modelarts.ModelArtsStopTrainingJobOperator`.

.. exampleinclude:: /../../tests/system/providers/huawei/example_modelarts.py
   :dedent: 4
   :language: python
   :start-after: [START howto_operator_modelarts_stop_training_job]
   :end-before: [END howto_operator_modelarts_stop_training_job]
