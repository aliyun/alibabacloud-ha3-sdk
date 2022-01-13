# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import time

from Tea.exceptions import TeaException, UnretryableException
from Tea.request import TeaRequest
from Tea.core import TeaCore
from alibabacloud_darabonba_encode_util.encoder import Encoder
from typing import Dict, Any, List

from alibabacloud_ha3engine import models as ha_3engine_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_darabonba_string.client import Client as StringClient
from alibabacloud_darabonba_map.client import Client as MapClient


class Client:
    _endpoint: str = None
    _instance_id: str = None
    _protocol: str = None
    _user_agent: str = None
    _credential: str = None
    _domainsuffix: str = None

    def __init__(
        self, 
        config: ha_3engine_models.Config,
    ):
        if UtilClient.is_unset(config):
            raise TeaException({
                'name': 'ParameterMissing',
                'message': "'config' can not be unset"
            })
        self._credential = self.get_realm_sign_str(config.access_user_name, config.access_pass_word)
        self._endpoint = config.endpoint
        self._instance_id = config.instance_id
        self._protocol = config.protocol
        self._user_agent = config.user_agent
        self._domainsuffix = 'ha.aliyuncs.com'

    def _request(
        self,
        method: str,
        pathname: str,
        query: Dict[str, Any],
        headers: Dict[str, str],
        body: Any,
        runtime: util_models.RuntimeOptions,
    ) -> Dict[str, Any]:
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 5)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.protocol = UtilClient.default_string(self._protocol, 'HTTP')
                _request.method = method
                _request.pathname = pathname
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._instance_id}.{self._domainsuffix}'),
                    'authorization': f'Basic {self._credential}',
                    'content-type': 'application/json; charset=utf-8'
                }, headers)
                if not UtilClient.is_unset(query):
                    _request.query = UtilClient.stringify_map_value(query)
                    _request.headers['X-Opensearch-Request-ID'] = UtilClient.get_nonce()
                if not UtilClient.is_unset(body):
                    _request.headers['X-Opensearch-Swift-Request-ID'] = UtilClient.get_nonce()
                    _request.body = UtilClient.to_jsonstring(body)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                obj_str = UtilClient.read_as_string(_response.body)
                if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
                    raw_map = {
                        'errors': UtilClient.parse_json(obj_str)
                    }
                    raise TeaException({
                        'message': _response.status_message,
                        'data': raw_map,
                        'code': _response.status_code
                    })
                if UtilClient.empty(obj_str):
                    rawbody_map = {
                        'status': _response.status_message,
                        'code': _response.status_code
                    }
                    return {
                        'body': UtilClient.to_jsonstring(rawbody_map),
                        'headers': _response.headers
                    }
                return {
                    'body': obj_str,
                    'headers': _response.headers
                }
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def _request_async(
        self,
        method: str,
        pathname: str,
        query: Dict[str, Any],
        headers: Dict[str, str],
        body: Any,
        runtime: util_models.RuntimeOptions,
    ) -> Dict[str, Any]:
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'httpProxy': runtime.http_proxy,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 5)
            },
            'backoff': {
                'policy': UtilClient.default_string(runtime.backoff_policy, 'no'),
                'period': UtilClient.default_number(runtime.backoff_period, 1)
            },
            'ignoreSSL': runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.protocol = UtilClient.default_string(self._protocol, 'HTTP')
                _request.method = method
                _request.pathname = pathname
                _request.headers = TeaCore.merge({
                    'user-agent': self.get_user_agent(),
                    'host': UtilClient.default_string(self._endpoint, f'{self._instance_id}.{self._domainsuffix}'),
                    'authorization': f'Basic {self._credential}',
                    'content-type': 'application/json; charset=utf-8'
                }, headers)
                if not UtilClient.is_unset(query):
                    _request.query = UtilClient.stringify_map_value(query)
                    _request.headers['X-Opensearch-Request-ID'] = UtilClient.get_nonce()
                if not UtilClient.is_unset(body):
                    _request.headers['X-Opensearch-Swift-Request-ID'] = UtilClient.get_nonce()
                    _request.body = UtilClient.to_jsonstring(body)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                obj_str = await UtilClient.read_as_string_async(_response.body)
                if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
                    raw_map = {
                        'errors': UtilClient.parse_json(obj_str)
                    }
                    raise TeaException({
                        'message': _response.status_message,
                        'data': raw_map,
                        'code': _response.status_code
                    })
                if UtilClient.empty(obj_str):
                    rawbody_map = {
                        'status': _response.status_message,
                        'code': _response.status_code
                    }
                    return {
                        'body': UtilClient.to_jsonstring(rawbody_map),
                        'headers': _response.headers
                    }
                return {
                    'body': obj_str,
                    'headers': _response.headers
                }
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def set_user_agent(
        self,
        user_agent: str,
    ) -> None:
        """
        设置Client UA 配置.
        """
        self._user_agent = user_agent

    def append_user_agent(
        self,
        user_agent: str,
    ) -> None:
        """
        添加Client UA 配置.
        """
        self._user_agent = f'{self._user_agent} {user_agent}'

    def get_user_agent(self) -> str:
        """
        获取Client 配置 UA 配置.
        """
        user_agent = UtilClient.get_user_agent(self._user_agent)
        return user_agent

    def get_realm_sign_str(
        self,
        access_user_name: str,
        access_pass_word: str,
    ) -> str:
        """
        计算用户请求识别特征, 遵循 Basic Auth 生成规范.
        """
        access_user_name_str = StringClient.trim(access_user_name)
        access_pass_word_str = StringClient.trim(access_pass_word)
        realm_str = f'{access_user_name_str}:{access_pass_word_str}'
        return Encoder.base_64encode_to_string(StringClient.to_bytes(realm_str, 'UTF-8'))

    def build_ha_search_query(
        self,
        haquery: ha_3engine_models.HaQuery,
    ) -> str:
        if UtilClient.is_unset(haquery.query):
            raise TeaException({
                'name': 'ParameterMissing',
                'message': "'HaQuery.query' can not be unset"
            })
        temp_string = f'query={haquery.query}'
        config_str = self.build_ha_queryconfig_clause_str(haquery.config)
        temp_string = f"{temp_string}&&cluster={UtilClient.default_string(haquery.cluster, 'general')}"
        temp_string = f'{temp_string}&&config={config_str}'
        if not UtilClient.is_unset(haquery.filter):
            filter_str = haquery.filter
            if not UtilClient.empty(filter_str):
                field_value_trimed = StringClient.trim(filter_str)
                temp_string = f'{temp_string}&&filter={field_value_trimed}'
        if not UtilClient.is_unset(haquery.custom_query):
            for key_field in MapClient.key_set(haquery.custom_query):
                field_value = haquery.custom_query.get(key_field)
                if not UtilClient.empty(field_value):
                    field_value_trimed = StringClient.trim(field_value)
                    key_field_trimed = StringClient.trim(key_field)
                    temp_string = f'{temp_string}&&{key_field_trimed}={field_value_trimed}'
        if not UtilClient.is_unset(haquery.sort):
            sort_str = self.build_ha_query_sort_clause_str(haquery.sort)
            if not UtilClient.empty(sort_str):
                temp_string = f'{temp_string}&&sort={sort_str}'
        if not UtilClient.is_unset(haquery.aggregate):
            aggregate_clause_str = self.build_ha_query_aggregate_clause_str(haquery.aggregate)
            if not UtilClient.empty(aggregate_clause_str):
                temp_string = f'{temp_string}&&aggregate={aggregate_clause_str}'
        if not UtilClient.is_unset(haquery.distinct):
            distinct_clause_str = self.build_ha_query_distinct_clause_str(haquery.distinct)
            if not UtilClient.empty(distinct_clause_str):
                temp_string = f'{temp_string}&&distinct={distinct_clause_str}'
        kvpairs = self.build_searc_kv_pair_clause_str(haquery.kvpairs)
        if not UtilClient.empty(kvpairs):
            temp_string = f'{temp_string}&&kvpairs={kvpairs}'
        return temp_string

    def build_ha_query_aggregate_clause_str(
        self,
        clause: List[ha_3engine_models.HaQueryAggregateClause],
    ) -> str:
        temp_clause_string = ''
        for aggregate_clause in clause:
            temp_aggregate_clause_string = ''
            if UtilClient.is_unset(aggregate_clause.group_key) or UtilClient.is_unset(aggregate_clause.agg_fun):
                raise TeaException({
                    'name': 'ParameterMissing',
                    'message': "'HaQueryAggregateClause.groupKey/aggFun' can not be unset"
                })
            if not UtilClient.empty(aggregate_clause.group_key) and not UtilClient.empty(aggregate_clause.agg_fun):
                group_key_trimed = StringClient.trim(aggregate_clause.group_key)
                agg_fun_trimed = StringClient.trim(aggregate_clause.agg_fun)
                temp_aggregate_clause_string = f'group_key:{group_key_trimed},agg_fun:{agg_fun_trimed}'
            if not UtilClient.empty(aggregate_clause.range):
                range_trimed = StringClient.trim(aggregate_clause.range)
                temp_aggregate_clause_string = f'{temp_aggregate_clause_string},range:{range_trimed}'
            if not UtilClient.empty(aggregate_clause.max_group):
                max_group_trimed = StringClient.trim(aggregate_clause.max_group)
                temp_aggregate_clause_string = f'{temp_aggregate_clause_string},max_group:{max_group_trimed}'
            if not UtilClient.empty(aggregate_clause.agg_filter):
                agg_filter_trimed = StringClient.trim(aggregate_clause.agg_filter)
                temp_aggregate_clause_string = f'{temp_aggregate_clause_string},agg_filter:{agg_filter_trimed}'
            if not UtilClient.empty(aggregate_clause.agg_sampler_thres_hold):
                agg_sampler_thres_hold_trimed = StringClient.trim(aggregate_clause.agg_sampler_thres_hold)
                temp_aggregate_clause_string = f'{temp_aggregate_clause_string},agg_sampler_threshold:{agg_sampler_thres_hold_trimed}'
            if not UtilClient.empty(aggregate_clause.agg_sampler_step):
                agg_sampler_step_trimed = StringClient.trim(aggregate_clause.agg_sampler_step)
                temp_aggregate_clause_string = f'{temp_aggregate_clause_string},agg_sampler_step:{agg_sampler_step_trimed}'
            if not UtilClient.empty(temp_clause_string):
                temp_clause_string = f'{temp_clause_string};{temp_aggregate_clause_string}'
            else:
                temp_clause_string = f'{temp_aggregate_clause_string}'
        return temp_clause_string

    def build_ha_query_distinct_clause_str(
        self,
        clause: List[ha_3engine_models.HaQueryDistinctClause],
    ) -> str:
        temp_clause_string = ''
        for distinct_clause in clause:
            temp_distinct_clause_string = ''
            if UtilClient.is_unset(distinct_clause.dist_key):
                raise TeaException({
                    'name': 'ParameterMissing',
                    'message': "'HaQueryDistinctClause.distKey' can not be unset"
                })
            if not UtilClient.empty(distinct_clause.dist_key):
                dist_key_trimed = StringClient.trim(distinct_clause.dist_key)
                temp_distinct_clause_string = f'dist_key:{dist_key_trimed}'
            if not UtilClient.empty(distinct_clause.dist_count):
                dist_count_trimed = StringClient.trim(distinct_clause.dist_count)
                temp_distinct_clause_string = f'{temp_distinct_clause_string},dist_count:{dist_count_trimed}'
            if not UtilClient.empty(distinct_clause.dist_times):
                dist_times_trimed = StringClient.trim(distinct_clause.dist_times)
                temp_distinct_clause_string = f'{temp_distinct_clause_string},dist_times:{dist_times_trimed}'
            if not UtilClient.empty(distinct_clause.reserved):
                reserved_trimed = StringClient.trim(distinct_clause.reserved)
                temp_distinct_clause_string = f'{temp_distinct_clause_string},reserved:{reserved_trimed}'
            if not UtilClient.empty(distinct_clause.dist_filter):
                dist_filter_trimed = StringClient.trim(distinct_clause.dist_filter)
                temp_distinct_clause_string = f'{temp_distinct_clause_string},dist_filter:{dist_filter_trimed}'
            if not UtilClient.empty(distinct_clause.update_total_hit):
                update_total_hit_trimed = StringClient.trim(distinct_clause.update_total_hit)
                temp_distinct_clause_string = f'{temp_distinct_clause_string},update_total_hit:{update_total_hit_trimed}'
            if not UtilClient.empty(distinct_clause.grade):
                grade_trimed = StringClient.trim(distinct_clause.grade)
                temp_distinct_clause_string = f'{temp_distinct_clause_string},grade:{grade_trimed}'
            if not UtilClient.empty(temp_clause_string):
                temp_clause_string = f'{temp_clause_string};{temp_distinct_clause_string}'
            else:
                temp_clause_string = f'{temp_distinct_clause_string}'
        return temp_clause_string

    def build_ha_query_sort_clause_str(
        self,
        clause: List[ha_3engine_models.HaQuerySortClause],
    ) -> str:
        temp_clause_string = ''
        for sort_clause in clause:
            field_value_trimed = StringClient.trim(sort_clause.sort_order)
            key_field_trimed = StringClient.trim(sort_clause.sort_key)
            if UtilClient.equal_string(field_value_trimed, '+') or UtilClient.equal_string(field_value_trimed, '-'):
                if not UtilClient.empty(field_value_trimed) and not UtilClient.empty(key_field_trimed):
                    if UtilClient.empty(temp_clause_string):
                        temp_clause_string = f'{field_value_trimed}{key_field_trimed}'
                    else:
                        temp_clause_string = f'{temp_clause_string};{field_value_trimed}{key_field_trimed}'
        return temp_clause_string

    def build_ha_queryconfig_clause_str(
        self,
        clause: ha_3engine_models.HaQueryconfigClause,
    ) -> str:
        temp_clause_string = ''
        if UtilClient.is_unset(clause):
            raise TeaException({
                'name': 'ParameterMissing',
                'message': "'HaQueryconfigClause' can not be unset"
            })
        if UtilClient.is_unset(clause.start):
            clause.start = ''
        if UtilClient.is_unset(clause.hit):
            clause.hit = ''
        if UtilClient.is_unset(clause.format):
            clause.format = ''
        temp_clause_string = f"start:{UtilClient.default_string(clause.start, '1')}"
        temp_clause_string = f"{temp_clause_string},hit:{UtilClient.default_string(clause.hit, '10')}"
        temp_clause_string = f"{temp_clause_string},format:{UtilClient.default_string(StringClient.to_lower(clause.format), 'json')}"
        if not UtilClient.is_unset(clause.custom_config):
            for key_field in MapClient.key_set(clause.custom_config):
                field_value = clause.custom_config.get(key_field)
                if not UtilClient.empty(field_value):
                    field_value_trimed = StringClient.trim(field_value)
                    key_field_trimed = StringClient.trim(key_field)
                    if not UtilClient.empty(temp_clause_string):
                        temp_clause_string = f'{temp_clause_string},{key_field_trimed}:{field_value_trimed}'
                    else:
                        temp_clause_string = f'{key_field_trimed}:{field_value_trimed}'
        return temp_clause_string

    def build_sqlsearch_query(
        self,
        sqlquery: ha_3engine_models.SQLQuery,
    ) -> str:
        if UtilClient.is_unset(sqlquery.query):
            raise TeaException({
                'name': 'ParameterMissing',
                'message': "'SQLQuery.query' can not be unset"
            })
        temp_string = f'query={sqlquery.query}'
        kvpairs = self.build_searc_kv_pair_clause_str(sqlquery.kvpairs)
        if not UtilClient.empty(kvpairs):
            temp_string = f'{temp_string}&&kvpair={kvpairs}'
        return temp_string

    def build_searc_kv_pair_clause_str(
        self,
        kv_pair: Dict[str, str],
    ) -> str:
        tempkvpairs_string = f'__ops_request_id:{UtilClient.get_nonce()}'
        if not UtilClient.is_unset(kv_pair):
            for key_field in MapClient.key_set(kv_pair):
                field_value = kv_pair.get(key_field)
                if not UtilClient.empty(field_value):
                    field_value_trimed = StringClient.trim(field_value)
                    key_field_trimed = StringClient.trim(key_field)
                    tempkvpairs_string = f'{tempkvpairs_string},{key_field_trimed}:{field_value_trimed}'
        return tempkvpairs_string

    def search_ex(
        self,
        request: ha_3engine_models.SearchRequestModel,
        runtime: util_models.RuntimeOptions,
    ) -> ha_3engine_models.SearchResponseModel:
        """
        系统提供了丰富的搜索语法以满足用户各种场景下的搜索需求。
        """
        return TeaCore.from_map(
            ha_3engine_models.SearchResponseModel(),
            self._request('GET', f'/query', TeaCore.to_map(request.query), request.headers, None, runtime)
        )

    async def search_ex_async(
        self,
        request: ha_3engine_models.SearchRequestModel,
        runtime: util_models.RuntimeOptions,
    ) -> ha_3engine_models.SearchResponseModel:
        """
        系统提供了丰富的搜索语法以满足用户各种场景下的搜索需求。
        """
        return TeaCore.from_map(
            ha_3engine_models.SearchResponseModel(),
            await self._request_async('GET', f'/query', TeaCore.to_map(request.query), request.headers, None, runtime)
        )

    def search(
        self,
        request: ha_3engine_models.SearchRequestModel,
    ) -> ha_3engine_models.SearchResponseModel:
        """
        系统提供了丰富的搜索语法以满足用户各种场景下的搜索需求。
        """
        runtime = util_models.RuntimeOptions(
            connect_timeout=5000,
            read_timeout=10000,
            autoretry=False,
            ignore_ssl=False,
            max_idle_conns=50
        )
        return self.search_ex(request, runtime)

    async def search_async(
        self,
        request: ha_3engine_models.SearchRequestModel,
    ) -> ha_3engine_models.SearchResponseModel:
        """
        系统提供了丰富的搜索语法以满足用户各种场景下的搜索需求。
        """
        runtime = util_models.RuntimeOptions(
            connect_timeout=5000,
            read_timeout=10000,
            autoretry=False,
            ignore_ssl=False,
            max_idle_conns=50
        )
        return await self.search_ex_async(request, runtime)

    def push_document_ex(
        self,
        data_source_name: str,
        request: ha_3engine_models.PushDocumentsRequestModel,
        runtime: util_models.RuntimeOptions,
    ) -> ha_3engine_models.PushDocumentsResponseModel:
        """
        支持新增、更新、删除 等操作，以及对应批量操作
        """
        return TeaCore.from_map(
            ha_3engine_models.PushDocumentsResponseModel(),
            self._request('POST', f'/update/{data_source_name}/actions/bulk', None, request.headers, request.body, runtime)
        )

    async def push_document_ex_async(
        self,
        data_source_name: str,
        request: ha_3engine_models.PushDocumentsRequestModel,
        runtime: util_models.RuntimeOptions,
    ) -> ha_3engine_models.PushDocumentsResponseModel:
        """
        支持新增、更新、删除 等操作，以及对应批量操作
        """
        return TeaCore.from_map(
            ha_3engine_models.PushDocumentsResponseModel(),
            await self._request_async('POST', f'/update/{data_source_name}/actions/bulk', None, request.headers, request.body, runtime)
        )

    def push_documens(
        self,
        data_source_name: str,
        key_field: str,
        request: ha_3engine_models.PushDocumentsRequestModel,
    ) -> ha_3engine_models.PushDocumentsResponseModel:
        """
        支持新增、更新、删除 等操作，以及对应批量操作
        """
        runtime = util_models.RuntimeOptions(
            connect_timeout=5000,
            read_timeout=10000,
            autoretry=False,
            ignore_ssl=False,
            max_idle_conns=50
        )
        request.headers = {
            'X-Opensearch-Swift-PK-Field': key_field
        }
        return self.push_document_ex(data_source_name, request, runtime)

    async def push_documens_async(
        self,
        data_source_name: str,
        key_field: str,
        request: ha_3engine_models.PushDocumentsRequestModel,
    ) -> ha_3engine_models.PushDocumentsResponseModel:
        """
        支持新增、更新、删除 等操作，以及对应批量操作
        """
        runtime = util_models.RuntimeOptions(
            connect_timeout=5000,
            read_timeout=10000,
            autoretry=False,
            ignore_ssl=False,
            max_idle_conns=50
        )
        request.headers = {
            'X-Opensearch-Swift-PK-Field': key_field
        }
        return await self.push_document_ex_async(data_source_name, request, runtime)
