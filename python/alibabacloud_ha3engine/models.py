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
    ):
        self.endpoint = endpoint
        self.instance_id = instance_id
        self.protocol = protocol
        self.access_user_name = access_user_name
        self.access_pass_word = access_pass_word
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
        return self


class HaQueryconfigClause(TeaModel):
    def __init__(
        self,
        start: str = None,
        hit: str = None,
        format: str = None,
        custom_config: Dict[str, str] = None,
    ):
        # 从结果集中第 start_offset 开始返回 document 
        self.start = start
        # 返回文档的最大数量
        self.hit = hit
        # 指定用户返回数据格式. 支持 xml 和 json 类型数据返回  
        self.format = format
        # 扩展 配置参数
        self.custom_config = custom_config

    def validate(self):
        self.validate_required(self.start, 'start')
        self.validate_required(self.hit, 'hit')
        self.validate_required(self.format, 'format')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start is not None:
            result['start'] = self.start
        if self.hit is not None:
            result['hit'] = self.hit
        if self.format is not None:
            result['format'] = self.format
        if self.custom_config is not None:
            result['customConfig'] = self.custom_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('hit') is not None:
            self.hit = m.get('hit')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('customConfig') is not None:
            self.custom_config = m.get('customConfig')
        return self


class HaQuerySortClause(TeaModel):
    def __init__(
        self,
        sort_key: str = None,
        sort_order: str = None,
    ):
        # field为要进行统计的字段名，必须配置属性字段
        self.sort_key = sort_key
        # +为按字段值升序排序，-为降序排序
        self.sort_order = sort_order

    def validate(self):
        self.validate_required(self.sort_key, 'sort_key')
        self.validate_required(self.sort_order, 'sort_order')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sort_key is not None:
            result['sortKey'] = self.sort_key
        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sortKey') is not None:
            self.sort_key = m.get('sortKey')
        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')
        return self


class HaQueryAggregateClause(TeaModel):
    def __init__(
        self,
        group_key: str = None,
        agg_fun: str = None,
        range: str = None,
        max_group: str = None,
        agg_filter: str = None,
        agg_sampler_thres_hold: str = None,
        agg_sampler_step: str = None,
    ):
        # field为要进行统计的字段名，必须配置属性字段
        self.group_key = group_key
        # func可以为count()、sum(id)、max(id)、min(id)四种系统函数，含义分别为：文档个数、对id字段求和、取id字段最大值、取id字段最小值；支持同时进行多个函数的统计，中间用英文井号（#）分隔；sum、max、min的内容支持基本的算术运算
        self.agg_fun = agg_fun
        # 表示分段统计，可用于分布统计，只支持单个range参数。
        self.range = range
        # 最大返回组数
        self.max_group = max_group
        # 表示仅统计满足特定条件的文档
        self.agg_filter = agg_filter
        # ，抽样统计的阈值。表示该值之前的文档会依次统计，该值之后的文档会进行抽样统计；
        self.agg_sampler_thres_hold = agg_sampler_thres_hold
        # 抽样统计的步长，表示从agg_sampler_threshold后的文档将间隔agg_sampler_step个文档统计一次。对于sum和count类型的统计会把阈值后的抽样统计结果最后乘以步长进行估算，估算的结果再加上阈值前的统计结果就是最后的统计结果。
        self.agg_sampler_step = agg_sampler_step

    def validate(self):
        self.validate_required(self.group_key, 'group_key')
        self.validate_required(self.agg_fun, 'agg_fun')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_key is not None:
            result['group_key'] = self.group_key
        if self.agg_fun is not None:
            result['agg_fun'] = self.agg_fun
        if self.range is not None:
            result['range'] = self.range
        if self.max_group is not None:
            result['max_group'] = self.max_group
        if self.agg_filter is not None:
            result['agg_filter'] = self.agg_filter
        if self.agg_sampler_thres_hold is not None:
            result['agg_sampler_threshold'] = self.agg_sampler_thres_hold
        if self.agg_sampler_step is not None:
            result['agg_sampler_step'] = self.agg_sampler_step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_key') is not None:
            self.group_key = m.get('group_key')
        if m.get('agg_fun') is not None:
            self.agg_fun = m.get('agg_fun')
        if m.get('range') is not None:
            self.range = m.get('range')
        if m.get('max_group') is not None:
            self.max_group = m.get('max_group')
        if m.get('agg_filter') is not None:
            self.agg_filter = m.get('agg_filter')
        if m.get('agg_sampler_threshold') is not None:
            self.agg_sampler_thres_hold = m.get('agg_sampler_threshold')
        if m.get('agg_sampler_step') is not None:
            self.agg_sampler_step = m.get('agg_sampler_step')
        return self


class HaQueryDistinctClause(TeaModel):
    def __init__(
        self,
        dist_key: str = None,
        dist_count: str = None,
        dist_times: str = None,
        reserved: str = None,
        dist_filter: str = None,
        update_total_hit: str = None,
        grade: str = None,
    ):
        # 要打散的字段
        self.dist_key = dist_key
        # 一轮抽取的文档数
        self.dist_count = dist_count
        # 抽取的轮数
        self.dist_times = dist_times
        # 是否保留抽取之后剩余的文档。如果为false，为不保留，则搜索结果的total（总匹配结果数）会不准确。
        self.reserved = reserved
        # 过滤条件，被过滤的doc不参与distinct，只在后面的排序中，这些被过滤的doc将和被distinct出来的第一组doc一起参与排序。默认是全部参与distinct。
        self.dist_filter = dist_filter
        # 当reserved为false时，设置update_total_hit为true，则最终total_hit会减去被distinct丢弃的数目（不一定准确），为false则不减。
        self.update_total_hit = update_total_hit
        # 指定档位划分阈值，所有的文档将根据档位划分阈值划分成若干档，每个档位中各自根据distinct参数做distinct，可以不指定该参数，默认是所有文档都在同一档。档位的划分按照文档排序时第一维的排序依据的分数进行划分，两个档位阈值之间用 “|” 分开，档位的个数没有限制。例如：1、grade:3.0 ：表示根据第一维排序依据的分数分成两档，(< 3.0)的是第一档，(>= 3.0) 的是第二档；2、grade:3.0|5.0 ：表示分成三档，(< 3.0)是第一档，(>= 3.0，< 5.0)是第二档，(>= 5.0)是第三档。档位的先后顺序和第一维排序依据的顺序一致，即如果第一维排序依据是降序，则档位也是降序，反之亦然。
        self.grade = grade

    def validate(self):
        self.validate_required(self.dist_key, 'dist_key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dist_key is not None:
            result['dist_key'] = self.dist_key
        if self.dist_count is not None:
            result['dist_count'] = self.dist_count
        if self.dist_times is not None:
            result['dist_times'] = self.dist_times
        if self.reserved is not None:
            result['reserved'] = self.reserved
        if self.dist_filter is not None:
            result['dist_filter'] = self.dist_filter
        if self.update_total_hit is not None:
            result['update_total_hit'] = self.update_total_hit
        if self.grade is not None:
            result['grade'] = self.grade
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dist_key') is not None:
            self.dist_key = m.get('dist_key')
        if m.get('dist_count') is not None:
            self.dist_count = m.get('dist_count')
        if m.get('dist_times') is not None:
            self.dist_times = m.get('dist_times')
        if m.get('reserved') is not None:
            self.reserved = m.get('reserved')
        if m.get('dist_filter') is not None:
            self.dist_filter = m.get('dist_filter')
        if m.get('update_total_hit') is not None:
            self.update_total_hit = m.get('update_total_hit')
        if m.get('grade') is not None:
            self.grade = m.get('grade')
        return self


class HaQuery(TeaModel):
    def __init__(
        self,
        query: str = None,
        cluster: str = None,
        config: HaQueryconfigClause = None,
        filter: str = None,
        kvpairs: Dict[str, str] = None,
        sort: List[HaQuerySortClause] = None,
        aggregate: List[HaQueryAggregateClause] = None,
        distinct: List[HaQueryDistinctClause] = None,
        custom_query: Dict[str, str] = None,
    ):
        # 搜索主体，不能为空.并且可以指定多个查询条件及其之间的关系.
        self.query = query
        # cluster部分用于指定要查询的集群的名字。它不仅可以同时指定多个集群，还可以指定到集群中的哪些partition获取结果。
        self.cluster = cluster
        # config部分可以指定查询结果的起始位置、返回结果的数量、展现结果的格式、参与精排表达式文档个数等。
        self.config = config
        # 过滤功能支持用户根据查询条件，筛选出用户感兴趣的文档。会在通过query子句查找到的文档进行进一步的过滤，以返回最终所需结果。
        self.filter = filter
        # 为便于通过查询语句传递信息给具体的特征函数，用户可以在kvpairs子句中对排序表达式中的可变部分进行参数定义。
        self.kvpairs = kvpairs
        # 用户可以通过查询语句控制结果的排序方式，包括指定排序的字段和升降序。field为要排序的字段，+为按字段值升序排序，-为降序排序
        self.sort = sort
        # 一个关键词查询后可能会找到数以万计的文档，用户不太可能浏览所有的文档来获取自己需要的信息，有些情况下用户感兴趣的可能是一些统计的信息。
        self.aggregate = aggregate
        # 打散子句可以在一定程度上保证展示结果的多样性，以提升用户体验。如一次查询可以查出很多的文档，但是如果某个用户的多个文档分值都比较高，则都排在了前面，导致一页中所展示的结果几乎都属于同一用户，这样既不利于结果展示也不利于用户体验。对此，打散子句可以对每个用户的文档进行抽取，使得每个用户都有展示文档的机会。
        self.distinct = distinct
        # 扩展 配置参数
        self.custom_query = custom_query

    def validate(self):
        self.validate_required(self.query, 'query')
        self.validate_required(self.config, 'config')
        if self.config:
            self.config.validate()
        if self.sort:
            for k in self.sort:
                if k:
                    k.validate()
        if self.aggregate:
            for k in self.aggregate:
                if k:
                    k.validate()
        if self.distinct:
            for k in self.distinct:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.kvpairs is not None:
            result['kvpairs'] = self.kvpairs
        result['sort'] = []
        if self.sort is not None:
            for k in self.sort:
                result['sort'].append(k.to_map() if k else None)
        result['aggregate'] = []
        if self.aggregate is not None:
            for k in self.aggregate:
                result['aggregate'].append(k.to_map() if k else None)
        result['distinct'] = []
        if self.distinct is not None:
            for k in self.distinct:
                result['distinct'].append(k.to_map() if k else None)
        if self.custom_query is not None:
            result['customConfig'] = self.custom_query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('config') is not None:
            temp_model = HaQueryconfigClause()
            self.config = temp_model.from_map(m['config'])
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('kvpairs') is not None:
            self.kvpairs = m.get('kvpairs')
        self.sort = []
        if m.get('sort') is not None:
            for k in m.get('sort'):
                temp_model = HaQuerySortClause()
                self.sort.append(temp_model.from_map(k))
        self.aggregate = []
        if m.get('aggregate') is not None:
            for k in m.get('aggregate'):
                temp_model = HaQueryAggregateClause()
                self.aggregate.append(temp_model.from_map(k))
        self.distinct = []
        if m.get('distinct') is not None:
            for k in m.get('distinct'):
                temp_model = HaQueryDistinctClause()
                self.distinct.append(temp_model.from_map(k))
        if m.get('customConfig') is not None:
            self.custom_query = m.get('customConfig')
        return self


class SQLQuery(TeaModel):
    def __init__(
        self,
        query: str = None,
        kvpairs: Dict[str, str] = None,
    ):
        # 搜索主体，不能为空.
        self.query = query
        # cluster部分用于指定要查询的集群的名字。它不仅可以同时指定多个集群，还可以指定到集群中的哪些partition获取结果。
        self.kvpairs = kvpairs

    def validate(self):
        self.validate_required(self.query, 'query')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        if self.kvpairs is not None:
            result['kvpairs'] = self.kvpairs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('kvpairs') is not None:
            self.kvpairs = m.get('kvpairs')
        return self


class SearchQuery(TeaModel):
    def __init__(
        self,
        query: str = None,
        sql: str = None,
    ):
        # 适配于 Ha3 类型 query. 参数支持子句关键字请参照文档
        self.query = query
        # 适配于 SQL 类型 query. 参数支持子句关键字请参照文档.
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        if self.sql is not None:
            result['sql'] = self.sql
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sql') is not None:
            self.sql = m.get('sql')
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


