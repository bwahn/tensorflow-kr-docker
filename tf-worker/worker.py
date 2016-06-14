# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tensorflow as tf
import os
import logging
import sys
import ast

root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
root.addHandler(ch)

POD_NAME = os.environ.get('POD_NAME')
#CLUSTER_CONFIG = os.environ.get('CLUSTER_CONFIG')
logging.info(POD_NAME)


#def main(job_name, task_id, cluster_def):
def main(job_name, task_id):
    server = tf.train.Server(
        #cluster_def,
        {
            "ps": [
                "ps-0:8080",
                "ps-1:8080",
                "ps-2:8080",
                "ps-3:8080",
            ],
            "worker": [
                "worker-0:8080",
                "worker-1:8080",
                "worker-2:8080",
                "worker-3:8080",
                "worker-4:8080",
                "worker-5:8080",
                "worker-6:8080",
                "worker-7:8080",
            ],
            "master": [
                "master-0:8080",
            ],
        },
        job_name=job_name,
        task_index=task_id
    )
    server.join()


if __name__ == '__main__':
    this_job_name, this_task_id = POD_NAME.split('-', 2)
    #cluster_def = ast.literal_eval(CLUSTER_CONFIG)
    #main(this_job_name, int(this_task_id), cluster_def)
    main(this_job_name, int(this_task_id))
