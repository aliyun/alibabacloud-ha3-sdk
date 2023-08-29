# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import time

from Tea.exceptions import TeaException, UnretryableException
from Tea.request import TeaRequest
from Tea.core import TeaCore
from alibabacloud_darabonba_encode_util.encoder import Encoder
from typing import Dict, Any

from alibabacloud_ha3engine_vector import models as ha_3engine_vector_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_darabonba_string.client import Client as StringClient


class Client:
    _endpoint: str = None
    _instance_id: str = None
    _protocol: str = None
    _user_agent: str = None
    _credential: str = None
    _domainsuffix: str = None
    _http_proxy: str = None

    def __init__(
        self, 
        config: ha_3engine_vector_models.Config,
    ):
        if UtilClient.is_unset(config):
            raise TeaException({
                'name': 'ParameterMissing',
                'message': "'config' can not be unset"
            })
        if not UtilClient.empty(config.access_user_name) and not UtilClient.empty(config.access_pass_word):
            self._credential = self.get_realm_sign_str(config.access_user_name, config.access_pass_word)
        self._endpoint = config.endpoint
        self._instance_id = config.instance_id
        self._protocol = config.protocol
        self._user_agent = config.user_agent
        self._domainsuffix = 'ha.aliyuncs.com'
        self._http_proxy = config.http_proxy

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
                    raw_msg = None
                    try:
                        raw_msg = UtilClient.parse_json(obj_str)
                    except Exception as err:
                        raw_msg = obj_str
                    raw_map = {
                        'errors': raw_msg
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
                    raw_msg = None
                    try:
                        raw_msg = UtilClient.parse_json(obj_str)
                    except Exception as err:
                        raw_msg = obj_str
                    raw_map = {
                        'errors': raw_msg
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

    def query(
        self,
        request: ha_3engine_vector_models.QueryRequestModel,
    ) -> ha_3engine_vector_models.SearchResponseModel:
        """
        向量查询
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponseModel(),
            self._request('POST', f'/vector-service/query', None, None, UtilClient.to_jsonstring(TeaCore.to_map(request)), self.build_runtime_options())
        )

    async def query_async(
        self,
        request: ha_3engine_vector_models.QueryRequestModel,
    ) -> ha_3engine_vector_models.SearchResponseModel:
        """
        向量查询
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponseModel(),
            await self._request_async('POST', f'/vector-service/query', None, None, UtilClient.to_jsonstring(TeaCore.to_map(request)), await self.build_runtime_options_async())
        )

    def multi_query(
        self,
        request: ha_3engine_vector_models.MultiQueryRequestModel,
    ) -> ha_3engine_vector_models.SearchResponseModel:
        """
        多namespace查询
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponseModel(),
            self._request('POST', f'/vector-service/multi-query', None, None, UtilClient.to_jsonstring(TeaCore.to_map(request)), self.build_runtime_options())
        )

    async def multi_query_async(
        self,
        request: ha_3engine_vector_models.MultiQueryRequestModel,
    ) -> ha_3engine_vector_models.SearchResponseModel:
        """
        多namespace查询
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponseModel(),
            await self._request_async('POST', f'/vector-service/multi-query', None, None, UtilClient.to_jsonstring(TeaCore.to_map(request)), await self.build_runtime_options_async())
        )

    def fetch(
        self,
        request: ha_3engine_vector_models.FetchRequestModel,
    ) -> ha_3engine_vector_models.SearchResponseModel:
        """
        查询数据
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponseModel(),
            self._request('POST', f'/vector-service/fetch', None, None, UtilClient.to_jsonstring(TeaCore.to_map(request)), self.build_runtime_options())
        )

    async def fetch_async(
        self,
        request: ha_3engine_vector_models.FetchRequestModel,
    ) -> ha_3engine_vector_models.SearchResponseModel:
        """
        查询数据
        """
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponseModel(),
            await self._request_async('POST', f'/vector-service/fetch', None, None, UtilClient.to_jsonstring(TeaCore.to_map(request)), await self.build_runtime_options_async())
        )

    def stats(
        self,
        table_name: str,
    ) -> ha_3engine_vector_models.SearchResponseModel:
        """
        文档统计
        """
        body = {
            'tableName': table_name
        }
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponseModel(),
            self._request('POST', f'/vector-service/stats', None, None, UtilClient.to_jsonstring(body), self.build_runtime_options())
        )

    async def stats_async(
        self,
        table_name: str,
    ) -> ha_3engine_vector_models.SearchResponseModel:
        """
        文档统计
        """
        body = {
            'tableName': table_name
        }
        return TeaCore.from_map(
            ha_3engine_vector_models.SearchResponseModel(),
            await self._request_async('POST', f'/vector-service/stats', None, None, UtilClient.to_jsonstring(body), await self.build_runtime_options_async())
        )

    def push_documents(
        self,
        data_source_name: str,
        key_field: str,
        request: ha_3engine_vector_models.PushDocumentsRequestModel,
    ) -> ha_3engine_vector_models.PushDocumentsResponseModel:
        """
        支持新增、更新、删除 等操作，以及对应批量操作
        """
        request.headers = {
            'X-Opensearch-Swift-PK-Field': key_field
        }
        return TeaCore.from_map(
            ha_3engine_vector_models.PushDocumentsResponseModel(),
            self._request('POST', f'/update/{data_source_name}/actions/bulk', None, request.headers, request.body, self.build_runtime_options())
        )

    async def push_documents_async(
        self,
        data_source_name: str,
        key_field: str,
        request: ha_3engine_vector_models.PushDocumentsRequestModel,
    ) -> ha_3engine_vector_models.PushDocumentsResponseModel:
        """
        支持新增、更新、删除 等操作，以及对应批量操作
        """
        request.headers = {
            'X-Opensearch-Swift-PK-Field': key_field
        }
        return TeaCore.from_map(
            ha_3engine_vector_models.PushDocumentsResponseModel(),
            await self._request_async('POST', f'/update/{data_source_name}/actions/bulk', None, request.headers, request.body, await self.build_runtime_options_async())
        )

    def push_documents_with_swift(
        self,
        data_source_name: str,
        key_field: str,
        topic: str,
        swift: str,
        request: ha_3engine_vector_models.PushDocumentsRequestModel,
    ) -> ha_3engine_vector_models.PushDocumentsResponseModel:
        """
        用于内网环境的新增、更新、删除 等操作，以及对应批量操作
        """
        request.headers = {
            'X-Opensearch-Swift-PK-Field': key_field,
            'X-Opensearch-Swift-Topic': topic,
            'X-Opensearch-Swift-Swift': swift
        }
        return TeaCore.from_map(
            ha_3engine_vector_models.PushDocumentsResponseModel(),
            self._request('POST', f'/update/{data_source_name}/actions/bulk', None, request.headers, request.body, self.build_runtime_options())
        )

    async def push_documents_with_swift_async(
        self,
        data_source_name: str,
        key_field: str,
        topic: str,
        swift: str,
        request: ha_3engine_vector_models.PushDocumentsRequestModel,
    ) -> ha_3engine_vector_models.PushDocumentsResponseModel:
        """
        用于内网环境的新增、更新、删除 等操作，以及对应批量操作
        """
        request.headers = {
            'X-Opensearch-Swift-PK-Field': key_field,
            'X-Opensearch-Swift-Topic': topic,
            'X-Opensearch-Swift-Swift': swift
        }
        return TeaCore.from_map(
            ha_3engine_vector_models.PushDocumentsResponseModel(),
            await self._request_async('POST', f'/update/{data_source_name}/actions/bulk', None, request.headers, request.body, await self.build_runtime_options_async())
        )

    def build_runtime_options(self) -> util_models.RuntimeOptions:
        """
        构建RuntimeOptions
        """
        return util_models.RuntimeOptions(
            connect_timeout=5000,
            read_timeout=10000,
            autoretry=False,
            ignore_ssl=False,
            max_idle_conns=50,
            http_proxy=self._http_proxy
        )

    async def build_runtime_options_async(self) -> util_models.RuntimeOptions:
        """
        构建RuntimeOptions
        """
        return util_models.RuntimeOptions(
            connect_timeout=5000,
            read_timeout=10000,
            autoretry=False,
            ignore_ssl=False,
            max_idle_conns=50,
            http_proxy=self._http_proxy
        )
