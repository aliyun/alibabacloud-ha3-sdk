// This file is auto-generated, don't edit it. Thanks.
package client

import (
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  string_  "github.com/alibabacloud-go/darabonba-string/client"
  encodeutil  "github.com/alibabacloud-go/darabonba-encode-util/client"
  ha3util  "github.com/alibabacloud-go/alibabacloud-ha3-util/client"
  time  "github.com/alibabacloud-go/darabonba-time/client"
  number  "github.com/alibabacloud-go/darabonba-number/client"
  "github.com/alibabacloud-go/tea/tea"
)

type Config struct {
  Endpoint *string `json:"endpoint,omitempty" xml:"endpoint,omitempty"`
  InstanceId *string `json:"instanceId,omitempty" xml:"instanceId,omitempty"`
  Protocol *string `json:"protocol,omitempty" xml:"protocol,omitempty"`
  AccessUserName *string `json:"accessUserName,omitempty" xml:"accessUserName,omitempty"`
  AccessPassWord *string `json:"accessPassWord,omitempty" xml:"accessPassWord,omitempty"`
  UserAgent *string `json:"userAgent,omitempty" xml:"userAgent,omitempty"`
  RuntimeOptions *util.RuntimeOptions `json:"runtimeOptions,omitempty" xml:"runtimeOptions,omitempty"`
}

func (s Config) String() string {
  return tea.Prettify(s)
}

func (s Config) GoString() string {
  return s.String()
}

func (s *Config) SetEndpoint(v string) *Config {
  s.Endpoint = &v
  return s
}

func (s *Config) SetInstanceId(v string) *Config {
  s.InstanceId = &v
  return s
}

func (s *Config) SetProtocol(v string) *Config {
  s.Protocol = &v
  return s
}

func (s *Config) SetAccessUserName(v string) *Config {
  s.AccessUserName = &v
  return s
}

func (s *Config) SetAccessPassWord(v string) *Config {
  s.AccessPassWord = &v
  return s
}

func (s *Config) SetUserAgent(v string) *Config {
  s.UserAgent = &v
  return s
}

func (s *Config) SetRuntimeOptions(v *util.RuntimeOptions) *Config {
  s.RuntimeOptions = v
  return s
}

type SearchResponse struct {
  // headers
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // body
  Body *string `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s SearchResponse) String() string {
  return tea.Prettify(s)
}

func (s SearchResponse) GoString() string {
  return s.String()
}

func (s *SearchResponse) SetHeaders(v map[string]*string) *SearchResponse {
  s.Headers = v
  return s
}

func (s *SearchResponse) SetBody(v string) *SearchResponse {
  s.Body = &v
  return s
}

type QueryRequest struct {
  // 数据源名
  TableName *string `json:"tableName,omitempty" xml:"tableName,omitempty" require:"true"`
  // 向量数据
  Vector []*float32 `json:"vector,omitempty" xml:"vector,omitempty" require:"true" type:"Repeated"`
  // 查询向量的空间
  Namespace *string `json:"namespace,omitempty" xml:"namespace,omitempty"`
  // 返回个数
  TopK *int `json:"topK,omitempty" xml:"topK,omitempty"`
  // 查询的索引名
  IndexName *string `json:"indexName,omitempty" xml:"indexName,omitempty"`
  // 查询的稀疏向量
  SparseData *SparseData `json:"sparseData,omitempty" xml:"sparseData,omitempty"`
  // Query的权重
  Weight *float32 `json:"weight,omitempty" xml:"weight,omitempty"`
  // 需要向量化的内容
  Content *string `json:"content,omitempty" xml:"content,omitempty"`
  // 使用的模型
  Modal *string `json:"modal,omitempty" xml:"modal,omitempty"`
  // 是否返回文档中的向量信息
  IncludeVector *bool `json:"includeVector,omitempty" xml:"includeVector,omitempty"`
  // 需要返回值的字段列表
  OutputFields []*string `json:"outputFields,omitempty" xml:"outputFields,omitempty" type:"Repeated"`
  // 排序顺序, ASC：升序  DESC: 降序
  Order *string `json:"order,omitempty" xml:"order,omitempty"`
  // 查询参数
  SearchParams *string `json:"searchParams,omitempty" xml:"searchParams,omitempty"`
  // 过滤表达式
  Filter *string `json:"filter,omitempty" xml:"filter,omitempty"`
  // 分数过滤， 使用欧式距离时，只返回小于scoreThreshold的结果。使用内积时，只返回大于scoreThreshold的结果
  ScoreThreshold *float32 `json:"scoreThreshold,omitempty" xml:"scoreThreshold,omitempty"`
  // vector字段中包含的向量个数
  VectorCount *int `json:"vectorCount,omitempty" xml:"vectorCount,omitempty"`
  // 排序表达式
  Sort *string `json:"sort,omitempty" xml:"sort,omitempty"`
  // kvpairs
  Kvpairs map[string]*string `json:"kvpairs,omitempty" xml:"kvpairs,omitempty"`
}

func (s QueryRequest) String() string {
  return tea.Prettify(s)
}

func (s QueryRequest) GoString() string {
  return s.String()
}

func (s *QueryRequest) SetTableName(v string) *QueryRequest {
  s.TableName = &v
  return s
}

func (s *QueryRequest) SetVector(v []*float32) *QueryRequest {
  s.Vector = v
  return s
}

func (s *QueryRequest) SetNamespace(v string) *QueryRequest {
  s.Namespace = &v
  return s
}

func (s *QueryRequest) SetTopK(v int) *QueryRequest {
  s.TopK = &v
  return s
}

func (s *QueryRequest) SetIndexName(v string) *QueryRequest {
  s.IndexName = &v
  return s
}

func (s *QueryRequest) SetSparseData(v *SparseData) *QueryRequest {
  s.SparseData = v
  return s
}

func (s *QueryRequest) SetWeight(v float32) *QueryRequest {
  s.Weight = &v
  return s
}

func (s *QueryRequest) SetContent(v string) *QueryRequest {
  s.Content = &v
  return s
}

func (s *QueryRequest) SetModal(v string) *QueryRequest {
  s.Modal = &v
  return s
}

func (s *QueryRequest) SetIncludeVector(v bool) *QueryRequest {
  s.IncludeVector = &v
  return s
}

func (s *QueryRequest) SetOutputFields(v []*string) *QueryRequest {
  s.OutputFields = v
  return s
}

func (s *QueryRequest) SetOrder(v string) *QueryRequest {
  s.Order = &v
  return s
}

func (s *QueryRequest) SetSearchParams(v string) *QueryRequest {
  s.SearchParams = &v
  return s
}

func (s *QueryRequest) SetFilter(v string) *QueryRequest {
  s.Filter = &v
  return s
}

func (s *QueryRequest) SetScoreThreshold(v float32) *QueryRequest {
  s.ScoreThreshold = &v
  return s
}

func (s *QueryRequest) SetVectorCount(v int) *QueryRequest {
  s.VectorCount = &v
  return s
}

func (s *QueryRequest) SetSort(v string) *QueryRequest {
  s.Sort = &v
  return s
}

func (s *QueryRequest) SetKvpairs(v map[string]*string) *QueryRequest {
  s.Kvpairs = v
  return s
}

type SparseData struct {
  // 每个稀疏向量中包含的元素个数
  Count []*int `json:"count,omitempty" xml:"count,omitempty" type:"Repeated"`
  // 元素下标（需要从小到大排序）
  Indices []*int64 `json:"indices,omitempty" xml:"indices,omitempty" require:"true" type:"Repeated"`
  // 元素值（与下标一一对应）
  Values []*float32 `json:"values,omitempty" xml:"values,omitempty" require:"true" type:"Repeated"`
}

func (s SparseData) String() string {
  return tea.Prettify(s)
}

func (s SparseData) GoString() string {
  return s.String()
}

func (s *SparseData) SetCount(v []*int) *SparseData {
  s.Count = v
  return s
}

func (s *SparseData) SetIndices(v []*int64) *SparseData {
  s.Indices = v
  return s
}

func (s *SparseData) SetValues(v []*float32) *SparseData {
  s.Values = v
  return s
}

type MultiQueryRequest struct {
  // 数据源名
  TableName *string `json:"tableName,omitempty" xml:"tableName,omitempty" require:"true"`
  // 多向量列表
  Queries []*QueryRequest `json:"queries,omitempty" xml:"queries,omitempty" require:"true" type:"Repeated"`
  // 返回个数
  TopK *int `json:"topK,omitempty" xml:"topK,omitempty"`
  // 是否返回文档中的向量信息
  IncludeVector *bool `json:"includeVector,omitempty" xml:"includeVector,omitempty"`
  // 需要返回值的字段列表
  OutputFields []*string `json:"outputFields,omitempty" xml:"outputFields,omitempty" type:"Repeated"`
  // 排序顺序, ASC：升序  DESC: 降序
  Order *string `json:"order,omitempty" xml:"order,omitempty"`
  // 过滤表达式
  Filter *string `json:"filter,omitempty" xml:"filter,omitempty"`
  // 排序表达式
  Sort *string `json:"sort,omitempty" xml:"sort,omitempty"`
}

func (s MultiQueryRequest) String() string {
  return tea.Prettify(s)
}

func (s MultiQueryRequest) GoString() string {
  return s.String()
}

func (s *MultiQueryRequest) SetTableName(v string) *MultiQueryRequest {
  s.TableName = &v
  return s
}

func (s *MultiQueryRequest) SetQueries(v []*QueryRequest) *MultiQueryRequest {
  s.Queries = v
  return s
}

func (s *MultiQueryRequest) SetTopK(v int) *MultiQueryRequest {
  s.TopK = &v
  return s
}

func (s *MultiQueryRequest) SetIncludeVector(v bool) *MultiQueryRequest {
  s.IncludeVector = &v
  return s
}

func (s *MultiQueryRequest) SetOutputFields(v []*string) *MultiQueryRequest {
  s.OutputFields = v
  return s
}

func (s *MultiQueryRequest) SetOrder(v string) *MultiQueryRequest {
  s.Order = &v
  return s
}

func (s *MultiQueryRequest) SetFilter(v string) *MultiQueryRequest {
  s.Filter = &v
  return s
}

func (s *MultiQueryRequest) SetSort(v string) *MultiQueryRequest {
  s.Sort = &v
  return s
}

type FetchRequest struct {
  // 数据源名
  TableName *string `json:"tableName,omitempty" xml:"tableName,omitempty" require:"true"`
  // 主键列表，如果传了主键列表，下面的条件参数不生效
  Ids []*string `json:"ids,omitempty" xml:"ids,omitempty" type:"Repeated"`
  // 过滤表达式
  Filter *string `json:"filter,omitempty" xml:"filter,omitempty"`
  // 排序表达式
  Sort *string `json:"sort,omitempty" xml:"sort,omitempty"`
  // 返回的数据个数
  Limit *int `json:"limit,omitempty" xml:"limit,omitempty"`
  // 返回的数据开始下标，用于翻页
  Offset *int `json:"offset,omitempty" xml:"offset,omitempty"`
  // 是否返回向量数据
  IncludeVector *bool `json:"includeVector,omitempty" xml:"includeVector,omitempty"`
  // 需要返回的字段，不指定默认返回所有的字段
  OutputFields []*string `json:"outputFields,omitempty" xml:"outputFields,omitempty" type:"Repeated"`
  // kvpairs
  Kvpairs map[string]*string `json:"kvpairs,omitempty" xml:"kvpairs,omitempty"`
}

func (s FetchRequest) String() string {
  return tea.Prettify(s)
}

func (s FetchRequest) GoString() string {
  return s.String()
}

func (s *FetchRequest) SetTableName(v string) *FetchRequest {
  s.TableName = &v
  return s
}

func (s *FetchRequest) SetIds(v []*string) *FetchRequest {
  s.Ids = v
  return s
}

func (s *FetchRequest) SetFilter(v string) *FetchRequest {
  s.Filter = &v
  return s
}

func (s *FetchRequest) SetSort(v string) *FetchRequest {
  s.Sort = &v
  return s
}

func (s *FetchRequest) SetLimit(v int) *FetchRequest {
  s.Limit = &v
  return s
}

func (s *FetchRequest) SetOffset(v int) *FetchRequest {
  s.Offset = &v
  return s
}

func (s *FetchRequest) SetIncludeVector(v bool) *FetchRequest {
  s.IncludeVector = &v
  return s
}

func (s *FetchRequest) SetOutputFields(v []*string) *FetchRequest {
  s.OutputFields = v
  return s
}

func (s *FetchRequest) SetKvpairs(v map[string]*string) *FetchRequest {
  s.Kvpairs = v
  return s
}

type RankQuery struct {
  // 查询表达式
  Rrf map[string]*string `json:"rrf,omitempty" xml:"rrf,omitempty"`
}

func (s RankQuery) String() string {
  return tea.Prettify(s)
}

func (s RankQuery) GoString() string {
  return s.String()
}

func (s *RankQuery) SetRrf(v map[string]*string) *RankQuery {
  s.Rrf = v
  return s
}

type TextQuery struct {
  // ha3 query语法，支持多个文本索引的AND、OR嵌套
  QueryString *string `json:"queryString,omitempty" xml:"queryString,omitempty" require:"true"`
  // query查询参数：
  // 
  //       default_op: 指定在该次查询中使用的默认query 分词后的连接操作符，AND or OR。默认为AND。
  // 
  //       global_analyzer: 查询中指定全局的分词器，该分词器会覆盖schema的分词器，指定的值必须在analyzer.json里有配置。
  // 
  //       specific_index_analyzer: 查询中指定index使用另外的分词器，该分词器会覆盖global_analyzer和schema的分词器。
  // 
  //       no_token_indexes: 支持查询中指定的index不分词（除分词以外的其他流程如归一化、去停用词会正常执行），多个index之间用;分割。
  // 
  //       remove_stopwords: true or false 表示是否需要删除stop words，stop words在分词器中配置。默认true
  QueryParams map[string]*string `json:"queryParams,omitempty" xml:"queryParams,omitempty"`
  // 过滤条件表达式
  Filter *string `json:"filter,omitempty" xml:"filter,omitempty"`
  // text查询结果的权重，以score 	- weight的结果作为该路的排序分
  Weight *float32 `json:"weight,omitempty" xml:"weight,omitempty"`
  // 每个分片查找满足条件的文档的最大数量。到达这个数量后，查询将提前结束，不再继续查询索引。默认为0，不设置限制。
  TerminateAfter *int `json:"terminateAfter,omitempty" xml:"terminateAfter,omitempty"`
}

func (s TextQuery) String() string {
  return tea.Prettify(s)
}

func (s TextQuery) GoString() string {
  return s.String()
}

func (s *TextQuery) SetQueryString(v string) *TextQuery {
  s.QueryString = &v
  return s
}

func (s *TextQuery) SetQueryParams(v map[string]*string) *TextQuery {
  s.QueryParams = v
  return s
}

func (s *TextQuery) SetFilter(v string) *TextQuery {
  s.Filter = &v
  return s
}

func (s *TextQuery) SetWeight(v float32) *TextQuery {
  s.Weight = &v
  return s
}

func (s *TextQuery) SetTerminateAfter(v int) *TextQuery {
  s.TerminateAfter = &v
  return s
}

type SearchRequest struct {
  // 数据源名
  TableName *string `json:"tableName,omitempty" xml:"tableName,omitempty" require:"true"`
  // 返回结果的个数
  Size *int `json:"size,omitempty" xml:"size,omitempty"`
  // 从结果集的第from返回doc
  From *int `json:"from,omitempty" xml:"from,omitempty"`
  // 结果排序方向:DESC: 降序排序;ASC: 升序排序
  Order *string `json:"order,omitempty" xml:"order,omitempty"`
  // 指定需要在结果中返回的字段，默认为空
  OutputFields []*string `json:"outputFields,omitempty" xml:"outputFields,omitempty" type:"Repeated"`
  // KNN查询参数
  Knn *QueryRequest `json:"knn,omitempty" xml:"knn,omitempty"`
  // text查询参数
  Text *TextQuery `json:"text,omitempty" xml:"text,omitempty"`
  // 指定两路结果融合的方式，目前支持两种策略：默认策略：两路结果中相同pk的doc的分数按权重相加。按加权后的分数排序。rrf: 使用rrf融合两路结果
  Rank *RankQuery `json:"rank,omitempty" xml:"rank,omitempty"`
}

func (s SearchRequest) String() string {
  return tea.Prettify(s)
}

func (s SearchRequest) GoString() string {
  return s.String()
}

func (s *SearchRequest) SetTableName(v string) *SearchRequest {
  s.TableName = &v
  return s
}

func (s *SearchRequest) SetSize(v int) *SearchRequest {
  s.Size = &v
  return s
}

func (s *SearchRequest) SetFrom(v int) *SearchRequest {
  s.From = &v
  return s
}

func (s *SearchRequest) SetOrder(v string) *SearchRequest {
  s.Order = &v
  return s
}

func (s *SearchRequest) SetOutputFields(v []*string) *SearchRequest {
  s.OutputFields = v
  return s
}

func (s *SearchRequest) SetKnn(v *QueryRequest) *SearchRequest {
  s.Knn = v
  return s
}

func (s *SearchRequest) SetText(v *TextQuery) *SearchRequest {
  s.Text = v
  return s
}

func (s *SearchRequest) SetRank(v *RankQuery) *SearchRequest {
  s.Rank = v
  return s
}

type AggFuncDesc struct {
  // 可以指定统计值在结果集中字段的名称。默认结果字段为: FUNC_NAME(args)
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // 统计函数名：max, min, avg, sum, count
  Func *string `json:"func,omitempty" xml:"func,omitempty" require:"true"`
  // 统计函数的参数
  Args []*string `json:"args,omitempty" xml:"args,omitempty" require:"true" type:"Repeated"`
}

func (s AggFuncDesc) String() string {
  return tea.Prettify(s)
}

func (s AggFuncDesc) GoString() string {
  return s.String()
}

func (s *AggFuncDesc) SetName(v string) *AggFuncDesc {
  s.Name = &v
  return s
}

func (s *AggFuncDesc) SetFunc(v string) *AggFuncDesc {
  s.Func = &v
  return s
}

func (s *AggFuncDesc) SetArgs(v []*string) *AggFuncDesc {
  s.Args = v
  return s
}

type OrderByDesc struct {
  // 排序字段名称，必须指定结果集中的字段
  Field *string `json:"field,omitempty" xml:"field,omitempty" require:"true"`
  // 排序方向，DESC: 降序排列；ASC: 升序排列
  Direction *string `json:"direction,omitempty" xml:"direction,omitempty"`
}

func (s OrderByDesc) String() string {
  return tea.Prettify(s)
}

func (s OrderByDesc) GoString() string {
  return s.String()
}

func (s *OrderByDesc) SetField(v string) *OrderByDesc {
  s.Field = &v
  return s
}

func (s *OrderByDesc) SetDirection(v string) *OrderByDesc {
  s.Direction = &v
  return s
}

type AggregateRequest struct {
  // 需要统计的表名
  TableName *string `json:"tableName,omitempty" xml:"tableName,omitempty" require:"true"`
  // 过滤条件
  Filter *string `json:"filter,omitempty" xml:"filter,omitempty"`
  // 分组统计的字段列表
  GroupKeys []*string `json:"groupKeys,omitempty" xml:"groupKeys,omitempty" type:"Repeated"`
  // 统计函数列表
  AggFuncs []*AggFuncDesc `json:"aggFuncs,omitempty" xml:"aggFuncs,omitempty" require:"true" type:"Repeated"`
  // 统计结果排序方式，支持多维排序
  OrderBy []*OrderByDesc `json:"orderBy,omitempty" xml:"orderBy,omitempty" type:"Repeated"`
  // 超时时间，单位毫秒
  Timeout *int `json:"timeout,omitempty" xml:"timeout,omitempty"`
}

func (s AggregateRequest) String() string {
  return tea.Prettify(s)
}

func (s AggregateRequest) GoString() string {
  return s.String()
}

func (s *AggregateRequest) SetTableName(v string) *AggregateRequest {
  s.TableName = &v
  return s
}

func (s *AggregateRequest) SetFilter(v string) *AggregateRequest {
  s.Filter = &v
  return s
}

func (s *AggregateRequest) SetGroupKeys(v []*string) *AggregateRequest {
  s.GroupKeys = v
  return s
}

func (s *AggregateRequest) SetAggFuncs(v []*AggFuncDesc) *AggregateRequest {
  s.AggFuncs = v
  return s
}

func (s *AggregateRequest) SetOrderBy(v []*OrderByDesc) *AggregateRequest {
  s.OrderBy = v
  return s
}

func (s *AggregateRequest) SetTimeout(v int) *AggregateRequest {
  s.Timeout = &v
  return s
}

type BatchRequest struct {
  // 批量查询列表
  Queries []*QueryRequest `json:"queries,omitempty" xml:"queries,omitempty" require:"true" type:"Repeated"`
  // 超时时间，单位毫秒
  Timeout *int `json:"timeout,omitempty" xml:"timeout,omitempty"`
}

func (s BatchRequest) String() string {
  return tea.Prettify(s)
}

func (s BatchRequest) GoString() string {
  return s.String()
}

func (s *BatchRequest) SetQueries(v []*QueryRequest) *BatchRequest {
  s.Queries = v
  return s
}

func (s *BatchRequest) SetTimeout(v int) *BatchRequest {
  s.Timeout = &v
  return s
}

type PushDocumentsRequest struct {
  // headers
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // body
  Body []map[string]interface{} `json:"body,omitempty" xml:"body,omitempty" require:"true" type:"Repeated"`
}

func (s PushDocumentsRequest) String() string {
  return tea.Prettify(s)
}

func (s PushDocumentsRequest) GoString() string {
  return s.String()
}

func (s *PushDocumentsRequest) SetHeaders(v map[string]*string) *PushDocumentsRequest {
  s.Headers = v
  return s
}

func (s *PushDocumentsRequest) SetBody(v []map[string]interface{}) *PushDocumentsRequest {
  s.Body = v
  return s
}

type PushDocumentsResponse struct {
  // headers
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // body
  Body *string `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s PushDocumentsResponse) String() string {
  return tea.Prettify(s)
}

func (s PushDocumentsResponse) GoString() string {
  return s.String()
}

func (s *PushDocumentsResponse) SetHeaders(v map[string]*string) *PushDocumentsResponse {
  s.Headers = v
  return s
}

func (s *PushDocumentsResponse) SetBody(v string) *PushDocumentsResponse {
  s.Body = &v
  return s
}

// Description:
// 
// 获取所有表信息
type ListTablesResponseBody struct {
  // requestId
  // 
  // example:
  // 
  // 10D5E615-69F7-5F49-B850-00169ADE513C
  RequestId *string `json:"requestId,omitempty" xml:"requestId,omitempty"`
  // The result.
  Result []*ListTablesResponseBodyResult `json:"result,omitempty" xml:"result,omitempty" type:"Repeated"`
}

func (s ListTablesResponseBody) String() string {
  return tea.Prettify(s)
}

func (s ListTablesResponseBody) GoString() string {
  return s.String()
}

func (s *ListTablesResponseBody) SetRequestId(v string) *ListTablesResponseBody {
  s.RequestId = &v
  return s
}

func (s *ListTablesResponseBody) SetResult(v []*ListTablesResponseBodyResult) *ListTablesResponseBody {
  s.Result = v
  return s
}

type ListTablesResponseBodyResult struct     {
  // The state of the index table. Valid values: NEW, PUBLISH, IN_USE, NOT_USE, STOP_USE, RESTORE_USE, and FAIL. After an index is created in an OpenSearch Retrieval Engine Edition instance, the index enters the IN_USE state. If the first full index fails to be created in an OpenSearch Vector Search Edition instance of the new version, the index is in the FAIL state.
  // 
  // example:
  // 
  // IN_USE
  IndexStatus *string `json:"indexStatus,omitempty" xml:"indexStatus,omitempty"`
  // The index name.
  // 
  // example:
  // 
  // es_test_1b
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // The state of the index table. Valid values: NEW, PUBLISH, IN_USE, NOT_USE, STOP_USE, RESTORE_USE, and FAIL. After an index is created in an OpenSearch Retrieval Engine Edition instance, the index enters the IN_USE state. If the first full index fails to be created in an OpenSearch Vector Search Edition instance of the new version, the index is in the FAIL state.
  // 
  // example:
  // 
  // IN_USE
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
}

func (s ListTablesResponseBodyResult) String() string {
  return tea.Prettify(s)
}

func (s ListTablesResponseBodyResult) GoString() string {
  return s.String()
}

func (s *ListTablesResponseBodyResult) SetIndexStatus(v string) *ListTablesResponseBodyResult {
  s.IndexStatus = &v
  return s
}

func (s *ListTablesResponseBodyResult) SetName(v string) *ListTablesResponseBodyResult {
  s.Name = &v
  return s
}

func (s *ListTablesResponseBodyResult) SetStatus(v string) *ListTablesResponseBodyResult {
  s.Status = &v
  return s
}

type ListTablesResponse struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  StatusCode *int32 `json:"statusCode,omitempty" xml:"statusCode,omitempty"`
  Body *ListTablesResponseBody `json:"body,omitempty" xml:"body,omitempty"`
}

func (s ListTablesResponse) String() string {
  return tea.Prettify(s)
}

func (s ListTablesResponse) GoString() string {
  return s.String()
}

func (s *ListTablesResponse) SetHeaders(v map[string]*string) *ListTablesResponse {
  s.Headers = v
  return s
}

func (s *ListTablesResponse) SetStatusCode(v int32) *ListTablesResponse {
  s.StatusCode = &v
  return s
}

func (s *ListTablesResponse) SetBody(v *ListTablesResponseBody) *ListTablesResponse {
  s.Body = v
  return s
}

// Description:
// 
// 获取单表详情
type GetTableResponseBody struct {
  // requestId
  // 
  // example:
  // 
  // 2AE63638-5420-56DC-BF59-37D8174039A0
  RequestId *string `json:"requestId,omitempty" xml:"requestId,omitempty"`
  // The results returned.
  Result *GetTableResponseBodyResult `json:"result,omitempty" xml:"result,omitempty" type:"Struct"`
}

func (s GetTableResponseBody) String() string {
  return tea.Prettify(s)
}

func (s GetTableResponseBody) GoString() string {
  return s.String()
}

func (s *GetTableResponseBody) SetRequestId(v string) *GetTableResponseBody {
  s.RequestId = &v
  return s
}

func (s *GetTableResponseBody) SetResult(v *GetTableResponseBodyResult) *GetTableResponseBody {
  s.Result = v
  return s
}

type GetTableResponseBodyResult struct {
  // example:
  // 
  // test_oss
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // example:
  // 
  // 1
  PartitionCount *int32 `json:"partitionCount,omitempty" xml:"partitionCount,omitempty"`
  // example:
  // 
  // id
  PrimaryKey *string `json:"primaryKey,omitempty" xml:"primaryKey,omitempty"`
  // example:
  // 
  // {}
  RawSchema *string `json:"rawSchema,omitempty" xml:"rawSchema,omitempty"`
  // example:
  // 
  // 1
  DataProcessorCount *int32 `json:"dataProcessorCount,omitempty" xml:"dataProcessorCount,omitempty"`
  // The field. The value is a key-value pair in which the key indicates the field name and value indicates the field type.
  FieldSchema map[string]*string `json:"fieldSchema,omitempty" xml:"fieldSchema,omitempty"`
  // The state of the index table. Valid values: NEW, PUBLISH, IN_USE, NOT_USE, STOP_USE, RESTORE_USE, and FAIL. After an index is created in an OpenSearch Retrieval Engine Edition instance, the index enters the IN_USE state. If the first full index fails to be created in an OpenSearch Vector Search Edition instance of the new version, the index is in the FAIL state.
  // 
  // example:
  // 
  // IN_USE
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // The index schema.
  VectorIndex []*GetTableResponseBodyResultVectorIndex `json:"vectorIndex,omitempty" xml:"vectorIndex,omitempty" type:"Repeated"`
  DataSource *GetTableResponseBodyResultDataSource `json:"dataSource,omitempty" xml:"dataSource,omitempty" type:"Struct"`
  // The configurations about field processing.
  DataProcessConfig []*GetTableResponseBodyResultDataProcessConfig `json:"dataProcessConfig,omitempty" xml:"dataProcessConfig,omitempty" type:"Repeated"`
}

func (s GetTableResponseBodyResult) String() string {
  return tea.Prettify(s)
}

func (s GetTableResponseBodyResult) GoString() string {
  return s.String()
}

func (s *GetTableResponseBodyResult) SetName(v string) *GetTableResponseBodyResult {
  s.Name = &v
  return s
}

func (s *GetTableResponseBodyResult) SetPartitionCount(v int32) *GetTableResponseBodyResult {
  s.PartitionCount = &v
  return s
}

func (s *GetTableResponseBodyResult) SetPrimaryKey(v string) *GetTableResponseBodyResult {
  s.PrimaryKey = &v
  return s
}

func (s *GetTableResponseBodyResult) SetRawSchema(v string) *GetTableResponseBodyResult {
  s.RawSchema = &v
  return s
}

func (s *GetTableResponseBodyResult) SetDataProcessorCount(v int32) *GetTableResponseBodyResult {
  s.DataProcessorCount = &v
  return s
}

func (s *GetTableResponseBodyResult) SetFieldSchema(v map[string]*string) *GetTableResponseBodyResult {
  s.FieldSchema = v
  return s
}

func (s *GetTableResponseBodyResult) SetStatus(v string) *GetTableResponseBodyResult {
  s.Status = &v
  return s
}

func (s *GetTableResponseBodyResult) SetVectorIndex(v []*GetTableResponseBodyResultVectorIndex) *GetTableResponseBodyResult {
  s.VectorIndex = v
  return s
}

func (s *GetTableResponseBodyResult) SetDataSource(v *GetTableResponseBodyResultDataSource) *GetTableResponseBodyResult {
  s.DataSource = v
  return s
}

func (s *GetTableResponseBodyResult) SetDataProcessConfig(v []*GetTableResponseBodyResultDataProcessConfig) *GetTableResponseBodyResult {
  s.DataProcessConfig = v
  return s
}

type GetTableResponseBodyResultVectorIndex struct     {
  // The configurations of the index schema.
  AdvanceParams *GetTableResponseBodyResultVectorIndexAdvanceParams `json:"advanceParams,omitempty" xml:"advanceParams,omitempty" type:"Struct"`
  // The dimension of the vector.
  // 
  // example:
  // 
  // 128
  Dimension *string `json:"dimension,omitempty" xml:"dimension,omitempty"`
  // The distance type.
  // 
  // example:
  // 
  // SquaredEuclidean
  DistanceType *string `json:"distanceType,omitempty" xml:"distanceType,omitempty"`
  // The name of the index schema.
  // 
  // example:
  // 
  // test_odps
  IndexName *string `json:"indexName,omitempty" xml:"indexName,omitempty"`
  // The namespace field.
  // 
  // example:
  // 
  // namespace
  Namespace *string `json:"namespace,omitempty" xml:"namespace,omitempty"`
  // The field that stores the indexes of the elements in sparse vectors.
  // 
  // example:
  // 
  // sparse_indices
  SparseIndexField *string `json:"sparseIndexField,omitempty" xml:"sparseIndexField,omitempty"`
  // The field that stores the elements in sparse vectors.
  // 
  // example:
  // 
  // sparse_values
  SparseValueField *string `json:"sparseValueField,omitempty" xml:"sparseValueField,omitempty"`
  // The vector field.
  // 
  // example:
  // 
  // source_image_vector
  VectorField *string `json:"vectorField,omitempty" xml:"vectorField,omitempty"`
  // The vector retrieval algorithm.
  // 
  // example:
  // 
  // Qc
  VectorIndexType *string `json:"vectorIndexType,omitempty" xml:"vectorIndexType,omitempty"`
}

func (s GetTableResponseBodyResultVectorIndex) String() string {
  return tea.Prettify(s)
}

func (s GetTableResponseBodyResultVectorIndex) GoString() string {
  return s.String()
}

func (s *GetTableResponseBodyResultVectorIndex) SetAdvanceParams(v *GetTableResponseBodyResultVectorIndexAdvanceParams) *GetTableResponseBodyResultVectorIndex {
  s.AdvanceParams = v
  return s
}

func (s *GetTableResponseBodyResultVectorIndex) SetDimension(v string) *GetTableResponseBodyResultVectorIndex {
  s.Dimension = &v
  return s
}

func (s *GetTableResponseBodyResultVectorIndex) SetDistanceType(v string) *GetTableResponseBodyResultVectorIndex {
  s.DistanceType = &v
  return s
}

func (s *GetTableResponseBodyResultVectorIndex) SetIndexName(v string) *GetTableResponseBodyResultVectorIndex {
  s.IndexName = &v
  return s
}

func (s *GetTableResponseBodyResultVectorIndex) SetNamespace(v string) *GetTableResponseBodyResultVectorIndex {
  s.Namespace = &v
  return s
}

func (s *GetTableResponseBodyResultVectorIndex) SetSparseIndexField(v string) *GetTableResponseBodyResultVectorIndex {
  s.SparseIndexField = &v
  return s
}

func (s *GetTableResponseBodyResultVectorIndex) SetSparseValueField(v string) *GetTableResponseBodyResultVectorIndex {
  s.SparseValueField = &v
  return s
}

func (s *GetTableResponseBodyResultVectorIndex) SetVectorField(v string) *GetTableResponseBodyResultVectorIndex {
  s.VectorField = &v
  return s
}

func (s *GetTableResponseBodyResultVectorIndex) SetVectorIndexType(v string) *GetTableResponseBodyResultVectorIndex {
  s.VectorIndexType = &v
  return s
}

type GetTableResponseBodyResultVectorIndexAdvanceParams struct {
  // The index building parameters.
  // 
  // example:
  // 
  // {}
  BuildIndexParams *string `json:"buildIndexParams,omitempty" xml:"buildIndexParams,omitempty"`
  // The threshold for linear building.
  // 
  // example:
  // 
  // 5000
  LinearBuildThreshold *string `json:"linearBuildThreshold,omitempty" xml:"linearBuildThreshold,omitempty"`
  // The minimum number of retrieved candidate sets.
  // 
  // example:
  // 
  // 20000
  MinScanDocCnt *string `json:"minScanDocCnt,omitempty" xml:"minScanDocCnt,omitempty"`
  // The index retrieval parameters.
  // 
  // example:
  // 
  // {}
  SearchIndexParams *string `json:"searchIndexParams,omitempty" xml:"searchIndexParams,omitempty"`
}

func (s GetTableResponseBodyResultVectorIndexAdvanceParams) String() string {
  return tea.Prettify(s)
}

func (s GetTableResponseBodyResultVectorIndexAdvanceParams) GoString() string {
  return s.String()
}

func (s *GetTableResponseBodyResultVectorIndexAdvanceParams) SetBuildIndexParams(v string) *GetTableResponseBodyResultVectorIndexAdvanceParams {
  s.BuildIndexParams = &v
  return s
}

func (s *GetTableResponseBodyResultVectorIndexAdvanceParams) SetLinearBuildThreshold(v string) *GetTableResponseBodyResultVectorIndexAdvanceParams {
  s.LinearBuildThreshold = &v
  return s
}

func (s *GetTableResponseBodyResultVectorIndexAdvanceParams) SetMinScanDocCnt(v string) *GetTableResponseBodyResultVectorIndexAdvanceParams {
  s.MinScanDocCnt = &v
  return s
}

func (s *GetTableResponseBodyResultVectorIndexAdvanceParams) SetSearchIndexParams(v string) *GetTableResponseBodyResultVectorIndexAdvanceParams {
  s.SearchIndexParams = &v
  return s
}

type GetTableResponseBodyResultDataSource struct {
  // example:
  // 
  // true
  AutoBuildIndex *bool `json:"autoBuildIndex,omitempty" xml:"autoBuildIndex,omitempty"`
  Config *GetTableResponseBodyResultDataSourceConfig `json:"config,omitempty" xml:"config,omitempty" type:"Struct"`
  // example:
  // 
  // 1715160176
  DataTimeSec *int32 `json:"dataTimeSec,omitempty" xml:"dataTimeSec,omitempty"`
  // example:
  // 
  // odps
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
}

func (s GetTableResponseBodyResultDataSource) String() string {
  return tea.Prettify(s)
}

func (s GetTableResponseBodyResultDataSource) GoString() string {
  return s.String()
}

func (s *GetTableResponseBodyResultDataSource) SetAutoBuildIndex(v bool) *GetTableResponseBodyResultDataSource {
  s.AutoBuildIndex = &v
  return s
}

func (s *GetTableResponseBodyResultDataSource) SetConfig(v *GetTableResponseBodyResultDataSourceConfig) *GetTableResponseBodyResultDataSource {
  s.Config = v
  return s
}

func (s *GetTableResponseBodyResultDataSource) SetDataTimeSec(v int32) *GetTableResponseBodyResultDataSource {
  s.DataTimeSec = &v
  return s
}

func (s *GetTableResponseBodyResultDataSource) SetType(v string) *GetTableResponseBodyResultDataSource {
  s.Type = &v
  return s
}

type GetTableResponseBodyResultDataSourceConfig struct {
  // AK
  // 
  // example:
  // 
  // ak
  AccessKey *string `json:"accessKey,omitempty" xml:"accessKey,omitempty"`
  // AS
  // 
  // example:
  // 
  // as
  AccessSecret *string `json:"accessSecret,omitempty" xml:"accessSecret,omitempty"`
  // example:
  // 
  // heytea-ops-oss
  Bucket *string `json:"bucket,omitempty" xml:"bucket,omitempty"`
  // example:
  // 
  // http://service.cn-hangzhou.maxcompute.aliyun-inc.com/api
  Endpoint *string `json:"endpoint,omitempty" xml:"endpoint,omitempty"`
  // example:
  // 
  // namespace
  Namespace *string `json:"namespace,omitempty" xml:"namespace,omitempty"`
  // example:
  // 
  // /opensearch_index_data/sift_oss_test.data
  OssPath *string `json:"ossPath,omitempty" xml:"ossPath,omitempty"`
  // example:
  // 
  // ds=20220808
  Partition *string `json:"partition,omitempty" xml:"partition,omitempty"`
  // example:
  // 
  // vendor/sebastian/comparator/src/exceptions
  Path *string `json:"path,omitempty" xml:"path,omitempty"`
  // example:
  // 
  // dp_pdm_marketing_prod
  Project *string `json:"project,omitempty" xml:"project,omitempty"`
  // example:
  // 
  // test_add
  Table *string `json:"table,omitempty" xml:"table,omitempty"`
}

func (s GetTableResponseBodyResultDataSourceConfig) String() string {
  return tea.Prettify(s)
}

func (s GetTableResponseBodyResultDataSourceConfig) GoString() string {
  return s.String()
}

func (s *GetTableResponseBodyResultDataSourceConfig) SetAccessKey(v string) *GetTableResponseBodyResultDataSourceConfig {
  s.AccessKey = &v
  return s
}

func (s *GetTableResponseBodyResultDataSourceConfig) SetAccessSecret(v string) *GetTableResponseBodyResultDataSourceConfig {
  s.AccessSecret = &v
  return s
}

func (s *GetTableResponseBodyResultDataSourceConfig) SetBucket(v string) *GetTableResponseBodyResultDataSourceConfig {
  s.Bucket = &v
  return s
}

func (s *GetTableResponseBodyResultDataSourceConfig) SetEndpoint(v string) *GetTableResponseBodyResultDataSourceConfig {
  s.Endpoint = &v
  return s
}

func (s *GetTableResponseBodyResultDataSourceConfig) SetNamespace(v string) *GetTableResponseBodyResultDataSourceConfig {
  s.Namespace = &v
  return s
}

func (s *GetTableResponseBodyResultDataSourceConfig) SetOssPath(v string) *GetTableResponseBodyResultDataSourceConfig {
  s.OssPath = &v
  return s
}

func (s *GetTableResponseBodyResultDataSourceConfig) SetPartition(v string) *GetTableResponseBodyResultDataSourceConfig {
  s.Partition = &v
  return s
}

func (s *GetTableResponseBodyResultDataSourceConfig) SetPath(v string) *GetTableResponseBodyResultDataSourceConfig {
  s.Path = &v
  return s
}

func (s *GetTableResponseBodyResultDataSourceConfig) SetProject(v string) *GetTableResponseBodyResultDataSourceConfig {
  s.Project = &v
  return s
}

func (s *GetTableResponseBodyResultDataSourceConfig) SetTable(v string) *GetTableResponseBodyResultDataSourceConfig {
  s.Table = &v
  return s
}

type GetTableResponseBodyResultDataProcessConfig struct     {
  // The destination field.
  // 
  // example:
  // 
  // source_image_vector
  DstField *string `json:"dstField,omitempty" xml:"dstField,omitempty"`
  // The method used to process the field. Valid values: copy and vectorize. A value of copy indicates that the value of the source field is copied to the destination field. A value of vectorize indicates that the value of the source field is vectorized by a vectorization model and the output vector is stored in the destination field.
  // 
  // example:
  // 
  // vectorize
  Operator *string `json:"operator,omitempty" xml:"operator,omitempty"`
  // The information about the model.
  Params *GetTableResponseBodyResultDataProcessConfigParams `json:"params,omitempty" xml:"params,omitempty" type:"Struct"`
  // The source field.
  // 
  // example:
  // 
  // source_image
  SrcField *string `json:"srcField,omitempty" xml:"srcField,omitempty"`
}

func (s GetTableResponseBodyResultDataProcessConfig) String() string {
  return tea.Prettify(s)
}

func (s GetTableResponseBodyResultDataProcessConfig) GoString() string {
  return s.String()
}

func (s *GetTableResponseBodyResultDataProcessConfig) SetDstField(v string) *GetTableResponseBodyResultDataProcessConfig {
  s.DstField = &v
  return s
}

func (s *GetTableResponseBodyResultDataProcessConfig) SetOperator(v string) *GetTableResponseBodyResultDataProcessConfig {
  s.Operator = &v
  return s
}

func (s *GetTableResponseBodyResultDataProcessConfig) SetParams(v *GetTableResponseBodyResultDataProcessConfigParams) *GetTableResponseBodyResultDataProcessConfig {
  s.Params = v
  return s
}

func (s *GetTableResponseBodyResultDataProcessConfig) SetSrcField(v string) *GetTableResponseBodyResultDataProcessConfig {
  s.SrcField = &v
  return s
}

type GetTableResponseBodyResultDataProcessConfigParams struct {
  // The source of the data to be vectorized.
  SrcFieldConfig *GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig `json:"srcFieldConfig,omitempty" xml:"srcFieldConfig,omitempty" type:"Struct"`
  // The data type.
  // 
  // example:
  // 
  // image
  VectorModal *string `json:"vectorModal,omitempty" xml:"vectorModal,omitempty"`
  // The vectorization model.
  // 
  // example:
  // 
  // clip
  VectorModel *string `json:"vectorModel,omitempty" xml:"vectorModel,omitempty"`
}

func (s GetTableResponseBodyResultDataProcessConfigParams) String() string {
  return tea.Prettify(s)
}

func (s GetTableResponseBodyResultDataProcessConfigParams) GoString() string {
  return s.String()
}

func (s *GetTableResponseBodyResultDataProcessConfigParams) SetSrcFieldConfig(v *GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig) *GetTableResponseBodyResultDataProcessConfigParams {
  s.SrcFieldConfig = v
  return s
}

func (s *GetTableResponseBodyResultDataProcessConfigParams) SetVectorModal(v string) *GetTableResponseBodyResultDataProcessConfigParams {
  s.VectorModal = &v
  return s
}

func (s *GetTableResponseBodyResultDataProcessConfigParams) SetVectorModel(v string) *GetTableResponseBodyResultDataProcessConfigParams {
  s.VectorModel = &v
  return s
}

type GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig struct {
  // OSS Bucket
  // 
  // example:
  // 
  // test
  OssBucket *string `json:"ossBucket,omitempty" xml:"ossBucket,omitempty"`
  // The Object Storage Service (OSS) endpoint.
  // 
  // example:
  // 
  // oss-cn-hangzhou-internal.aliyuncs.com
  OssEndpoint *string `json:"ossEndpoint,omitempty" xml:"ossEndpoint,omitempty"`
  // The ID of the Alibaba Cloud account.
  // 
  // example:
  // 
  // uid
  Uid *string `json:"uid,omitempty" xml:"uid,omitempty"`
}

func (s GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig) String() string {
  return tea.Prettify(s)
}

func (s GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig) GoString() string {
  return s.String()
}

func (s *GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig) SetOssBucket(v string) *GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig {
  s.OssBucket = &v
  return s
}

func (s *GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig) SetOssEndpoint(v string) *GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig {
  s.OssEndpoint = &v
  return s
}

func (s *GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig) SetUid(v string) *GetTableResponseBodyResultDataProcessConfigParamsSrcFieldConfig {
  s.Uid = &v
  return s
}

type GetTableResponse struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  StatusCode *int32 `json:"statusCode,omitempty" xml:"statusCode,omitempty"`
  Body *GetTableResponseBody `json:"body,omitempty" xml:"body,omitempty"`
}

func (s GetTableResponse) String() string {
  return tea.Prettify(s)
}

func (s GetTableResponse) GoString() string {
  return s.String()
}

func (s *GetTableResponse) SetHeaders(v map[string]*string) *GetTableResponse {
  s.Headers = v
  return s
}

func (s *GetTableResponse) SetStatusCode(v int32) *GetTableResponse {
  s.StatusCode = &v
  return s
}

func (s *GetTableResponse) SetBody(v *GetTableResponseBody) *GetTableResponse {
  s.Body = v
  return s
}

// Description:
// 
// 创建表
type CreateTableRequest struct {
  // The index name.
  // 
  // example:
  // 
  // index_1
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // The number of data shards.
  // 
  // example:
  // 
  // 1
  PartitionCount *int32 `json:"partitionCount,omitempty" xml:"partitionCount,omitempty"`
  // The primary key field.
  // 
  // example:
  // 
  // id
  PrimaryKey *string `json:"primaryKey,omitempty" xml:"primaryKey,omitempty"`
  // The fields.
  FieldSchema map[string]*string `json:"fieldSchema,omitempty" xml:"fieldSchema,omitempty"`
  // The index schema.
  VectorIndex []*CreateTableRequestVectorIndex `json:"vectorIndex,omitempty" xml:"vectorIndex,omitempty" type:"Repeated"`
  // The number of resources used for data update.
  // 
  // example:
  // 
  // 1
  DataProcessorCount *int32 `json:"dataProcessorCount,omitempty" xml:"dataProcessorCount,omitempty"`
  // The configurations about field processing.
  DataProcessConfig []*CreateTableRequestDataProcessConfig `json:"dataProcessConfig,omitempty" xml:"dataProcessConfig,omitempty" type:"Repeated"`
  // The configurations of the data source.
  DataSource *CreateTableRequestDataSource `json:"dataSource,omitempty" xml:"dataSource,omitempty" type:"Struct"`
  // Specifies whether to perform only a dry run, without performing the actual request. The system only checks the validity of the data source. Valid values:true,false
  // 
  // example:
  // 
  // true
  DryRun *bool `json:"dryRun,omitempty" xml:"dryRun,omitempty"`
}

func (s CreateTableRequest) String() string {
  return tea.Prettify(s)
}

func (s CreateTableRequest) GoString() string {
  return s.String()
}

func (s *CreateTableRequest) SetName(v string) *CreateTableRequest {
  s.Name = &v
  return s
}

func (s *CreateTableRequest) SetPartitionCount(v int32) *CreateTableRequest {
  s.PartitionCount = &v
  return s
}

func (s *CreateTableRequest) SetPrimaryKey(v string) *CreateTableRequest {
  s.PrimaryKey = &v
  return s
}

func (s *CreateTableRequest) SetFieldSchema(v map[string]*string) *CreateTableRequest {
  s.FieldSchema = v
  return s
}

func (s *CreateTableRequest) SetVectorIndex(v []*CreateTableRequestVectorIndex) *CreateTableRequest {
  s.VectorIndex = v
  return s
}

func (s *CreateTableRequest) SetDataProcessorCount(v int32) *CreateTableRequest {
  s.DataProcessorCount = &v
  return s
}

func (s *CreateTableRequest) SetDataProcessConfig(v []*CreateTableRequestDataProcessConfig) *CreateTableRequest {
  s.DataProcessConfig = v
  return s
}

func (s *CreateTableRequest) SetDataSource(v *CreateTableRequestDataSource) *CreateTableRequest {
  s.DataSource = v
  return s
}

func (s *CreateTableRequest) SetDryRun(v bool) *CreateTableRequest {
  s.DryRun = &v
  return s
}

type CreateTableRequestVectorIndex struct     {
  // The configurations of the index schema.
  AdvanceParams *CreateTableRequestVectorIndexAdvanceParams `json:"advanceParams,omitempty" xml:"advanceParams,omitempty" type:"Struct"`
  // The dimension of the vector.
  // 
  // example:
  // 
  // 128
  Dimension *string `json:"dimension,omitempty" xml:"dimension,omitempty"`
  // The distance type.
  // 
  // example:
  // 
  // SquaredEuclidean
  DistanceType *string `json:"distanceType,omitempty" xml:"distanceType,omitempty"`
  // The name of the index schema.
  // 
  // example:
  // 
  // case_index
  IndexName *string `json:"indexName,omitempty" xml:"indexName,omitempty"`
  // The namespace field.
  // 
  // example:
  // 
  // namespace
  Namespace *string `json:"namespace,omitempty" xml:"namespace,omitempty"`
  // The field that stores the indexes of the elements in sparse vectors.
  // 
  // example:
  // 
  // sparse_indices
  SparseIndexField *string `json:"sparseIndexField,omitempty" xml:"sparseIndexField,omitempty"`
  // The field that stores the elements in sparse vectors.
  // 
  // example:
  // 
  // sparse_values
  SparseValueField *string `json:"sparseValueField,omitempty" xml:"sparseValueField,omitempty"`
  // The vector field.
  // 
  // example:
  // 
  // source_image_vector
  VectorField *string `json:"vectorField,omitempty" xml:"vectorField,omitempty"`
  // The vector retrieval algorithm.
  // 
  // example:
  // 
  // Qc
  VectorIndexType *string `json:"vectorIndexType,omitempty" xml:"vectorIndexType,omitempty"`
}

func (s CreateTableRequestVectorIndex) String() string {
  return tea.Prettify(s)
}

func (s CreateTableRequestVectorIndex) GoString() string {
  return s.String()
}

func (s *CreateTableRequestVectorIndex) SetAdvanceParams(v *CreateTableRequestVectorIndexAdvanceParams) *CreateTableRequestVectorIndex {
  s.AdvanceParams = v
  return s
}

func (s *CreateTableRequestVectorIndex) SetDimension(v string) *CreateTableRequestVectorIndex {
  s.Dimension = &v
  return s
}

func (s *CreateTableRequestVectorIndex) SetDistanceType(v string) *CreateTableRequestVectorIndex {
  s.DistanceType = &v
  return s
}

func (s *CreateTableRequestVectorIndex) SetIndexName(v string) *CreateTableRequestVectorIndex {
  s.IndexName = &v
  return s
}

func (s *CreateTableRequestVectorIndex) SetNamespace(v string) *CreateTableRequestVectorIndex {
  s.Namespace = &v
  return s
}

func (s *CreateTableRequestVectorIndex) SetSparseIndexField(v string) *CreateTableRequestVectorIndex {
  s.SparseIndexField = &v
  return s
}

func (s *CreateTableRequestVectorIndex) SetSparseValueField(v string) *CreateTableRequestVectorIndex {
  s.SparseValueField = &v
  return s
}

func (s *CreateTableRequestVectorIndex) SetVectorField(v string) *CreateTableRequestVectorIndex {
  s.VectorField = &v
  return s
}

func (s *CreateTableRequestVectorIndex) SetVectorIndexType(v string) *CreateTableRequestVectorIndex {
  s.VectorIndexType = &v
  return s
}

type CreateTableRequestVectorIndexAdvanceParams struct {
  // The index building parameters.
  // 
  // example:
  // 
  // {}
  BuildIndexParams *string `json:"buildIndexParams,omitempty" xml:"buildIndexParams,omitempty"`
  // The threshold for linear building.
  // 
  // example:
  // 
  // 5000
  LinearBuildThreshold *string `json:"linearBuildThreshold,omitempty" xml:"linearBuildThreshold,omitempty"`
  // The minimum number of retrieved candidate sets.
  // 
  // example:
  // 
  // 20000
  MinScanDocCnt *string `json:"minScanDocCnt,omitempty" xml:"minScanDocCnt,omitempty"`
  // The index retrieval parameters.
  // 
  // example:
  // 
  // {}
  SearchIndexParams *string `json:"searchIndexParams,omitempty" xml:"searchIndexParams,omitempty"`
}

func (s CreateTableRequestVectorIndexAdvanceParams) String() string {
  return tea.Prettify(s)
}

func (s CreateTableRequestVectorIndexAdvanceParams) GoString() string {
  return s.String()
}

func (s *CreateTableRequestVectorIndexAdvanceParams) SetBuildIndexParams(v string) *CreateTableRequestVectorIndexAdvanceParams {
  s.BuildIndexParams = &v
  return s
}

func (s *CreateTableRequestVectorIndexAdvanceParams) SetLinearBuildThreshold(v string) *CreateTableRequestVectorIndexAdvanceParams {
  s.LinearBuildThreshold = &v
  return s
}

func (s *CreateTableRequestVectorIndexAdvanceParams) SetMinScanDocCnt(v string) *CreateTableRequestVectorIndexAdvanceParams {
  s.MinScanDocCnt = &v
  return s
}

func (s *CreateTableRequestVectorIndexAdvanceParams) SetSearchIndexParams(v string) *CreateTableRequestVectorIndexAdvanceParams {
  s.SearchIndexParams = &v
  return s
}

type CreateTableRequestDataProcessConfig struct     {
  // The destination field.
  // 
  // example:
  // 
  // source_image_vector
  DstField *string `json:"dstField,omitempty" xml:"dstField,omitempty"`
  // The method used to process the field. Valid values: copy and vectorize. A value of copy specifies that the value of the source field is copied to the destination field. A value of vectorize specifies that the value of the source field is vectorized by a vectorization model and the output vector is stored in the destination field.
  // 
  // example:
  // 
  // vectorize
  Operator *string `json:"operator,omitempty" xml:"operator,omitempty"`
  // The information about the model.
  Params *CreateTableRequestDataProcessConfigParams `json:"params,omitempty" xml:"params,omitempty" type:"Struct"`
  // The source field.
  // 
  // example:
  // 
  // source_image
  SrcField *string `json:"srcField,omitempty" xml:"srcField,omitempty"`
}

func (s CreateTableRequestDataProcessConfig) String() string {
  return tea.Prettify(s)
}

func (s CreateTableRequestDataProcessConfig) GoString() string {
  return s.String()
}

func (s *CreateTableRequestDataProcessConfig) SetDstField(v string) *CreateTableRequestDataProcessConfig {
  s.DstField = &v
  return s
}

func (s *CreateTableRequestDataProcessConfig) SetOperator(v string) *CreateTableRequestDataProcessConfig {
  s.Operator = &v
  return s
}

func (s *CreateTableRequestDataProcessConfig) SetParams(v *CreateTableRequestDataProcessConfigParams) *CreateTableRequestDataProcessConfig {
  s.Params = v
  return s
}

func (s *CreateTableRequestDataProcessConfig) SetSrcField(v string) *CreateTableRequestDataProcessConfig {
  s.SrcField = &v
  return s
}

type CreateTableRequestDataProcessConfigParams struct {
  // The source of the data to be vectorized.
  SrcFieldConfig *CreateTableRequestDataProcessConfigParamsSrcFieldConfig `json:"srcFieldConfig,omitempty" xml:"srcFieldConfig,omitempty" type:"Struct"`
  // The data type.
  // 
  // example:
  // 
  // image
  VectorModal *string `json:"vectorModal,omitempty" xml:"vectorModal,omitempty"`
  // The vectorization model.
  // 
  // example:
  // 
  // clip
  VectorModel *string `json:"vectorModel,omitempty" xml:"vectorModel,omitempty"`
}

func (s CreateTableRequestDataProcessConfigParams) String() string {
  return tea.Prettify(s)
}

func (s CreateTableRequestDataProcessConfigParams) GoString() string {
  return s.String()
}

func (s *CreateTableRequestDataProcessConfigParams) SetSrcFieldConfig(v *CreateTableRequestDataProcessConfigParamsSrcFieldConfig) *CreateTableRequestDataProcessConfigParams {
  s.SrcFieldConfig = v
  return s
}

func (s *CreateTableRequestDataProcessConfigParams) SetVectorModal(v string) *CreateTableRequestDataProcessConfigParams {
  s.VectorModal = &v
  return s
}

func (s *CreateTableRequestDataProcessConfigParams) SetVectorModel(v string) *CreateTableRequestDataProcessConfigParams {
  s.VectorModel = &v
  return s
}

type CreateTableRequestDataProcessConfigParamsSrcFieldConfig struct {
  // The OSS bucket.
  // 
  // example:
  // 
  // test
  OssBucket *string `json:"ossBucket,omitempty" xml:"ossBucket,omitempty"`
  // The OSS endpoint.
  // 
  // example:
  // 
  // oss-cn-hangzhou-internal.aliyuncs.com
  OssEndpoint *string `json:"ossEndpoint,omitempty" xml:"ossEndpoint,omitempty"`
  // The ID of the Alibaba Cloud account.
  // 
  // example:
  // 
  // uid
  Uid *string `json:"uid,omitempty" xml:"uid,omitempty"`
}

func (s CreateTableRequestDataProcessConfigParamsSrcFieldConfig) String() string {
  return tea.Prettify(s)
}

func (s CreateTableRequestDataProcessConfigParamsSrcFieldConfig) GoString() string {
  return s.String()
}

func (s *CreateTableRequestDataProcessConfigParamsSrcFieldConfig) SetOssBucket(v string) *CreateTableRequestDataProcessConfigParamsSrcFieldConfig {
  s.OssBucket = &v
  return s
}

func (s *CreateTableRequestDataProcessConfigParamsSrcFieldConfig) SetOssEndpoint(v string) *CreateTableRequestDataProcessConfigParamsSrcFieldConfig {
  s.OssEndpoint = &v
  return s
}

func (s *CreateTableRequestDataProcessConfigParamsSrcFieldConfig) SetUid(v string) *CreateTableRequestDataProcessConfigParamsSrcFieldConfig {
  s.Uid = &v
  return s
}

type CreateTableRequestDataSource struct {
  // Specifies whether to automatically rebuild the index.
  // 
  // example:
  // 
  // true
  AutoBuildIndex *bool `json:"autoBuildIndex,omitempty" xml:"autoBuildIndex,omitempty"`
  // The configurations of the data source.
  Config *CreateTableRequestDataSourceConfig `json:"config,omitempty" xml:"config,omitempty" type:"Struct"`
  // The start timestamp from which incremental data is retrieved.
  // 
  // example:
  // 
  // 1715160176
  DataTimeSec *int32 `json:"dataTimeSec,omitempty" xml:"dataTimeSec,omitempty"`
  // The data source type. Valid values: odps, swift, and oss.
  // 
  // example:
  // 
  // odps
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
}

func (s CreateTableRequestDataSource) String() string {
  return tea.Prettify(s)
}

func (s CreateTableRequestDataSource) GoString() string {
  return s.String()
}

func (s *CreateTableRequestDataSource) SetAutoBuildIndex(v bool) *CreateTableRequestDataSource {
  s.AutoBuildIndex = &v
  return s
}

func (s *CreateTableRequestDataSource) SetConfig(v *CreateTableRequestDataSourceConfig) *CreateTableRequestDataSource {
  s.Config = v
  return s
}

func (s *CreateTableRequestDataSource) SetDataTimeSec(v int32) *CreateTableRequestDataSource {
  s.DataTimeSec = &v
  return s
}

func (s *CreateTableRequestDataSource) SetType(v string) *CreateTableRequestDataSource {
  s.Type = &v
  return s
}

type CreateTableRequestDataSourceConfig struct {
  // The AccessKey ID of the MaxCompute data source.
  // 
  // example:
  // 
  // ak
  AccessKey *string `json:"accessKey,omitempty" xml:"accessKey,omitempty"`
  // The AccessKey secret of the MaxCompute data source.
  // 
  // example:
  // 
  // as
  AccessSecret *string `json:"accessSecret,omitempty" xml:"accessSecret,omitempty"`
  // The OSS bucket.
  // 
  // example:
  // 
  // antsys-flytest-ci
  Bucket *string `json:"bucket,omitempty" xml:"bucket,omitempty"`
  Catalog *string `json:"catalog,omitempty" xml:"catalog,omitempty"`
  Database *string `json:"database,omitempty" xml:"database,omitempty"`
  // The endpoint of the MaxCompute data source.
  // 
  // example:
  // 
  // http://service.cn-hangzhou.maxcompute.aliyun-inc.com/api
  Endpoint *string `json:"endpoint,omitempty" xml:"endpoint,omitempty"`
  // The Object Storage Service (OSS) path.
  // 
  // example:
  // 
  // oss://opensearch
  OssPath *string `json:"ossPath,omitempty" xml:"ossPath,omitempty"`
  // The partition in the MaxCompute table. This parameter is required if type is set to odps.
  // 
  // example:
  // 
  // ds=20220713
  Partition *string `json:"partition,omitempty" xml:"partition,omitempty"`
  // The name of the MaxCompute project that is used as the data source.
  // 
  // example:
  // 
  // project_20210220122847_3218
  Project *string `json:"project,omitempty" xml:"project,omitempty"`
  // The name of the MaxCompute table that is used as the data source.
  // 
  // example:
  // 
  // test56
  Table *string `json:"table,omitempty" xml:"table,omitempty"`
  Tag *string `json:"tag,omitempty" xml:"tag,omitempty"`
}

func (s CreateTableRequestDataSourceConfig) String() string {
  return tea.Prettify(s)
}

func (s CreateTableRequestDataSourceConfig) GoString() string {
  return s.String()
}

func (s *CreateTableRequestDataSourceConfig) SetAccessKey(v string) *CreateTableRequestDataSourceConfig {
  s.AccessKey = &v
  return s
}

func (s *CreateTableRequestDataSourceConfig) SetAccessSecret(v string) *CreateTableRequestDataSourceConfig {
  s.AccessSecret = &v
  return s
}

func (s *CreateTableRequestDataSourceConfig) SetBucket(v string) *CreateTableRequestDataSourceConfig {
  s.Bucket = &v
  return s
}

func (s *CreateTableRequestDataSourceConfig) SetCatalog(v string) *CreateTableRequestDataSourceConfig {
  s.Catalog = &v
  return s
}

func (s *CreateTableRequestDataSourceConfig) SetDatabase(v string) *CreateTableRequestDataSourceConfig {
  s.Database = &v
  return s
}

func (s *CreateTableRequestDataSourceConfig) SetEndpoint(v string) *CreateTableRequestDataSourceConfig {
  s.Endpoint = &v
  return s
}

func (s *CreateTableRequestDataSourceConfig) SetOssPath(v string) *CreateTableRequestDataSourceConfig {
  s.OssPath = &v
  return s
}

func (s *CreateTableRequestDataSourceConfig) SetPartition(v string) *CreateTableRequestDataSourceConfig {
  s.Partition = &v
  return s
}

func (s *CreateTableRequestDataSourceConfig) SetProject(v string) *CreateTableRequestDataSourceConfig {
  s.Project = &v
  return s
}

func (s *CreateTableRequestDataSourceConfig) SetTable(v string) *CreateTableRequestDataSourceConfig {
  s.Table = &v
  return s
}

func (s *CreateTableRequestDataSourceConfig) SetTag(v string) *CreateTableRequestDataSourceConfig {
  s.Tag = &v
  return s
}

type CreateTableResponseBody struct {
  // id of request
  // 
  // example:
  // 
  // 2AE63638-5420-56DC-BF59-37D8174039A0
  RequestId *string `json:"requestId,omitempty" xml:"requestId,omitempty"`
  // Map
  // 
  // example:
  // 
  // {}
  Result map[string]interface{} `json:"result,omitempty" xml:"result,omitempty"`
}

func (s CreateTableResponseBody) String() string {
  return tea.Prettify(s)
}

func (s CreateTableResponseBody) GoString() string {
  return s.String()
}

func (s *CreateTableResponseBody) SetRequestId(v string) *CreateTableResponseBody {
  s.RequestId = &v
  return s
}

func (s *CreateTableResponseBody) SetResult(v map[string]interface{}) *CreateTableResponseBody {
  s.Result = v
  return s
}

type CreateTableResponse struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  StatusCode *int32 `json:"statusCode,omitempty" xml:"statusCode,omitempty"`
  Body *CreateTableResponseBody `json:"body,omitempty" xml:"body,omitempty"`
}

func (s CreateTableResponse) String() string {
  return tea.Prettify(s)
}

func (s CreateTableResponse) GoString() string {
  return s.String()
}

func (s *CreateTableResponse) SetHeaders(v map[string]*string) *CreateTableResponse {
  s.Headers = v
  return s
}

func (s *CreateTableResponse) SetStatusCode(v int32) *CreateTableResponse {
  s.StatusCode = &v
  return s
}

func (s *CreateTableResponse) SetBody(v *CreateTableResponseBody) *CreateTableResponse {
  s.Body = v
  return s
}

// Description:
// 
// 修改表.
type ModifyTableRequest struct {
  // The configurations about field processing.
  DataProcessConfig []*ModifyTableRequestDataProcessConfig `json:"dataProcessConfig,omitempty" xml:"dataProcessConfig,omitempty" type:"Repeated"`
  // The configurations of the data source.
  DataSource *ModifyTableRequestDataSource `json:"dataSource,omitempty" xml:"dataSource,omitempty" type:"Struct"`
  // The fields.
  FieldSchema map[string]*string `json:"fieldSchema,omitempty" xml:"fieldSchema,omitempty"`
  // The number of data shards.
  // 
  // example:
  // 
  // 1
  PartitionCount *int32 `json:"partitionCount,omitempty" xml:"partitionCount,omitempty"`
  // The primary key field.
  // 
  // example:
  // 
  // id
  PrimaryKey *string `json:"primaryKey,omitempty" xml:"primaryKey,omitempty"`
  // The instance schema. If this parameter is specified, the parameters about the index are not required.
  // 
  // example:
  // 
  // {}
  RawSchema *string `json:"rawSchema,omitempty" xml:"rawSchema,omitempty"`
  // The index schema.
  VectorIndex []*ModifyTableRequestVectorIndex `json:"vectorIndex,omitempty" xml:"vectorIndex,omitempty" type:"Repeated"`
  // Specifies whether to perform only a dry run, without performing the actual request. The system only checks the validity of the data source. Valid values:true,false
  // 
  // example:
  // 
  // true
  DryRun *bool `json:"dryRun,omitempty" xml:"dryRun,omitempty"`
}

func (s ModifyTableRequest) String() string {
  return tea.Prettify(s)
}

func (s ModifyTableRequest) GoString() string {
  return s.String()
}

func (s *ModifyTableRequest) SetDataProcessConfig(v []*ModifyTableRequestDataProcessConfig) *ModifyTableRequest {
  s.DataProcessConfig = v
  return s
}

func (s *ModifyTableRequest) SetDataSource(v *ModifyTableRequestDataSource) *ModifyTableRequest {
  s.DataSource = v
  return s
}

func (s *ModifyTableRequest) SetFieldSchema(v map[string]*string) *ModifyTableRequest {
  s.FieldSchema = v
  return s
}

func (s *ModifyTableRequest) SetPartitionCount(v int32) *ModifyTableRequest {
  s.PartitionCount = &v
  return s
}

func (s *ModifyTableRequest) SetPrimaryKey(v string) *ModifyTableRequest {
  s.PrimaryKey = &v
  return s
}

func (s *ModifyTableRequest) SetRawSchema(v string) *ModifyTableRequest {
  s.RawSchema = &v
  return s
}

func (s *ModifyTableRequest) SetVectorIndex(v []*ModifyTableRequestVectorIndex) *ModifyTableRequest {
  s.VectorIndex = v
  return s
}

func (s *ModifyTableRequest) SetDryRun(v bool) *ModifyTableRequest {
  s.DryRun = &v
  return s
}

type ModifyTableRequestDataProcessConfig struct     {
  // The destination field.
  // 
  // example:
  // 
  // source_image_vector
  DstField *string `json:"dstField,omitempty" xml:"dstField,omitempty"`
  // The method used to process the field. Valid values: copy and vectorize. A value of copy specifies that the value of the source field is copied to the destination field. A value of vectorize specifies that the value of the source field is vectorized by a vectorization model and the output vector is stored in the destination field.
  // 
  // example:
  // 
  // vectorize
  Operator *string `json:"operator,omitempty" xml:"operator,omitempty"`
  // The information about the model.
  Params *ModifyTableRequestDataProcessConfigParams `json:"params,omitempty" xml:"params,omitempty" type:"Struct"`
  // The source field.
  // 
  // example:
  // 
  // source_image
  SrcField *string `json:"srcField,omitempty" xml:"srcField,omitempty"`
}

func (s ModifyTableRequestDataProcessConfig) String() string {
  return tea.Prettify(s)
}

func (s ModifyTableRequestDataProcessConfig) GoString() string {
  return s.String()
}

func (s *ModifyTableRequestDataProcessConfig) SetDstField(v string) *ModifyTableRequestDataProcessConfig {
  s.DstField = &v
  return s
}

func (s *ModifyTableRequestDataProcessConfig) SetOperator(v string) *ModifyTableRequestDataProcessConfig {
  s.Operator = &v
  return s
}

func (s *ModifyTableRequestDataProcessConfig) SetParams(v *ModifyTableRequestDataProcessConfigParams) *ModifyTableRequestDataProcessConfig {
  s.Params = v
  return s
}

func (s *ModifyTableRequestDataProcessConfig) SetSrcField(v string) *ModifyTableRequestDataProcessConfig {
  s.SrcField = &v
  return s
}

type ModifyTableRequestDataProcessConfigParams struct {
  // The source of the data to be vectorized.
  SrcFieldConfig *ModifyTableRequestDataProcessConfigParamsSrcFieldConfig `json:"srcFieldConfig,omitempty" xml:"srcFieldConfig,omitempty" type:"Struct"`
  // The data type.
  // 
  // example:
  // 
  // image
  VectorModal *string `json:"vectorModal,omitempty" xml:"vectorModal,omitempty"`
  // The vectorization model.
  // 
  // example:
  // 
  // clip
  VectorModel *string `json:"vectorModel,omitempty" xml:"vectorModel,omitempty"`
}

func (s ModifyTableRequestDataProcessConfigParams) String() string {
  return tea.Prettify(s)
}

func (s ModifyTableRequestDataProcessConfigParams) GoString() string {
  return s.String()
}

func (s *ModifyTableRequestDataProcessConfigParams) SetSrcFieldConfig(v *ModifyTableRequestDataProcessConfigParamsSrcFieldConfig) *ModifyTableRequestDataProcessConfigParams {
  s.SrcFieldConfig = v
  return s
}

func (s *ModifyTableRequestDataProcessConfigParams) SetVectorModal(v string) *ModifyTableRequestDataProcessConfigParams {
  s.VectorModal = &v
  return s
}

func (s *ModifyTableRequestDataProcessConfigParams) SetVectorModel(v string) *ModifyTableRequestDataProcessConfigParams {
  s.VectorModel = &v
  return s
}

type ModifyTableRequestDataProcessConfigParamsSrcFieldConfig struct {
  // The name of the OSS bucket.
  // 
  // example:
  // 
  // test
  OssBucket *string `json:"ossBucket,omitempty" xml:"ossBucket,omitempty"`
  // The OSS endpoint.
  // 
  // example:
  // 
  // oss-cn-hangzhou-internal.aliyuncs.com
  OssEndpoint *string `json:"ossEndpoint,omitempty" xml:"ossEndpoint,omitempty"`
  // The ID of the Alibaba Cloud account.
  // 
  // example:
  // 
  // uid
  Uid *string `json:"uid,omitempty" xml:"uid,omitempty"`
}

func (s ModifyTableRequestDataProcessConfigParamsSrcFieldConfig) String() string {
  return tea.Prettify(s)
}

func (s ModifyTableRequestDataProcessConfigParamsSrcFieldConfig) GoString() string {
  return s.String()
}

func (s *ModifyTableRequestDataProcessConfigParamsSrcFieldConfig) SetOssBucket(v string) *ModifyTableRequestDataProcessConfigParamsSrcFieldConfig {
  s.OssBucket = &v
  return s
}

func (s *ModifyTableRequestDataProcessConfigParamsSrcFieldConfig) SetOssEndpoint(v string) *ModifyTableRequestDataProcessConfigParamsSrcFieldConfig {
  s.OssEndpoint = &v
  return s
}

func (s *ModifyTableRequestDataProcessConfigParamsSrcFieldConfig) SetUid(v string) *ModifyTableRequestDataProcessConfigParamsSrcFieldConfig {
  s.Uid = &v
  return s
}

type ModifyTableRequestDataSource struct {
  // Specifies whether to automatically rebuild the index.
  // 
  // example:
  // 
  // true
  AutoBuildIndex *bool `json:"autoBuildIndex,omitempty" xml:"autoBuildIndex,omitempty"`
  // The configurations of the data source.
  Config *ModifyTableRequestDataSourceConfig `json:"config,omitempty" xml:"config,omitempty" type:"Struct"`
  // The start timestamp from which incremental data is retrieved.
  // 
  // example:
  // 
  // 1715160176
  DataTimeSec *int32 `json:"dataTimeSec,omitempty" xml:"dataTimeSec,omitempty"`
}

func (s ModifyTableRequestDataSource) String() string {
  return tea.Prettify(s)
}

func (s ModifyTableRequestDataSource) GoString() string {
  return s.String()
}

func (s *ModifyTableRequestDataSource) SetAutoBuildIndex(v bool) *ModifyTableRequestDataSource {
  s.AutoBuildIndex = &v
  return s
}

func (s *ModifyTableRequestDataSource) SetConfig(v *ModifyTableRequestDataSourceConfig) *ModifyTableRequestDataSource {
  s.Config = v
  return s
}

func (s *ModifyTableRequestDataSource) SetDataTimeSec(v int32) *ModifyTableRequestDataSource {
  s.DataTimeSec = &v
  return s
}

type ModifyTableRequestDataSourceConfig struct {
  // The AccessKey ID of the MaxCompute data source.
  // 
  // example:
  // 
  // AK
  AccessKey *string `json:"accessKey,omitempty" xml:"accessKey,omitempty"`
  // The AccessKey secret of the MaxCompute data source.
  // 
  // example:
  // 
  // AS
  AccessSecret *string `json:"accessSecret,omitempty" xml:"accessSecret,omitempty"`
  // The name of the OSS bucket.
  // 
  // example:
  // 
  // antsys-shujiang-osstest
  Bucket *string `json:"bucket,omitempty" xml:"bucket,omitempty"`
  Catalog *string `json:"catalog,omitempty" xml:"catalog,omitempty"`
  Database *string `json:"database,omitempty" xml:"database,omitempty"`
  // The endpoint of the MaxCompute data source.
  // 
  // example:
  // 
  // http://service.cn-hangzhou.maxcompute.aliyun-inc.com/api
  Endpoint *string `json:"endpoint,omitempty" xml:"endpoint,omitempty"`
  // The path of the Object Storage Service (OSS) object.
  // 
  // example:
  // 
  // oss://opensearch
  OssPath *string `json:"ossPath,omitempty" xml:"ossPath,omitempty"`
  // The partition in the MaxCompute table.
  // 
  // example:
  // 
  // ds=20231220
  Partition *string `json:"partition,omitempty" xml:"partition,omitempty"`
  // The name of the MaxCompute project that is used as the data source.
  // 
  // example:
  // 
  // yw_dw_rpt
  Project *string `json:"project,omitempty" xml:"project,omitempty"`
  // The name of the MaxCompute table that is used as the data source.
  // 
  // example:
  // 
  // behavior
  Table *string `json:"table,omitempty" xml:"table,omitempty"`
  Tag *string `json:"tag,omitempty" xml:"tag,omitempty"`
}

func (s ModifyTableRequestDataSourceConfig) String() string {
  return tea.Prettify(s)
}

func (s ModifyTableRequestDataSourceConfig) GoString() string {
  return s.String()
}

func (s *ModifyTableRequestDataSourceConfig) SetAccessKey(v string) *ModifyTableRequestDataSourceConfig {
  s.AccessKey = &v
  return s
}

func (s *ModifyTableRequestDataSourceConfig) SetAccessSecret(v string) *ModifyTableRequestDataSourceConfig {
  s.AccessSecret = &v
  return s
}

func (s *ModifyTableRequestDataSourceConfig) SetBucket(v string) *ModifyTableRequestDataSourceConfig {
  s.Bucket = &v
  return s
}

func (s *ModifyTableRequestDataSourceConfig) SetCatalog(v string) *ModifyTableRequestDataSourceConfig {
  s.Catalog = &v
  return s
}

func (s *ModifyTableRequestDataSourceConfig) SetDatabase(v string) *ModifyTableRequestDataSourceConfig {
  s.Database = &v
  return s
}

func (s *ModifyTableRequestDataSourceConfig) SetEndpoint(v string) *ModifyTableRequestDataSourceConfig {
  s.Endpoint = &v
  return s
}

func (s *ModifyTableRequestDataSourceConfig) SetOssPath(v string) *ModifyTableRequestDataSourceConfig {
  s.OssPath = &v
  return s
}

func (s *ModifyTableRequestDataSourceConfig) SetPartition(v string) *ModifyTableRequestDataSourceConfig {
  s.Partition = &v
  return s
}

func (s *ModifyTableRequestDataSourceConfig) SetProject(v string) *ModifyTableRequestDataSourceConfig {
  s.Project = &v
  return s
}

func (s *ModifyTableRequestDataSourceConfig) SetTable(v string) *ModifyTableRequestDataSourceConfig {
  s.Table = &v
  return s
}

func (s *ModifyTableRequestDataSourceConfig) SetTag(v string) *ModifyTableRequestDataSourceConfig {
  s.Tag = &v
  return s
}

type ModifyTableRequestVectorIndex struct     {
  // The configurations of the index schema.
  AdvanceParams *ModifyTableRequestVectorIndexAdvanceParams `json:"advanceParams,omitempty" xml:"advanceParams,omitempty" type:"Struct"`
  // The dimension of the vector.
  // 
  // example:
  // 
  // 128
  Dimension *string `json:"dimension,omitempty" xml:"dimension,omitempty"`
  // The distance type.
  // 
  // example:
  // 
  // SquaredEuclidean
  DistanceType *string `json:"distanceType,omitempty" xml:"distanceType,omitempty"`
  // The name of the index schema.
  // 
  // example:
  // 
  // test_api
  IndexName *string `json:"indexName,omitempty" xml:"indexName,omitempty"`
  // The namespace field.
  // 
  // example:
  // 
  // namespace
  Namespace *string `json:"namespace,omitempty" xml:"namespace,omitempty"`
  // The field that stores the indexes of the elements in sparse vectors.
  // 
  // example:
  // 
  // sparse_indices
  SparseIndexField *string `json:"sparseIndexField,omitempty" xml:"sparseIndexField,omitempty"`
  // The field that stores the elements in sparse vectors.
  // 
  // example:
  // 
  // sparse_values
  SparseValueField *string `json:"sparseValueField,omitempty" xml:"sparseValueField,omitempty"`
  // The vector field.
  // 
  // example:
  // 
  // source_image_vector
  VectorField *string `json:"vectorField,omitempty" xml:"vectorField,omitempty"`
  // The vector retrieval algorithm.
  // 
  // example:
  // 
  // Qc
  VectorIndexType *string `json:"vectorIndexType,omitempty" xml:"vectorIndexType,omitempty"`
}

func (s ModifyTableRequestVectorIndex) String() string {
  return tea.Prettify(s)
}

func (s ModifyTableRequestVectorIndex) GoString() string {
  return s.String()
}

func (s *ModifyTableRequestVectorIndex) SetAdvanceParams(v *ModifyTableRequestVectorIndexAdvanceParams) *ModifyTableRequestVectorIndex {
  s.AdvanceParams = v
  return s
}

func (s *ModifyTableRequestVectorIndex) SetDimension(v string) *ModifyTableRequestVectorIndex {
  s.Dimension = &v
  return s
}

func (s *ModifyTableRequestVectorIndex) SetDistanceType(v string) *ModifyTableRequestVectorIndex {
  s.DistanceType = &v
  return s
}

func (s *ModifyTableRequestVectorIndex) SetIndexName(v string) *ModifyTableRequestVectorIndex {
  s.IndexName = &v
  return s
}

func (s *ModifyTableRequestVectorIndex) SetNamespace(v string) *ModifyTableRequestVectorIndex {
  s.Namespace = &v
  return s
}

func (s *ModifyTableRequestVectorIndex) SetSparseIndexField(v string) *ModifyTableRequestVectorIndex {
  s.SparseIndexField = &v
  return s
}

func (s *ModifyTableRequestVectorIndex) SetSparseValueField(v string) *ModifyTableRequestVectorIndex {
  s.SparseValueField = &v
  return s
}

func (s *ModifyTableRequestVectorIndex) SetVectorField(v string) *ModifyTableRequestVectorIndex {
  s.VectorField = &v
  return s
}

func (s *ModifyTableRequestVectorIndex) SetVectorIndexType(v string) *ModifyTableRequestVectorIndex {
  s.VectorIndexType = &v
  return s
}

type ModifyTableRequestVectorIndexAdvanceParams struct {
  // The index building parameters.
  // 
  // example:
  // 
  // {}
  BuildIndexParams *string `json:"buildIndexParams,omitempty" xml:"buildIndexParams,omitempty"`
  // The threshold for linear building.
  // 
  // example:
  // 
  // 5000
  LinearBuildThreshold *string `json:"linearBuildThreshold,omitempty" xml:"linearBuildThreshold,omitempty"`
  // The minimum number of retrieved candidate sets.
  // 
  // example:
  // 
  // 20000
  MinScanDocCnt *string `json:"minScanDocCnt,omitempty" xml:"minScanDocCnt,omitempty"`
  // The index retrieval parameters.
  // 
  // example:
  // 
  // {}
  SearchIndexParams *string `json:"searchIndexParams,omitempty" xml:"searchIndexParams,omitempty"`
}

func (s ModifyTableRequestVectorIndexAdvanceParams) String() string {
  return tea.Prettify(s)
}

func (s ModifyTableRequestVectorIndexAdvanceParams) GoString() string {
  return s.String()
}

func (s *ModifyTableRequestVectorIndexAdvanceParams) SetBuildIndexParams(v string) *ModifyTableRequestVectorIndexAdvanceParams {
  s.BuildIndexParams = &v
  return s
}

func (s *ModifyTableRequestVectorIndexAdvanceParams) SetLinearBuildThreshold(v string) *ModifyTableRequestVectorIndexAdvanceParams {
  s.LinearBuildThreshold = &v
  return s
}

func (s *ModifyTableRequestVectorIndexAdvanceParams) SetMinScanDocCnt(v string) *ModifyTableRequestVectorIndexAdvanceParams {
  s.MinScanDocCnt = &v
  return s
}

func (s *ModifyTableRequestVectorIndexAdvanceParams) SetSearchIndexParams(v string) *ModifyTableRequestVectorIndexAdvanceParams {
  s.SearchIndexParams = &v
  return s
}

type ModifyTableResponseBody struct {
  // id of request
  // 
  // example:
  // 
  // FE03180A-0E29-5474-8A86-33F0683294A4
  RequestId *string `json:"requestId,omitempty" xml:"requestId,omitempty"`
  // Map
  // 
  // example:
  // 
  // {}
  Result map[string]interface{} `json:"result,omitempty" xml:"result,omitempty"`
}

func (s ModifyTableResponseBody) String() string {
  return tea.Prettify(s)
}

func (s ModifyTableResponseBody) GoString() string {
  return s.String()
}

func (s *ModifyTableResponseBody) SetRequestId(v string) *ModifyTableResponseBody {
  s.RequestId = &v
  return s
}

func (s *ModifyTableResponseBody) SetResult(v map[string]interface{}) *ModifyTableResponseBody {
  s.Result = v
  return s
}

type ModifyTableResponse struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  StatusCode *int32 `json:"statusCode,omitempty" xml:"statusCode,omitempty"`
  Body *ModifyTableResponseBody `json:"body,omitempty" xml:"body,omitempty"`
}

func (s ModifyTableResponse) String() string {
  return tea.Prettify(s)
}

func (s ModifyTableResponse) GoString() string {
  return s.String()
}

func (s *ModifyTableResponse) SetHeaders(v map[string]*string) *ModifyTableResponse {
  s.Headers = v
  return s
}

func (s *ModifyTableResponse) SetStatusCode(v int32) *ModifyTableResponse {
  s.StatusCode = &v
  return s
}

func (s *ModifyTableResponse) SetBody(v *ModifyTableResponseBody) *ModifyTableResponse {
  s.Body = v
  return s
}

// Description:
// 
// 删除表
type DeleteTableResponseBody struct {
  // requestId
  // 
  // example:
  // 
  // E7B7D598-B080-5C8E-AA35-D43EC0D5F886
  RequestId *string `json:"requestId,omitempty" xml:"requestId,omitempty"`
  // Map
  // 
  // example:
  // 
  // {}
  Result map[string]interface{} `json:"result,omitempty" xml:"result,omitempty"`
}

func (s DeleteTableResponseBody) String() string {
  return tea.Prettify(s)
}

func (s DeleteTableResponseBody) GoString() string {
  return s.String()
}

func (s *DeleteTableResponseBody) SetRequestId(v string) *DeleteTableResponseBody {
  s.RequestId = &v
  return s
}

func (s *DeleteTableResponseBody) SetResult(v map[string]interface{}) *DeleteTableResponseBody {
  s.Result = v
  return s
}

type DeleteTableResponse struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  StatusCode *int32 `json:"statusCode,omitempty" xml:"statusCode,omitempty"`
  Body *DeleteTableResponseBody `json:"body,omitempty" xml:"body,omitempty"`
}

func (s DeleteTableResponse) String() string {
  return tea.Prettify(s)
}

func (s DeleteTableResponse) GoString() string {
  return s.String()
}

func (s *DeleteTableResponse) SetHeaders(v map[string]*string) *DeleteTableResponse {
  s.Headers = v
  return s
}

func (s *DeleteTableResponse) SetStatusCode(v int32) *DeleteTableResponse {
  s.StatusCode = &v
  return s
}

func (s *DeleteTableResponse) SetBody(v *DeleteTableResponseBody) *DeleteTableResponse {
  s.Body = v
  return s
}

// Description:
// 
// 表停止使用
type StopTableResponseBody struct {
  // The request ID.
  // 
  // example:
  // 
  // E7B7D598-B080-5C8E-AA35-D43EC0D5F886
  RequestId *string `json:"requestId,omitempty" xml:"requestId,omitempty"`
  // The index map.
  // 
  // example:
  // 
  // {}
  Result map[string]interface{} `json:"result,omitempty" xml:"result,omitempty"`
}

func (s StopTableResponseBody) String() string {
  return tea.Prettify(s)
}

func (s StopTableResponseBody) GoString() string {
  return s.String()
}

func (s *StopTableResponseBody) SetRequestId(v string) *StopTableResponseBody {
  s.RequestId = &v
  return s
}

func (s *StopTableResponseBody) SetResult(v map[string]interface{}) *StopTableResponseBody {
  s.Result = v
  return s
}

type StopTableResponse struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  StatusCode *int32 `json:"statusCode,omitempty" xml:"statusCode,omitempty"`
  Body *StopTableResponseBody `json:"body,omitempty" xml:"body,omitempty"`
}

func (s StopTableResponse) String() string {
  return tea.Prettify(s)
}

func (s StopTableResponse) GoString() string {
  return s.String()
}

func (s *StopTableResponse) SetHeaders(v map[string]*string) *StopTableResponse {
  s.Headers = v
  return s
}

func (s *StopTableResponse) SetStatusCode(v int32) *StopTableResponse {
  s.StatusCode = &v
  return s
}

func (s *StopTableResponse) SetBody(v *StopTableResponseBody) *StopTableResponse {
  s.Body = v
  return s
}

// Description:
// 
// 表恢复使用
type StartTableResponseBody struct {
  // The request ID.
  // 
  // example:
  // 
  // D39EE0F1-D7EF-5F46-B781-6BF4185308B0
  RequestId *string `json:"requestId,omitempty" xml:"requestId,omitempty"`
  // The index map.
  // 
  // example:
  // 
  // {}
  Result map[string]interface{} `json:"result,omitempty" xml:"result,omitempty"`
}

func (s StartTableResponseBody) String() string {
  return tea.Prettify(s)
}

func (s StartTableResponseBody) GoString() string {
  return s.String()
}

func (s *StartTableResponseBody) SetRequestId(v string) *StartTableResponseBody {
  s.RequestId = &v
  return s
}

func (s *StartTableResponseBody) SetResult(v map[string]interface{}) *StartTableResponseBody {
  s.Result = v
  return s
}

type StartTableResponse struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  StatusCode *int32 `json:"statusCode,omitempty" xml:"statusCode,omitempty"`
  Body *StartTableResponseBody `json:"body,omitempty" xml:"body,omitempty"`
}

func (s StartTableResponse) String() string {
  return tea.Prettify(s)
}

func (s StartTableResponse) GoString() string {
  return s.String()
}

func (s *StartTableResponse) SetHeaders(v map[string]*string) *StartTableResponse {
  s.Headers = v
  return s
}

func (s *StartTableResponse) SetStatusCode(v int32) *StartTableResponse {
  s.StatusCode = &v
  return s
}

func (s *StartTableResponse) SetBody(v *StartTableResponseBody) *StartTableResponse {
  s.Body = v
  return s
}

// Description:
// 
// 
// 
//  	- 索引重建
type ReindexRequest struct {
  // The timestamp in seconds. The value must be of the INTEGER type. This parameter is required if you specify an API data source.
  // 
  // example:
  // 
  // 1640867288
  DataTimeSec *int32 `json:"dataTimeSec,omitempty" xml:"dataTimeSec,omitempty"`
  // oss data path
  // 
  // example:
  // 
  // oss://opensearch
  OssDataPath *string `json:"ossDataPath,omitempty" xml:"ossDataPath,omitempty"`
  // The partition in the MaxCompute table. This parameter is required if type is set to odps.
  // 
  // example:
  // 
  // ds=20220713
  Partition *string `json:"partition,omitempty" xml:"partition,omitempty"`
}

func (s ReindexRequest) String() string {
  return tea.Prettify(s)
}

func (s ReindexRequest) GoString() string {
  return s.String()
}

func (s *ReindexRequest) SetDataTimeSec(v int32) *ReindexRequest {
  s.DataTimeSec = &v
  return s
}

func (s *ReindexRequest) SetOssDataPath(v string) *ReindexRequest {
  s.OssDataPath = &v
  return s
}

func (s *ReindexRequest) SetPartition(v string) *ReindexRequest {
  s.Partition = &v
  return s
}

type ReindexResponseBody struct {
  // requestId
  // 
  // example:
  // 
  // 10D5E615-69F7-5F49-B850-00169ADE513C
  RequestId *string `json:"requestId,omitempty" xml:"requestId,omitempty"`
  // Map
  // 
  // example:
  // 
  // {}
  Result map[string]interface{} `json:"result,omitempty" xml:"result,omitempty"`
}

func (s ReindexResponseBody) String() string {
  return tea.Prettify(s)
}

func (s ReindexResponseBody) GoString() string {
  return s.String()
}

func (s *ReindexResponseBody) SetRequestId(v string) *ReindexResponseBody {
  s.RequestId = &v
  return s
}

func (s *ReindexResponseBody) SetResult(v map[string]interface{}) *ReindexResponseBody {
  s.Result = v
  return s
}

type ReindexResponse struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  StatusCode *int32 `json:"statusCode,omitempty" xml:"statusCode,omitempty"`
  Body *ReindexResponseBody `json:"body,omitempty" xml:"body,omitempty"`
}

func (s ReindexResponse) String() string {
  return tea.Prettify(s)
}

func (s ReindexResponse) GoString() string {
  return s.String()
}

func (s *ReindexResponse) SetHeaders(v map[string]*string) *ReindexResponse {
  s.Headers = v
  return s
}

func (s *ReindexResponse) SetStatusCode(v int32) *ReindexResponse {
  s.StatusCode = &v
  return s
}

func (s *ReindexResponse) SetBody(v *ReindexResponseBody) *ReindexResponse {
  s.Body = v
  return s
}

// Description:
// 
// 获取索引版本列表
type ListTableGenerationsResponseBody struct {
  // requestId
  // 
  // example:
  // 
  // F6E3D968-529C-5C40-AFDD-133A8B8FD930
  RequestId *string `json:"requestId,omitempty" xml:"requestId,omitempty"`
  // The result.
  Result []*ListTableGenerationsResponseBodyResult `json:"result,omitempty" xml:"result,omitempty" type:"Repeated"`
}

func (s ListTableGenerationsResponseBody) String() string {
  return tea.Prettify(s)
}

func (s ListTableGenerationsResponseBody) GoString() string {
  return s.String()
}

func (s *ListTableGenerationsResponseBody) SetRequestId(v string) *ListTableGenerationsResponseBody {
  s.RequestId = &v
  return s
}

func (s *ListTableGenerationsResponseBody) SetResult(v []*ListTableGenerationsResponseBodyResult) *ListTableGenerationsResponseBody {
  s.Result = v
  return s
}

type ListTableGenerationsResponseBodyResult struct     {
  // The ID of the full index version.
  // 
  // example:
  // 
  // 1708674867
  GenerationId *int64 `json:"generationId,omitempty" xml:"generationId,omitempty"`
}

func (s ListTableGenerationsResponseBodyResult) String() string {
  return tea.Prettify(s)
}

func (s ListTableGenerationsResponseBodyResult) GoString() string {
  return s.String()
}

func (s *ListTableGenerationsResponseBodyResult) SetGenerationId(v int64) *ListTableGenerationsResponseBodyResult {
  s.GenerationId = &v
  return s
}

type ListTableGenerationsResponse struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  StatusCode *int32 `json:"statusCode,omitempty" xml:"statusCode,omitempty"`
  Body *ListTableGenerationsResponseBody `json:"body,omitempty" xml:"body,omitempty"`
}

func (s ListTableGenerationsResponse) String() string {
  return tea.Prettify(s)
}

func (s ListTableGenerationsResponse) GoString() string {
  return s.String()
}

func (s *ListTableGenerationsResponse) SetHeaders(v map[string]*string) *ListTableGenerationsResponse {
  s.Headers = v
  return s
}

func (s *ListTableGenerationsResponse) SetStatusCode(v int32) *ListTableGenerationsResponse {
  s.StatusCode = &v
  return s
}

func (s *ListTableGenerationsResponse) SetBody(v *ListTableGenerationsResponseBody) *ListTableGenerationsResponse {
  s.Body = v
  return s
}

// Description:
// 
// 获取索引版本详情
type GetTableGenerationResponseBody struct {
  // requestId
  // 
  // example:
  // 
  // E7B7D598-B080-5C8E-AA35-D43EC0D5F886
  RequestId *string `json:"requestId,omitempty" xml:"requestId,omitempty"`
  // The result returned.
  Result *GetTableGenerationResponseBodyResult `json:"result,omitempty" xml:"result,omitempty" type:"Struct"`
}

func (s GetTableGenerationResponseBody) String() string {
  return tea.Prettify(s)
}

func (s GetTableGenerationResponseBody) GoString() string {
  return s.String()
}

func (s *GetTableGenerationResponseBody) SetRequestId(v string) *GetTableGenerationResponseBody {
  s.RequestId = &v
  return s
}

func (s *GetTableGenerationResponseBody) SetResult(v *GetTableGenerationResponseBodyResult) *GetTableGenerationResponseBody {
  s.Result = v
  return s
}

type GetTableGenerationResponseBodyResult struct {
  // generationId
  // 
  // example:
  // 
  // 1708674867
  GenerationId *int64 `json:"generationId,omitempty" xml:"generationId,omitempty"`
  // starting, building, ready, stopped, failed
  // 
  // example:
  // 
  // ready
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
}

func (s GetTableGenerationResponseBodyResult) String() string {
  return tea.Prettify(s)
}

func (s GetTableGenerationResponseBodyResult) GoString() string {
  return s.String()
}

func (s *GetTableGenerationResponseBodyResult) SetGenerationId(v int64) *GetTableGenerationResponseBodyResult {
  s.GenerationId = &v
  return s
}

func (s *GetTableGenerationResponseBodyResult) SetStatus(v string) *GetTableGenerationResponseBodyResult {
  s.Status = &v
  return s
}

type GetTableGenerationResponse struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  StatusCode *int32 `json:"statusCode,omitempty" xml:"statusCode,omitempty"`
  Body *GetTableGenerationResponseBody `json:"body,omitempty" xml:"body,omitempty"`
}

func (s GetTableGenerationResponse) String() string {
  return tea.Prettify(s)
}

func (s GetTableGenerationResponse) GoString() string {
  return s.String()
}

func (s *GetTableGenerationResponse) SetHeaders(v map[string]*string) *GetTableGenerationResponse {
  s.Headers = v
  return s
}

func (s *GetTableGenerationResponse) SetStatusCode(v int32) *GetTableGenerationResponse {
  s.StatusCode = &v
  return s
}

func (s *GetTableGenerationResponse) SetBody(v *GetTableGenerationResponseBody) *GetTableGenerationResponse {
  s.Body = v
  return s
}

// Description:
// 
// 获取任务列表
type ListTasksRequest struct {
  // The timestamp that indicates the end of the time range to query.
  // 
  // example:
  // 
  // 1690423741577
  End *int64 `json:"end,omitempty" xml:"end,omitempty"`
  // The timestamp that indicates the beginning of the time range to query.
  // 
  // example:
  // 
  // 1687238865434
  Start *int64 `json:"start,omitempty" xml:"start,omitempty"`
}

func (s ListTasksRequest) String() string {
  return tea.Prettify(s)
}

func (s ListTasksRequest) GoString() string {
  return s.String()
}

func (s *ListTasksRequest) SetEnd(v int64) *ListTasksRequest {
  s.End = &v
  return s
}

func (s *ListTasksRequest) SetStart(v int64) *ListTasksRequest {
  s.Start = &v
  return s
}

type ListTasksResponseBody struct {
  // The request ID.
  // 
  // example:
  // 
  // D39EE0F1-D7EF-5F46-B781-6BF4185308B0
  RequestId *string `json:"requestId,omitempty" xml:"requestId,omitempty"`
  // The result.
  // 
  // example:
  // 
  // {}
  Result interface{} `json:"result,omitempty" xml:"result,omitempty"`
}

func (s ListTasksResponseBody) String() string {
  return tea.Prettify(s)
}

func (s ListTasksResponseBody) GoString() string {
  return s.String()
}

func (s *ListTasksResponseBody) SetRequestId(v string) *ListTasksResponseBody {
  s.RequestId = &v
  return s
}

func (s *ListTasksResponseBody) SetResult(v interface{}) *ListTasksResponseBody {
  s.Result = v
  return s
}

type ListTasksResponse struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  StatusCode *int32 `json:"statusCode,omitempty" xml:"statusCode,omitempty"`
  Body *ListTasksResponseBody `json:"body,omitempty" xml:"body,omitempty"`
}

func (s ListTasksResponse) String() string {
  return tea.Prettify(s)
}

func (s ListTasksResponse) GoString() string {
  return s.String()
}

func (s *ListTasksResponse) SetHeaders(v map[string]*string) *ListTasksResponse {
  s.Headers = v
  return s
}

func (s *ListTasksResponse) SetStatusCode(v int32) *ListTasksResponse {
  s.StatusCode = &v
  return s
}

func (s *ListTasksResponse) SetBody(v *ListTasksResponseBody) *ListTasksResponse {
  s.Body = v
  return s
}

type Client struct {
  Endpoint  *string
  InstanceId  *string
  Protocol  *string
  UserAgent  *string
  Credential  *string
  Domainsuffix  *string
  RuntimeOptions  *util.RuntimeOptions
}

func NewClient(config *Config)(*Client, error) {
  client := new(Client)
  err := client.Init(config)
  return client, err
}

func (client *Client)Init(config *Config)(_err error) {
  if tea.BoolValue(util.IsUnset(config)) {
    _err = tea.NewSDKError(map[string]interface{}{
      "name": "ParameterMissing",
      "message": "'config' can not be unset",
    })
    return _err
  }

  if tea.BoolValue(util.IsUnset(config.Endpoint)) {
    _err = tea.NewSDKError(map[string]interface{}{
      "name": "ParameterMissing",
      "message": "'config.endpoint' can not be unset",
    })
    return _err
  }

  if !tea.BoolValue(util.Empty(config.AccessUserName)) && !tea.BoolValue(util.Empty(config.AccessPassWord)) {
    client.Credential = client.GetRealmSignStr(config.AccessUserName, config.AccessPassWord)
  }

  client.Endpoint = client.GetEndpoint(config.Endpoint)
  client.InstanceId = client.GetInstanceId(config)
  client.Protocol = config.Protocol
  client.UserAgent = config.UserAgent
  client.Domainsuffix = tea.String("ha.aliyuncs.com")
  client.RuntimeOptions = client.BuildRuntimeOptions(config.RuntimeOptions)
  return nil
}


func (client *Client) _request(method *string, pathname *string, query map[string]interface{}, headers map[string]*string, body interface{}, runtime *util.RuntimeOptions) (_result map[string]interface{}, _err error) {
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(runtime.MaxAttempts),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(runtime.BackoffPolicy),
      "period": tea.IntValue(runtime.BackoffPeriod),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := make(map[string]interface{})
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(map[string]interface{}, error){
      request_ := tea.NewRequest()
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("HTTP"))
      request_.Method = method
      request_.Pathname = pathname
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.InstanceId) + "." + tea.StringValue(client.Domainsuffix))),
        "authorization": tea.String("Basic " + tea.StringValue(client.Credential)),
        "content-type": tea.String("application/json; charset=utf-8"),
        },headers)
      if !tea.BoolValue(util.IsUnset(query)) {
        request_.Query = util.StringifyMapValue(query)
        request_.Headers["X-Opensearch-Request-ID"] = util.GetNonce()
      }

      if !tea.BoolValue(util.IsUnset(body)) {
        request_.Headers["X-Opensearch-Swift-Request-ID"] = util.GetNonce()
        if tea.BoolValue(string_.Equals(tea.String("deflate"), request_.Headers["Content-Encoding"])) && !tea.BoolValue(string_.Contains(pathname, tea.String("actions/bulk"))) {
          compressed, _err := ha3util.DeflateCompress(string_.ToBytes(util.ToJSONString(body), tea.String("UTF-8")))
          if _err != nil {
            return _result, _err
          }

          request_.Body = tea.ToReader(compressed)
        } else {
          request_.Body = tea.ToReader(util.ToJSONString(body))
        }

      }

      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      objStr, _err := util.ReadAsString(response_.Body)
      if _err != nil {
        return _result, _err
      }

      if tea.BoolValue(util.Is4xx(response_.StatusCode)) || tea.BoolValue(util.Is5xx(response_.StatusCode)) {
        var rawMsg interface{}
        _, tryErr := func()(_r map[string]interface{}, _e error) {
          defer func() {
            if r := tea.Recover(recover()); r != nil {
              _e = r
            }
          }()
          rawMsg = util.ParseJSON(objStr)

          return nil, nil
        }()

        if tryErr != nil {
          var err = &tea.SDKError{}
          if _t, ok := tryErr.(*tea.SDKError); ok {
            err = _t
          } else {
            err.Message = tea.String(tryErr.Error())
          }
          rawMsg = objStr
        }
        rawMap := map[string]interface{}{
          "errors": rawMsg,
          "headers": response_.Headers,
        }
        _err = tea.NewSDKError(map[string]interface{}{
          "message": tea.StringValue(response_.StatusMessage),
          "data": rawMap,
          "code": tea.IntValue(response_.StatusCode),
        })
        return _result, _err
      }

      if tea.BoolValue(util.Empty(objStr)) {
        rawbodyMap := map[string]interface{}{
          "status": tea.StringValue(response_.StatusMessage),
          "code": tea.IntValue(response_.StatusCode),
        }
        _result = make(map[string]interface{})
        _err = tea.Convert(map[string]interface{}{
          "body": tea.StringValue(util.ToJSONString(rawbodyMap)),
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      _result = make(map[string]interface{})
      _err = tea.Convert(map[string]interface{}{
        "body": tea.StringValue(objStr),
        "headers": response_.Headers,
      }, &_result)
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

func (client *Client) _openApiRequest(method *string, pathname *string, query map[string]interface{}, headers map[string]*string, body interface{}, runtime *util.RuntimeOptions) (_result map[string]interface{}, _err error) {
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(runtime.MaxAttempts),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(runtime.BackoffPolicy),
      "period": tea.IntValue(runtime.BackoffPeriod),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := make(map[string]interface{})
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(map[string]interface{}, error){
      request_ := tea.NewRequest()
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("HTTP"))
      request_.Method = method
      request_.Pathname = pathname
      request_.Headers = tea.Merge(map[string]*string{
        "host": client.Endpoint,
        "authorization": tea.String("Basic " + tea.StringValue(client.Credential)),
        "content-type": tea.String("application/json; charset=utf-8"),
        },headers)
      if !tea.BoolValue(util.IsUnset(query)) {
        request_.Query = util.StringifyMapValue(query)
      }

      if !tea.BoolValue(util.IsUnset(body)) {
        request_.Body = tea.ToReader(util.ToJSONString(body))
      }

      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      objStr, _err := util.ReadAsString(response_.Body)
      if _err != nil {
        return _result, _err
      }

      if tea.BoolValue(util.Is4xx(response_.StatusCode)) || tea.BoolValue(util.Is5xx(response_.StatusCode)) {
        var rawMsg interface{}
        _, tryErr := func()(_r map[string]interface{}, _e error) {
          defer func() {
            if r := tea.Recover(recover()); r != nil {
              _e = r
            }
          }()
          rawMsg = util.ParseJSON(objStr)

          return nil, nil
        }()

        if tryErr != nil {
          var err = &tea.SDKError{}
          if _t, ok := tryErr.(*tea.SDKError); ok {
            err = _t
          } else {
            err.Message = tea.String(tryErr.Error())
          }
          rawMsg = objStr
        }
        _err = tea.NewSDKError(map[string]interface{}{
          "message": tea.StringValue(objStr),
          "data": rawMsg,
          "code": tea.IntValue(response_.StatusCode),
        })
        return _result, _err
      }

      obj := util.ParseJSON(objStr)
      _result = make(map[string]interface{})
      _err = tea.Convert(map[string]interface{}{
        "body": obj,
        "headers": response_.Headers,
        "statusCode": tea.IntValue(response_.StatusCode),
      }, &_result)
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}


// Description:
// 
// 如果用户传了实例id，则直接使用，否则从endpoint中解析实例id,
func (client *Client) GetInstanceId (config *Config) (_result *string) {
  if !tea.BoolValue(util.IsUnset(config.InstanceId)) {
    _result = config.InstanceId
    return _result
  }

  values := string_.Split(client.Endpoint, tea.String("."), tea.Int(2))
  value := values[0]
  _result = value
  return _result
}

// Description:
// 
// 如果endpoint 配置以 http:// 或 https:// 开头，则去掉头部的 http:// 或 https://, 否则直接返回
func (client *Client) GetEndpoint (endpoint *string) (_result *string) {
  if tea.BoolValue(string_.HasPrefix(endpoint, tea.String("http://"))) {
    _body := string_.Replace(endpoint, tea.String("http://"), tea.String(""), tea.Int(1))
    _result = _body
    return _result
  }

  if tea.BoolValue(string_.HasPrefix(endpoint, tea.String("https://"))) {
    _body := string_.Replace(endpoint, tea.String("https://"), tea.String(""), tea.Int(1))
    _result = _body
    return _result
  }

  _result = endpoint
  return _result
}

// Description:
// 
// 设置Client UA 配置.
func (client *Client) SetUserAgent (userAgent *string) {
  client.UserAgent = userAgent
}

// Description:
// 
// 添加Client UA 配置.
func (client *Client) AppendUserAgent (userAgent *string) {
  client.UserAgent = tea.String(tea.StringValue(client.UserAgent) + " " + tea.StringValue(userAgent))
}

// Description:
// 
// 获取Client 配置 UA 配置.
func (client *Client) GetUserAgent () (_result *string) {
  userAgent := util.GetUserAgent(client.UserAgent)
  _result = userAgent
  return _result
}

// Description:
// 
// 计算用户请求识别特征, 遵循 Basic Auth 生成规范.
func (client *Client) GetRealmSignStr (accessUserName *string, accessPassWord *string) (_result *string) {
  accessUserNameStr := string_.Trim(accessUserName)
  accessPassWordStr := string_.Trim(accessPassWord)
  realmStr := tea.String(tea.StringValue(accessUserNameStr) + ":" + tea.StringValue(accessPassWordStr))
  _body := encodeutil.Base64EncodeToString(string_.ToBytes(realmStr, tea.String("UTF-8")))
  _result = _body
  return _result
}

// Description:
// 
// 向量查询
func (client *Client) Query (request *QueryRequest) (_result *SearchResponse, _err error) {
  headers := client.GetHeadersFromRunTimeOption()
  _result = &SearchResponse{}
  _body, _err := client._request(tea.String("POST"), tea.String("/vector-service/query"), nil, headers, util.ToJSONString(request), client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 向量预测查询
func (client *Client) InferenceQuery (request *QueryRequest) (_result *SearchResponse, _err error) {
  headers := client.GetHeadersFromRunTimeOption()
  _result = &SearchResponse{}
  _body, _err := client._request(tea.String("POST"), tea.String("/vector-service/inference-query"), nil, headers, util.ToJSONString(request), client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 多namespace查询
func (client *Client) MultiQuery (request *MultiQueryRequest) (_result *SearchResponse, _err error) {
  headers := client.GetHeadersFromRunTimeOption()
  _result = &SearchResponse{}
  _body, _err := client._request(tea.String("POST"), tea.String("/vector-service/multi-query"), nil, headers, util.ToJSONString(request), client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 查询数据
func (client *Client) Fetch (request *FetchRequest) (_result *SearchResponse, _err error) {
  headers := client.GetHeadersFromRunTimeOption()
  _result = &SearchResponse{}
  _body, _err := client._request(tea.String("POST"), tea.String("/vector-service/fetch"), nil, headers, util.ToJSONString(request), client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 文本向量混合检索
func (client *Client) Search (request *SearchRequest) (_result *SearchResponse, _err error) {
  headers := client.GetHeadersFromRunTimeOption()
  _result = &SearchResponse{}
  _body, _err := client._request(tea.String("POST"), tea.String("/vector-service/search"), nil, headers, util.ToJSONString(request), client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 向量引擎统计语法
func (client *Client) Aggregate (request *AggregateRequest) (_result *SearchResponse, _err error) {
  headers := client.GetHeadersFromRunTimeOption()
  _result = &SearchResponse{}
  _body, _err := client._request(tea.String("POST"), tea.String("/vector-service/aggregate"), nil, headers, util.ToJSONString(request), client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 批量查询
func (client *Client) BatchQuery (request *BatchRequest) (_result *SearchResponse, _err error) {
  headers := client.GetHeadersFromRunTimeOption()
  _result = &SearchResponse{}
  _body, _err := client._request(tea.String("POST"), tea.String("/vector-service/batch-query"), nil, headers, util.ToJSONString(request), client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 文档统计
func (client *Client) Stats (tableName *string) (_result *SearchResponse, _err error) {
  body := map[string]interface{}{
    "tableName": tea.StringValue(tableName),
  }
  _result = &SearchResponse{}
  _body, _err := client._request(tea.String("POST"), tea.String("/vector-service/stats"), nil, nil, util.ToJSONString(body), client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 校验网络是否通畅
// 
// 检查vpc & 用户名密码配置是否正确
func (client *Client) Active () (_result *SearchResponse, _err error) {
  _result = &SearchResponse{}
  _body, _err := client._request(tea.String("GET"), tea.String("/network/active"), nil, nil, nil, client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 支持新增、更新、删除 等操作，以及对应批量操作
func (client *Client) PushDocuments (dataSourceName *string, keyField *string, request *PushDocumentsRequest) (_result *PushDocumentsResponse, _err error) {
  request.Headers = tea.Merge(map[string]*string{
    "X-Opensearch-Swift-PK-Field": keyField,
    "X-Opensearch-Validate-Data": tea.String("true"),
    },request.Headers)
  _result = &PushDocumentsResponse{}
  _body, _err := client._request(tea.String("POST"), tea.String("/update/" + tea.StringValue(dataSourceName) + "/actions/bulk"), nil, request.Headers, request.Body, client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 构建RuntimeOptions
func (client *Client) BuildRuntimeOptions (runtimeOptions *util.RuntimeOptions) (_result *util.RuntimeOptions) {
  if tea.BoolValue(util.IsUnset(runtimeOptions)) {
    _result = &util.RuntimeOptions{}
    return _result
  }

  if tea.BoolValue(util.IsUnset(runtimeOptions.ReadTimeout)) {
    runtimeOptions.ReadTimeout = tea.Int(10000)
  }

  if tea.BoolValue(util.IsUnset(runtimeOptions.ConnectTimeout)) {
    runtimeOptions.ConnectTimeout = tea.Int(5000)
  }

  if tea.BoolValue(util.IsUnset(runtimeOptions.MaxIdleConns)) {
    runtimeOptions.MaxIdleConns = tea.Int(50)
  }

  if tea.BoolValue(util.IsUnset(runtimeOptions.MaxAttempts)) {
    runtimeOptions.MaxAttempts = tea.Int(5)
  }

  if tea.BoolValue(util.IsUnset(runtimeOptions.BackoffPolicy)) {
    runtimeOptions.BackoffPolicy = tea.String("no")
  }

  if tea.BoolValue(util.IsUnset(runtimeOptions.BackoffPeriod)) {
    runtimeOptions.BackoffPeriod = tea.Int(1)
  }

  _result = runtimeOptions
  return _result
}

// Description:
// 
// 从runtimeoptions中获取headers
func (client *Client) GetHeadersFromRunTimeOption () (_result map[string]*string) {
  options := client.RuntimeOptions
  headers := make(map[string]*string)
  if !tea.BoolValue(util.IsUnset(options.ExtendsParameters)) && !tea.BoolValue(util.IsUnset(options.ExtendsParameters.Headers)) && !tea.BoolValue(util.Empty(options.ExtendsParameters.Headers["Content-Encoding"])) {
    contentEncoding := options.ExtendsParameters.Headers["Content-Encoding"]
    if tea.BoolValue(string_.Equals(tea.String("deflate"), contentEncoding)) {
      headers["Content-Encoding"] = tea.String("deflate")
    }

  }

  _result = headers
  return _result
}

// Description:
// 
// 获取表列表
func (client *Client) ListTables () (_result *ListTablesResponse, _err error) {
  _result = &ListTablesResponse{}
  _body, _err := client._openApiRequest(tea.String("GET"), tea.String("/openapi/ha3/instances/" + tea.StringValue(client.InstanceId) + "/tables"), nil, nil, nil, client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 获取表详情
func (client *Client) GetTable (tableName *string) (_result *GetTableResponse, _err error) {
  _result = &GetTableResponse{}
  _body, _err := client._openApiRequest(tea.String("GET"), tea.String("/openapi/ha3/instances/" + tea.StringValue(client.InstanceId) + "/tables/" + tea.StringValue(tableName)), nil, nil, nil, client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 创建表
func (client *Client) CreateTable (request *CreateTableRequest) (_result *CreateTableResponse, _err error) {
  query := map[string]interface{}{}
  if !tea.BoolValue(util.IsUnset(request.DryRun)) {
    query["dryRun"] = request.DryRun
  }

  _result = &CreateTableResponse{}
  _body, _err := client._openApiRequest(tea.String("POST"), tea.String("/openapi/ha3/instances/" + tea.StringValue(client.InstanceId) + "/tables"), query, nil, util.ToJSONString(request), client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 修改表
func (client *Client) ModifyTable (tableName *string, request *ModifyTableRequest) (_result *ModifyTableResponse, _err error) {
  query := map[string]interface{}{}
  if !tea.BoolValue(util.IsUnset(request.DryRun)) {
    query["dryRun"] = request.DryRun
  }

  _result = &ModifyTableResponse{}
  _body, _err := client._openApiRequest(tea.String("PUT"), tea.String("/openapi/ha3/instances/" + tea.StringValue(client.InstanceId) + "/tables/" + tea.StringValue(tableName)), query, nil, util.ToJSONString(request), client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 删除表
func (client *Client) DeleteTable (tableName *string) (_result *DeleteTableResponse, _err error) {
  _result = &DeleteTableResponse{}
  _body, _err := client._openApiRequest(tea.String("DELETE"), tea.String("/openapi/ha3/instances/" + tea.StringValue(client.InstanceId) + "/tables/" + tea.StringValue(tableName)), nil, nil, nil, client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 表停止使用
func (client *Client) StopTable (tableName *string) (_result *StopTableResponse, _err error) {
  _result = &StopTableResponse{}
  _body, _err := client._openApiRequest(tea.String("POST"), tea.String("/openapi/ha3/instances/" + tea.StringValue(client.InstanceId) + "/indexes/" + tea.StringValue(tableName) + "/stopIndex"), nil, nil, nil, client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 表恢复使用
func (client *Client) StartTable (tableName *string) (_result *StartTableResponse, _err error) {
  _result = &StartTableResponse{}
  _body, _err := client._openApiRequest(tea.String("POST"), tea.String("/openapi/ha3/instances/" + tea.StringValue(client.InstanceId) + "/indexes/" + tea.StringValue(tableName) + "/startIndex"), nil, nil, nil, client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 索引重建
func (client *Client) Reindex (tableName *string, request *ReindexRequest) (_result *ReindexResponse, _err error) {
  _result = &ReindexResponse{}
  _body, _err := client._openApiRequest(tea.String("POST"), tea.String("/openapi/ha3/instances/" + tea.StringValue(client.InstanceId) + "/tables/" + tea.StringValue(tableName) + "/reindex"), nil, nil, util.ToJSONString(request), client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 获取索引版本列表
func (client *Client) ListTableGenerations (tableName *string) (_result *ListTableGenerationsResponse, _err error) {
  _result = &ListTableGenerationsResponse{}
  _body, _err := client._openApiRequest(tea.String("GET"), tea.String("/openapi/ha3/instances/" + tea.StringValue(client.InstanceId) + "/tables/" + tea.StringValue(tableName) + "/index_versions"), nil, nil, nil, client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 获取索引版本详情
func (client *Client) GetTableGeneration (tableName *string, generationId *string) (_result *GetTableGenerationResponse, _err error) {
  _result = &GetTableGenerationResponse{}
  _body, _err := client._openApiRequest(tea.String("GET"), tea.String("/openapi/ha3/instances/" + tea.StringValue(client.InstanceId) + "/tables/" + tea.StringValue(tableName) + "/index_versions/" + tea.StringValue(generationId)), nil, nil, nil, client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

// Description:
// 
// 获取任务列表
func (client *Client) ListTasks (request *ListTasksRequest) (_result *ListTasksResponse, _err error) {
  query := map[string]interface{}{}
  one := number.ParseLong(tea.String("1000"))
  if !tea.BoolValue(util.IsUnset(request.End)) {
    query["end"] = number.Mul(request.End, one)
  }

  if !tea.BoolValue(util.IsUnset(request.Start)) {
    query["start"] = number.Mul(request.Start, one)
  } else {
    now := number.ParseLong(time.Unix())
    period := number.ParseLong(tea.String("86400"))
    query["start"] = number.Mul(number.Sub(now, period), one)
  }

  _result = &ListTasksResponse{}
  _body, _err := client._openApiRequest(tea.String("GET"), tea.String("/openapi/ha3/instances/" + tea.StringValue(client.InstanceId) + "/tasks"), query, nil, nil, client.RuntimeOptions)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Convert(_body, &_result)
  return _result, _err
}

