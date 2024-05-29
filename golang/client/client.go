// This file is auto-generated, don't edit it. Thanks.
package client

import (
	encodeutil "github.com/alibabacloud-go/darabonba-encode-util/client"
	string_ "github.com/alibabacloud-go/darabonba-string/client"
	util "github.com/alibabacloud-go/tea-utils/v2/service"
	"github.com/alibabacloud-go/tea/tea"
)

type Config struct {
	Endpoint       *string `json:"endpoint,omitempty" xml:"endpoint,omitempty"`
	InstanceId     *string `json:"instanceId,omitempty" xml:"instanceId,omitempty"`
	Protocol       *string `json:"protocol,omitempty" xml:"protocol,omitempty"`
	AccessUserName *string `json:"accessUserName,omitempty" xml:"accessUserName,omitempty"`
	AccessPassWord *string `json:"accessPassWord,omitempty" xml:"accessPassWord,omitempty"`
	UserAgent      *string `json:"userAgent,omitempty" xml:"userAgent,omitempty"`
	HttpProxy      *string `json:"httpProxy,omitempty" xml:"httpProxy,omitempty"`
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

func (s *Config) SetHttpProxy(v string) *Config {
	s.HttpProxy = &v
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
	Endpoint     *string
	InstanceId   *string
	Protocol     *string
	UserAgent    *string
	Credential   *string
	Domainsuffix *string
	HttpProxy    *string
}

func NewClient(config *Config) (*Client, error) {
	client := new(Client)
	err := client.Init(config)
	return client, err
}

func (client *Client) Init(config *Config) (_err error) {
	if tea.BoolValue(util.IsUnset(config)) {
		_err = tea.NewSDKError(map[string]interface{}{
			"name":    "ParameterMissing",
			"message": "'config' can not be unset",
		})
		return _err
	}

	if !tea.BoolValue(util.Empty(config.AccessUserName)) && !tea.BoolValue(util.Empty(config.AccessPassWord)) {
		client.Credential = client.GetRealmSignStr(config.AccessUserName, config.AccessPassWord)
	}

	client.Endpoint = config.Endpoint
	client.InstanceId = config.InstanceId
	client.Protocol = config.Protocol
	client.UserAgent = config.UserAgent
	client.Domainsuffix = tea.String("ha.aliyuncs.com")
	client.HttpProxy = config.HttpProxy
	return nil
}

func (client *Client) _request(method *string, pathname *string, query map[string]interface{}, headers map[string]*string, body interface{}, runtime *util.RuntimeOptions) (_result map[string]interface{}, _err error) {
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(5))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
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

		_resp, _err = func() (map[string]interface{}, error) {
			request_ := tea.NewRequest()
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("HTTP"))
			request_.Method = method
			request_.Pathname = pathname
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":    client.GetUserAgent(),
				"host":          util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.InstanceId)+"."+tea.StringValue(client.Domainsuffix))),
				"authorization": tea.String("Basic " + tea.StringValue(client.Credential)),
				"content-type":  tea.String("application/json; charset=utf-8"),
			}, headers)
			if !tea.BoolValue(util.IsUnset(query)) {
				request_.Query = util.StringifyMapValue(query)
				request_.Headers["X-Opensearch-Request-ID"] = util.GetNonce()
			}

			if !tea.BoolValue(util.IsUnset(body)) {
				request_.Headers["X-Opensearch-Swift-Request-ID"] = util.GetNonce()
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
				_, tryErr := func() (_r map[string]interface{}, _e error) {
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
					"data":    rawMap,
					"code":    tea.IntValue(response_.StatusCode),
				})
				return _result, _err
			}

			if tea.BoolValue(util.Empty(objStr)) {
				rawbodyMap := map[string]interface{}{
					"status": tea.StringValue(response_.StatusMessage),
					"code":   tea.IntValue(response_.StatusCode),
				}
				_result = make(map[string]interface{})
				_err = tea.Convert(map[string]interface{}{
					"body":    tea.StringValue(util.ToJSONString(rawbodyMap)),
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			_result = make(map[string]interface{})
			_err = tea.Convert(map[string]interface{}{
				"body":    tea.StringValue(objStr),
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
// 设置Client UA 配置.
func (client *Client) SetUserAgent(userAgent *string) {
	client.UserAgent = userAgent
}

// Description:
//
// 添加Client UA 配置.
func (client *Client) AppendUserAgent(userAgent *string) {
	client.UserAgent = tea.String(tea.StringValue(client.UserAgent) + " " + tea.StringValue(userAgent))
}

// Description:
//
// 获取Client 配置 UA 配置.
func (client *Client) GetUserAgent() (_result *string) {
	userAgent := util.GetUserAgent(client.UserAgent)
	_result = userAgent
	return _result
}

// Description:
//
// 计算用户请求识别特征, 遵循 Basic Auth 生成规范.
func (client *Client) GetRealmSignStr(accessUserName *string, accessPassWord *string) (_result *string) {
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
func (client *Client) Query(request *QueryRequest) (_result *SearchResponse, _err error) {
	_result = &SearchResponse{}
	buildRuntimeOptionsTmp, err := client.BuildRuntimeOptions()
	if err != nil {
		_err = err
		return _result, _err
	}
	_body, _err := client._request(tea.String("POST"), tea.String("/vector-service/query"), nil, nil, util.ToJSONString(request), buildRuntimeOptionsTmp)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Convert(_body, &_result)
	return _result, _err
}

// Description:
//
// 向量预测查询
func (client *Client) InferenceQuery(request *QueryRequest) (_result *SearchResponse, _err error) {
	_result = &SearchResponse{}
	buildRuntimeOptionsTmp, err := client.BuildRuntimeOptions()
	if err != nil {
		_err = err
		return _result, _err
	}
	_body, _err := client._request(tea.String("POST"), tea.String("/vector-service/inference-query"), nil, nil, util.ToJSONString(request), buildRuntimeOptionsTmp)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Convert(_body, &_result)
	return _result, _err
}

// Description:
//
// 多namespace查询
func (client *Client) MultiQuery(request *MultiQueryRequest) (_result *SearchResponse, _err error) {
	_result = &SearchResponse{}
	buildRuntimeOptionsTmp, err := client.BuildRuntimeOptions()
	if err != nil {
		_err = err
		return _result, _err
	}
	_body, _err := client._request(tea.String("POST"), tea.String("/vector-service/multi-query"), nil, nil, util.ToJSONString(request), buildRuntimeOptionsTmp)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Convert(_body, &_result)
	return _result, _err
}

// Description:
//
// 查询数据
func (client *Client) Fetch(request *FetchRequest) (_result *SearchResponse, _err error) {
	_result = &SearchResponse{}
	buildRuntimeOptionsTmp, err := client.BuildRuntimeOptions()
	if err != nil {
		_err = err
		return _result, _err
	}
	_body, _err := client._request(tea.String("POST"), tea.String("/vector-service/fetch"), nil, nil, util.ToJSONString(request), buildRuntimeOptionsTmp)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Convert(_body, &_result)
	return _result, _err
}

// Description:
//
// 文档统计
func (client *Client) Stats(tableName *string) (_result *SearchResponse, _err error) {
	body := map[string]interface{}{
		"tableName": tea.StringValue(tableName),
	}
	_result = &SearchResponse{}
	buildRuntimeOptionsTmp, err := client.BuildRuntimeOptions()
	if err != nil {
		_err = err
		return _result, _err
	}
	_body, _err := client._request(tea.String("POST"), tea.String("/vector-service/stats"), nil, nil, util.ToJSONString(body), buildRuntimeOptionsTmp)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Convert(_body, &_result)
	return _result, _err
}

// Description:
//
// 支持新增、更新、删除 等操作，以及对应批量操作
func (client *Client) PushDocuments(dataSourceName *string, keyField *string, request *PushDocumentsRequest) (_result *PushDocumentsResponse, _err error) {
	request.Headers = tea.Merge(map[string]*string{
		"X-Opensearch-Swift-PK-Field": keyField,
	}, request.Headers)
	_result = &PushDocumentsResponse{}
	buildRuntimeOptionsTmp, err := client.BuildRuntimeOptions()
	if err != nil {
		_err = err
		return _result, _err
	}
	_body, _err := client._request(tea.String("POST"), tea.String("/update/"+tea.StringValue(dataSourceName)+"/actions/bulk"), nil, request.Headers, request.Body, buildRuntimeOptionsTmp)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Convert(_body, &_result)
	return _result, _err
}

// Description:
//
// 用于内网环境的新增、更新、删除 等操作，以及对应批量操作
func (client *Client) PushDocumentsWithSwift(dataSourceName *string, keyField *string, topic *string, swift *string, request *PushDocumentsRequest) (_result *PushDocumentsResponse, _err error) {
	request.Headers = map[string]*string{
		"X-Opensearch-Swift-PK-Field": keyField,
		"X-Opensearch-Swift-Topic":    topic,
		"X-Opensearch-Swift-Swift":    swift,
	}
	_result = &PushDocumentsResponse{}
	buildRuntimeOptionsTmp, err := client.BuildRuntimeOptions()
	if err != nil {
		_err = err
		return _result, _err
	}
	_body, _err := client._request(tea.String("POST"), tea.String("/update/"+tea.StringValue(dataSourceName)+"/actions/bulk"), nil, request.Headers, request.Body, buildRuntimeOptionsTmp)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Convert(_body, &_result)
	return _result, _err
}

// Description:
//
// 构建RuntimeOptions
func (client *Client) BuildRuntimeOptions() (_result *util.RuntimeOptions, _err error) {
	_result = &util.RuntimeOptions{}
	return _result, _err
}
