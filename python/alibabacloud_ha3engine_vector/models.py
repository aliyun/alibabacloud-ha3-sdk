# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any

from alibabacloud_tea_util import models as util_models


class Config(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        instance_id: str = None,
        protocol: str = None,
        access_user_name: str = None,
        access_pass_word: str = None,
        user_agent: str = None,
        runtime_options: util_models.RuntimeOptions = None,
    ):
        self.endpoint = endpoint
        self.instance_id = instance_id
        self.protocol = protocol
        self.access_user_name = access_user_name
        self.access_pass_word = access_pass_word
        self.user_agent = user_agent
        self.runtime_options = runtime_options

    def validate(self):
        if self.runtime_options:
            self.runtime_options.validate()

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
        if self.runtime_options is not None:
            result['runtimeOptions'] = self.runtime_options.to_map()
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
        if m.get('runtimeOptions') is not None:
            temp_model = util_models.RuntimeOptions()
            self.runtime_options = temp_model.from_map(m['runtimeOptions'])
        return self


class SearchResponse(TeaModel):
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


class SparseData(TeaModel):
    def __init__(
        self,
        count: List[int] = None,
        indices: List[int] = None,
        values: List[float] = None,
    ):
        # 每个稀疏向量中包含的元素个数
        self.count = count
        # 元素下标（需要从小到大排序）
        self.indices = indices
        # 元素值（与下标一一对应）
        self.values = values

    def validate(self):
        self.validate_required(self.indices, 'indices')
        self.validate_required(self.values, 'values')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.indices is not None:
            result['indices'] = self.indices
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('indices') is not None:
            self.indices = m.get('indices')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class QueryRequest(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        vector: List[float] = None,
        namespace: str = None,
        top_k: int = None,
        index_name: str = None,
        sparse_data: SparseData = None,
        weight: float = None,
        content: str = None,
        modal: str = None,
        include_vector: bool = None,
        output_fields: List[str] = None,
        order: str = None,
        search_params: str = None,
        filter: str = None,
        score_threshold: float = None,
        vector_count: int = None,
        sort: str = None,
    ):
        # 数据源名
        self.table_name = table_name
        # 向量数据
        self.vector = vector
        # 查询向量的空间
        self.namespace = namespace
        # 返回个数
        self.top_k = top_k
        # 查询的索引名
        self.index_name = index_name
        # 查询的稀疏向量
        self.sparse_data = sparse_data
        # Query的权重
        self.weight = weight
        # 需要向量化的内容
        self.content = content
        # 使用的模型
        self.modal = modal
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
        # 排序表达式
        self.sort = sort

    def validate(self):
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.vector, 'vector')
        if self.sparse_data:
            self.sparse_data.validate()

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
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.sparse_data is not None:
            result['sparseData'] = self.sparse_data.to_map()
        if self.weight is not None:
            result['weight'] = self.weight
        if self.content is not None:
            result['content'] = self.content
        if self.modal is not None:
            result['modal'] = self.modal
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
        if self.sort is not None:
            result['sort'] = self.sort
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
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('sparseData') is not None:
            temp_model = SparseData()
            self.sparse_data = temp_model.from_map(m['sparseData'])
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('modal') is not None:
            self.modal = m.get('modal')
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
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        return self


class MultiQueryRequest(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        queries: List[QueryRequest] = None,
        top_k: int = None,
        include_vector: bool = None,
        output_fields: List[str] = None,
        order: str = None,
        filter: str = None,
        sort: str = None,
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
        # 排序表达式
        self.sort = sort

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
        if self.sort is not None:
            result['sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        self.queries = []
        if m.get('queries') is not None:
            for k in m.get('queries'):
                temp_model = QueryRequest()
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
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        return self


class FetchRequest(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        ids: List[str] = None,
        filter: str = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
        include_vector: bool = None,
        output_fields: List[str] = None,
    ):
        # 数据源名
        self.table_name = table_name
        # 主键列表，如果传了主键列表，下面的条件参数不生效
        self.ids = ids
        # 过滤表达式
        self.filter = filter
        # 排序表达式
        self.sort = sort
        # 返回的数据个数
        self.limit = limit
        # 返回的数据开始下标，用于翻页
        self.offset = offset
        # 是否返回向量数据
        self.include_vector = include_vector
        # 需要返回的字段，不指定默认返回所有的字段
        self.output_fields = output_fields

    def validate(self):
        self.validate_required(self.table_name, 'table_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.ids is not None:
            result['ids'] = self.ids
        if self.filter is not None:
            result['filter'] = self.filter
        if self.sort is not None:
            result['sort'] = self.sort
        if self.limit is not None:
            result['limit'] = self.limit
        if self.offset is not None:
            result['offset'] = self.offset
        if self.include_vector is not None:
            result['includeVector'] = self.include_vector
        if self.output_fields is not None:
            result['outputFields'] = self.output_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('includeVector') is not None:
            self.include_vector = m.get('includeVector')
        if m.get('outputFields') is not None:
            self.output_fields = m.get('outputFields')
        return self


class PushDocumentsRequest(TeaModel):
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


class PushDocumentsResponse(TeaModel):
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


