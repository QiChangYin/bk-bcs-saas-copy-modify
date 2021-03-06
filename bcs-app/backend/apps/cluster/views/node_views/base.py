# -*- coding: utf-8 -*-
#
# Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
# Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
from backend.components import paas_cc
from backend.utils.errcodes import ErrorCode
from backend.utils.error_codes import error_codes


class Nodes:

    def get_node_by_id(self, access_token, project_id, cluster_id, node_id):
        """get node detail info by node id
        """
        resp = paas_cc.get_node(access_token, project_id, node_id, cluster_id=cluster_id)
        if resp.get('code') != ErrorCode.NoError:
            raise error_codes.APIError(resp.get('message'))
        return resp.get('data') or {}

    def update_nodes_in_cluster(self, access_token, project_id, cluster_id, node_ips, status):
        """update nodes status in the same cluster
        """
        data = [
            {'inner_ip': ip, 'status': status}
            for ip in node_ips
        ]
        resp = paas_cc.update_node_list(access_token, project_id, cluster_id, data=data)
        if resp.get('code') != ErrorCode.NoError:
            raise error_codes.APIError(resp.get('message'))
        return resp.get('data') or []
