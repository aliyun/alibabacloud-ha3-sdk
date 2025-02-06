// This file is auto-generated, don't edit it. Thanks.
package client

import (
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  string_  "github.com/alibabacloud-go/darabonba-string/client"
  encodeutil  "github.com/alibabacloud-go/darabonba-encode-util/client"
  ha3util  "github.com/alibabacloud-go/alibabacloud-ha3-util/client"
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

  if !tea.BoolValue(util.Empty(config.AccessUserName)) && !tea.BoolValue(util.Empty(config.AccessPassWord)) {
    client.Credential = client.GetRealmSignStr(config.AccessUserName, config.AccessPassWord)
  }

  client.Endpoint = client.GetEndpoint(config.Endpoint)
  client.InstanceId = config.InstanceId
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

