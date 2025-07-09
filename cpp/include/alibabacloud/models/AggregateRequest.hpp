// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_MODELS_AGGREGATEREQUEST_HPP_
#define ALIBABACLOUD_MODELS_AGGREGATEREQUEST_HPP_
#include <darabonba/Core.hpp>
#include <vector>
#include <alibabacloud/models/AggFuncDesc.hpp>
#include <alibabacloud/models/OrderByDesc.hpp>
using namespace std;
using json = nlohmann::json;
namespace AlibabaCloud
{
namespace HA3
{
namespace Models
{
  class AggregateRequest : public Darabonba::Model {
  public:
    friend void to_json(Darabonba::Json& j, const AggregateRequest& obj) { 
      DARABONBA_PTR_TO_JSON(tableName, tableName_);
      DARABONBA_PTR_TO_JSON(filter, filter_);
      DARABONBA_PTR_TO_JSON(groupKeys, groupKeys_);
      DARABONBA_PTR_TO_JSON(aggFuncs, aggFuncs_);
      DARABONBA_PTR_TO_JSON(orderBy, orderBy_);
      DARABONBA_PTR_TO_JSON(timeout, timeout_);
    };
    friend void from_json(const Darabonba::Json& j, AggregateRequest& obj) { 
      DARABONBA_PTR_FROM_JSON(tableName, tableName_);
      DARABONBA_PTR_FROM_JSON(filter, filter_);
      DARABONBA_PTR_FROM_JSON(groupKeys, groupKeys_);
      DARABONBA_PTR_FROM_JSON(aggFuncs, aggFuncs_);
      DARABONBA_PTR_FROM_JSON(orderBy, orderBy_);
      DARABONBA_PTR_FROM_JSON(timeout, timeout_);
    };
    AggregateRequest() = default ;
    AggregateRequest(const AggregateRequest &) = default ;
    AggregateRequest(AggregateRequest &&) = default ;
    AggregateRequest(const Darabonba::Json & obj) { from_json(obj, *this); };
    virtual ~AggregateRequest() = default ;
    AggregateRequest& operator=(const AggregateRequest &) = default ;
    AggregateRequest& operator=(AggregateRequest &&) = default ;
    virtual void validate() const override {
        DARABONBA_VALIDATE_REQUIRED(tableName_);
        DARABONBA_VALIDATE_REQUIRED(aggFuncs_);
    };
    virtual void fromMap(const Darabonba::Json &obj) override { from_json(obj, *this); validate(); };
    virtual Darabonba::Json toMap() const override { Darabonba::Json obj; to_json(obj, *this); return obj; };
    virtual bool empty() const override { this->tableName_ != nullptr
        && this->filter_ != nullptr && this->groupKeys_ != nullptr && this->aggFuncs_ != nullptr && this->orderBy_ != nullptr && this->timeout_ != nullptr; };
    // tableName Field Functions 
    bool hasTableName() const { return this->tableName_ != nullptr;};
    void deleteTableName() { this->tableName_ = nullptr;};
    inline string tableName() const { DARABONBA_PTR_GET_DEFAULT(tableName_, "") };
    inline AggregateRequest& setTableName(string tableName) { DARABONBA_PTR_SET_VALUE(tableName_, tableName) };


    // filter Field Functions 
    bool hasFilter() const { return this->filter_ != nullptr;};
    void deleteFilter() { this->filter_ = nullptr;};
    inline string filter() const { DARABONBA_PTR_GET_DEFAULT(filter_, "") };
    inline AggregateRequest& setFilter(string filter) { DARABONBA_PTR_SET_VALUE(filter_, filter) };


    // groupKeys Field Functions 
    bool hasGroupKeys() const { return this->groupKeys_ != nullptr;};
    void deleteGroupKeys() { this->groupKeys_ = nullptr;};
    inline const vector<string> & groupKeys() const { DARABONBA_PTR_GET_CONST(groupKeys_, vector<string>) };
    inline vector<string> groupKeys() { DARABONBA_PTR_GET(groupKeys_, vector<string>) };
    inline AggregateRequest& setGroupKeys(const vector<string> & groupKeys) { DARABONBA_PTR_SET_VALUE(groupKeys_, groupKeys) };
    inline AggregateRequest& setGroupKeys(vector<string> && groupKeys) { DARABONBA_PTR_SET_RVALUE(groupKeys_, groupKeys) };


    // aggFuncs Field Functions 
    bool hasAggFuncs() const { return this->aggFuncs_ != nullptr;};
    void deleteAggFuncs() { this->aggFuncs_ = nullptr;};
    inline const vector<AggFuncDesc> & aggFuncs() const { DARABONBA_PTR_GET_CONST(aggFuncs_, vector<AggFuncDesc>) };
    inline vector<AggFuncDesc> aggFuncs() { DARABONBA_PTR_GET(aggFuncs_, vector<AggFuncDesc>) };
    inline AggregateRequest& setAggFuncs(const vector<AggFuncDesc> & aggFuncs) { DARABONBA_PTR_SET_VALUE(aggFuncs_, aggFuncs) };
    inline AggregateRequest& setAggFuncs(vector<AggFuncDesc> && aggFuncs) { DARABONBA_PTR_SET_RVALUE(aggFuncs_, aggFuncs) };


    // orderBy Field Functions 
    bool hasOrderBy() const { return this->orderBy_ != nullptr;};
    void deleteOrderBy() { this->orderBy_ = nullptr;};
    inline const vector<OrderByDesc> & orderBy() const { DARABONBA_PTR_GET_CONST(orderBy_, vector<OrderByDesc>) };
    inline vector<OrderByDesc> orderBy() { DARABONBA_PTR_GET(orderBy_, vector<OrderByDesc>) };
    inline AggregateRequest& setOrderBy(const vector<OrderByDesc> & orderBy) { DARABONBA_PTR_SET_VALUE(orderBy_, orderBy) };
    inline AggregateRequest& setOrderBy(vector<OrderByDesc> && orderBy) { DARABONBA_PTR_SET_RVALUE(orderBy_, orderBy) };


    // timeout Field Functions 
    bool hasTimeout() const { return this->timeout_ != nullptr;};
    void deleteTimeout() { this->timeout_ = nullptr;};
    inline int32_t timeout() const { DARABONBA_PTR_GET_DEFAULT(timeout_, 0) };
    inline AggregateRequest& setTimeout(int32_t timeout) { DARABONBA_PTR_SET_VALUE(timeout_, timeout) };


  protected:
    // 需要统计的表名
    std::shared_ptr<string> tableName_ = nullptr;
    // 过滤条件
    std::shared_ptr<string> filter_ = nullptr;
    // 分组统计的字段列表
    std::shared_ptr<vector<string>> groupKeys_ = nullptr;
    // 统计函数列表
    std::shared_ptr<vector<AggFuncDesc>> aggFuncs_ = nullptr;
    // 统计结果排序方式，支持多维排序
    std::shared_ptr<vector<OrderByDesc>> orderBy_ = nullptr;
    // 超时时间，单位毫秒
    std::shared_ptr<int32_t> timeout_ = nullptr;
  };

  } // namespace Models
} // namespace AlibabaCloud
} // namespace HA3
#endif
