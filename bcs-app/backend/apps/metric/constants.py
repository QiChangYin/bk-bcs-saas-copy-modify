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
from django.conf import settings

# 数据平台访问域名
URI_FIELDS_BASE = settings.BK_PAAS_HOST

# 数据平台app_code
DATA_APP_CODE = 'data'

# 数据平台清洗URL
_URI_DATA_CLEAN = '%2Fs%2Fdata%2Fdataset%2Finfo%2F{data_id}%2F%23data_clean'
URI_DATA_CLEAN = f'{settings.BK_PAAS_HOST}?app={DATA_APP_CODE}&url=' + _URI_DATA_CLEAN
