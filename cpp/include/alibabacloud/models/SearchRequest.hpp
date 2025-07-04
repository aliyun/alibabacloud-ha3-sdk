// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_MODELS_SEARCHREQUEST_HPP_
#define ALIBABACLOUD_MODELS_SEARCHREQUEST_HPP_
#include <darabonba/Core.hpp>
#include <vector>
#include <alibabacloud/models/QueryRequest.hpp>
#include <alibabacloud/models/TextQuery.hpp>
#include <alibabacloud/models/RankQuery.hpp>
using namespace std;
using json = nlohmann::json;
namespace AlibabaCloud
{
namespace HA3
{
namespace Models
{
  class SearchRequest : public Darabonba::Model {
  public:
    friend void to_json(Darabonba::Json& j, const SearchRequest& obj) { 
      DARABONBA_PTR_TO_JSON(tableName, tableName_);
      DARABONBA_PTR_TO_JSON(size, size_);
      DARABONBA_PTR_TO_JSON(from, from_);
      DARABONBA_PTR_TO_JSON(order, order_);
      DARABONBA_PTR_TO_JSON(outputFields, outputFields_);
      DARABONBA_PTR_TO_JSON(knn, knn_);
      DARABONBA_PTR_TO_JSON(text, text_);
      DARABONBA_PTR_TO_JSON(rank, rank_);
    };
    friend void from_json(const Darabonba::Json& j, SearchRequest& obj) { 
      DARABONBA_PTR_FROM_JSON(tableName, tableName_);
      DARABONBA_PTR_FROM_JSON(size, size_);
      DARABONBA_PTR_FROM_JSON(from, from_);
      DARABONBA_PTR_FROM_JSON(order, order_);
      DARABONBA_PTR_FROM_JSON(outputFields, outputFields_);
      DARABONBA_PTR_FROM_JSON(knn, knn_);
      DARABONBA_PTR_FROM_JSON(text, text_);
      DARABONBA_PTR_FROM_JSON(rank, rank_);
    };
    SearchRequest() = default ;
    SearchRequest(const SearchRequest &) = default ;
    SearchRequest(SearchRequest &&) = default ;
    SearchRequest(const Darabonba::Json & obj) { from_json(obj, *this); };
    virtual ~SearchRequest() = default ;
    SearchRequest& operator=(const SearchRequest &) = default ;
    SearchRequest& operator=(SearchRequest &&) = default ;
    virtual void validate() const override {
        DARABONBA_VALIDATE_REQUIRED(tableName_);
    };
    virtual void fromMap(const Darabonba::Json &obj) override { from_json(obj, *this); validate(); };
    virtual Darabonba::Json toMap() const override { Darabonba::Json obj; to_json(obj, *this); return obj; };
    virtual bool empty() const override { this->tableName_ != nullptr
        && this->size_ != nullptr && this->from_ != nullptr && this->order_ != nullptr && this->outputFields_ != nullptr && this->knn_ != nullptr
        && this->text_ != nullptr && this->rank_ != nullptr; };
    // tableName Field Functions 
    bool hasTableName() const { return this->tableName_ != nullptr;};
    void deleteTableName() { this->tableName_ = nullptr;};
    inline string tableName() const { DARABONBA_PTR_GET_DEFAULT(tableName_, "") };
    inline SearchRequest& setTableName(string tableName) { DARABONBA_PTR_SET_VALUE(tableName_, tableName) };


    // size Field Functions 
    bool hasSize() const { return this->size_ != nullptr;};
    void deleteSize() { this->size_ = nullptr;};
    inline int32_t size() const { DARABONBA_PTR_GET_DEFAULT(size_, 0) };
    inline SearchRequest& setSize(int32_t size) { DARABONBA_PTR_SET_VALUE(size_, size) };


    // from Field Functions 
    bool hasFrom() const { return this->from_ != nullptr;};
    void deleteFrom() { this->from_ = nullptr;};
    inline int32_t from() const { DARABONBA_PTR_GET_DEFAULT(from_, 0) };
    inline SearchRequest& setFrom(int32_t from) { DARABONBA_PTR_SET_VALUE(from_, from) };


    // order Field Functions 
    bool hasOrder() const { return this->order_ != nullptr;};
    void deleteOrder() { this->order_ = nullptr;};
    inline string order() const { DARABONBA_PTR_GET_DEFAULT(order_, "") };
    inline SearchRequest& setOrder(string order) { DARABONBA_PTR_SET_VALUE(order_, order) };


    // outputFields Field Functions 
    bool hasOutputFields() const { return this->outputFields_ != nullptr;};
    void deleteOutputFields() { this->outputFields_ = nullptr;};
    inline const vector<string> & outputFields() const { DARABONBA_PTR_GET_CONST(outputFields_, vector<string>) };
    inline vector<string> outputFields() { DARABONBA_PTR_GET(outputFields_, vector<string>) };
    inline SearchRequest& setOutputFields(const vector<string> & outputFields) { DARABONBA_PTR_SET_VALUE(outputFields_, outputFields) };
    inline SearchRequest& setOutputFields(vector<string> && outputFields) { DARABONBA_PTR_SET_RVALUE(outputFields_, outputFields) };


    // knn Field Functions 
    bool hasKnn() const { return this->knn_ != nullptr;};
    void deleteKnn() { this->knn_ = nullptr;};
    inline const QueryRequest & knn() const { DARABONBA_PTR_GET_CONST(knn_, QueryRequest) };
    inline QueryRequest knn() { DARABONBA_PTR_GET(knn_, QueryRequest) };
    inline SearchRequest& setKnn(const QueryRequest & knn) { DARABONBA_PTR_SET_VALUE(knn_, knn) };
    inline SearchRequest& setKnn(QueryRequest && knn) { DARABONBA_PTR_SET_RVALUE(knn_, knn) };


    // text Field Functions 
    bool hasText() const { return this->text_ != nullptr;};
    void deleteText() { this->text_ = nullptr;};
    inline const TextQuery & text() const { DARABONBA_PTR_GET_CONST(text_, TextQuery) };
    inline TextQuery text() { DARABONBA_PTR_GET(text_, TextQuery) };
    inline SearchRequest& setText(const TextQuery & text) { DARABONBA_PTR_SET_VALUE(text_, text) };
    inline SearchRequest& setText(TextQuery && text) { DARABONBA_PTR_SET_RVALUE(text_, text) };


    // rank Field Functions 
    bool hasRank() const { return this->rank_ != nullptr;};
    void deleteRank() { this->rank_ = nullptr;};
    inline const RankQuery & rank() const { DARABONBA_PTR_GET_CONST(rank_, RankQuery) };
    inline RankQuery rank() { DARABONBA_PTR_GET(rank_, RankQuery) };
    inline SearchRequest& setRank(const RankQuery & rank) { DARABONBA_PTR_SET_VALUE(rank_, rank) };
    inline SearchRequest& setRank(RankQuery && rank) { DARABONBA_PTR_SET_RVALUE(rank_, rank) };


  protected:
    // 数据源名
    std::shared_ptr<string> tableName_ = nullptr;
    // 返回结果的个数
    std::shared_ptr<int32_t> size_ = nullptr;
    // 从结果集的第from返回doc
    std::shared_ptr<int32_t> from_ = nullptr;
    // 结果排序方向:DESC: 降序排序;ASC: 升序排序
    std::shared_ptr<string> order_ = nullptr;
    // 指定需要在结果中返回的字段，默认为空
    std::shared_ptr<vector<string>> outputFields_ = nullptr;
    // KNN查询参数
    std::shared_ptr<QueryRequest> knn_ = nullptr;
    // text查询参数
    std::shared_ptr<TextQuery> text_ = nullptr;
    // 指定两路结果融合的方式，目前支持两种策略：默认策略：两路结果中相同pk的doc的分数按权重相加。按加权后的分数排序。rrf: 使用rrf融合两路结果
    std::shared_ptr<RankQuery> rank_ = nullptr;
  };

  } // namespace Models
} // namespace AlibabaCloud
} // namespace HA3
#endif
