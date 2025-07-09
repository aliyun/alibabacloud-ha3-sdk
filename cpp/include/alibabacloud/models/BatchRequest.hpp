// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_MODELS_BATCHREQUEST_HPP_
#define ALIBABACLOUD_MODELS_BATCHREQUEST_HPP_
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
  class BatchRequest : public Darabonba::Model {
  public:
    friend void to_json(Darabonba::Json& j, const BatchRequest& obj) { 
      DARABONBA_PTR_TO_JSON(queries, queries_);
      DARABONBA_PTR_TO_JSON(timeout, timeout_);
    };
    friend void from_json(const Darabonba::Json& j, BatchRequest& obj) { 
      DARABONBA_PTR_FROM_JSON(queries, queries_);
      DARABONBA_PTR_FROM_JSON(timeout, timeout_);
    };
    BatchRequest() = default ;
    BatchRequest(const BatchRequest &) = default ;
    BatchRequest(BatchRequest &&) = default ;
    BatchRequest(const Darabonba::Json & obj) { from_json(obj, *this); };
    virtual ~BatchRequest() = default ;
    BatchRequest& operator=(const BatchRequest &) = default ;
    BatchRequest& operator=(BatchRequest &&) = default ;
    virtual void validate() const override {
        DARABONBA_VALIDATE_REQUIRED(queries_);
    };
    virtual void fromMap(const Darabonba::Json &obj) override { from_json(obj, *this); validate(); };
    virtual Darabonba::Json toMap() const override { Darabonba::Json obj; to_json(obj, *this); return obj; };
    virtual bool empty() const override { this->queries_ != nullptr
        && this->timeout_ != nullptr; };
    // queries Field Functions 
    bool hasQueries() const { return this->queries_ != nullptr;};
    void deleteQueries() { this->queries_ = nullptr;};
    inline const vector<QueryRequest> & queries() const { DARABONBA_PTR_GET_CONST(queries_, vector<QueryRequest>) };
    inline vector<QueryRequest> queries() { DARABONBA_PTR_GET(queries_, vector<QueryRequest>) };
    inline BatchRequest& setQueries(const vector<QueryRequest> & queries) { DARABONBA_PTR_SET_VALUE(queries_, queries) };
    inline BatchRequest& setQueries(vector<QueryRequest> && queries) { DARABONBA_PTR_SET_RVALUE(queries_, queries) };


    // timeout Field Functions 
    bool hasTimeout() const { return this->timeout_ != nullptr;};
    void deleteTimeout() { this->timeout_ = nullptr;};
    inline int32_t timeout() const { DARABONBA_PTR_GET_DEFAULT(timeout_, 0) };
    inline BatchRequest& setTimeout(int32_t timeout) { DARABONBA_PTR_SET_VALUE(timeout_, timeout) };


  protected:
    // 批量查询列表
    std::shared_ptr<vector<QueryRequest>> queries_ = nullptr;
    // 超时时间，单位毫秒
    std::shared_ptr<int32_t> timeout_ = nullptr;
  };

  } // namespace Models
} // namespace AlibabaCloud
} // namespace HA3
#endif
