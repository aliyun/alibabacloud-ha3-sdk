// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_HA3_HPP_
#define ALIBABACLOUD_HA3_HPP_
#include <darabonba/Core.hpp>
#include <alibabacloud/HA3Model.hpp>
#include <alibabacloud/HA3.hpp>
#include <map>
#include <darabonba/Runtime.hpp>
using namespace std;
using json = nlohmann::json;
namespace AlibabaCloud
{
namespace HA3
{
  class Client {
    public:

      Client(AlibabaCloud::HA3::Models::Config &config);

      json _request(const string &method, const string &pathname, const json &query, const map<string, string> &headers, const Darabonba::Json &body, const Darabonba::RuntimeOptions &runtime);

      Darabonba::Json _openApiRequest(const string &method, const string &pathname, const json &query, const map<string, string> &headers, const Darabonba::Json &body, const Darabonba::RuntimeOptions &runtime);
      /**
       * 如果用户传了实例id，则直接使用，否则从endpoint中解析实例id,
       */
      string getInstanceId(const AlibabaCloud::HA3::Models::Config &config);

      /**
       * 如果endpoint 配置以 http:// 或 https:// 开头，则去掉头部的 http:// 或 https://, 否则直接返回
       */
      string getEndpoint(const string &endpoint);

      /**
       * 设置Client UA 配置.
       */
      void setUserAgent(const string &userAgent);

      /**
       * 添加Client UA 配置.
       */
      void appendUserAgent(const string &userAgent);

      /**
       * 获取Client 配置 UA 配置.
       */
      string getUserAgent();

      /**
       * 计算用户请求识别特征, 遵循 Basic Auth 生成规范.
       */
      string getRealmSignStr(const string &accessUserName, const string &accessPassWord);

      /**
       * 向量查询
       */
      Models::SearchResponse query(const Models::QueryRequest &request);

      /**
       * 向量预测查询
       */
      Models::SearchResponse inferenceQuery(const Models::QueryRequest &request);

      /**
       * 多namespace查询
       */
      Models::SearchResponse multiQuery(const Models::MultiQueryRequest &request);

      /**
       * 查询数据
       */
      Models::SearchResponse fetch(const Models::FetchRequest &request);

      /**
       * 文本向量混合检索
       */
      Models::SearchResponse search(const Models::SearchRequest &request);

      /**
       * 向量引擎统计语法
       */
      Models::SearchResponse aggregate(const Models::AggregateRequest &request);

      /**
       * 批量查询
       */
      Models::SearchResponse batchQuery(const Models::BatchRequest &request);

      /**
       * 文档统计
       */
      Models::SearchResponse stats(const string &tableName);

      /**
       * 校验网络是否通畅
       * 检查vpc & 用户名密码配置是否正确
       */
      Models::SearchResponse active();

      /**
       * 支持新增、更新、删除 等操作，以及对应批量操作
       */
      Models::PushDocumentsResponse pushDocuments(const string &dataSourceName, const string &keyField, const Models::PushDocumentsRequest &request);

      /**
       * 构建RuntimeOptions
       */
      Darabonba::RuntimeOptions buildRuntimeOptions(const Darabonba::RuntimeOptions &runtimeOptions);

      /**
       * 从runtimeoptions中获取headers
       */
      map<string, string> getHeadersFromRunTimeOption();

      /**
       * 获取表列表
       */
      Models::ListTablesResponse listTables();

      /**
       * 获取表详情
       */
      Models::GetTableResponse getTable(const string &tableName);

      /**
       * 创建表
       */
      Models::CreateTableResponse createTable(const Models::CreateTableRequest &request);

      /**
       * 修改表
       */
      Models::ModifyTableResponse modifyTable(const string &tableName, const Models::ModifyTableRequest &request);

      /**
       * 删除表
       */
      Models::DeleteTableResponse deleteTable(const string &tableName);

      /**
       * 表停止使用
       */
      Models::StopTableResponse stopTable(const string &tableName);

      /**
       * 表恢复使用
       */
      Models::StartTableResponse startTable(const string &tableName);

      /**
       * 索引重建
       */
      Models::ReindexResponse reindex(const string &tableName, const Models::ReindexRequest &request);

      /**
       * 获取索引版本列表
       */
      Models::ListTableGenerationsResponse listTableGenerations(const string &tableName);

      /**
       * 获取索引版本详情
       */
      Models::GetTableGenerationResponse getTableGeneration(const string &tableName, const string &generationId);

      /**
       * 获取任务列表
       */
      Models::ListTasksResponse listTasks(const Models::ListTasksRequest &request);
    protected:
      string _endpoint;

      string _instanceId;

      string _protocol;

      string _userAgent;

      string _credential;

      string _domainsuffix;

      Darabonba::RuntimeOptions _runtimeOptions;
  };
} // namespace AlibabaCloud
} // namespace HA3
#endif
