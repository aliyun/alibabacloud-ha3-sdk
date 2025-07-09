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


class Sort(TeaModel):
    def __init__(
        self,
        order: str = None,
        expression: str = None,
    ):
        # 排序顺序, ASC：升序  DESC: 降序
        self.order = order
        # 表达式
        self.expression = expression

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['order'] = self.order
        if self.expression is not None:
            result['expression'] = self.expression
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('expression') is not None:
            self.expression = m.get('expression')
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
        kvpairs: Dict[str, str] = None,
        content_type: str = None,
        video_frame_top_k: int = None,
        sorts: List[Sort] = None,
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
        # kvpairs
        self.kvpairs = kvpairs
        # 视频预测数据类型：text、image、video_uri、video_base64
        self.content_type = content_type
        # 召回帧的数量，默认值为100
        self.video_frame_top_k = video_frame_top_k
        # 多维排序，配置sorts后，结果中的score字段会变成多值字段，对应每一维排序的分数
        self.sorts = sorts

    def validate(self):
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.vector, 'vector')
        if self.sparse_data:
            self.sparse_data.validate()
        if self.sorts:
            for k in self.sorts:
                if k:
                    k.validate()

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
        if self.kvpairs is not None:
            result['kvpairs'] = self.kvpairs
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.video_frame_top_k is not None:
            result['videoFrameTopK'] = self.video_frame_top_k
        result['sorts'] = []
        if self.sorts is not None:
            for k in self.sorts:
                result['sorts'].append(k.to_map() if k else None)
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
        if m.get('kvpairs') is not None:
            self.kvpairs = m.get('kvpairs')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('videoFrameTopK') is not None:
            self.video_frame_top_k = m.get('videoFrameTopK')
        self.sorts = []
        if m.get('sorts') is not None:
            for k in m.get('sorts'):
                temp_model = Sort()
                self.sorts.append(temp_model.from_map(k))
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
        mode: str = None,
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
        # 用于配置多路结果中相同pk doc如何计算分数。mode可以配置：sum, max, min。默认为sum
        self.mode = mode

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
        if self.mode is not None:
            result['mode'] = self.mode
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
        if m.get('mode') is not None:
            self.mode = m.get('mode')
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
        kvpairs: Dict[str, str] = None,
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
        # kvpairs
        self.kvpairs = kvpairs

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
        if self.kvpairs is not None:
            result['kvpairs'] = self.kvpairs
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
        if m.get('kvpairs') is not None:
            self.kvpairs = m.get('kvpairs')
        return self


class RankQuery(TeaModel):
    def __init__(
        self,
        rrf: Dict[str, str] = None,
    ):
        # 查询表达式
        self.rrf = rrf

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rrf is not None:
            result['rrf'] = self.rrf
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rrf') is not None:
            self.rrf = m.get('rrf')
        return self


class TextQuery(TeaModel):
    def __init__(
        self,
        query_string: str = None,
        query_params: Dict[str, str] = None,
        filter: str = None,
        weight: float = None,
        terminate_after: int = None,
    ):
        # ha3 query语法，支持多个文本索引的AND、OR嵌套
        self.query_string = query_string
        # query查询参数：
        #       default_op: 指定在该次查询中使用的默认query 分词后的连接操作符，AND or OR。默认为AND。
        #       global_analyzer: 查询中指定全局的分词器，该分词器会覆盖schema的分词器，指定的值必须在analyzer.json里有配置。
        #       specific_index_analyzer: 查询中指定index使用另外的分词器，该分词器会覆盖global_analyzer和schema的分词器。
        #       no_token_indexes: 支持查询中指定的index不分词（除分词以外的其他流程如归一化、去停用词会正常执行），多个index之间用;分割。
        #       remove_stopwords: true or false 表示是否需要删除stop words，stop words在分词器中配置。默认true
        self.query_params = query_params
        # 过滤条件表达式
        self.filter = filter
        # text查询结果的权重，以score * weight的结果作为该路的排序分
        self.weight = weight
        # 每个分片查找满足条件的文档的最大数量。到达这个数量后，查询将提前结束，不再继续查询索引。默认为0，不设置限制。
        self.terminate_after = terminate_after

    def validate(self):
        self.validate_required(self.query_string, 'query_string')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_string is not None:
            result['queryString'] = self.query_string
        if self.query_params is not None:
            result['queryParams'] = self.query_params
        if self.filter is not None:
            result['filter'] = self.filter
        if self.weight is not None:
            result['weight'] = self.weight
        if self.terminate_after is not None:
            result['terminateAfter'] = self.terminate_after
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queryString') is not None:
            self.query_string = m.get('queryString')
        if m.get('queryParams') is not None:
            self.query_params = m.get('queryParams')
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('terminateAfter') is not None:
            self.terminate_after = m.get('terminateAfter')
        return self


class SearchRequest(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        size: int = None,
        from_: int = None,
        order: str = None,
        output_fields: List[str] = None,
        knn: QueryRequest = None,
        text: TextQuery = None,
        rank: RankQuery = None,
    ):
        # 数据源名
        self.table_name = table_name
        # 返回结果的个数
        self.size = size
        # 从结果集的第from返回doc
        self.from_ = from_
        # 结果排序方向:DESC: 降序排序;ASC: 升序排序
        self.order = order
        # 指定需要在结果中返回的字段，默认为空
        self.output_fields = output_fields
        # KNN查询参数
        self.knn = knn
        # text查询参数
        self.text = text
        # 指定两路结果融合的方式，目前支持两种策略：默认策略：两路结果中相同pk的doc的分数按权重相加。按加权后的分数排序。rrf: 使用rrf融合两路结果
        self.rank = rank

    def validate(self):
        self.validate_required(self.table_name, 'table_name')
        if self.knn:
            self.knn.validate()
        if self.text:
            self.text.validate()
        if self.rank:
            self.rank.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.size is not None:
            result['size'] = self.size
        if self.from_ is not None:
            result['from'] = self.from_
        if self.order is not None:
            result['order'] = self.order
        if self.output_fields is not None:
            result['outputFields'] = self.output_fields
        if self.knn is not None:
            result['knn'] = self.knn.to_map()
        if self.text is not None:
            result['text'] = self.text.to_map()
        if self.rank is not None:
            result['rank'] = self.rank.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('outputFields') is not None:
            self.output_fields = m.get('outputFields')
        if m.get('knn') is not None:
            temp_model = QueryRequest()
            self.knn = temp_model.from_map(m['knn'])
        if m.get('text') is not None:
            temp_model = TextQuery()
            self.text = temp_model.from_map(m['text'])
        if m.get('rank') is not None:
            temp_model = RankQuery()
            self.rank = temp_model.from_map(m['rank'])
        return self


class AggFuncDesc(TeaModel):
    def __init__(
        self,
        name: str = None,
        func: str = None,
        args: List[str] = None,
    ):
        # 可以指定统计值在结果集中字段的名称。默认结果字段为: FUNC_NAME(args)
        self.name = name
        # 统计函数名：max, min, avg, sum, count
        self.func = func
        # 统计函数的参数
        self.args = args

    def validate(self):
        self.validate_required(self.func, 'func')
        self.validate_required(self.args, 'args')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.func is not None:
            result['func'] = self.func
        if self.args is not None:
            result['args'] = self.args
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('func') is not None:
            self.func = m.get('func')
        if m.get('args') is not None:
            self.args = m.get('args')
        return self


class OrderByDesc(TeaModel):
    def __init__(
        self,
        field: str = None,
        direction: str = None,
    ):
        # 排序字段名称，必须指定结果集中的字段
        self.field = field
        # 排序方向，DESC: 降序排列；ASC: 升序排列
        self.direction = direction

    def validate(self):
        self.validate_required(self.field, 'field')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['field'] = self.field
        if self.direction is not None:
            result['direction'] = self.direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            self.field = m.get('field')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        return self


class AggregateRequest(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        filter: str = None,
        group_keys: List[str] = None,
        agg_funcs: List[AggFuncDesc] = None,
        order_by: List[OrderByDesc] = None,
        timeout: int = None,
    ):
        # 需要统计的表名
        self.table_name = table_name
        # 过滤条件
        self.filter = filter
        # 分组统计的字段列表
        self.group_keys = group_keys
        # 统计函数列表
        self.agg_funcs = agg_funcs
        # 统计结果排序方式，支持多维排序
        self.order_by = order_by
        # 超时时间，单位毫秒
        self.timeout = timeout

    def validate(self):
        self.validate_required(self.table_name, 'table_name')
        self.validate_required(self.agg_funcs, 'agg_funcs')
        if self.agg_funcs:
            for k in self.agg_funcs:
                if k:
                    k.validate()
        if self.order_by:
            for k in self.order_by:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.filter is not None:
            result['filter'] = self.filter
        if self.group_keys is not None:
            result['groupKeys'] = self.group_keys
        result['aggFuncs'] = []
        if self.agg_funcs is not None:
            for k in self.agg_funcs:
                result['aggFuncs'].append(k.to_map() if k else None)
        result['orderBy'] = []
        if self.order_by is not None:
            for k in self.order_by:
                result['orderBy'].append(k.to_map() if k else None)
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('groupKeys') is not None:
            self.group_keys = m.get('groupKeys')
        self.agg_funcs = []
        if m.get('aggFuncs') is not None:
            for k in m.get('aggFuncs'):
                temp_model = AggFuncDesc()
                self.agg_funcs.append(temp_model.from_map(k))
        self.order_by = []
        if m.get('orderBy') is not None:
            for k in m.get('orderBy'):
                temp_model = OrderByDesc()
                self.order_by.append(temp_model.from_map(k))
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class BatchRequest(TeaModel):
    def __init__(
        self,
        queries: List[QueryRequest] = None,
        timeout: int = None,
    ):
        # 批量查询列表
        self.queries = queries
        # 超时时间，单位毫秒
        self.timeout = timeout

    def validate(self):
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
        result['queries'] = []
        if self.queries is not None:
            for k in self.queries:
                result['queries'].append(k.to_map() if k else None)
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.queries = []
        if m.get('queries') is not None:
            for k in m.get('queries'):
                temp_model = QueryRequest()
                self.queries.append(temp_model.from_map(k))
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
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


class ListTablesResponseBodyResult(TeaModel):
    def __init__(
        self,
        index_status: str = None,
        name: str = None,
        status: str = None,
    ):
        # The state of the index table. Valid values: NEW, PUBLISH, IN_USE, NOT_USE, STOP_USE, RESTORE_USE, and FAIL. After an index is created in an OpenSearch Retrieval Engine Edition instance, the index enters the IN_USE state. If the first full index fails to be created in an OpenSearch Vector Search Edition instance of the new version, the index is in the FAIL state.
        self.index_status = index_status
        # The index name.
        self.name = name
        # The state of the index table. Valid values: NEW, PUBLISH, IN_USE, NOT_USE, STOP_USE, RESTORE_USE, and FAIL. After an index is created in an OpenSearch Retrieval Engine Edition instance, the index enters the IN_USE state. If the first full index fails to be created in an OpenSearch Vector Search Edition instance of the new version, the index is in the FAIL state.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_status is not None:
            result['indexStatus'] = self.index_status
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('indexStatus') is not None:
            self.index_status = m.get('indexStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListTablesResponseBody(TeaModel):
    """
    获取所有表信息
    """
    def __init__(
        self,
        request_id: str = None,
        result: List[ListTablesResponseBodyResult] = None,
    ):
        # requestId
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListTablesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTablesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableResponseBodyResultVectorIndexAdvanceParams(TeaModel):
    def __init__(
        self,
        build_index_params: str = None,
        linear_build_threshold: str = None,
        min_scan_doc_cnt: str = None,
        search_index_params: str = None,
    ):
        # The index building parameters.
        self.build_index_params = build_index_params
        # The threshold for linear building.
        self.linear_build_threshold = linear_build_threshold
        # The minimum number of retrieved candidate sets.
        self.min_scan_doc_cnt = min_scan_doc_cnt
        # The index retrieval parameters.
        self.search_index_params = search_index_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_index_params is not None:
            result['buildIndexParams'] = self.build_index_params
        if self.linear_build_threshold is not None:
            result['linearBuildThreshold'] = self.linear_build_threshold
        if self.min_scan_doc_cnt is not None:
            result['minScanDocCnt'] = self.min_scan_doc_cnt
        if self.search_index_params is not None:
            result['searchIndexParams'] = self.search_index_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildIndexParams') is not None:
            self.build_index_params = m.get('buildIndexParams')
        if m.get('linearBuildThreshold') is not None:
            self.linear_build_threshold = m.get('linearBuildThreshold')
        if m.get('minScanDocCnt') is not None:
            self.min_scan_doc_cnt = m.get('minScanDocCnt')
        if m.get('searchIndexParams') is not None:
            self.search_index_params = m.get('searchIndexParams')
        return self


class GetTableResponseBodyResultVectorIndex(TeaModel):
    def __init__(
        self,
        advance_params: GetTableResponseBodyResultVectorIndexAdvanceParams = None,
        dimension: str = None,
        distance_type: str = None,
        index_name: str = None,
        namespace: str = None,
        sparse_index_field: str = None,
        sparse_value_field: str = None,
        vector_field: str = None,
        vector_index_type: str = None,
    ):
        # The configurations of the index schema.
        self.advance_params = advance_params
        # The dimension of the vector.
        self.dimension = dimension
        # The distance type.
        self.distance_type = distance_type
        # The name of the index schema.
        self.index_name = index_name
        # The namespace field.
        self.namespace = namespace
        # The field that stores the indexes of the elements in sparse vectors.
        self.sparse_index_field = sparse_index_field
        # The field that stores the elements in sparse vectors.
        self.sparse_value_field = sparse_value_field
        # The vector field.
        self.vector_field = vector_field
        # The vector retrieval algorithm.
        self.vector_index_type = vector_index_type

    def validate(self):
        if self.advance_params:
            self.advance_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advance_params is not None:
            result['advanceParams'] = self.advance_params.to_map()
        if self.dimension is not None:
            result['dimension'] = self.dimension
        if self.distance_type is not None:
            result['distanceType'] = self.distance_type
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.sparse_index_field is not None:
            result['sparseIndexField'] = self.sparse_index_field
        if self.sparse_value_field is not None:
            result['sparseValueField'] = self.sparse_value_field
        if self.vector_field is not None:
            result['vectorField'] = self.vector_field
        if self.vector_index_type is not None:
            result['vectorIndexType'] = self.vector_index_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advanceParams') is not None:
            temp_model = GetTableResponseBodyResultVectorIndexAdvanceParams()
            self.advance_params = temp_model.from_map(m['advanceParams'])
        if m.get('dimension') is not None:
            self.dimension = m.get('dimension')
        if m.get('distanceType') is not None:
            self.distance_type = m.get('distanceType')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('sparseIndexField') is not None:
            self.sparse_index_field = m.get('sparseIndexField')
        if m.get('sparseValueField') is not None:
            self.sparse_value_field = m.get('sparseValueField')
        if m.get('vectorField') is not None:
            self.vector_field = m.get('vectorField')
        if m.get('vectorIndexType') is not None:
            self.vector_index_type = m.get('vectorIndexType')
        return self


class GetTableResponseBodyResultDataSourceConfig(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        bucket: str = None,
        endpoint: str = None,
        namespace: str = None,
        oss_path: str = None,
        partition: str = None,
        path: str = None,
        project: str = None,
        table: str = None,
    ):
        # AK
        self.access_key = access_key
        # AS
        self.access_secret = access_secret
        self.bucket = bucket
        self.endpoint = endpoint
        self.namespace = namespace
        self.oss_path = oss_path
        self.partition = partition
        self.path = path
        self.project = project
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class GetTableResponseBodyResultDataSource(TeaModel):
    def __init__(
        self,
        auto_build_index: bool = None,
        config: GetTableResponseBodyResultDataSourceConfig = None,
        data_time_sec: int = None,
        type: str = None,
    ):
        self.auto_build_index = auto_build_index
        self.config = config
        self.data_time_sec = data_time_sec
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.data_time_sec is not None:
            result['dataTimeSec'] = self.data_time_sec
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('config') is not None:
            temp_model = GetTableResponseBodyResultDataSourceConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('dataTimeSec') is not None:
            self.data_time_sec = m.get('dataTimeSec')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig(TeaModel):
    def __init__(
        self,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        uid: str = None,
    ):
        # OSS Bucket
        self.oss_bucket = oss_bucket
        # The Object Storage Service (OSS) endpoint.
        self.oss_endpoint = oss_endpoint
        # The ID of the Alibaba Cloud account.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_bucket is not None:
            result['ossBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['ossEndpoint'] = self.oss_endpoint
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ossBucket') is not None:
            self.oss_bucket = m.get('ossBucket')
        if m.get('ossEndpoint') is not None:
            self.oss_endpoint = m.get('ossEndpoint')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetTableResponseBodyResultDataProcessConfigParams(TeaModel):
    def __init__(
        self,
        src_field_config: GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig = None,
        vector_modal: str = None,
        vector_model: str = None,
    ):
        # The source of the data to be vectorized.
        self.src_field_config = src_field_config
        # The data type.
        self.vector_modal = vector_modal
        # The vectorization model.
        self.vector_model = vector_model

    def validate(self):
        if self.src_field_config:
            self.src_field_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src_field_config is not None:
            result['srcFieldConfig'] = self.src_field_config.to_map()
        if self.vector_modal is not None:
            result['vectorModal'] = self.vector_modal
        if self.vector_model is not None:
            result['vectorModel'] = self.vector_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('srcFieldConfig') is not None:
            temp_model = GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig()
            self.src_field_config = temp_model.from_map(m['srcFieldConfig'])
        if m.get('vectorModal') is not None:
            self.vector_modal = m.get('vectorModal')
        if m.get('vectorModel') is not None:
            self.vector_model = m.get('vectorModel')
        return self


class GetTableResponseBodyResultDataProcessConfig(TeaModel):
    def __init__(
        self,
        dst_field: str = None,
        operator: str = None,
        params: GetTableResponseBodyResultDataProcessConfigParams = None,
        src_field: str = None,
    ):
        # The destination field.
        self.dst_field = dst_field
        # The method used to process the field. Valid values: copy and vectorize. A value of copy indicates that the value of the source field is copied to the destination field. A value of vectorize indicates that the value of the source field is vectorized by a vectorization model and the output vector is stored in the destination field.
        self.operator = operator
        # The information about the model.
        self.params = params
        # The source field.
        self.src_field = src_field

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_field is not None:
            result['dstField'] = self.dst_field
        if self.operator is not None:
            result['operator'] = self.operator
        if self.params is not None:
            result['params'] = self.params.to_map()
        if self.src_field is not None:
            result['srcField'] = self.src_field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dstField') is not None:
            self.dst_field = m.get('dstField')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('params') is not None:
            temp_model = GetTableResponseBodyResultDataProcessConfigParams()
            self.params = temp_model.from_map(m['params'])
        if m.get('srcField') is not None:
            self.src_field = m.get('srcField')
        return self


class GetTableResponseBodyResult(TeaModel):
    def __init__(
        self,
        name: str = None,
        partition_count: int = None,
        primary_key: str = None,
        raw_schema: str = None,
        data_processor_count: int = None,
        field_schema: Dict[str, str] = None,
        status: str = None,
        vector_index: List[GetTableResponseBodyResultVectorIndex] = None,
        data_source: GetTableResponseBodyResultDataSource = None,
        data_process_config: List[GetTableResponseBodyResultDataProcessConfig] = None,
    ):
        self.name = name
        self.partition_count = partition_count
        self.primary_key = primary_key
        self.raw_schema = raw_schema
        self.data_processor_count = data_processor_count
        # The field. The value is a key-value pair in which the key indicates the field name and value indicates the field type.
        self.field_schema = field_schema
        # The state of the index table. Valid values: NEW, PUBLISH, IN_USE, NOT_USE, STOP_USE, RESTORE_USE, and FAIL. After an index is created in an OpenSearch Retrieval Engine Edition instance, the index enters the IN_USE state. If the first full index fails to be created in an OpenSearch Vector Search Edition instance of the new version, the index is in the FAIL state.
        self.status = status
        # The index schema.
        self.vector_index = vector_index
        self.data_source = data_source
        # The configurations about field processing.
        self.data_process_config = data_process_config

    def validate(self):
        if self.vector_index:
            for k in self.vector_index:
                if k:
                    k.validate()
        if self.data_source:
            self.data_source.validate()
        if self.data_process_config:
            for k in self.data_process_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.partition_count is not None:
            result['partitionCount'] = self.partition_count
        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key
        if self.raw_schema is not None:
            result['rawSchema'] = self.raw_schema
        if self.data_processor_count is not None:
            result['dataProcessorCount'] = self.data_processor_count
        if self.field_schema is not None:
            result['fieldSchema'] = self.field_schema
        if self.status is not None:
            result['status'] = self.status
        result['vectorIndex'] = []
        if self.vector_index is not None:
            for k in self.vector_index:
                result['vectorIndex'].append(k.to_map() if k else None)
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        result['dataProcessConfig'] = []
        if self.data_process_config is not None:
            for k in self.data_process_config:
                result['dataProcessConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('partitionCount') is not None:
            self.partition_count = m.get('partitionCount')
        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')
        if m.get('rawSchema') is not None:
            self.raw_schema = m.get('rawSchema')
        if m.get('dataProcessorCount') is not None:
            self.data_processor_count = m.get('dataProcessorCount')
        if m.get('fieldSchema') is not None:
            self.field_schema = m.get('fieldSchema')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.vector_index = []
        if m.get('vectorIndex') is not None:
            for k in m.get('vectorIndex'):
                temp_model = GetTableResponseBodyResultVectorIndex()
                self.vector_index.append(temp_model.from_map(k))
        if m.get('dataSource') is not None:
            temp_model = GetTableResponseBodyResultDataSource()
            self.data_source = temp_model.from_map(m['dataSource'])
        self.data_process_config = []
        if m.get('dataProcessConfig') is not None:
            for k in m.get('dataProcessConfig'):
                temp_model = GetTableResponseBodyResultDataProcessConfig()
                self.data_process_config.append(temp_model.from_map(k))
        return self


class GetTableResponseBody(TeaModel):
    """
    获取单表详情
    """
    def __init__(
        self,
        request_id: str = None,
        result: GetTableResponseBodyResult = None,
    ):
        # requestId
        self.request_id = request_id
        # The results returned.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetTableResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTableRequestVectorIndexAdvanceParams(TeaModel):
    def __init__(
        self,
        build_index_params: str = None,
        linear_build_threshold: str = None,
        min_scan_doc_cnt: str = None,
        search_index_params: str = None,
    ):
        # The index building parameters.
        self.build_index_params = build_index_params
        # The threshold for linear building.
        self.linear_build_threshold = linear_build_threshold
        # The minimum number of retrieved candidate sets.
        self.min_scan_doc_cnt = min_scan_doc_cnt
        # The index retrieval parameters.
        self.search_index_params = search_index_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_index_params is not None:
            result['buildIndexParams'] = self.build_index_params
        if self.linear_build_threshold is not None:
            result['linearBuildThreshold'] = self.linear_build_threshold
        if self.min_scan_doc_cnt is not None:
            result['minScanDocCnt'] = self.min_scan_doc_cnt
        if self.search_index_params is not None:
            result['searchIndexParams'] = self.search_index_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildIndexParams') is not None:
            self.build_index_params = m.get('buildIndexParams')
        if m.get('linearBuildThreshold') is not None:
            self.linear_build_threshold = m.get('linearBuildThreshold')
        if m.get('minScanDocCnt') is not None:
            self.min_scan_doc_cnt = m.get('minScanDocCnt')
        if m.get('searchIndexParams') is not None:
            self.search_index_params = m.get('searchIndexParams')
        return self


class CreateTableRequestVectorIndex(TeaModel):
    def __init__(
        self,
        advance_params: CreateTableRequestVectorIndexAdvanceParams = None,
        dimension: str = None,
        distance_type: str = None,
        index_name: str = None,
        namespace: str = None,
        sparse_index_field: str = None,
        sparse_value_field: str = None,
        vector_field: str = None,
        vector_index_type: str = None,
    ):
        # The configurations of the index schema.
        self.advance_params = advance_params
        # The dimension of the vector.
        self.dimension = dimension
        # The distance type.
        self.distance_type = distance_type
        # The name of the index schema.
        self.index_name = index_name
        # The namespace field.
        self.namespace = namespace
        # The field that stores the indexes of the elements in sparse vectors.
        self.sparse_index_field = sparse_index_field
        # The field that stores the elements in sparse vectors.
        self.sparse_value_field = sparse_value_field
        # The vector field.
        self.vector_field = vector_field
        # The vector retrieval algorithm.
        self.vector_index_type = vector_index_type

    def validate(self):
        if self.advance_params:
            self.advance_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advance_params is not None:
            result['advanceParams'] = self.advance_params.to_map()
        if self.dimension is not None:
            result['dimension'] = self.dimension
        if self.distance_type is not None:
            result['distanceType'] = self.distance_type
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.sparse_index_field is not None:
            result['sparseIndexField'] = self.sparse_index_field
        if self.sparse_value_field is not None:
            result['sparseValueField'] = self.sparse_value_field
        if self.vector_field is not None:
            result['vectorField'] = self.vector_field
        if self.vector_index_type is not None:
            result['vectorIndexType'] = self.vector_index_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advanceParams') is not None:
            temp_model = CreateTableRequestVectorIndexAdvanceParams()
            self.advance_params = temp_model.from_map(m['advanceParams'])
        if m.get('dimension') is not None:
            self.dimension = m.get('dimension')
        if m.get('distanceType') is not None:
            self.distance_type = m.get('distanceType')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('sparseIndexField') is not None:
            self.sparse_index_field = m.get('sparseIndexField')
        if m.get('sparseValueField') is not None:
            self.sparse_value_field = m.get('sparseValueField')
        if m.get('vectorField') is not None:
            self.vector_field = m.get('vectorField')
        if m.get('vectorIndexType') is not None:
            self.vector_index_type = m.get('vectorIndexType')
        return self


class CreateTableRequestDataProcessConfigParamsSrcFieldConfig(TeaModel):
    def __init__(
        self,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        uid: str = None,
    ):
        # The OSS bucket.
        self.oss_bucket = oss_bucket
        # The OSS endpoint.
        self.oss_endpoint = oss_endpoint
        # The ID of the Alibaba Cloud account.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_bucket is not None:
            result['ossBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['ossEndpoint'] = self.oss_endpoint
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ossBucket') is not None:
            self.oss_bucket = m.get('ossBucket')
        if m.get('ossEndpoint') is not None:
            self.oss_endpoint = m.get('ossEndpoint')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateTableRequestDataProcessConfigParams(TeaModel):
    def __init__(
        self,
        src_field_config: CreateTableRequestDataProcessConfigParamsSrcFieldConfig = None,
        vector_modal: str = None,
        vector_model: str = None,
    ):
        # The source of the data to be vectorized.
        self.src_field_config = src_field_config
        # The data type.
        self.vector_modal = vector_modal
        # The vectorization model.
        self.vector_model = vector_model

    def validate(self):
        if self.src_field_config:
            self.src_field_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src_field_config is not None:
            result['srcFieldConfig'] = self.src_field_config.to_map()
        if self.vector_modal is not None:
            result['vectorModal'] = self.vector_modal
        if self.vector_model is not None:
            result['vectorModel'] = self.vector_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('srcFieldConfig') is not None:
            temp_model = CreateTableRequestDataProcessConfigParamsSrcFieldConfig()
            self.src_field_config = temp_model.from_map(m['srcFieldConfig'])
        if m.get('vectorModal') is not None:
            self.vector_modal = m.get('vectorModal')
        if m.get('vectorModel') is not None:
            self.vector_model = m.get('vectorModel')
        return self


class CreateTableRequestDataProcessConfig(TeaModel):
    def __init__(
        self,
        dst_field: str = None,
        operator: str = None,
        params: CreateTableRequestDataProcessConfigParams = None,
        src_field: str = None,
    ):
        # The destination field.
        self.dst_field = dst_field
        # The method used to process the field. Valid values: copy and vectorize. A value of copy specifies that the value of the source field is copied to the destination field. A value of vectorize specifies that the value of the source field is vectorized by a vectorization model and the output vector is stored in the destination field.
        self.operator = operator
        # The information about the model.
        self.params = params
        # The source field.
        self.src_field = src_field

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_field is not None:
            result['dstField'] = self.dst_field
        if self.operator is not None:
            result['operator'] = self.operator
        if self.params is not None:
            result['params'] = self.params.to_map()
        if self.src_field is not None:
            result['srcField'] = self.src_field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dstField') is not None:
            self.dst_field = m.get('dstField')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('params') is not None:
            temp_model = CreateTableRequestDataProcessConfigParams()
            self.params = temp_model.from_map(m['params'])
        if m.get('srcField') is not None:
            self.src_field = m.get('srcField')
        return self


class CreateTableRequestDataSourceConfig(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        bucket: str = None,
        catalog: str = None,
        database: str = None,
        endpoint: str = None,
        oss_path: str = None,
        partition: str = None,
        project: str = None,
        table: str = None,
        tag: str = None,
    ):
        # The AccessKey ID of the MaxCompute data source.
        self.access_key = access_key
        # The AccessKey secret of the MaxCompute data source.
        self.access_secret = access_secret
        # The OSS bucket.
        self.bucket = bucket
        self.catalog = catalog
        self.database = database
        # The endpoint of the MaxCompute data source.
        self.endpoint = endpoint
        # The Object Storage Service (OSS) path.
        self.oss_path = oss_path
        # The partition in the MaxCompute table. This parameter is required if type is set to odps.
        self.partition = partition
        # The name of the MaxCompute project that is used as the data source.
        self.project = project
        # The name of the MaxCompute table that is used as the data source.
        self.table = table
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.catalog is not None:
            result['catalog'] = self.catalog
        if self.database is not None:
            result['database'] = self.database
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        if self.tag is not None:
            result['tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('catalog') is not None:
            self.catalog = m.get('catalog')
        if m.get('database') is not None:
            self.database = m.get('database')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        return self


class CreateTableRequestDataSource(TeaModel):
    def __init__(
        self,
        auto_build_index: bool = None,
        config: CreateTableRequestDataSourceConfig = None,
        data_time_sec: int = None,
        type: str = None,
    ):
        # Specifies whether to automatically rebuild the index.
        self.auto_build_index = auto_build_index
        # The configurations of the data source.
        self.config = config
        # The start timestamp from which incremental data is retrieved.
        self.data_time_sec = data_time_sec
        # The data source type. Valid values: odps, swift, and oss.
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.data_time_sec is not None:
            result['dataTimeSec'] = self.data_time_sec
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('config') is not None:
            temp_model = CreateTableRequestDataSourceConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('dataTimeSec') is not None:
            self.data_time_sec = m.get('dataTimeSec')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateTableRequest(TeaModel):
    """
    创建表
    """
    def __init__(
        self,
        name: str = None,
        partition_count: int = None,
        primary_key: str = None,
        field_schema: Dict[str, str] = None,
        vector_index: List[CreateTableRequestVectorIndex] = None,
        data_processor_count: int = None,
        data_process_config: List[CreateTableRequestDataProcessConfig] = None,
        data_source: CreateTableRequestDataSource = None,
        dry_run: bool = None,
    ):
        # The index name.
        self.name = name
        # The number of data shards.
        self.partition_count = partition_count
        # The primary key field.
        self.primary_key = primary_key
        # The fields.
        self.field_schema = field_schema
        # The index schema.
        self.vector_index = vector_index
        # The number of resources used for data update.
        self.data_processor_count = data_processor_count
        # The configurations about field processing.
        self.data_process_config = data_process_config
        # The configurations of the data source.
        self.data_source = data_source
        # Specifies whether to perform only a dry run, without performing the actual request. The system only checks the validity of the data source. Valid values:true,false
        self.dry_run = dry_run

    def validate(self):
        if self.vector_index:
            for k in self.vector_index:
                if k:
                    k.validate()
        if self.data_process_config:
            for k in self.data_process_config:
                if k:
                    k.validate()
        if self.data_source:
            self.data_source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.partition_count is not None:
            result['partitionCount'] = self.partition_count
        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key
        if self.field_schema is not None:
            result['fieldSchema'] = self.field_schema
        result['vectorIndex'] = []
        if self.vector_index is not None:
            for k in self.vector_index:
                result['vectorIndex'].append(k.to_map() if k else None)
        if self.data_processor_count is not None:
            result['dataProcessorCount'] = self.data_processor_count
        result['dataProcessConfig'] = []
        if self.data_process_config is not None:
            for k in self.data_process_config:
                result['dataProcessConfig'].append(k.to_map() if k else None)
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('partitionCount') is not None:
            self.partition_count = m.get('partitionCount')
        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')
        if m.get('fieldSchema') is not None:
            self.field_schema = m.get('fieldSchema')
        self.vector_index = []
        if m.get('vectorIndex') is not None:
            for k in m.get('vectorIndex'):
                temp_model = CreateTableRequestVectorIndex()
                self.vector_index.append(temp_model.from_map(k))
        if m.get('dataProcessorCount') is not None:
            self.data_processor_count = m.get('dataProcessorCount')
        self.data_process_config = []
        if m.get('dataProcessConfig') is not None:
            for k in m.get('dataProcessConfig'):
                temp_model = CreateTableRequestDataProcessConfig()
                self.data_process_config.append(temp_model.from_map(k))
        if m.get('dataSource') is not None:
            temp_model = CreateTableRequestDataSource()
            self.data_source = temp_model.from_map(m['dataSource'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # Map
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTableRequestDataProcessConfigParamsSrcFieldConfig(TeaModel):
    def __init__(
        self,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        uid: str = None,
    ):
        # The name of the OSS bucket.
        self.oss_bucket = oss_bucket
        # The OSS endpoint.
        self.oss_endpoint = oss_endpoint
        # The ID of the Alibaba Cloud account.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_bucket is not None:
            result['ossBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['ossEndpoint'] = self.oss_endpoint
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ossBucket') is not None:
            self.oss_bucket = m.get('ossBucket')
        if m.get('ossEndpoint') is not None:
            self.oss_endpoint = m.get('ossEndpoint')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ModifyTableRequestDataProcessConfigParams(TeaModel):
    def __init__(
        self,
        src_field_config: ModifyTableRequestDataProcessConfigParamsSrcFieldConfig = None,
        vector_modal: str = None,
        vector_model: str = None,
    ):
        # The source of the data to be vectorized.
        self.src_field_config = src_field_config
        # The data type.
        self.vector_modal = vector_modal
        # The vectorization model.
        self.vector_model = vector_model

    def validate(self):
        if self.src_field_config:
            self.src_field_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src_field_config is not None:
            result['srcFieldConfig'] = self.src_field_config.to_map()
        if self.vector_modal is not None:
            result['vectorModal'] = self.vector_modal
        if self.vector_model is not None:
            result['vectorModel'] = self.vector_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('srcFieldConfig') is not None:
            temp_model = ModifyTableRequestDataProcessConfigParamsSrcFieldConfig()
            self.src_field_config = temp_model.from_map(m['srcFieldConfig'])
        if m.get('vectorModal') is not None:
            self.vector_modal = m.get('vectorModal')
        if m.get('vectorModel') is not None:
            self.vector_model = m.get('vectorModel')
        return self


class ModifyTableRequestDataProcessConfig(TeaModel):
    def __init__(
        self,
        dst_field: str = None,
        operator: str = None,
        params: ModifyTableRequestDataProcessConfigParams = None,
        src_field: str = None,
    ):
        # The destination field.
        self.dst_field = dst_field
        # The method used to process the field. Valid values: copy and vectorize. A value of copy specifies that the value of the source field is copied to the destination field. A value of vectorize specifies that the value of the source field is vectorized by a vectorization model and the output vector is stored in the destination field.
        self.operator = operator
        # The information about the model.
        self.params = params
        # The source field.
        self.src_field = src_field

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_field is not None:
            result['dstField'] = self.dst_field
        if self.operator is not None:
            result['operator'] = self.operator
        if self.params is not None:
            result['params'] = self.params.to_map()
        if self.src_field is not None:
            result['srcField'] = self.src_field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dstField') is not None:
            self.dst_field = m.get('dstField')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('params') is not None:
            temp_model = ModifyTableRequestDataProcessConfigParams()
            self.params = temp_model.from_map(m['params'])
        if m.get('srcField') is not None:
            self.src_field = m.get('srcField')
        return self


class ModifyTableRequestDataSourceConfig(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        bucket: str = None,
        catalog: str = None,
        database: str = None,
        endpoint: str = None,
        oss_path: str = None,
        partition: str = None,
        project: str = None,
        table: str = None,
        tag: str = None,
    ):
        # The AccessKey ID of the MaxCompute data source.
        self.access_key = access_key
        # The AccessKey secret of the MaxCompute data source.
        self.access_secret = access_secret
        # The name of the OSS bucket.
        self.bucket = bucket
        self.catalog = catalog
        self.database = database
        # The endpoint of the MaxCompute data source.
        self.endpoint = endpoint
        # The path of the Object Storage Service (OSS) object.
        self.oss_path = oss_path
        # The partition in the MaxCompute table.
        self.partition = partition
        # The name of the MaxCompute project that is used as the data source.
        self.project = project
        # The name of the MaxCompute table that is used as the data source.
        self.table = table
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.catalog is not None:
            result['catalog'] = self.catalog
        if self.database is not None:
            result['database'] = self.database
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        if self.tag is not None:
            result['tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('catalog') is not None:
            self.catalog = m.get('catalog')
        if m.get('database') is not None:
            self.database = m.get('database')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        return self


class ModifyTableRequestDataSource(TeaModel):
    def __init__(
        self,
        auto_build_index: bool = None,
        config: ModifyTableRequestDataSourceConfig = None,
        data_time_sec: int = None,
    ):
        # Specifies whether to automatically rebuild the index.
        self.auto_build_index = auto_build_index
        # The configurations of the data source.
        self.config = config
        # The start timestamp from which incremental data is retrieved.
        self.data_time_sec = data_time_sec

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.data_time_sec is not None:
            result['dataTimeSec'] = self.data_time_sec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('config') is not None:
            temp_model = ModifyTableRequestDataSourceConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('dataTimeSec') is not None:
            self.data_time_sec = m.get('dataTimeSec')
        return self


class ModifyTableRequestVectorIndexAdvanceParams(TeaModel):
    def __init__(
        self,
        build_index_params: str = None,
        linear_build_threshold: str = None,
        min_scan_doc_cnt: str = None,
        search_index_params: str = None,
    ):
        # The index building parameters.
        self.build_index_params = build_index_params
        # The threshold for linear building.
        self.linear_build_threshold = linear_build_threshold
        # The minimum number of retrieved candidate sets.
        self.min_scan_doc_cnt = min_scan_doc_cnt
        # The index retrieval parameters.
        self.search_index_params = search_index_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_index_params is not None:
            result['buildIndexParams'] = self.build_index_params
        if self.linear_build_threshold is not None:
            result['linearBuildThreshold'] = self.linear_build_threshold
        if self.min_scan_doc_cnt is not None:
            result['minScanDocCnt'] = self.min_scan_doc_cnt
        if self.search_index_params is not None:
            result['searchIndexParams'] = self.search_index_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildIndexParams') is not None:
            self.build_index_params = m.get('buildIndexParams')
        if m.get('linearBuildThreshold') is not None:
            self.linear_build_threshold = m.get('linearBuildThreshold')
        if m.get('minScanDocCnt') is not None:
            self.min_scan_doc_cnt = m.get('minScanDocCnt')
        if m.get('searchIndexParams') is not None:
            self.search_index_params = m.get('searchIndexParams')
        return self


class ModifyTableRequestVectorIndex(TeaModel):
    def __init__(
        self,
        advance_params: ModifyTableRequestVectorIndexAdvanceParams = None,
        dimension: str = None,
        distance_type: str = None,
        index_name: str = None,
        namespace: str = None,
        sparse_index_field: str = None,
        sparse_value_field: str = None,
        vector_field: str = None,
        vector_index_type: str = None,
    ):
        # The configurations of the index schema.
        self.advance_params = advance_params
        # The dimension of the vector.
        self.dimension = dimension
        # The distance type.
        self.distance_type = distance_type
        # The name of the index schema.
        self.index_name = index_name
        # The namespace field.
        self.namespace = namespace
        # The field that stores the indexes of the elements in sparse vectors.
        self.sparse_index_field = sparse_index_field
        # The field that stores the elements in sparse vectors.
        self.sparse_value_field = sparse_value_field
        # The vector field.
        self.vector_field = vector_field
        # The vector retrieval algorithm.
        self.vector_index_type = vector_index_type

    def validate(self):
        if self.advance_params:
            self.advance_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advance_params is not None:
            result['advanceParams'] = self.advance_params.to_map()
        if self.dimension is not None:
            result['dimension'] = self.dimension
        if self.distance_type is not None:
            result['distanceType'] = self.distance_type
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.sparse_index_field is not None:
            result['sparseIndexField'] = self.sparse_index_field
        if self.sparse_value_field is not None:
            result['sparseValueField'] = self.sparse_value_field
        if self.vector_field is not None:
            result['vectorField'] = self.vector_field
        if self.vector_index_type is not None:
            result['vectorIndexType'] = self.vector_index_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advanceParams') is not None:
            temp_model = ModifyTableRequestVectorIndexAdvanceParams()
            self.advance_params = temp_model.from_map(m['advanceParams'])
        if m.get('dimension') is not None:
            self.dimension = m.get('dimension')
        if m.get('distanceType') is not None:
            self.distance_type = m.get('distanceType')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('sparseIndexField') is not None:
            self.sparse_index_field = m.get('sparseIndexField')
        if m.get('sparseValueField') is not None:
            self.sparse_value_field = m.get('sparseValueField')
        if m.get('vectorField') is not None:
            self.vector_field = m.get('vectorField')
        if m.get('vectorIndexType') is not None:
            self.vector_index_type = m.get('vectorIndexType')
        return self


class ModifyTableRequest(TeaModel):
    """
    修改表.
    """
    def __init__(
        self,
        data_process_config: List[ModifyTableRequestDataProcessConfig] = None,
        data_source: ModifyTableRequestDataSource = None,
        field_schema: Dict[str, str] = None,
        partition_count: int = None,
        primary_key: str = None,
        raw_schema: str = None,
        vector_index: List[ModifyTableRequestVectorIndex] = None,
        dry_run: bool = None,
    ):
        # The configurations about field processing.
        self.data_process_config = data_process_config
        # The configurations of the data source.
        self.data_source = data_source
        # The fields.
        self.field_schema = field_schema
        # The number of data shards.
        self.partition_count = partition_count
        # The primary key field.
        self.primary_key = primary_key
        # The instance schema. If this parameter is specified, the parameters about the index are not required.
        self.raw_schema = raw_schema
        # The index schema.
        self.vector_index = vector_index
        # Specifies whether to perform only a dry run, without performing the actual request. The system only checks the validity of the data source. Valid values:true,false
        self.dry_run = dry_run

    def validate(self):
        if self.data_process_config:
            for k in self.data_process_config:
                if k:
                    k.validate()
        if self.data_source:
            self.data_source.validate()
        if self.vector_index:
            for k in self.vector_index:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dataProcessConfig'] = []
        if self.data_process_config is not None:
            for k in self.data_process_config:
                result['dataProcessConfig'].append(k.to_map() if k else None)
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        if self.field_schema is not None:
            result['fieldSchema'] = self.field_schema
        if self.partition_count is not None:
            result['partitionCount'] = self.partition_count
        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key
        if self.raw_schema is not None:
            result['rawSchema'] = self.raw_schema
        result['vectorIndex'] = []
        if self.vector_index is not None:
            for k in self.vector_index:
                result['vectorIndex'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_process_config = []
        if m.get('dataProcessConfig') is not None:
            for k in m.get('dataProcessConfig'):
                temp_model = ModifyTableRequestDataProcessConfig()
                self.data_process_config.append(temp_model.from_map(k))
        if m.get('dataSource') is not None:
            temp_model = ModifyTableRequestDataSource()
            self.data_source = temp_model.from_map(m['dataSource'])
        if m.get('fieldSchema') is not None:
            self.field_schema = m.get('fieldSchema')
        if m.get('partitionCount') is not None:
            self.partition_count = m.get('partitionCount')
        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')
        if m.get('rawSchema') is not None:
            self.raw_schema = m.get('rawSchema')
        self.vector_index = []
        if m.get('vectorIndex') is not None:
            for k in m.get('vectorIndex'):
                temp_model = ModifyTableRequestVectorIndex()
                self.vector_index.append(temp_model.from_map(k))
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # id of request
        self.request_id = request_id
        # Map
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTableResponseBody(TeaModel):
    """
    删除表
    """
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # requestId
        self.request_id = request_id
        # Map
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTableResponseBody(TeaModel):
    """
    表停止使用
    """
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The index map.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class StopTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTableResponseBody(TeaModel):
    """
    表恢复使用
    """
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The index map.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class StartTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReindexRequest(TeaModel):
    """
    *\
    索引重建
    """
    def __init__(
        self,
        data_time_sec: int = None,
        oss_data_path: str = None,
        partition: str = None,
    ):
        # The timestamp in seconds. The value must be of the INTEGER type. This parameter is required if you specify an API data source.
        self.data_time_sec = data_time_sec
        # oss data path
        self.oss_data_path = oss_data_path
        # The partition in the MaxCompute table. This parameter is required if type is set to odps.
        self.partition = partition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_time_sec is not None:
            result['dataTimeSec'] = self.data_time_sec
        if self.oss_data_path is not None:
            result['ossDataPath'] = self.oss_data_path
        if self.partition is not None:
            result['partition'] = self.partition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataTimeSec') is not None:
            self.data_time_sec = m.get('dataTimeSec')
        if m.get('ossDataPath') is not None:
            self.oss_data_path = m.get('ossDataPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        return self


class ReindexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # requestId
        self.request_id = request_id
        # Map
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ReindexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReindexResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReindexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTableGenerationsResponseBodyResult(TeaModel):
    def __init__(
        self,
        generation_id: int = None,
    ):
        # The ID of the full index version.
        self.generation_id = generation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generation_id is not None:
            result['generationId'] = self.generation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generationId') is not None:
            self.generation_id = m.get('generationId')
        return self


class ListTableGenerationsResponseBody(TeaModel):
    """
    获取索引版本列表
    """
    def __init__(
        self,
        request_id: str = None,
        result: List[ListTableGenerationsResponseBodyResult] = None,
    ):
        # requestId
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListTableGenerationsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListTableGenerationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTableGenerationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTableGenerationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableGenerationResponseBodyResult(TeaModel):
    def __init__(
        self,
        generation_id: int = None,
        status: str = None,
    ):
        # generationId
        self.generation_id = generation_id
        # starting, building, ready, stopped, failed
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generation_id is not None:
            result['generationId'] = self.generation_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generationId') is not None:
            self.generation_id = m.get('generationId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetTableGenerationResponseBody(TeaModel):
    """
    获取索引版本详情
    """
    def __init__(
        self,
        request_id: str = None,
        result: GetTableGenerationResponseBodyResult = None,
    ):
        # requestId
        self.request_id = request_id
        # The result returned.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetTableGenerationResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetTableGenerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTableGenerationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTableGenerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    """
    获取任务列表
    """
    def __init__(
        self,
        end: int = None,
        start: int = None,
    ):
        # The timestamp that indicates the end of the time range to query.
        self.end = end
        # The timestamp that indicates the beginning of the time range to query.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Any = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


