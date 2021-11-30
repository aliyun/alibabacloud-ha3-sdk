# -*- coding: utf-8 -*-


import hashlib
import time
import uuid
from base64 import b64encode

from Tea.exceptions import TeaException, UnretryableException
from Tea.request import TeaRequest
from Tea.core import TeaCore
from typing import Dict, Any

from alibabacloud_ha3engine import models as ha3_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class Client(object):
    """
    *\
    """
    _endpoint: str = None
    _protocol: str = None
    _user_agent: str = None
    _credential: str = None

    def __init__(
            self,
            config: ha3_models.Config,
    ):
        if UtilClient.is_unset(config):
            raise TeaException({
                'name': 'ParameterMissing',
                'message': "'config' can not be unset"
            })
        self._credential = self._basic_auth_str(config.access_user, config.access_secret)
        self._endpoint = config.endpoint
        self._protocol = config.protocol
        self._user_agent = config.user_agent

    def _basic_auth_str(self, username: str, password: str) -> str:

        if isinstance(username, str):
            username = username.encode('latin1')

        if isinstance(password, str):
            password = password.encode('latin1')

        authstr = 'Basic ' + b64encode(b':'.join((username, password))).strip().decode("ascii")
        return authstr

    def _gen_x_request_id(self):
        return uuid.uuid4().__str__()

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
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
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
                    'host': self._endpoint,
                    'x-request-id': self._gen_x_request_id()
                }, headers)
                if not UtilClient.is_unset(query):
                    _request.query = UtilClient.stringify_map_value(query)
                if not UtilClient.is_unset(body):
                    req_body = UtilClient.to_jsonstring(body)
                    _request.headers['Content-Type'] = 'application/json'
                    _request.body = req_body
                _request.headers['Authorization'] = self._credential
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                obj_str = UtilClient.read_as_string(_response.body)
                if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
                    raise TeaException({
                        'message': _response.status_message,
                        'data': obj_str,
                        'code': _response.status_code
                    })
                obj = UtilClient.parse_json(obj_str)
                res = UtilClient.assert_as_map(obj)
                return {
                    'body': res,
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
                'maxAttempts': UtilClient.default_number(runtime.max_attempts, 3)
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
                    'host': self._endpoint,
                    'x-request-id': self._gen_x_request_id()
                }, headers)
                if not UtilClient.is_unset(query):
                    _request.query = UtilClient.stringify_map_value(query)
                if not UtilClient.is_unset(body):
                    req_body = UtilClient.to_jsonstring(body)
                    _request.headers['Content-Type'] = 'application/json'
                    _request.body = req_body
                _request.headers['Authorization'] = self._credential
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                obj_str = await UtilClient.read_as_string_async(_response.body)
                if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
                    raise TeaException({
                        'message': _response.status_message,
                        'data': obj_str,
                        'code': _response.status_code
                    })
                obj = UtilClient.parse_json(obj_str)
                res = UtilClient.assert_as_map(obj)
                return {
                    'body': res,
                    'headers': _response.headers
                }
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def search_ex(
            self,
            request: ha3_models.SearchRequestModel,
            runtime: util_models.RuntimeOptions,
    ) -> ha3_models.SearchResponseModel:
        """
        系统提供了丰富的搜索语法以满足用户各种场景下的搜索需求。
        """
        return TeaCore.from_map(
            ha3_models.SearchResponseModel(),
            self._request('GET', '/search', TeaCore.to_map(request.query), request.headers, None, runtime)
        )

    async def search_ex_async(
            self,
            request: ha3_models.SearchRequestModel,
            runtime: util_models.RuntimeOptions,
    ) -> ha3_models.SearchResponseModel:
        """
        系统提供了丰富的搜索语法以满足用户各种场景下的搜索需求。
        """
        return TeaCore.from_map(
            ha3_models.SearchResponseModel(),
            await self._request_async('GET', '/search', TeaCore.to_map(request.query), request.headers, None, runtime)
        )

    def search(
            self,
            request: ha3_models.SearchRequestModel,
    ) -> ha3_models.SearchResponseModel:
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

    def push_document_ex(
            self,
            table_name: str,
            request: ha3_models.PushDocumentRequestModel,
            runtime: util_models.RuntimeOptions,
    ) -> ha3_models.PushDocumentResponseModel:
        """
        支持新增、更新、删除 等操作，以及对应批量操作
        """
        return TeaCore.from_map(
            ha3_models.PushDocumentResponseModel(),
            self._request('POST', f'/update/{table_name}/actions/bulk', None, request.headers, request.body, runtime)
        )

    async def search_async(
            self,
            request: ha3_models.SearchRequestModel,
    ) -> ha3_models.SearchResponseModel:
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

    async def push_document_ex_async(
            self,
            table_name: str,
            request: ha3_models.PushDocumentRequestModel,
            runtime: util_models.RuntimeOptions,
    ) -> ha3_models.PushDocumentResponseModel:
        """
        支持新增、更新、删除 等操作，以及对应批量操作
        """
        return TeaCore.from_map(
            ha3_models.PushDocumentResponseModel(),
            await self._request_async('POST', f'/update/{table_name}/actions/bulk', None, request.headers, request.body,
                                      runtime)
        )

    def push_document(
            self,
            table_name: str,
            request: ha3_models.PushDocumentRequestModel,
    ) -> ha3_models.PushDocumentResponseModel:
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
        return self.push_document_ex(table_name, request, runtime)

    async def push_document_async(
            self,
            table_name: str,
            request: ha3_models.PushDocumentRequestModel,
    ) -> ha3_models.PushDocumentResponseModel:
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
        return await self.push_document_ex_async(table_name, request, runtime)

    def set_user_agent(
            self,
            user_agent: str,
    ) -> None:
        self._user_agent = user_agent

    def append_user_agent(
            self,
            user_agent: str,
    ) -> None:
        self._user_agent = f'{self._user_agent} {user_agent}'

    def get_user_agent(self) -> str:
        user_agent = UtilClient.get_user_agent(self._user_agent)
        return user_agent
