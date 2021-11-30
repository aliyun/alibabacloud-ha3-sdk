# -*- coding: utf-8 -*-


from Tea.model import TeaModel
from typing import Dict, List, Any


class Config(TeaModel):
    def __init__(
            self,
            endpoint: str = None,
            protocol: str = None,
            access_user: str = None,
            access_secret: str = None,
            user_agent: str = None,
    ):
        self.endpoint = endpoint
        self.protocol = protocol
        self.access_user = access_user
        self.access_secret = access_secret
        self.user_agent = user_agent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.access_user is not None:
            result['accessKey'] = self.access_user
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('accessKey') is not None:
            self.access_user = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        return self


class SearchQuery(TeaModel):
    def __init__(
            self,
            query: str = None
    ):
        # 搜索主体，不能为空。主要支持子句有 config子句、query子句、sort子句、filter子句、aggregate子句、distinct子句 、kvpairs子句。
        self.query = query

    def validate(self):
        self.validate_required(self.query, 'query')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class SearchRequestModel(TeaModel):
    def __init__(
            self,
            headers: Dict[str, str] = None,
            query: SearchQuery = None,
    ):
        # headers
        self.headers = headers
        # query
        self.query = query

    def validate(self):
        self.validate_required(self.query, 'query')
        if self.query:
            self.query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.query is not None:
            result['query'] = self.query.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('query') is not None:
            temp_model = SearchQuery()
            self.query = temp_model.from_map(m['query'])
        return self


class SearchResultFacetItems(TeaModel):
    def __init__(
            self,
            value: str = None,
            count: int = None,
    ):
        self.value = value
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['value'] = self.value
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class SearchResultFacet(TeaModel):
    """
    *\
    """

    def __init__(
            self,
            key: str = None,
            items: List[SearchResultFacetItems] = None,
    ):
        self.key = key
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = SearchResultFacetItems()
                self.items.append(temp_model.from_map(k))
        return self


class SearchResult(TeaModel):
    """
    实际返回结果，包括查询耗时searchtime、引擎总结果数total、本次请求返回结果数num、本次查询最大返回结果数viewtotal、查询结果items、统计结果facet等信息
    """

    def __init__(
            self,
            searchtime: float = None,
            total: int = None,
            viewtotal: int = None,
            num: int = None,
            items: List[dict] = None,
            facet: List[SearchResultFacet] = None,
    ):
        # 指引擎耗时，单位为秒。
        self.searchtime = searchtime
        # total为一次查询（不考虑config子句）引擎中符合条件的结果数（在结果数较多情况下，该值会做优化），一般用来做展示。
        self.total = total
        # 考虑到性能及相关性，引擎最多会返回viewtotal个结果。如果需要翻页的话，要求start+hit必需要小于viewtotal
        self.viewtotal = viewtotal
        # num为本次查询请求（受限于config子句的start及hit）实际返回的条目，不会超过hit值。
        self.num = num
        # 包含查询召回数据信息，其中fields为搜索召回内容。
        self.items = items
        # 用于存放Aggregate子句返回的信息。
        self.facet = facet

    def validate(self):
        if self.facet:
            for k in self.facet:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.searchtime is not None:
            result['searchtime'] = self.searchtime
        if self.total is not None:
            result['total'] = self.total
        if self.viewtotal is not None:
            result['viewtotal'] = self.viewtotal
        if self.num is not None:
            result['num'] = self.num
        if self.items is not None:
            result['items'] = self.items
        result['facet'] = []
        if self.facet is not None:
            for k in self.facet:
                result['facet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('searchtime') is not None:
            self.searchtime = m.get('searchtime')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('viewtotal') is not None:
            self.viewtotal = m.get('viewtotal')
        if m.get('num') is not None:
            self.num = m.get('num')
        if m.get('items') is not None:
            self.items = m.get('items')
        self.facet = []
        if m.get('facet') is not None:
            for k in m.get('facet'):
                temp_model = SearchResultFacet()
                self.facet.append(temp_model.from_map(k))
        return self


class Error(TeaModel):
    """
    *\
    """

    def __init__(
            self,
            code: int = None,
            message: str = None,
    ):
        # 错误代码
        self.code = code
        # 错误描述
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class SearchResponse(TeaModel):
    """
    *\
    """

    def __init__(
            self,
            status: str = None,
            request_id: str = None,
            result: SearchResult = None,
            errors: List[Error] = None,
    ):
        self.status = status
        self.request_id = request_id
        self.result = result
        self.errors = errors

    def validate(self):
        if self.result:
            self.result.validate()
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        result['errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['errors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('result') is not None:
            temp_model = SearchResult()
            self.result = temp_model.from_map(m['result'])
        self.errors = []
        if m.get('errors') is not None:
            for k in m.get('errors'):
                temp_model = Error()
                self.errors.append(temp_model.from_map(k))
        return self


class SearchResponseModel(TeaModel):
    def __init__(
            self,
            headers: Dict[str, str] = None,
            body: SearchResponse = None,
    ):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class Document(TeaModel):
    """
    *\
    """

    def __init__(
            self,
            cmd: str = None,
            timestamp: int = None,
            fields: Dict[str, Any] = None,
    ):
        # 必选字段。定义该文档的操作行为，可以为“add”、“update”、“delete”，标准版不支持“update”。建议一个请求中进行批量更新操作，提高网络交互及处理效率。“add”表示新增文档，如果该主键对应文档已经存在，则执行先“delete”再“add”的操作；“update”表示更新文档，对该主键对应文档进行部分字段更新；“delete”表示删除文档，如果该主键对应文档已经不存在，则认为删除成功。
        self.cmd = cmd
        # 可选字段。用来记录文档实际发生时间，单位为毫秒。系统会用该时间戳来作为同一主键文档更新顺序的判断标准，该选项仅支持高级版，标准版应用，没有该timestamp选项，若指定该选项，推送会报4007错误码。在没有该timestamp项时，默认以文档发送到Ha3的时间作为文档更新时间进行操作。
        self.timestamp = timestamp
        # 必选字段。要操作的文档内容，主键字段必选，系统所有操作都是通过主键来进行的。对于“delete”只需要提供文档主键即可。
        self.fields = fields

    def validate(self):
        self.validate_required(self.cmd, 'cmd')
        self.validate_required(self.fields, 'fields')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cmd is not None:
            result['cmd'] = self.cmd
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.fields is not None:
            result['fields'] = self.fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cmd') is not None:
            self.cmd = m.get('cmd')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        return self


class PushDocumentRequestModel(TeaModel):
    def __init__(
            self,
            headers: Dict[str, str] = None,
            body: List[Document] = None,
    ):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Document()
                self.body.append(temp_model.from_map(k))
        return self


class Response(TeaModel):
    """
    *\
    """

    def __init__(
            self,
            status: str = None,
            request_id: str = None,
            errors: List[Error] = None,
    ):
        self.status = status
        self.request_id = request_id
        self.errors = errors

    def validate(self):
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.request_id is not None:
            result['request_id'] = self.request_id
        result['errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['errors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        self.errors = []
        if m.get('errors') is not None:
            for k in m.get('errors'):
                temp_model = Error()
                self.errors.append(temp_model.from_map(k))
        return self


class PushDocumentResponseModel(TeaModel):
    def __init__(
            self,
            headers: Dict[str, str] = None,
            body: Response = None,
    ):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = Response()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchResultItemFullJson(TeaModel):
    """
    *\
    """

    def __init__(
            self,
            fields: Dict[str, Any] = None,
            variable_value: Dict[str, Any] = None,
            sort_expr_values: List[int] = None,
    ):
        # 搜索召回内容
        self.fields = fields
        # 表示自定义参数返回结果，如获取distance距离值，variableValue 节点只有在config子句的format为xml或者fulljson时才能展现出来，json格式默认不展示。
        self.variable_value = variable_value
        # 表示对应文档排序分。
        self.sort_expr_values = sort_expr_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['fields'] = self.fields
        if self.variable_value is not None:
            result['variableValue'] = self.variable_value
        if self.sort_expr_values is not None:
            result['sortExprValues'] = self.sort_expr_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('variableValue') is not None:
            self.variable_value = m.get('variableValue')
        if m.get('sortExprValues') is not None:
            self.sort_expr_values = m.get('sortExprValues')
        return self
