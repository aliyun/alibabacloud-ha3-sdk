# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class Config(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        instance_id: str = None,
        protocol: str = None,
        access_user_name: str = None,
        access_pass_word: str = None,
        user_agent: str = None,
        http_proxy: str = None,
    ):
        self.endpoint = endpoint
        self.instance_id = instance_id
        self.protocol = protocol
        self.access_user_name = access_user_name
        self.access_pass_word = access_pass_word
        self.user_agent = user_agent
        self.http_proxy = http_proxy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.access_user_name is not None:
            result['accessUserName'] = self.access_user_name
        if self.access_pass_word is not None:
            result['accessPassWord'] = self.access_pass_word
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        if self.http_proxy is not None:
            result['httpProxy'] = self.http_proxy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('accessUserName') is not None:
            self.access_user_name = m.get('accessUserName')
        if m.get('accessPassWord') is not None:
            self.access_pass_word = m.get('accessPassWord')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        if m.get('httpProxy') is not None:
            self.http_proxy = m.get('httpProxy')
        return self


class SearchResponseModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: str = None,
    ):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class QueryRequestModel(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        vector: List[float] = None,
        namespace: str = None,
        top_k: int = None,
        include_vector: bool = None,
        output_fields: List[str] = None,
        order: str = None,
        search_params: str = None,
        filter: str = None,
        score_threshold: float = None,
        vector_count: int = None,
    ):
        # 数据源名
        self.table_name = table_name
        # 向量数据
        self.vector = vector
        # 查询向量的空间
        self.namespace = namespace
        # 返回个数
        self.top_k = top_k
        # 是否返回文档中的向量信息
        self.include_vector = include_vector
        # 需要返回值的字段列表
        self.output_fields = output_fields
        # 排序顺序, ASC：升序  DESC: 降序
        self.order = order
        # 查询参数
        self.search_params = search_params
        # 过滤表达式
        self.filter = filter
        # 分数过滤， 使用欧式距离时，只返回小于scoreThreshold的结果。使用内积时，只返回大于scoreThreshold的结果
        self.score_threshold = score_threshold
        # vector字段中包含的向量个数
        self.vector_count = vector_count

    def validate(self):
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.vector, 'vector')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.vector is not None:
            result['vector'] = self.vector
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.top_k is not None:
            result['topK'] = self.top_k
        if self.include_vector is not None:
            result['includeVector'] = self.include_vector
        if self.output_fields is not None:
            result['outputFields'] = self.output_fields
        if self.order is not None:
            result['order'] = self.order
        if self.search_params is not None:
            result['searchParams'] = self.search_params
        if self.filter is not None:
            result['filter'] = self.filter
        if self.score_threshold is not None:
            result['scoreThreshold'] = self.score_threshold
        if self.vector_count is not None:
            result['vectorCount'] = self.vector_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('vector') is not None:
            self.vector = m.get('vector')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        if m.get('includeVector') is not None:
            self.include_vector = m.get('includeVector')
        if m.get('outputFields') is not None:
            self.output_fields = m.get('outputFields')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('searchParams') is not None:
            self.search_params = m.get('searchParams')
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('scoreThreshold') is not None:
            self.score_threshold = m.get('scoreThreshold')
        if m.get('vectorCount') is not None:
            self.vector_count = m.get('vectorCount')
        return self


class Query(TeaModel):
    def __init__(
        self,
        vector: List[float] = None,
        vector_count: int = None,
        top_k: int = None,
        namespace: str = None,
        search_params: str = None,
        score_threshold: float = None,
    ):
        # 查询的向量数据，多个向量可以平铺开
        self.vector = vector
        # vector字段中向量的个数
        self.vector_count = vector_count
        # 返回个数
        self.top_k = top_k
        # 查询向量的空间
        self.namespace = namespace
        # 向量查询参数
        self.search_params = search_params
        # 分数过滤， 使用欧式距离时，只返回小于scoreThreshold的结果。使用内积时，只返回大于scoreThreshold的结果
        self.score_threshold = score_threshold

    def validate(self):
        self.validate_required(self.vector, 'vector')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vector is not None:
            result['vector'] = self.vector
        if self.vector_count is not None:
            result['vectorCount'] = self.vector_count
        if self.top_k is not None:
            result['topK'] = self.top_k
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.search_params is not None:
            result['searchParams'] = self.search_params
        if self.score_threshold is not None:
            result['scoreThreshold'] = self.score_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vector') is not None:
            self.vector = m.get('vector')
        if m.get('vectorCount') is not None:
            self.vector_count = m.get('vectorCount')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('searchParams') is not None:
            self.search_params = m.get('searchParams')
        if m.get('scoreThreshold') is not None:
            self.score_threshold = m.get('scoreThreshold')
        return self


class MultiQueryRequestModel(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        queries: List[Query] = None,
        top_k: int = None,
        include_vector: bool = None,
        output_fields: List[str] = None,
        order: str = None,
        filter: str = None,
    ):
        # 数据源名
        self.table_name = table_name
        # 多向量列表
        self.queries = queries
        # 返回个数
        self.top_k = top_k
        # 是否返回文档中的向量信息
        self.include_vector = include_vector
        # 需要返回值的字段列表
        self.output_fields = output_fields
        # 排序顺序, ASC：升序  DESC: 降序
        self.order = order
        # 过滤表达式
        self.filter = filter

    def validate(self):
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.queries, 'queries')
        if self.queries:
            for k in self.queries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['tableName'] = self.table_name
        result['queries'] = []
        if self.queries is not None:
            for k in self.queries:
                result['queries'].append(k.to_map() if k else None)
        if self.top_k is not None:
            result['topK'] = self.top_k
        if self.include_vector is not None:
            result['includeVector'] = self.include_vector
        if self.output_fields is not None:
            result['outputFields'] = self.output_fields
        if self.order is not None:
            result['order'] = self.order
        if self.filter is not None:
            result['filter'] = self.filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        self.queries = []
        if m.get('queries') is not None:
            for k in m.get('queries'):
                temp_model = Query()
                self.queries.append(temp_model.from_map(k))
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        if m.get('includeVector') is not None:
            self.include_vector = m.get('includeVector')
        if m.get('outputFields') is not None:
            self.output_fields = m.get('outputFields')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        return self


class FetchRequestModel(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        ids: List[str] = None,
    ):
        # 数据源名
        self.table_name = table_name
        # 主键列表
        self.ids = ids

    def validate(self):
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.ids, 'ids')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.ids is not None:
            result['ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        return self


class PushDocumentsRequestModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: List[Dict[str, Any]] = None,
    ):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class PushDocumentsResponseModel(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: str = None,
    ):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


