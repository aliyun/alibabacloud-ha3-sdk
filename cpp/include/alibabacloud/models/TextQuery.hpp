// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_MODELS_TEXTQUERY_HPP_
#define ALIBABACLOUD_MODELS_TEXTQUERY_HPP_
#include <darabonba/Core.hpp>
#include <map>
using namespace std;
using json = nlohmann::json;
namespace AlibabaCloud
{
namespace HA3
{
namespace Models
{
  class TextQuery : public Darabonba::Model {
  public:
    friend void to_json(Darabonba::Json& j, const TextQuery& obj) { 
      DARABONBA_PTR_TO_JSON(queryString, queryString_);
      DARABONBA_PTR_TO_JSON(queryParams, queryParams_);
      DARABONBA_PTR_TO_JSON(filter, filter_);
      DARABONBA_PTR_TO_JSON(weight, weight_);
      DARABONBA_PTR_TO_JSON(terminateAfter, terminateAfter_);
    };
    friend void from_json(const Darabonba::Json& j, TextQuery& obj) { 
      DARABONBA_PTR_FROM_JSON(queryString, queryString_);
      DARABONBA_PTR_FROM_JSON(queryParams, queryParams_);
      DARABONBA_PTR_FROM_JSON(filter, filter_);
      DARABONBA_PTR_FROM_JSON(weight, weight_);
      DARABONBA_PTR_FROM_JSON(terminateAfter, terminateAfter_);
    };
    TextQuery() = default ;
    TextQuery(const TextQuery &) = default ;
    TextQuery(TextQuery &&) = default ;
    TextQuery(const Darabonba::Json & obj) { from_json(obj, *this); };
    virtual ~TextQuery() = default ;
    TextQuery& operator=(const TextQuery &) = default ;
    TextQuery& operator=(TextQuery &&) = default ;
    virtual void validate() const override {
        DARABONBA_VALIDATE_REQUIRED(queryString_);
    };
    virtual void fromMap(const Darabonba::Json &obj) override { from_json(obj, *this); validate(); };
    virtual Darabonba::Json toMap() const override { Darabonba::Json obj; to_json(obj, *this); return obj; };
    virtual bool empty() const override { this->queryString_ != nullptr
        && this->queryParams_ != nullptr && this->filter_ != nullptr && this->weight_ != nullptr && this->terminateAfter_ != nullptr; };
    // queryString Field Functions 
    bool hasQueryString() const { return this->queryString_ != nullptr;};
    void deleteQueryString() { this->queryString_ = nullptr;};
    inline string queryString() const { DARABONBA_PTR_GET_DEFAULT(queryString_, "") };
    inline TextQuery& setQueryString(string queryString) { DARABONBA_PTR_SET_VALUE(queryString_, queryString) };


    // queryParams Field Functions 
    bool hasQueryParams() const { return this->queryParams_ != nullptr;};
    void deleteQueryParams() { this->queryParams_ = nullptr;};
    inline const map<string, string> & queryParams() const { DARABONBA_PTR_GET_CONST(queryParams_, map<string, string>) };
    inline map<string, string> queryParams() { DARABONBA_PTR_GET(queryParams_, map<string, string>) };
    inline TextQuery& setQueryParams(const map<string, string> & queryParams) { DARABONBA_PTR_SET_VALUE(queryParams_, queryParams) };
    inline TextQuery& setQueryParams(map<string, string> && queryParams) { DARABONBA_PTR_SET_RVALUE(queryParams_, queryParams) };


    // filter Field Functions 
    bool hasFilter() const { return this->filter_ != nullptr;};
    void deleteFilter() { this->filter_ = nullptr;};
    inline string filter() const { DARABONBA_PTR_GET_DEFAULT(filter_, "") };
    inline TextQuery& setFilter(string filter) { DARABONBA_PTR_SET_VALUE(filter_, filter) };


    // weight Field Functions 
    bool hasWeight() const { return this->weight_ != nullptr;};
    void deleteWeight() { this->weight_ = nullptr;};
    inline float weight() const { DARABONBA_PTR_GET_DEFAULT(weight_, 0.0) };
    inline TextQuery& setWeight(float weight) { DARABONBA_PTR_SET_VALUE(weight_, weight) };


    // terminateAfter Field Functions 
    bool hasTerminateAfter() const { return this->terminateAfter_ != nullptr;};
    void deleteTerminateAfter() { this->terminateAfter_ = nullptr;};
    inline int32_t terminateAfter() const { DARABONBA_PTR_GET_DEFAULT(terminateAfter_, 0) };
    inline TextQuery& setTerminateAfter(int32_t terminateAfter) { DARABONBA_PTR_SET_VALUE(terminateAfter_, terminateAfter) };


  protected:
    // ha3 query语法，支持多个文本索引的AND、OR嵌套
    std::shared_ptr<string> queryString_ = nullptr;
    // query查询参数：
    //       default_op: 指定在该次查询中使用的默认query 分词后的连接操作符，AND or OR。默认为AND。
    //       global_analyzer: 查询中指定全局的分词器，该分词器会覆盖schema的分词器，指定的值必须在analyzer.json里有配置。
    //       specific_index_analyzer: 查询中指定index使用另外的分词器，该分词器会覆盖global_analyzer和schema的分词器。
    //       no_token_indexes: 支持查询中指定的index不分词（除分词以外的其他流程如归一化、去停用词会正常执行），多个index之间用;分割。
    //       remove_stopwords: true or false 表示是否需要删除stop words，stop words在分词器中配置。默认true
    std::shared_ptr<map<string, string>> queryParams_ = nullptr;
    // 过滤条件表达式
    std::shared_ptr<string> filter_ = nullptr;
    // text查询结果的权重，以score * weight的结果作为该路的排序分
    std::shared_ptr<float> weight_ = nullptr;
    // 每个分片查找满足条件的文档的最大数量。到达这个数量后，查询将提前结束，不再继续查询索引。默认为0，不设置限制。
    std::shared_ptr<int32_t> terminateAfter_ = nullptr;
  };

  } // namespace Models
} // namespace AlibabaCloud
} // namespace HA3
#endif
