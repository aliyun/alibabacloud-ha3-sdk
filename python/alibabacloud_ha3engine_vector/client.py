# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import time

from Tea.exceptions import TeaException, UnretryableException
from Tea.request import TeaRequest
from Tea.core import TeaCore
from alibabacloud_darabonba_encode_util.encoder import Encoder
from typing import Dict, Any

from alibabacloud_tea_util import models as util_models
from alibabacloud_ha3engine_vector import models as ha_3engine_vector_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_darabonba_string.client import Client as StringClient
from alibabacloud_ha3_util.client import Client as Ha3UtilClient
from alibabacloud_darabonba_number.client import Client as NumberClient
from alibabacloud_darabonba_time.client import Client as TimeClient


class Client:
    _endpoint: str = None
    _instance_id: str = None
    _protocol: str = None
    _user_agent: str = None
    _credential: str = None
    _domainsuffix: str = None
    _runtime_options: util_models.RuntimeOptions = None

    def __init__(
        self, 
        config: ha_3engine_vector_models.Config,
    ):
        if UtilClient.is_unset(config):
            raise TeaException({
                'name': 'ParameterMissing',
                'message': "'config' can not be unset"
            })
        if UtilClient.is_unset(config.endpoint):
            raise TeaException({
                'name': 'ParameterMissing',
                'message': "'config.endpoint' can not be unset"
            })
        if not UtilClient.empty(config.access_user_name) and not UtilClient.empty(config.access_pass_word):
            self._credential = self.get_realm_sign_str(config.access_user_name, config.access_pass_word)
        self._endpoint = self.get_endpoint(config.endpoint)
        self._instance_id = self.get_instance_id(config)
        self._protocol = config.protocol
        self._user_agent = config.user_agent
        self._domainsuffix = 'ha.aliyuncs.com'
        self._runtime_options = self.build_runtime_options(config.runtime_options)

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
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': runtime.max_attempts
            },
            'backoff': {
                'policy': runtime.backoff_policy,
                'period': runtime.backoff_period
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
                    if StringClient.equals('deflate', _request.headers.get('Content-Encoding')) and not StringClient.contains(pathname, 'actions/bulk'):
                        compressed = Ha3UtilClient.deflate_compress(StringClient.to_bytes(UtilClient.to_jsonstring(body), 'UTF-8'))
                        _request.body = compressed
                    else:
                        _request.body = UtilClient.to_jsonstring(body)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                obj_str = UtilClient.read_as_string(_response.body)
                if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
                    raw_msg = None
                    try:
                        raw_msg = UtilClient.parse_json(obj_str)
                    except Exception as err:
                        raw_msg = obj_str
                    raw_map = {
                        'errors': raw_msg,
                        'headers': _response.headers
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
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': runtime.max_attempts
            },
            'backoff': {
                'policy': runtime.backoff_policy,
                'period': runtime.backoff_period
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
                    if StringClient.equals('deflate', _request.headers.get('Content-Encoding')) and not StringClient.contains(pathname, 'actions/bulk'):
                        compressed = await Ha3UtilClient.deflate_compress_async(StringClient.to_bytes(UtilClient.to_jsonstring(body), 'UTF-8'))
                        _request.body = compressed
                    else:
                        _request.body = UtilClient.to_jsonstring(body)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                obj_str = await UtilClient.read_as_string_async(_response.body)
                if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
                    raw_msg = None
                    try:
                        raw_msg = UtilClient.parse_json(obj_str)
                    except Exception as err:
                        raw_msg = obj_str
                    raw_map = {
                        'errors': raw_msg,
                        'headers': _response.headers
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

    def _open_api_request(
        self,
        method: str,
        pathname: str,
        query: Dict[str, Any],
        headers: Dict[str, str],
        body: Any,
        runtime: util_models.RuntimeOptions,
    ) -> dict:
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': runtime.max_attempts
            },
            'backoff': {
                'policy': runtime.backoff_policy,
                'period': runtime.backoff_period
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
                    'host': self._endpoint,
                    'authorization': f'Basic {self._credential}',
                    'content-type': 'application/json; charset=utf-8'
                }, headers)
                if not UtilClient.is_unset(query):
                    _request.query = UtilClient.stringify_map_value(query)
                if not UtilClient.is_unset(body):
                    _request.body = UtilClient.to_jsonstring(body)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                obj_str = UtilClient.read_as_string(_response.body)
                if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
                    raw_msg = None
                    try:
                        raw_msg = UtilClient.parse_json(obj_str)
                    except Exception as err:
                        raw_msg = obj_str
                    raise TeaException({
                        'message': obj_str,
                        'data': raw_msg,
                        'code': _response.status_code
                    })
                obj = UtilClient.parse_json(obj_str)
                return {
                    'body': obj,
                    'headers': _response.headers,
                    'statusCode': _response.status_code
                }
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def _open_api_request_async(
        self,
        method: str,
        pathname: str,
        query: Dict[str, Any],
        headers: Dict[str, str],
        body: Any,
        runtime: util_models.RuntimeOptions,
    ) -> dict:
        runtime.validate()
        _runtime = {
            'timeouted': 'retry',
            'readTimeout': runtime.read_timeout,
            'connectTimeout': runtime.connect_timeout,
            'httpsProxy': runtime.https_proxy,
            'noProxy': runtime.no_proxy,
            'maxIdleConns': runtime.max_idle_conns,
            'retry': {
                'retryable': runtime.autoretry,
                'maxAttempts': runtime.max_attempts
            },
            'backoff': {
                'policy': runtime.backoff_policy,
                'period': runtime.backoff_period
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
                    'host': self._endpoint,
                    'authorization': f'Basic {self._credential}',
                    'content-type': 'application/json; charset=utf-8'
                }, headers)
                if not UtilClient.is_unset(query):
                    _request.query = UtilClient.stringify_map_value(query)
                if not UtilClient.is_unset(body):
                    _request.body = UtilClient.to_jsonstring(body)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                obj_str = await UtilClient.read_as_string_async(_response.body)
                if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
                    raw_msg = None
                    try:
                        raw_msg = UtilClient.parse_json(obj_str)
                    except Exception as err:
                        raw_msg = obj_str
                    raise TeaException({
                        'message': obj_str,
                        'data': raw_msg,
                        'code': _response.status_code
                    })
                obj = UtilClient.parse_json(obj_str)
                return {
                    'body': obj,
                    'headers': _response.headers,
                    'statusCode': _response.status_code
                }
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_instance_id(
        self,
        config: ha_3engine_vector_models.Config,
    ) -> str:
        """
        如果用户传了实例id，则直接使用，否则从endpoint中解析实例id,
        """
        if not UtilClient.is_unset(config.instance_id):
            return config.instance_id
        values = StringClient.split(self._endpoint, '.', 2)
        value = values[0]
        return value

    def get_endpoint(
        self,
        endpoint: str,
    ) -> str:
        """
        如果endpoint 配置以 http:// 或 https:// 开头，则去掉头部的 http:// 或 https://, 否则直接返回
        """
        if StringClient.has_prefix(endpoint, 'http://'):
            return StringClient.replace(endpoint, 'http://', '', 1)
        if StringClient.has_prefix(endpoint, 'https://'):
            return StringClient.replace(endpoint, 'https://', '', 1)
        return endpoint

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

    def query(
        self,
        request: ha_3engine_vector_models.QueryRequest,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        向量查询
        """
        headers = self.get_headers_from_run_time_option()
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            self._request('POST', f'/vector-service/query', None, headers, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    async def query_async(
        self,
        request: ha_3engine_vector_models.QueryRequest,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        向量查询
        """
        headers = self.get_headers_from_run_time_option()
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            await self._request_async('POST', f'/vector-service/query', None, headers, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    def inference_query(
        self,
        request: ha_3engine_vector_models.QueryRequest,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        向量预测查询
        """
        headers = self.get_headers_from_run_time_option()
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            self._request('POST', f'/vector-service/inference-query', None, headers, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    async def inference_query_async(
        self,
        request: ha_3engine_vector_models.QueryRequest,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        向量预测查询
        """
        headers = self.get_headers_from_run_time_option()
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            await self._request_async('POST', f'/vector-service/inference-query', None, headers, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    def multi_query(
        self,
        request: ha_3engine_vector_models.MultiQueryRequest,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        多namespace查询
        """
        headers = self.get_headers_from_run_time_option()
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            self._request('POST', f'/vector-service/multi-query', None, headers, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    async def multi_query_async(
        self,
        request: ha_3engine_vector_models.MultiQueryRequest,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        多namespace查询
        """
        headers = self.get_headers_from_run_time_option()
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            await self._request_async('POST', f'/vector-service/multi-query', None, headers, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    def fetch(
        self,
        request: ha_3engine_vector_models.FetchRequest,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        查询数据
        """
        headers = self.get_headers_from_run_time_option()
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            self._request('POST', f'/vector-service/fetch', None, headers, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    async def fetch_async(
        self,
        request: ha_3engine_vector_models.FetchRequest,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        查询数据
        """
        headers = self.get_headers_from_run_time_option()
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            await self._request_async('POST', f'/vector-service/fetch', None, headers, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    def search(
        self,
        request: ha_3engine_vector_models.SearchRequest,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        文本向量混合检索
        """
        headers = self.get_headers_from_run_time_option()
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            self._request('POST', f'/vector-service/search', None, headers, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    async def search_async(
        self,
        request: ha_3engine_vector_models.SearchRequest,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        文本向量混合检索
        """
        headers = self.get_headers_from_run_time_option()
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            await self._request_async('POST', f'/vector-service/search', None, headers, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    def aggregate(
        self,
        request: ha_3engine_vector_models.AggregateRequest,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        向量引擎统计语法
        """
        headers = self.get_headers_from_run_time_option()
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            self._request('POST', f'/vector-service/aggregate', None, headers, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    async def aggregate_async(
        self,
        request: ha_3engine_vector_models.AggregateRequest,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        向量引擎统计语法
        """
        headers = self.get_headers_from_run_time_option()
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            await self._request_async('POST', f'/vector-service/aggregate', None, headers, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    def batch_query(
        self,
        request: ha_3engine_vector_models.BatchRequest,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        批量查询
        """
        headers = self.get_headers_from_run_time_option()
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            self._request('POST', f'/vector-service/batch-query', None, headers, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    async def batch_query_async(
        self,
        request: ha_3engine_vector_models.BatchRequest,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        批量查询
        """
        headers = self.get_headers_from_run_time_option()
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            await self._request_async('POST', f'/vector-service/batch-query', None, headers, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    def stats(
        self,
        table_name: str,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        文档统计
        """
        body = {
            'tableName': table_name
        }
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            self._request('POST', f'/vector-service/stats', None, None, UtilClient.to_jsonstring(body), self._runtime_options)
        )

    async def stats_async(
        self,
        table_name: str,
    ) -> ha_3engine_vector_models.SearchResponse:
        """
        文档统计
        """
        body = {
            'tableName': table_name
        }
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            await self._request_async('POST', f'/vector-service/stats', None, None, UtilClient.to_jsonstring(body), self._runtime_options)
        )

    def active(self) -> ha_3engine_vector_models.SearchResponse:
        """
        校验网络是否通畅
        检查vpc & 用户名密码配置是否正确
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            self._request('GET', f'/network/active', None, None, None, self._runtime_options)
        )

    async def active_async(self) -> ha_3engine_vector_models.SearchResponse:
        """
        校验网络是否通畅
        检查vpc & 用户名密码配置是否正确
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponse(),
            await self._request_async('GET', f'/network/active', None, None, None, self._runtime_options)
        )

    def push_documents(
        self,
        data_source_name: str,
        key_field: str,
        request: ha_3engine_vector_models.PushDocumentsRequest,
    ) -> ha_3engine_vector_models.PushDocumentsResponse:
        """
        支持新增、更新、删除 等操作，以及对应批量操作
        """
        request.headers = TeaCore.merge({
            'X-Opensearch-Swift-PK-Field': key_field,
            'X-Opensearch-Validate-Data': 'true'
        }, request.headers)
        return TeaCore.from_map(
            ha_3engine_vector_models.PushDocumentsResponse(),
            self._request('POST', f'/update/{data_source_name}/actions/bulk', None, request.headers, request.body, self._runtime_options)
        )

    async def push_documents_async(
        self,
        data_source_name: str,
        key_field: str,
        request: ha_3engine_vector_models.PushDocumentsRequest,
    ) -> ha_3engine_vector_models.PushDocumentsResponse:
        """
        支持新增、更新、删除 等操作，以及对应批量操作
        """
        request.headers = TeaCore.merge({
            'X-Opensearch-Swift-PK-Field': key_field,
            'X-Opensearch-Validate-Data': 'true'
        }, request.headers)
        return TeaCore.from_map(
            ha_3engine_vector_models.PushDocumentsResponse(),
            await self._request_async('POST', f'/update/{data_source_name}/actions/bulk', None, request.headers, request.body, self._runtime_options)
        )

    def build_runtime_options(
        self,
        runtime_options: util_models.RuntimeOptions,
    ) -> util_models.RuntimeOptions:
        """
        构建RuntimeOptions
        """
        if UtilClient.is_unset(runtime_options):
            return util_models.RuntimeOptions(
                read_timeout=10000,
                connect_timeout=5000,
                autoretry=True,
                max_attempts=2,
                ignore_ssl=False,
                max_idle_conns=50
            )
        # 默认开启SDK层面的重试，如果想要关闭重试，可以手动设置maxAttempts=0
        runtime_options.autoretry = True
        if UtilClient.is_unset(runtime_options.read_timeout):
            runtime_options.read_timeout = 10000
        if UtilClient.is_unset(runtime_options.connect_timeout):
            runtime_options.connect_timeout = 5000
        if UtilClient.is_unset(runtime_options.max_idle_conns):
            runtime_options.max_idle_conns = 50
        if UtilClient.is_unset(runtime_options.max_attempts):
            runtime_options.max_attempts = 2
        if UtilClient.is_unset(runtime_options.backoff_policy):
            runtime_options.backoff_policy = 'no'
        if UtilClient.is_unset(runtime_options.backoff_period):
            runtime_options.backoff_period = 1
        return runtime_options

    def get_headers_from_run_time_option(self) -> Dict[str, str]:
        """
        从runtimeoptions中获取headers
        """
        options = self._runtime_options
        headers = {}
        if not UtilClient.is_unset(options.extends_parameters) and not UtilClient.is_unset(options.extends_parameters.headers) and not UtilClient.empty(options.extends_parameters.headers.get('Content-Encoding')):
            content_encoding = options.extends_parameters.headers.get('Content-Encoding')
            if StringClient.equals('deflate', content_encoding):
                headers['Content-Encoding'] = 'deflate'
        return headers

    def list_tables(self) -> ha_3engine_vector_models.ListTablesResponse:
        """
        获取表列表
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.ListTablesResponse(),
            self._open_api_request('GET', f'/openapi/ha3/instances/{self._instance_id}/tables', None, None, None, self._runtime_options)
        )

    async def list_tables_async(self) -> ha_3engine_vector_models.ListTablesResponse:
        """
        获取表列表
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.ListTablesResponse(),
            await self._open_api_request_async('GET', f'/openapi/ha3/instances/{self._instance_id}/tables', None, None, None, self._runtime_options)
        )

    def get_table(
        self,
        table_name: str,
    ) -> ha_3engine_vector_models.GetTableResponse:
        """
        获取表详情
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.GetTableResponse(),
            self._open_api_request('GET', f'/openapi/ha3/instances/{self._instance_id}/tables/{table_name}', None, None, None, self._runtime_options)
        )

    async def get_table_async(
        self,
        table_name: str,
    ) -> ha_3engine_vector_models.GetTableResponse:
        """
        获取表详情
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.GetTableResponse(),
            await self._open_api_request_async('GET', f'/openapi/ha3/instances/{self._instance_id}/tables/{table_name}', None, None, None, self._runtime_options)
        )

    def create_table(
        self,
        request: ha_3engine_vector_models.CreateTableRequest,
    ) -> ha_3engine_vector_models.CreateTableResponse:
        """
        创建表
        """
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        return TeaCore.from_map(
            ha_3engine_vector_models.CreateTableResponse(),
            self._open_api_request('POST', f'/openapi/ha3/instances/{self._instance_id}/tables', query, None, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    async def create_table_async(
        self,
        request: ha_3engine_vector_models.CreateTableRequest,
    ) -> ha_3engine_vector_models.CreateTableResponse:
        """
        创建表
        """
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        return TeaCore.from_map(
            ha_3engine_vector_models.CreateTableResponse(),
            await self._open_api_request_async('POST', f'/openapi/ha3/instances/{self._instance_id}/tables', query, None, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    def modify_table(
        self,
        table_name: str,
        request: ha_3engine_vector_models.ModifyTableRequest,
    ) -> ha_3engine_vector_models.ModifyTableResponse:
        """
        修改表
        """
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        return TeaCore.from_map(
            ha_3engine_vector_models.ModifyTableResponse(),
            self._open_api_request('PUT', f'/openapi/ha3/instances/{self._instance_id}/tables/{table_name}', query, None, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    async def modify_table_async(
        self,
        table_name: str,
        request: ha_3engine_vector_models.ModifyTableRequest,
    ) -> ha_3engine_vector_models.ModifyTableResponse:
        """
        修改表
        """
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        return TeaCore.from_map(
            ha_3engine_vector_models.ModifyTableResponse(),
            await self._open_api_request_async('PUT', f'/openapi/ha3/instances/{self._instance_id}/tables/{table_name}', query, None, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    def delete_table(
        self,
        table_name: str,
    ) -> ha_3engine_vector_models.DeleteTableResponse:
        """
        删除表
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.DeleteTableResponse(),
            self._open_api_request('DELETE', f'/openapi/ha3/instances/{self._instance_id}/tables/{table_name}', None, None, None, self._runtime_options)
        )

    async def delete_table_async(
        self,
        table_name: str,
    ) -> ha_3engine_vector_models.DeleteTableResponse:
        """
        删除表
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.DeleteTableResponse(),
            await self._open_api_request_async('DELETE', f'/openapi/ha3/instances/{self._instance_id}/tables/{table_name}', None, None, None, self._runtime_options)
        )

    def stop_table(
        self,
        table_name: str,
    ) -> ha_3engine_vector_models.StopTableResponse:
        """
        表停止使用
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.StopTableResponse(),
            self._open_api_request('POST', f'/openapi/ha3/instances/{self._instance_id}/indexes/{table_name}/stopIndex', None, None, None, self._runtime_options)
        )

    async def stop_table_async(
        self,
        table_name: str,
    ) -> ha_3engine_vector_models.StopTableResponse:
        """
        表停止使用
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.StopTableResponse(),
            await self._open_api_request_async('POST', f'/openapi/ha3/instances/{self._instance_id}/indexes/{table_name}/stopIndex', None, None, None, self._runtime_options)
        )

    def start_table(
        self,
        table_name: str,
    ) -> ha_3engine_vector_models.StartTableResponse:
        """
        表恢复使用
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.StartTableResponse(),
            self._open_api_request('POST', f'/openapi/ha3/instances/{self._instance_id}/indexes/{table_name}/startIndex', None, None, None, self._runtime_options)
        )

    async def start_table_async(
        self,
        table_name: str,
    ) -> ha_3engine_vector_models.StartTableResponse:
        """
        表恢复使用
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.StartTableResponse(),
            await self._open_api_request_async('POST', f'/openapi/ha3/instances/{self._instance_id}/indexes/{table_name}/startIndex', None, None, None, self._runtime_options)
        )

    def reindex(
        self,
        table_name: str,
        request: ha_3engine_vector_models.ReindexRequest,
    ) -> ha_3engine_vector_models.ReindexResponse:
        """
        索引重建
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.ReindexResponse(),
            self._open_api_request('POST', f'/openapi/ha3/instances/{self._instance_id}/tables/{table_name}/reindex', None, None, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    async def reindex_async(
        self,
        table_name: str,
        request: ha_3engine_vector_models.ReindexRequest,
    ) -> ha_3engine_vector_models.ReindexResponse:
        """
        索引重建
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.ReindexResponse(),
            await self._open_api_request_async('POST', f'/openapi/ha3/instances/{self._instance_id}/tables/{table_name}/reindex', None, None, UtilClient.to_jsonstring(request), self._runtime_options)
        )

    def list_table_generations(
        self,
        table_name: str,
    ) -> ha_3engine_vector_models.ListTableGenerationsResponse:
        """
        获取索引版本列表
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.ListTableGenerationsResponse(),
            self._open_api_request('GET', f'/openapi/ha3/instances/{self._instance_id}/tables/{table_name}/index_versions', None, None, None, self._runtime_options)
        )

    async def list_table_generations_async(
        self,
        table_name: str,
    ) -> ha_3engine_vector_models.ListTableGenerationsResponse:
        """
        获取索引版本列表
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.ListTableGenerationsResponse(),
            await self._open_api_request_async('GET', f'/openapi/ha3/instances/{self._instance_id}/tables/{table_name}/index_versions', None, None, None, self._runtime_options)
        )

    def get_table_generation(
        self,
        table_name: str,
        generation_id: str,
    ) -> ha_3engine_vector_models.GetTableGenerationResponse:
        """
        获取索引版本详情
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.GetTableGenerationResponse(),
            self._open_api_request('GET', f'/openapi/ha3/instances/{self._instance_id}/tables/{table_name}/index_versions/{generation_id}', None, None, None, self._runtime_options)
        )

    async def get_table_generation_async(
        self,
        table_name: str,
        generation_id: str,
    ) -> ha_3engine_vector_models.GetTableGenerationResponse:
        """
        获取索引版本详情
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.GetTableGenerationResponse(),
            await self._open_api_request_async('GET', f'/openapi/ha3/instances/{self._instance_id}/tables/{table_name}/index_versions/{generation_id}', None, None, None, self._runtime_options)
        )

    def list_tasks(
        self,
        request: ha_3engine_vector_models.ListTasksRequest,
    ) -> ha_3engine_vector_models.ListTasksResponse:
        """
        获取任务列表
        """
        query = {}
        one = NumberClient.parse_long('1000')
        if not UtilClient.is_unset(request.end):
            query['end'] = NumberClient.mul(request.end, one)
        if not UtilClient.is_unset(request.start):
            query['start'] = NumberClient.mul(request.start, one)
        else:
            now = NumberClient.parse_long(TimeClient.unix())
            period = NumberClient.parse_long('86400')
            query['start'] = NumberClient.mul(NumberClient.sub(now, period), one)
        return TeaCore.from_map(
            ha_3engine_vector_models.ListTasksResponse(),
            self._open_api_request('GET', f'/openapi/ha3/instances/{self._instance_id}/tasks', query, None, None, self._runtime_options)
        )

    async def list_tasks_async(
        self,
        request: ha_3engine_vector_models.ListTasksRequest,
    ) -> ha_3engine_vector_models.ListTasksResponse:
        """
        获取任务列表
        """
        query = {}
        one = NumberClient.parse_long('1000')
        if not UtilClient.is_unset(request.end):
            query['end'] = NumberClient.mul(request.end, one)
        if not UtilClient.is_unset(request.start):
            query['start'] = NumberClient.mul(request.start, one)
        else:
            now = NumberClient.parse_long(TimeClient.unix())
            period = NumberClient.parse_long('86400')
            query['start'] = NumberClient.mul(NumberClient.sub(now, period), one)
        return TeaCore.from_map(
            ha_3engine_vector_models.ListTasksResponse(),
            await self._open_api_request_async('GET', f'/openapi/ha3/instances/{self._instance_id}/tasks', query, None, None, self._runtime_options)
        )
