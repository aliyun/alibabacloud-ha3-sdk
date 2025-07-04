// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_MODELS_MULTIQUERYREQUEST_HPP_
#define ALIBABACLOUD_MODELS_MULTIQUERYREQUEST_HPP_
#include <darabonba/Core.hpp>
#include <vector>
#include <alibabacloud/models/QueryRequest.hpp>
using namespace std;
using json = nlohmann::json;
namespace AlibabaCloud
{
namespace HA3
{
namespace Models
{
  class MultiQueryRequest : public Darabonba::Model {
  public:
    friend void to_json(Darabonba::Json& j, const MultiQueryRequest& obj) { 
      DARABONBA_PTR_TO_JSON(tableName, tableName_);
      DARABONBA_PTR_TO_JSON(queries, queries_);
      DARABONBA_PTR_TO_JSON(topK, topK_);
      DARABONBA_PTR_TO_JSON(includeVector, includeVector_);
      DARABONBA_PTR_TO_JSON(outputFields, outputFields_);
      DARABONBA_PTR_TO_JSON(order, order_);
      DARABONBA_PTR_TO_JSON(filter, filter_);
      DARABONBA_PTR_TO_JSON(sort, sort_);
      DARABONBA_PTR_TO_JSON(mode, mode_);
    };
    friend void from_json(const Darabonba::Json& j, MultiQueryRequest& obj) { 
      DARABONBA_PTR_FROM_JSON(tableName, tableName_);
      DARABONBA_PTR_FROM_JSON(queries, queries_);
      DARABONBA_PTR_FROM_JSON(topK, topK_);
      DARABONBA_PTR_FROM_JSON(includeVector, includeVector_);
      DARABONBA_PTR_FROM_JSON(outputFields, outputFields_);
      DARABONBA_PTR_FROM_JSON(order, order_);
      DARABONBA_PTR_FROM_JSON(filter, filter_);
      DARABONBA_PTR_FROM_JSON(sort, sort_);
      DARABONBA_PTR_FROM_JSON(mode, mode_);
    };
    MultiQueryRequest() = default ;
    MultiQueryRequest(const MultiQueryRequest &) = default ;
    MultiQueryRequest(MultiQueryRequest &&) = default ;
    MultiQueryRequest(const Darabonba::Json & obj) { from_json(obj, *this); };
    virtual ~MultiQueryRequest() = default ;
    MultiQueryRequest& operator=(const MultiQueryRequest &) = default ;
    MultiQueryRequest& operator=(MultiQueryRequest &&) = default ;
    virtual void validate() const override {
        DARABONBA_VALIDATE_REQUIRED(tableName_);
        DARABONBA_VALIDATE_REQUIRED(queries_);
    };
    virtual void fromMap(const Darabonba::Json &obj) override { from_json(obj, *this); validate(); };
    virtual Darabonba::Json toMap() const override { Darabonba::Json obj; to_json(obj, *this); return obj; };
    virtual bool empty() const override { this->tableName_ != nullptr
        && this->queries_ != nullptr && this->topK_ != nullptr && this->includeVector_ != nullptr && this->outputFields_ != nullptr && this->order_ != nullptr
        && this->filter_ != nullptr && this->sort_ != nullptr && this->mode_ != nullptr; };
    // tableName Field Functions 
    bool hasTableName() const { return this->tableName_ != nullptr;};
    void deleteTableName() { this->tableName_ = nullptr;};
    inline string tableName() const { DARABONBA_PTR_GET_DEFAULT(tableName_, "") };
    inline MultiQueryRequest& setTableName(string tableName) { DARABONBA_PTR_SET_VALUE(tableName_, tableName) };


    // queries Field Functions 
    bool hasQueries() const { return this->queries_ != nullptr;};
    void deleteQueries() { this->queries_ = nullptr;};
    inline const vector<QueryRequest> & queries() const { DARABONBA_PTR_GET_CONST(queries_, vector<QueryRequest>) };
    inline vector<QueryRequest> queries() { DARABONBA_PTR_GET(queries_, vector<QueryRequest>) };
    inline MultiQueryRequest& setQueries(const vector<QueryRequest> & queries) { DARABONBA_PTR_SET_VALUE(queries_, queries) };
    inline MultiQueryRequest& setQueries(vector<QueryRequest> && queries) { DARABONBA_PTR_SET_RVALUE(queries_, queries) };


    // topK Field Functions 
    bool hasTopK() const { return this->topK_ != nullptr;};
    void deleteTopK() { this->topK_ = nullptr;};
    inline int32_t topK() const { DARABONBA_PTR_GET_DEFAULT(topK_, 0) };
    inline MultiQueryRequest& setTopK(int32_t topK) { DARABONBA_PTR_SET_VALUE(topK_, topK) };


    // includeVector Field Functions 
    bool hasIncludeVector() const { return this->includeVector_ != nullptr;};
    void deleteIncludeVector() { this->includeVector_ = nullptr;};
    inline bool includeVector() const { DARABONBA_PTR_GET_DEFAULT(includeVector_, false) };
    inline MultiQueryRequest& setIncludeVector(bool includeVector) { DARABONBA_PTR_SET_VALUE(includeVector_, includeVector) };


    // outputFields Field Functions 
    bool hasOutputFields() const { return this->outputFields_ != nullptr;};
    void deleteOutputFields() { this->outputFields_ = nullptr;};
    inline const vector<string> & outputFields() const { DARABONBA_PTR_GET_CONST(outputFields_, vector<string>) };
    inline vector<string> outputFields() { DARABONBA_PTR_GET(outputFields_, vector<string>) };
    inline MultiQueryRequest& setOutputFields(const vector<string> & outputFields) { DARABONBA_PTR_SET_VALUE(outputFields_, outputFields) };
    inline MultiQueryRequest& setOutputFields(vector<string> && outputFields) { DARABONBA_PTR_SET_RVALUE(outputFields_, outputFields) };


    // order Field Functions 
    bool hasOrder() const { return this->order_ != nullptr;};
    void deleteOrder() { this->order_ = nullptr;};
    inline string order() const { DARABONBA_PTR_GET_DEFAULT(order_, "") };
    inline MultiQueryRequest& setOrder(string order) { DARABONBA_PTR_SET_VALUE(order_, order) };


    // filter Field Functions 
    bool hasFilter() const { return this->filter_ != nullptr;};
    void deleteFilter() { this->filter_ = nullptr;};
    inline string filter() const { DARABONBA_PTR_GET_DEFAULT(filter_, "") };
    inline MultiQueryRequest& setFilter(string filter) { DARABONBA_PTR_SET_VALUE(filter_, filter) };


    // sort Field Functions 
    bool hasSort() const { return this->sort_ != nullptr;};
    void deleteSort() { this->sort_ = nullptr;};
    inline string sort() const { DARABONBA_PTR_GET_DEFAULT(sort_, "") };
    inline MultiQueryRequest& setSort(string sort) { DARABONBA_PTR_SET_VALUE(sort_, sort) };


    // mode Field Functions 
    bool hasMode() const { return this->mode_ != nullptr;};
    void deleteMode() { this->mode_ = nullptr;};
    inline string mode() const { DARABONBA_PTR_GET_DEFAULT(mode_, "") };
    inline MultiQueryRequest& setMode(string mode) { DARABONBA_PTR_SET_VALUE(mode_, mode) };


  protected:
    // 数据源名
    std::shared_ptr<string> tableName_ = nullptr;
    // 多向量列表
    std::shared_ptr<vector<QueryRequest>> queries_ = nullptr;
    // 返回个数
    std::shared_ptr<int32_t> topK_ = nullptr;
    // 是否返回文档中的向量信息
    std::shared_ptr<bool> includeVector_ = nullptr;
    // 需要返回值的字段列表
    std::shared_ptr<vector<string>> outputFields_ = nullptr;
    // 排序顺序, ASC：升序  DESC: 降序
    std::shared_ptr<string> order_ = nullptr;
    // 过滤表达式
    std::shared_ptr<string> filter_ = nullptr;
    // 排序表达式
    std::shared_ptr<string> sort_ = nullptr;
    // 用于配置多路结果中相同pk doc如何计算分数。mode可以配置：sum, max, min。默认为sum
    std::shared_ptr<string> mode_ = nullptr;
  };

  } // namespace Models
} // namespace AlibabaCloud
} // namespace HA3
#endif
