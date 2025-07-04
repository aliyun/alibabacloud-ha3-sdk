// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_MODELS_QUERYREQUEST_HPP_
#define ALIBABACLOUD_MODELS_QUERYREQUEST_HPP_
#include <darabonba/Core.hpp>
#include <vector>
#include <alibabacloud/models/SparseData.hpp>
#include <map>
#include <alibabacloud/models/Sort.hpp>
using namespace std;
using json = nlohmann::json;
namespace AlibabaCloud
{
namespace HA3
{
namespace Models
{
  class QueryRequest : public Darabonba::Model {
  public:
    friend void to_json(Darabonba::Json& j, const QueryRequest& obj) { 
      DARABONBA_PTR_TO_JSON(tableName, tableName_);
      DARABONBA_PTR_TO_JSON(vector, vector_);
      DARABONBA_PTR_TO_JSON(namespace, namespace_);
      DARABONBA_PTR_TO_JSON(topK, topK_);
      DARABONBA_PTR_TO_JSON(indexName, indexName_);
      DARABONBA_PTR_TO_JSON(sparseData, sparseData_);
      DARABONBA_PTR_TO_JSON(weight, weight_);
      DARABONBA_PTR_TO_JSON(content, content_);
      DARABONBA_PTR_TO_JSON(modal, modal_);
      DARABONBA_PTR_TO_JSON(includeVector, includeVector_);
      DARABONBA_PTR_TO_JSON(outputFields, outputFields_);
      DARABONBA_PTR_TO_JSON(order, order_);
      DARABONBA_PTR_TO_JSON(searchParams, searchParams_);
      DARABONBA_PTR_TO_JSON(filter, filter_);
      DARABONBA_PTR_TO_JSON(scoreThreshold, scoreThreshold_);
      DARABONBA_PTR_TO_JSON(vectorCount, vectorCount_);
      DARABONBA_PTR_TO_JSON(sort, sort_);
      DARABONBA_PTR_TO_JSON(kvpairs, kvpairs_);
      DARABONBA_PTR_TO_JSON(contentType, contentType_);
      DARABONBA_PTR_TO_JSON(videoFrameTopK, videoFrameTopK_);
      DARABONBA_PTR_TO_JSON(sorts, sorts_);
    };
    friend void from_json(const Darabonba::Json& j, QueryRequest& obj) { 
      DARABONBA_PTR_FROM_JSON(tableName, tableName_);
      DARABONBA_PTR_FROM_JSON(vector, vector_);
      DARABONBA_PTR_FROM_JSON(namespace, namespace_);
      DARABONBA_PTR_FROM_JSON(topK, topK_);
      DARABONBA_PTR_FROM_JSON(indexName, indexName_);
      DARABONBA_PTR_FROM_JSON(sparseData, sparseData_);
      DARABONBA_PTR_FROM_JSON(weight, weight_);
      DARABONBA_PTR_FROM_JSON(content, content_);
      DARABONBA_PTR_FROM_JSON(modal, modal_);
      DARABONBA_PTR_FROM_JSON(includeVector, includeVector_);
      DARABONBA_PTR_FROM_JSON(outputFields, outputFields_);
      DARABONBA_PTR_FROM_JSON(order, order_);
      DARABONBA_PTR_FROM_JSON(searchParams, searchParams_);
      DARABONBA_PTR_FROM_JSON(filter, filter_);
      DARABONBA_PTR_FROM_JSON(scoreThreshold, scoreThreshold_);
      DARABONBA_PTR_FROM_JSON(vectorCount, vectorCount_);
      DARABONBA_PTR_FROM_JSON(sort, sort_);
      DARABONBA_PTR_FROM_JSON(kvpairs, kvpairs_);
      DARABONBA_PTR_FROM_JSON(contentType, contentType_);
      DARABONBA_PTR_FROM_JSON(videoFrameTopK, videoFrameTopK_);
      DARABONBA_PTR_FROM_JSON(sorts, sorts_);
    };
    QueryRequest() = default ;
    QueryRequest(const QueryRequest &) = default ;
    QueryRequest(QueryRequest &&) = default ;
    QueryRequest(const Darabonba::Json & obj) { from_json(obj, *this); };
    virtual ~QueryRequest() = default ;
    QueryRequest& operator=(const QueryRequest &) = default ;
    QueryRequest& operator=(QueryRequest &&) = default ;
    virtual void validate() const override {
        DARABONBA_VALIDATE_REQUIRED(tableName_);
        DARABONBA_VALIDATE_REQUIRED(vector_);
    };
    virtual void fromMap(const Darabonba::Json &obj) override { from_json(obj, *this); validate(); };
    virtual Darabonba::Json toMap() const override { Darabonba::Json obj; to_json(obj, *this); return obj; };
    virtual bool empty() const override { this->tableName_ != nullptr
        && this->vector_ != nullptr && this->namespace_ != nullptr && this->topK_ != nullptr && this->indexName_ != nullptr && this->sparseData_ != nullptr
        && this->weight_ != nullptr && this->content_ != nullptr && this->modal_ != nullptr && this->includeVector_ != nullptr && this->outputFields_ != nullptr
        && this->order_ != nullptr && this->searchParams_ != nullptr && this->filter_ != nullptr && this->scoreThreshold_ != nullptr && this->vectorCount_ != nullptr
        && this->sort_ != nullptr && this->kvpairs_ != nullptr && this->contentType_ != nullptr && this->videoFrameTopK_ != nullptr && this->sorts_ != nullptr; };
    // tableName Field Functions 
    bool hasTableName() const { return this->tableName_ != nullptr;};
    void deleteTableName() { this->tableName_ = nullptr;};
    inline string tableName() const { DARABONBA_PTR_GET_DEFAULT(tableName_, "") };
    inline QueryRequest& setTableName(string tableName) { DARABONBA_PTR_SET_VALUE(tableName_, tableName) };


    // vector Field Functions 
    bool hasVector() const { return this->vector_ != nullptr;};
    void deleteVector() { this->vector_ = nullptr;};
    inline const vector<float> & _vector() const { DARABONBA_PTR_GET_CONST(vector_, vector<float>) };
    inline vector<float> _vector() { DARABONBA_PTR_GET(vector_, vector<float>) };
    inline QueryRequest& setVector(const vector<float> & _vector) { DARABONBA_PTR_SET_VALUE(vector_, _vector) };
    inline QueryRequest& setVector(vector<float> && _vector) { DARABONBA_PTR_SET_RVALUE(vector_, _vector) };


    // namespace Field Functions 
    bool hasNamespace() const { return this->namespace_ != nullptr;};
    void deleteNamespace() { this->namespace_ = nullptr;};
    inline string _namespace() const { DARABONBA_PTR_GET_DEFAULT(namespace_, "") };
    inline QueryRequest& setNamespace(string _namespace) { DARABONBA_PTR_SET_VALUE(namespace_, _namespace) };


    // topK Field Functions 
    bool hasTopK() const { return this->topK_ != nullptr;};
    void deleteTopK() { this->topK_ = nullptr;};
    inline int32_t topK() const { DARABONBA_PTR_GET_DEFAULT(topK_, 0) };
    inline QueryRequest& setTopK(int32_t topK) { DARABONBA_PTR_SET_VALUE(topK_, topK) };


    // indexName Field Functions 
    bool hasIndexName() const { return this->indexName_ != nullptr;};
    void deleteIndexName() { this->indexName_ = nullptr;};
    inline string indexName() const { DARABONBA_PTR_GET_DEFAULT(indexName_, "") };
    inline QueryRequest& setIndexName(string indexName) { DARABONBA_PTR_SET_VALUE(indexName_, indexName) };


    // sparseData Field Functions 
    bool hasSparseData() const { return this->sparseData_ != nullptr;};
    void deleteSparseData() { this->sparseData_ = nullptr;};
    inline const SparseData & sparseData() const { DARABONBA_PTR_GET_CONST(sparseData_, SparseData) };
    inline SparseData sparseData() { DARABONBA_PTR_GET(sparseData_, SparseData) };
    inline QueryRequest& setSparseData(const SparseData & sparseData) { DARABONBA_PTR_SET_VALUE(sparseData_, sparseData) };
    inline QueryRequest& setSparseData(SparseData && sparseData) { DARABONBA_PTR_SET_RVALUE(sparseData_, sparseData) };


    // weight Field Functions 
    bool hasWeight() const { return this->weight_ != nullptr;};
    void deleteWeight() { this->weight_ = nullptr;};
    inline float weight() const { DARABONBA_PTR_GET_DEFAULT(weight_, 0.0) };
    inline QueryRequest& setWeight(float weight) { DARABONBA_PTR_SET_VALUE(weight_, weight) };


    // content Field Functions 
    bool hasContent() const { return this->content_ != nullptr;};
    void deleteContent() { this->content_ = nullptr;};
    inline string content() const { DARABONBA_PTR_GET_DEFAULT(content_, "") };
    inline QueryRequest& setContent(string content) { DARABONBA_PTR_SET_VALUE(content_, content) };


    // modal Field Functions 
    bool hasModal() const { return this->modal_ != nullptr;};
    void deleteModal() { this->modal_ = nullptr;};
    inline string modal() const { DARABONBA_PTR_GET_DEFAULT(modal_, "") };
    inline QueryRequest& setModal(string modal) { DARABONBA_PTR_SET_VALUE(modal_, modal) };


    // includeVector Field Functions 
    bool hasIncludeVector() const { return this->includeVector_ != nullptr;};
    void deleteIncludeVector() { this->includeVector_ = nullptr;};
    inline bool includeVector() const { DARABONBA_PTR_GET_DEFAULT(includeVector_, false) };
    inline QueryRequest& setIncludeVector(bool includeVector) { DARABONBA_PTR_SET_VALUE(includeVector_, includeVector) };


    // outputFields Field Functions 
    bool hasOutputFields() const { return this->outputFields_ != nullptr;};
    void deleteOutputFields() { this->outputFields_ = nullptr;};
    inline const vector<string> & outputFields() const { DARABONBA_PTR_GET_CONST(outputFields_, vector<string>) };
    inline vector<string> outputFields() { DARABONBA_PTR_GET(outputFields_, vector<string>) };
    inline QueryRequest& setOutputFields(const vector<string> & outputFields) { DARABONBA_PTR_SET_VALUE(outputFields_, outputFields) };
    inline QueryRequest& setOutputFields(vector<string> && outputFields) { DARABONBA_PTR_SET_RVALUE(outputFields_, outputFields) };


    // order Field Functions 
    bool hasOrder() const { return this->order_ != nullptr;};
    void deleteOrder() { this->order_ = nullptr;};
    inline string order() const { DARABONBA_PTR_GET_DEFAULT(order_, "") };
    inline QueryRequest& setOrder(string order) { DARABONBA_PTR_SET_VALUE(order_, order) };


    // searchParams Field Functions 
    bool hasSearchParams() const { return this->searchParams_ != nullptr;};
    void deleteSearchParams() { this->searchParams_ = nullptr;};
    inline string searchParams() const { DARABONBA_PTR_GET_DEFAULT(searchParams_, "") };
    inline QueryRequest& setSearchParams(string searchParams) { DARABONBA_PTR_SET_VALUE(searchParams_, searchParams) };


    // filter Field Functions 
    bool hasFilter() const { return this->filter_ != nullptr;};
    void deleteFilter() { this->filter_ = nullptr;};
    inline string filter() const { DARABONBA_PTR_GET_DEFAULT(filter_, "") };
    inline QueryRequest& setFilter(string filter) { DARABONBA_PTR_SET_VALUE(filter_, filter) };


    // scoreThreshold Field Functions 
    bool hasScoreThreshold() const { return this->scoreThreshold_ != nullptr;};
    void deleteScoreThreshold() { this->scoreThreshold_ = nullptr;};
    inline float scoreThreshold() const { DARABONBA_PTR_GET_DEFAULT(scoreThreshold_, 0.0) };
    inline QueryRequest& setScoreThreshold(float scoreThreshold) { DARABONBA_PTR_SET_VALUE(scoreThreshold_, scoreThreshold) };


    // vectorCount Field Functions 
    bool hasVectorCount() const { return this->vectorCount_ != nullptr;};
    void deleteVectorCount() { this->vectorCount_ = nullptr;};
    inline int32_t vectorCount() const { DARABONBA_PTR_GET_DEFAULT(vectorCount_, 0) };
    inline QueryRequest& setVectorCount(int32_t vectorCount) { DARABONBA_PTR_SET_VALUE(vectorCount_, vectorCount) };


    // sort Field Functions 
    bool hasSort() const { return this->sort_ != nullptr;};
    void deleteSort() { this->sort_ = nullptr;};
    inline string sort() const { DARABONBA_PTR_GET_DEFAULT(sort_, "") };
    inline QueryRequest& setSort(string sort) { DARABONBA_PTR_SET_VALUE(sort_, sort) };


    // kvpairs Field Functions 
    bool hasKvpairs() const { return this->kvpairs_ != nullptr;};
    void deleteKvpairs() { this->kvpairs_ = nullptr;};
    inline const map<string, string> & kvpairs() const { DARABONBA_PTR_GET_CONST(kvpairs_, map<string, string>) };
    inline map<string, string> kvpairs() { DARABONBA_PTR_GET(kvpairs_, map<string, string>) };
    inline QueryRequest& setKvpairs(const map<string, string> & kvpairs) { DARABONBA_PTR_SET_VALUE(kvpairs_, kvpairs) };
    inline QueryRequest& setKvpairs(map<string, string> && kvpairs) { DARABONBA_PTR_SET_RVALUE(kvpairs_, kvpairs) };


    // contentType Field Functions 
    bool hasContentType() const { return this->contentType_ != nullptr;};
    void deleteContentType() { this->contentType_ = nullptr;};
    inline string contentType() const { DARABONBA_PTR_GET_DEFAULT(contentType_, "") };
    inline QueryRequest& setContentType(string contentType) { DARABONBA_PTR_SET_VALUE(contentType_, contentType) };


    // videoFrameTopK Field Functions 
    bool hasVideoFrameTopK() const { return this->videoFrameTopK_ != nullptr;};
    void deleteVideoFrameTopK() { this->videoFrameTopK_ = nullptr;};
    inline int32_t videoFrameTopK() const { DARABONBA_PTR_GET_DEFAULT(videoFrameTopK_, 0) };
    inline QueryRequest& setVideoFrameTopK(int32_t videoFrameTopK) { DARABONBA_PTR_SET_VALUE(videoFrameTopK_, videoFrameTopK) };


    // sorts Field Functions 
    bool hasSorts() const { return this->sorts_ != nullptr;};
    void deleteSorts() { this->sorts_ = nullptr;};
    inline const vector<Sort> & sorts() const { DARABONBA_PTR_GET_CONST(sorts_, vector<Sort>) };
    inline vector<Sort> sorts() { DARABONBA_PTR_GET(sorts_, vector<Sort>) };
    inline QueryRequest& setSorts(const vector<Sort> & sorts) { DARABONBA_PTR_SET_VALUE(sorts_, sorts) };
    inline QueryRequest& setSorts(vector<Sort> && sorts) { DARABONBA_PTR_SET_RVALUE(sorts_, sorts) };


  protected:
    // 数据源名
    std::shared_ptr<string> tableName_ = nullptr;
    // 向量数据
    std::shared_ptr<vector<float>> vector_ = nullptr;
    // 查询向量的空间
    std::shared_ptr<string> namespace_ = nullptr;
    // 返回个数
    std::shared_ptr<int32_t> topK_ = nullptr;
    // 查询的索引名
    std::shared_ptr<string> indexName_ = nullptr;
    // 查询的稀疏向量
    std::shared_ptr<SparseData> sparseData_ = nullptr;
    // Query的权重
    std::shared_ptr<float> weight_ = nullptr;
    // 需要向量化的内容
    std::shared_ptr<string> content_ = nullptr;
    // 使用的模型
    std::shared_ptr<string> modal_ = nullptr;
    // 是否返回文档中的向量信息
    std::shared_ptr<bool> includeVector_ = nullptr;
    // 需要返回值的字段列表
    std::shared_ptr<vector<string>> outputFields_ = nullptr;
    // 排序顺序, ASC：升序  DESC: 降序
    std::shared_ptr<string> order_ = nullptr;
    // 查询参数
    std::shared_ptr<string> searchParams_ = nullptr;
    // 过滤表达式
    std::shared_ptr<string> filter_ = nullptr;
    // 分数过滤， 使用欧式距离时，只返回小于scoreThreshold的结果。使用内积时，只返回大于scoreThreshold的结果
    std::shared_ptr<float> scoreThreshold_ = nullptr;
    // vector字段中包含的向量个数
    std::shared_ptr<int32_t> vectorCount_ = nullptr;
    // 排序表达式
    std::shared_ptr<string> sort_ = nullptr;
    // kvpairs
    std::shared_ptr<map<string, string>> kvpairs_ = nullptr;
    // 视频预测数据类型：text、image、video_uri、video_base64
    std::shared_ptr<string> contentType_ = nullptr;
    // 召回帧的数量，默认值为100
    std::shared_ptr<int32_t> videoFrameTopK_ = nullptr;
    // 多维排序，配置sorts后，结果中的score字段会变成多值字段，对应每一维排序的分数
    std::shared_ptr<vector<Sort>> sorts_ = nullptr;
  };

  } // namespace Models
} // namespace AlibabaCloud
} // namespace HA3
#endif
