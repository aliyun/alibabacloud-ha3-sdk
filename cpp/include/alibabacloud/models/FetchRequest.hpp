// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_MODELS_FETCHREQUEST_HPP_
#define ALIBABACLOUD_MODELS_FETCHREQUEST_HPP_
#include <darabonba/Core.hpp>
#include <vector>
#include <map>
using namespace std;
using json = nlohmann::json;
namespace AlibabaCloud
{
namespace HA3
{
namespace Models
{
  class FetchRequest : public Darabonba::Model {
  public:
    friend void to_json(Darabonba::Json& j, const FetchRequest& obj) { 
      DARABONBA_PTR_TO_JSON(tableName, tableName_);
      DARABONBA_PTR_TO_JSON(ids, ids_);
      DARABONBA_PTR_TO_JSON(filter, filter_);
      DARABONBA_PTR_TO_JSON(sort, sort_);
      DARABONBA_PTR_TO_JSON(limit, limit_);
      DARABONBA_PTR_TO_JSON(offset, offset_);
      DARABONBA_PTR_TO_JSON(includeVector, includeVector_);
      DARABONBA_PTR_TO_JSON(outputFields, outputFields_);
      DARABONBA_PTR_TO_JSON(kvpairs, kvpairs_);
    };
    friend void from_json(const Darabonba::Json& j, FetchRequest& obj) { 
      DARABONBA_PTR_FROM_JSON(tableName, tableName_);
      DARABONBA_PTR_FROM_JSON(ids, ids_);
      DARABONBA_PTR_FROM_JSON(filter, filter_);
      DARABONBA_PTR_FROM_JSON(sort, sort_);
      DARABONBA_PTR_FROM_JSON(limit, limit_);
      DARABONBA_PTR_FROM_JSON(offset, offset_);
      DARABONBA_PTR_FROM_JSON(includeVector, includeVector_);
      DARABONBA_PTR_FROM_JSON(outputFields, outputFields_);
      DARABONBA_PTR_FROM_JSON(kvpairs, kvpairs_);
    };
    FetchRequest() = default ;
    FetchRequest(const FetchRequest &) = default ;
    FetchRequest(FetchRequest &&) = default ;
    FetchRequest(const Darabonba::Json & obj) { from_json(obj, *this); };
    virtual ~FetchRequest() = default ;
    FetchRequest& operator=(const FetchRequest &) = default ;
    FetchRequest& operator=(FetchRequest &&) = default ;
    virtual void validate() const override {
        DARABONBA_VALIDATE_REQUIRED(tableName_);
    };
    virtual void fromMap(const Darabonba::Json &obj) override { from_json(obj, *this); validate(); };
    virtual Darabonba::Json toMap() const override { Darabonba::Json obj; to_json(obj, *this); return obj; };
    virtual bool empty() const override { this->tableName_ != nullptr
        && this->ids_ != nullptr && this->filter_ != nullptr && this->sort_ != nullptr && this->limit_ != nullptr && this->offset_ != nullptr
        && this->includeVector_ != nullptr && this->outputFields_ != nullptr && this->kvpairs_ != nullptr; };
    // tableName Field Functions 
    bool hasTableName() const { return this->tableName_ != nullptr;};
    void deleteTableName() { this->tableName_ = nullptr;};
    inline string tableName() const { DARABONBA_PTR_GET_DEFAULT(tableName_, "") };
    inline FetchRequest& setTableName(string tableName) { DARABONBA_PTR_SET_VALUE(tableName_, tableName) };


    // ids Field Functions 
    bool hasIds() const { return this->ids_ != nullptr;};
    void deleteIds() { this->ids_ = nullptr;};
    inline const vector<string> & ids() const { DARABONBA_PTR_GET_CONST(ids_, vector<string>) };
    inline vector<string> ids() { DARABONBA_PTR_GET(ids_, vector<string>) };
    inline FetchRequest& setIds(const vector<string> & ids) { DARABONBA_PTR_SET_VALUE(ids_, ids) };
    inline FetchRequest& setIds(vector<string> && ids) { DARABONBA_PTR_SET_RVALUE(ids_, ids) };


    // filter Field Functions 
    bool hasFilter() const { return this->filter_ != nullptr;};
    void deleteFilter() { this->filter_ = nullptr;};
    inline string filter() const { DARABONBA_PTR_GET_DEFAULT(filter_, "") };
    inline FetchRequest& setFilter(string filter) { DARABONBA_PTR_SET_VALUE(filter_, filter) };


    // sort Field Functions 
    bool hasSort() const { return this->sort_ != nullptr;};
    void deleteSort() { this->sort_ = nullptr;};
    inline string sort() const { DARABONBA_PTR_GET_DEFAULT(sort_, "") };
    inline FetchRequest& setSort(string sort) { DARABONBA_PTR_SET_VALUE(sort_, sort) };


    // limit Field Functions 
    bool hasLimit() const { return this->limit_ != nullptr;};
    void deleteLimit() { this->limit_ = nullptr;};
    inline int32_t limit() const { DARABONBA_PTR_GET_DEFAULT(limit_, 0) };
    inline FetchRequest& setLimit(int32_t limit) { DARABONBA_PTR_SET_VALUE(limit_, limit) };


    // offset Field Functions 
    bool hasOffset() const { return this->offset_ != nullptr;};
    void deleteOffset() { this->offset_ = nullptr;};
    inline int32_t offset() const { DARABONBA_PTR_GET_DEFAULT(offset_, 0) };
    inline FetchRequest& setOffset(int32_t offset) { DARABONBA_PTR_SET_VALUE(offset_, offset) };


    // includeVector Field Functions 
    bool hasIncludeVector() const { return this->includeVector_ != nullptr;};
    void deleteIncludeVector() { this->includeVector_ = nullptr;};
    inline bool includeVector() const { DARABONBA_PTR_GET_DEFAULT(includeVector_, false) };
    inline FetchRequest& setIncludeVector(bool includeVector) { DARABONBA_PTR_SET_VALUE(includeVector_, includeVector) };


    // outputFields Field Functions 
    bool hasOutputFields() const { return this->outputFields_ != nullptr;};
    void deleteOutputFields() { this->outputFields_ = nullptr;};
    inline const vector<string> & outputFields() const { DARABONBA_PTR_GET_CONST(outputFields_, vector<string>) };
    inline vector<string> outputFields() { DARABONBA_PTR_GET(outputFields_, vector<string>) };
    inline FetchRequest& setOutputFields(const vector<string> & outputFields) { DARABONBA_PTR_SET_VALUE(outputFields_, outputFields) };
    inline FetchRequest& setOutputFields(vector<string> && outputFields) { DARABONBA_PTR_SET_RVALUE(outputFields_, outputFields) };


    // kvpairs Field Functions 
    bool hasKvpairs() const { return this->kvpairs_ != nullptr;};
    void deleteKvpairs() { this->kvpairs_ = nullptr;};
    inline const map<string, string> & kvpairs() const { DARABONBA_PTR_GET_CONST(kvpairs_, map<string, string>) };
    inline map<string, string> kvpairs() { DARABONBA_PTR_GET(kvpairs_, map<string, string>) };
    inline FetchRequest& setKvpairs(const map<string, string> & kvpairs) { DARABONBA_PTR_SET_VALUE(kvpairs_, kvpairs) };
    inline FetchRequest& setKvpairs(map<string, string> && kvpairs) { DARABONBA_PTR_SET_RVALUE(kvpairs_, kvpairs) };


  protected:
    // 数据源名
    std::shared_ptr<string> tableName_ = nullptr;
    // 主键列表，如果传了主键列表，下面的条件参数不生效
    std::shared_ptr<vector<string>> ids_ = nullptr;
    // 过滤表达式
    std::shared_ptr<string> filter_ = nullptr;
    // 排序表达式
    std::shared_ptr<string> sort_ = nullptr;
    // 返回的数据个数
    std::shared_ptr<int32_t> limit_ = nullptr;
    // 返回的数据开始下标，用于翻页
    std::shared_ptr<int32_t> offset_ = nullptr;
    // 是否返回向量数据
    std::shared_ptr<bool> includeVector_ = nullptr;
    // 需要返回的字段，不指定默认返回所有的字段
    std::shared_ptr<vector<string>> outputFields_ = nullptr;
    // kvpairs
    std::shared_ptr<map<string, string>> kvpairs_ = nullptr;
  };

  } // namespace Models
} // namespace AlibabaCloud
} // namespace HA3
#endif
