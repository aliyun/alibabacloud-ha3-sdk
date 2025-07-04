#include <darabonba/Core.hpp>
#include <alibabacloud/HA3.hpp>
#include <map>
#include <darabonba/Runtime.hpp>
#include <darabonba/policy/Retry.hpp>
#include <darabonba/Exception.hpp>
#include <darabonba/Convert.hpp>
#include <alibabacloud/Utils.hpp>
#include <alibabacloud/Util.hpp>
#include <darabonba/Bytes.hpp>
#include <darabonba/Stream.hpp>
#include <darabonba/Date.hpp>
#include <darabonba/Number.hpp>
using namespace std;
using namespace Darabonba;
using json = nlohmann::json;
using namespace AlibabaCloud::OpenApi;
using namespace AlibabaCloud::HA3::Models;
using Ha3UtilClient = AlibabaCloud::HA3::Util::Client;
namespace AlibabaCloud
{
namespace HA3
{

AlibabaCloud::HA3::Client::Client(AlibabaCloud::HA3::Models::Config &config){
  if (config.empty()) {
    throw ResponseException(json({
      {"code" , "ParameterMissing"},
      {"message" , "'config' can not be unset"}
    }).get<map<string, string>>());
  }

  if (!config.hasEndpoint() && config.endpoint() != "") {
    throw ResponseException(json({
      {"code" , "ParameterMissing"},
      {"message" , "'config.endpoint' can not be unset"}
    }).get<map<string, string>>());
  }

  if (!!config.hasAccessUserName() && (config.accessUserName() != "") && !!config.hasAccessPassWord() && (config.accessPassWord() != "")) {
    this->_credential = getRealmSignStr(config.accessUserName(), config.accessPassWord());
  }

  this->_endpoint = getEndpoint(config.endpoint());
  this->_instanceId = getInstanceId(config);
  this->_protocol = config.protocol();
  this->_userAgent = config.userAgent();
  this->_domainsuffix = "ha.aliyuncs.com";
  this->_runtimeOptions = buildRuntimeOptions(config.runtimeOptions());
}


json Client::_request(const string &method, const string &pathname, const json &query, const map<string, string> &headers, const Darabonba::Json &body, const Darabonba::RuntimeOptions &runtime) {
  Darabonba::RuntimeOptions runtime_(json({
    {"timeouted", "retry"},
    {"readTimeout", runtime.readTimeout()},
    {"connectTimeout", runtime.connectTimeout()},
    {"httpsProxy", runtime.httpsProxy()},
    {"noProxy", runtime.noProxy()},
    {"maxIdleConns", runtime.maxIdleConns()},
    {"retry", json({
      {"retryable" , runtime.autoretry()},
      {"maxAttempts" , runtime.maxAttempts()}
    })},
    {"backoff", json({
      {"policy" , runtime.backoffPolicy()},
      {"period" , runtime.backoffPeriod()}
    })},
    {"ignoreSSL", runtime.ignoreSSL()}
    }));

  shared_ptr<Darabonba::Http::Request> _lastRequest = nullptr;
  shared_ptr<Darabonba::Http::MCurlResponse> _lastResponse = nullptr;
  Darabonba::Exception _lastException;
  int _retriesAttempted = 0;
  Darabonba::Policy::RetryPolicyContext _context = json({
    {"retriesAttempted" , _retriesAttempted}
  });
  while (Darabonba::allowRetry(runtime_.retryOptions(), _context)) {
    if (_retriesAttempted > 0) {
      int _backoffTime = Darabonba::getBackoffTime(runtime_.retryOptions(), _context);
      if (_backoffTime > 0) {
        Darabonba::sleep(_backoffTime);
      }
    }
    _retriesAttempted++;
    try {
      Darabonba::Http::Request request_ = Darabonba::Http::Request();
      request_.setProtocol(Darabonba::Convert::stringVal(Darabonba::defaultVal(_protocol, "HTTP")));
      request_.setMethod(method);
      request_.setPathname(pathname);
      request_.setHeaders(Darabonba::Core::merge(json({
          {"user-agent" , getUserAgent()},
          {"host" , Darabonba::Convert::stringVal(Darabonba::defaultVal(_endpoint, DARA_STRING_TEMPLATE("" , _instanceId , "." , _domainsuffix)))},
          {"authorization" , DARA_STRING_TEMPLATE("Basic " , _credential)},
          {"content-type" , "application/json; charset=utf-8"}
        }),
        headers
      ).get<map<string, string>>());
      if (!Darabonba::isNull(query)) {
        request_.setQuery(Utils::Utils::stringifyMapValue(query));
        request_.addHeader("X-Opensearch-Request-ID", Utils::Utils::getNonce());
      }

      if (!Darabonba::isNull(body)) {
        request_.addHeader("X-Opensearch-Swift-Request-ID", Utils::Utils::getNonce());
        if (("deflate" == request_.headers().at("Content-Encoding")) && !Darabonba::String::contains(pathname, "actions/bulk")) {
          Darabonba::Bytes compressed = Ha3UtilClient::deflateCompress(Darabonba::BytesUtil::from(json(body).dump(), "utf-8"));
          request_.setBody(Darabonba::Stream::toReadable(compressed));
        } else {
          request_.setBody(Darabonba::Stream::toReadable(json(body).dump()));
        }

      }

      _lastRequest = make_shared<Darabonba::Http::Request>(request_);
      auto futureResp_ = Darabonba::Core::doAction(request_, runtime_);
      shared_ptr<Darabonba::Http::MCurlResponse> response_ = futureResp_.get();
      _lastResponse  = response_;

      string objStr = Darabonba::Stream::readAsString(response_->body());
      if ((response_->statusCode() >= 400) && (response_->statusCode() < 600)) {
        Darabonba::Json rawMsg = nullptr;
        try {
          rawMsg = json::parse(objStr);
        } catch (const Darabonba::Exception err) {
          rawMsg = objStr;
        }        
        json rawMap = json({
          {"errors" , rawMsg},
          {"headers" , response_->headers()}
        });
        throw ResponseException(json({
          // message = __response.statusMessage,
          {"data" , rawMap},
          {"code" , DARA_STRING_TEMPLATE("" , response_->statusCode())}
        }));
      }

      if ((objStr == "") || Darabonba::isNull(objStr)) {
        json rawbodyMap = json({
          // status = __response.statusMessage,
          {"code" , DARA_STRING_TEMPLATE("" , response_->statusCode())}
        });
        return json({
          {"body" , rawbodyMap.dump()},
          {"headers" , response_->headers()}
        });
      }

      return json({
        {"body" , objStr},
        {"headers" , response_->headers()}
      });
    } catch (const Darabonba::Exception& ex) {
      _context = Darabonba::Policy::RetryPolicyContext(json({
        {"retriesAttempted" , _retriesAttempted},
        {"lastRequest" , _lastRequest},
        {"lastResponse" , _lastResponse},
        {"exception" , ex},
      }));
      continue;
    }
  }

  throw *_context.exception();
}

Darabonba::Json Client::_openApiRequest(const string &method, const string &pathname, const json &query, const map<string, string> &headers, const Darabonba::Json &body, const Darabonba::RuntimeOptions &runtime) {
  Darabonba::RuntimeOptions runtime_(json({
    {"timeouted", "retry"},
    {"readTimeout", runtime.readTimeout()},
    {"connectTimeout", runtime.connectTimeout()},
    {"httpsProxy", runtime.httpsProxy()},
    {"noProxy", runtime.noProxy()},
    {"maxIdleConns", runtime.maxIdleConns()},
    {"retry", json({
      {"retryable" , runtime.autoretry()},
      {"maxAttempts" , runtime.maxAttempts()}
    })},
    {"backoff", json({
      {"policy" , runtime.backoffPolicy()},
      {"period" , runtime.backoffPeriod()}
    })},
    {"ignoreSSL", runtime.ignoreSSL()}
    }));

  shared_ptr<Darabonba::Http::Request> _lastRequest = nullptr;
  shared_ptr<Darabonba::Http::MCurlResponse> _lastResponse = nullptr;
  Darabonba::Exception _lastException;
  int _retriesAttempted = 0;
  Darabonba::Policy::RetryPolicyContext _context = json({
    {"retriesAttempted" , _retriesAttempted}
  });
  while (Darabonba::allowRetry(runtime_.retryOptions(), _context)) {
    if (_retriesAttempted > 0) {
      int _backoffTime = Darabonba::getBackoffTime(runtime_.retryOptions(), _context);
      if (_backoffTime > 0) {
        Darabonba::sleep(_backoffTime);
      }
    }
    _retriesAttempted++;
    try {
      Darabonba::Http::Request request_ = Darabonba::Http::Request();
      request_.setProtocol(Darabonba::Convert::stringVal(Darabonba::defaultVal(_protocol, "HTTP")));
      request_.setMethod(method);
      request_.setPathname(pathname);
      request_.setHeaders(Darabonba::Core::merge(json({
          {"host" , _endpoint},
          {"authorization" , DARA_STRING_TEMPLATE("Basic " , _credential)},
          {"content-type" , "application/json; charset=utf-8"}
        }),
        headers
      ).get<map<string, string>>());
      if (!Darabonba::isNull(query)) {
        request_.setQuery(Utils::Utils::stringifyMapValue(query));
      }

      if (!Darabonba::isNull(body)) {
        request_.setBody(Darabonba::Stream::toReadable(json(body).dump()));
      }

      _lastRequest = make_shared<Darabonba::Http::Request>(request_);
      auto futureResp_ = Darabonba::Core::doAction(request_, runtime_);
      shared_ptr<Darabonba::Http::MCurlResponse> response_ = futureResp_.get();
      _lastResponse  = response_;

      string objStr = Darabonba::Stream::readAsString(response_->body());
      if ((response_->statusCode() >= 400) && (response_->statusCode() < 600)) {
        Darabonba::Json rawMsg = nullptr;
        try {
          rawMsg = json::parse(objStr);
        } catch (const Darabonba::Exception err) {
          rawMsg = objStr;
        }        
        throw ResponseException(json({
          {"message" , objStr},
          {"data" , json(rawMsg)},
          {"code" , DARA_STRING_TEMPLATE("" , response_->statusCode())}
        }));
      }

      Darabonba::Json obj = json::parse(objStr);
      return json({
        {"body" , obj},
        {"headers" , response_->headers()},
        {"statusCode" , response_->statusCode()}
      });
    } catch (const Darabonba::Exception& ex) {
      _context = Darabonba::Policy::RetryPolicyContext(json({
        {"retriesAttempted" , _retriesAttempted},
        {"lastRequest" , _lastRequest},
        {"lastResponse" , _lastResponse},
        {"exception" , ex},
      }));
      continue;
    }
  }

  throw *_context.exception();
}

/**
 * 如果用户传了实例id，则直接使用，否则从endpoint中解析实例id,
 */
string Client::getInstanceId(const AlibabaCloud::HA3::Models::Config &config) {
  if (!!config.hasInstanceId() && (config.instanceId() != "")) {
    return config.instanceId();
  }

  vector<string> values = Darabonba::String::split(this->_endpoint, ".");
  string value = values.at(0);
  return value;
}

/**
 * 如果endpoint 配置以 http:// 或 https:// 开头，则去掉头部的 http:// 或 https://, 否则直接返回
 */
string Client::getEndpoint(const string &endpoint) {
  if (Darabonba::String::hasPrefix(endpoint, "http://")) {
    return Darabonba::String::replace(endpoint, "http://", "");
  }

  if (Darabonba::String::hasPrefix(endpoint, "https://")) {
    return Darabonba::String::replace(endpoint, "https://", "");
  }

  return endpoint;
}

/**
 * 设置Client UA 配置.
 */
void Client::setUserAgent(const string &userAgent) {
  this->_userAgent = userAgent;
}

/**
 * 添加Client UA 配置.
 */
void Client::appendUserAgent(const string &userAgent) {
  this->_userAgent = DARA_STRING_TEMPLATE("" , _userAgent , " " , userAgent);
}

/**
 * 获取Client 配置 UA 配置.
 */
string Client::getUserAgent() {
  string userAgent = Utils::Utils::getUserAgent(_userAgent);
  return userAgent;
}

/**
 * 计算用户请求识别特征, 遵循 Basic Auth 生成规范.
 */
string Client::getRealmSignStr(const string &accessUserName, const string &accessPassWord) {
  string accessUserNameStr = Darabonba::String::trim(accessUserName);
  string accessPassWordStr = Darabonba::String::trim(accessPassWord);
  string realmStr = DARA_STRING_TEMPLATE("" , accessUserNameStr , ":" , accessPassWordStr);
  Darabonba::Bytes realmBytes = Darabonba::BytesUtil::from(realmStr, "utf-8");
  return Darabonba::Encode::Encoder::base64EncodeToString(realmBytes);
}

/**
 * 向量查询
 */
SearchResponse Client::query(const QueryRequest &request) {
  map<string, string> headers = getHeadersFromRunTimeOption();
  return json(_request("POST", DARA_STRING_TEMPLATE("/vector-service/query"), nullptr, headers, json(request).dump(), _runtimeOptions)).get<SearchResponse>();
}

/**
 * 向量预测查询
 */
SearchResponse Client::inferenceQuery(const QueryRequest &request) {
  map<string, string> headers = getHeadersFromRunTimeOption();
  return json(_request("POST", DARA_STRING_TEMPLATE("/vector-service/inference-query"), nullptr, headers, json(request).dump(), _runtimeOptions)).get<SearchResponse>();
}

/**
 * 多namespace查询
 */
SearchResponse Client::multiQuery(const MultiQueryRequest &request) {
  map<string, string> headers = getHeadersFromRunTimeOption();
  return json(_request("POST", DARA_STRING_TEMPLATE("/vector-service/multi-query"), nullptr, headers, json(request).dump(), _runtimeOptions)).get<SearchResponse>();
}

/**
 * 查询数据
 */
SearchResponse Client::fetch(const FetchRequest &request) {
  map<string, string> headers = getHeadersFromRunTimeOption();
  return json(_request("POST", DARA_STRING_TEMPLATE("/vector-service/fetch"), nullptr, headers, json(request).dump(), _runtimeOptions)).get<SearchResponse>();
}

/**
 * 文本向量混合检索
 */
SearchResponse Client::search(const SearchRequest &request) {
  map<string, string> headers = getHeadersFromRunTimeOption();
  return json(_request("POST", DARA_STRING_TEMPLATE("/vector-service/search"), nullptr, headers, json(request).dump(), _runtimeOptions)).get<SearchResponse>();
}

/**
 * 向量引擎统计语法
 */
SearchResponse Client::aggregate(const AggregateRequest &request) {
  map<string, string> headers = getHeadersFromRunTimeOption();
  return json(_request("POST", DARA_STRING_TEMPLATE("/vector-service/aggregate"), nullptr, headers, json(request).dump(), _runtimeOptions)).get<SearchResponse>();
}

/**
 * 批量查询
 */
SearchResponse Client::batchQuery(const BatchRequest &request) {
  map<string, string> headers = getHeadersFromRunTimeOption();
  return json(_request("POST", DARA_STRING_TEMPLATE("/vector-service/batch-query"), nullptr, headers, json(request).dump(), _runtimeOptions)).get<SearchResponse>();
}

/**
 * 文档统计
 */
SearchResponse Client::stats(const string &tableName) {
  json body = json({
    {"tableName" , tableName}
  });
  map<string, string> headers = {};
  return json(_request("POST", DARA_STRING_TEMPLATE("/vector-service/stats"), nullptr, headers, body.dump(), _runtimeOptions)).get<SearchResponse>();
}

/**
 * 校验网络是否通畅
 * 检查vpc & 用户名密码配置是否正确
 */
SearchResponse Client::active() {
  map<string, string> headers = {};
  return json(_request("GET", DARA_STRING_TEMPLATE("/network/active"), nullptr, headers, nullptr, _runtimeOptions)).get<SearchResponse>();
}

/**
 * 支持新增、更新、删除 等操作，以及对应批量操作
 */
PushDocumentsResponse Client::pushDocuments(const string &dataSourceName, const string &keyField, const PushDocumentsRequest &request) {
  map<string, string> headers = Darabonba::Core::merge(json({
      {"X-Opensearch-Swift-PK-Field" , keyField},
      {"X-Opensearch-Validate-Data" , "true"}
    }),
    request.headers()
  ).get<map<string, string>>();
  return json(_request("POST", DARA_STRING_TEMPLATE("/update/" , dataSourceName , "/actions/bulk"), nullptr, headers, request.body(), _runtimeOptions)).get<PushDocumentsResponse>();
}

/**
 * 构建RuntimeOptions
 */
Darabonba::RuntimeOptions Client::buildRuntimeOptions(const Darabonba::RuntimeOptions &runtimeOptions) {
  if (runtimeOptions.empty()) {
    return RuntimeOptions(json({
      {"readTimeout" , 10000},
      {"connectTimeout" , 5000},
      {"autoretry" , true},
      {"maxAttempts" , 2},
      {"ignoreSSL" , false},
      {"maxIdleConns" , 50}
    }));
  }

  Darabonba::RuntimeOptions ret = RuntimeOptions(json({
    {"readTimeout" , runtimeOptions.readTimeout()},
    {"connectTimeout" , runtimeOptions.connectTimeout()},
    // 默认开启SDK层面的重试，如果想要关闭重试，可以手动设置maxAttempts=0
    {"autoretry" , true},
    {"maxAttempts" , runtimeOptions.maxAttempts()},
    {"maxIdleConns" , runtimeOptions.maxIdleConns()},
    {"backoffPolicy" , runtimeOptions.backoffPolicy()},
    {"backoffPeriod" , runtimeOptions.backoffPeriod()}
  }));
  if (!runtimeOptions.hasReadTimeout()) {
    ret.setReadTimeout(10000);
  }

  if (!runtimeOptions.hasConnectTimeout()) {
    ret.setConnectTimeout(5000);
  }

  if (!runtimeOptions.hasMaxIdleConns()) {
    ret.setMaxIdleConns(50);
  }

  if (!runtimeOptions.hasMaxAttempts()) {
    ret.setMaxAttempts(2);
  }

  if (!runtimeOptions.hasBackoffPolicy()) {
    ret.setBackoffPolicy("no");
  }

  if (!runtimeOptions.hasBackoffPeriod()) {
    ret.setBackoffPeriod(1);
  }

  return runtimeOptions;
}

/**
 * 从runtimeoptions中获取headers
 */
map<string, string> Client::getHeadersFromRunTimeOption() {
  Darabonba::RuntimeOptions options = _runtimeOptions;
  map<string, string> headers = {};
  if (!!options.hasExtendsParameters() && !!options.extendsParameters().hasHeaders() && !Darabonba::isNull(options.extendsParameters().headers()["Content-Encoding"]) && options.extendsParameters().headers().at("Content-Encoding") != "") {
    string contentEncoding = options.extendsParameters().headers().at("Content-Encoding");
    if ("deflate" == contentEncoding) {
      headers["Content-Encoding"] = "deflate";
    }

  }

  return headers;
}

/**
 * 获取表列表
 */
ListTablesResponse Client::listTables() {
  map<string, string> headers = {};
  return json(_openApiRequest("GET", DARA_STRING_TEMPLATE("/openapi/ha3/instances/" , _instanceId , "/tables"), nullptr, headers, nullptr, _runtimeOptions)).get<ListTablesResponse>();
}

/**
 * 获取表详情
 */
GetTableResponse Client::getTable(const string &tableName) {
  map<string, string> headers = {};
  return json(_openApiRequest("GET", DARA_STRING_TEMPLATE("/openapi/ha3/instances/" , _instanceId , "/tables/" , tableName), nullptr, headers, nullptr, _runtimeOptions)).get<GetTableResponse>();
}

/**
 * 创建表
 */
CreateTableResponse Client::createTable(const CreateTableRequest &request) {
  json query = {};
  if (!!request.hasDryRun()) {
    query["dryRun"] = request.dryRun();
  }

  map<string, string> headers = {};
  return json(_openApiRequest("POST", DARA_STRING_TEMPLATE("/openapi/ha3/instances/" , _instanceId , "/tables"), query, headers, json(request).dump(), _runtimeOptions)).get<CreateTableResponse>();
}

/**
 * 修改表
 */
ModifyTableResponse Client::modifyTable(const string &tableName, const ModifyTableRequest &request) {
  json query = {};
  if (!!request.hasDryRun()) {
    query["dryRun"] = request.dryRun();
  }

  map<string, string> headers = {};
  return json(_openApiRequest("PUT", DARA_STRING_TEMPLATE("/openapi/ha3/instances/" , _instanceId , "/tables/" , tableName), query, headers, json(request).dump(), _runtimeOptions)).get<ModifyTableResponse>();
}

/**
 * 删除表
 */
DeleteTableResponse Client::deleteTable(const string &tableName) {
  map<string, string> headers = {};
  return json(_openApiRequest("DELETE", DARA_STRING_TEMPLATE("/openapi/ha3/instances/" , _instanceId , "/tables/" , tableName), nullptr, headers, nullptr, _runtimeOptions)).get<DeleteTableResponse>();
}

/**
 * 表停止使用
 */
StopTableResponse Client::stopTable(const string &tableName) {
  map<string, string> headers = {};
  return json(_openApiRequest("POST", DARA_STRING_TEMPLATE("/openapi/ha3/instances/" , _instanceId , "/indexes/" , tableName , "/stopIndex"), nullptr, headers, nullptr, _runtimeOptions)).get<StopTableResponse>();
}

/**
 * 表恢复使用
 */
StartTableResponse Client::startTable(const string &tableName) {
  map<string, string> headers = {};
  return json(_openApiRequest("POST", DARA_STRING_TEMPLATE("/openapi/ha3/instances/" , _instanceId , "/indexes/" , tableName , "/startIndex"), nullptr, headers, nullptr, _runtimeOptions)).get<StartTableResponse>();
}

/**
 * 索引重建
 */
ReindexResponse Client::reindex(const string &tableName, const ReindexRequest &request) {
  map<string, string> headers = {};
  return json(_openApiRequest("POST", DARA_STRING_TEMPLATE("/openapi/ha3/instances/" , _instanceId , "/tables/" , tableName , "/reindex"), nullptr, headers, json(request).dump(), _runtimeOptions)).get<ReindexResponse>();
}

/**
 * 获取索引版本列表
 */
ListTableGenerationsResponse Client::listTableGenerations(const string &tableName) {
  map<string, string> headers = {};
  return json(_openApiRequest("GET", DARA_STRING_TEMPLATE("/openapi/ha3/instances/" , _instanceId , "/tables/" , tableName , "/index_versions"), nullptr, headers, nullptr, _runtimeOptions)).get<ListTableGenerationsResponse>();
}

/**
 * 获取索引版本详情
 */
GetTableGenerationResponse Client::getTableGeneration(const string &tableName, const string &generationId) {
  map<string, string> headers = {};
  return json(_openApiRequest("GET", DARA_STRING_TEMPLATE("/openapi/ha3/instances/" , _instanceId , "/tables/" , tableName , "/index_versions/" , generationId), nullptr, headers, nullptr, _runtimeOptions)).get<GetTableGenerationResponse>();
}

/**
 * 获取任务列表
 */
ListTasksResponse Client::listTasks(const ListTasksRequest &request) {
  json query = {};
  int64_t one = 1000L;
  if (!!request.hasEnd()) {
    query["end"] = request.end() * one;
  }

  if (!!request.hasStart()) {
    query["start"] = request.start() * one;
  } else {
    shared_ptr<Darabonba::Date> date = make_shared<Darabonba::Date>(Utils::Utils::getTimestamp());
    int32_t now = date->unix();
    int64_t period = 86400L;
    query["start"] = (Darabonba::Number::itol(now) - period) * one;
  }

  map<string, string> headers = {};
  return json(_openApiRequest("GET", DARA_STRING_TEMPLATE("/openapi/ha3/instances/" , _instanceId , "/tasks"), query, headers, nullptr, _runtimeOptions)).get<ListTasksResponse>();
}
} // namespace AlibabaCloud
} // namespace HA3