// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_MODELS_SPARSEDATA_HPP_
#define ALIBABACLOUD_MODELS_SPARSEDATA_HPP_
#include <darabonba/Core.hpp>
#include <vector>
using namespace std;
using json = nlohmann::json;
namespace AlibabaCloud
{
namespace HA3
{
namespace Models
{
  class SparseData : public Darabonba::Model {
  public:
    friend void to_json(Darabonba::Json& j, const SparseData& obj) { 
      DARABONBA_PTR_TO_JSON(count, count_);
      DARABONBA_PTR_TO_JSON(indices, indices_);
      DARABONBA_PTR_TO_JSON(values, values_);
    };
    friend void from_json(const Darabonba::Json& j, SparseData& obj) { 
      DARABONBA_PTR_FROM_JSON(count, count_);
      DARABONBA_PTR_FROM_JSON(indices, indices_);
      DARABONBA_PTR_FROM_JSON(values, values_);
    };
    SparseData() = default ;
    SparseData(const SparseData &) = default ;
    SparseData(SparseData &&) = default ;
    SparseData(const Darabonba::Json & obj) { from_json(obj, *this); };
    virtual ~SparseData() = default ;
    SparseData& operator=(const SparseData &) = default ;
    SparseData& operator=(SparseData &&) = default ;
    virtual void validate() const override {
        DARABONBA_VALIDATE_REQUIRED(indices_);
        DARABONBA_VALIDATE_REQUIRED(values_);
    };
    virtual void fromMap(const Darabonba::Json &obj) override { from_json(obj, *this); validate(); };
    virtual Darabonba::Json toMap() const override { Darabonba::Json obj; to_json(obj, *this); return obj; };
    virtual bool empty() const override { this->count_ != nullptr
        && this->indices_ != nullptr && this->values_ != nullptr; };
    // count Field Functions 
    bool hasCount() const { return this->count_ != nullptr;};
    void deleteCount() { this->count_ = nullptr;};
    inline const vector<int32_t> & count() const { DARABONBA_PTR_GET_CONST(count_, vector<int32_t>) };
    inline vector<int32_t> count() { DARABONBA_PTR_GET(count_, vector<int32_t>) };
    inline SparseData& setCount(const vector<int32_t> & count) { DARABONBA_PTR_SET_VALUE(count_, count) };
    inline SparseData& setCount(vector<int32_t> && count) { DARABONBA_PTR_SET_RVALUE(count_, count) };


    // indices Field Functions 
    bool hasIndices() const { return this->indices_ != nullptr;};
    void deleteIndices() { this->indices_ = nullptr;};
    inline const vector<int64_t> & indices() const { DARABONBA_PTR_GET_CONST(indices_, vector<int64_t>) };
    inline vector<int64_t> indices() { DARABONBA_PTR_GET(indices_, vector<int64_t>) };
    inline SparseData& setIndices(const vector<int64_t> & indices) { DARABONBA_PTR_SET_VALUE(indices_, indices) };
    inline SparseData& setIndices(vector<int64_t> && indices) { DARABONBA_PTR_SET_RVALUE(indices_, indices) };


    // values Field Functions 
    bool hasValues() const { return this->values_ != nullptr;};
    void deleteValues() { this->values_ = nullptr;};
    inline const vector<float> & values() const { DARABONBA_PTR_GET_CONST(values_, vector<float>) };
    inline vector<float> values() { DARABONBA_PTR_GET(values_, vector<float>) };
    inline SparseData& setValues(const vector<float> & values) { DARABONBA_PTR_SET_VALUE(values_, values) };
    inline SparseData& setValues(vector<float> && values) { DARABONBA_PTR_SET_RVALUE(values_, values) };


  protected:
    // 每个稀疏向量中包含的元素个数
    std::shared_ptr<vector<int32_t>> count_ = nullptr;
    // 元素下标（需要从小到大排序）
    std::shared_ptr<vector<int64_t>> indices_ = nullptr;
    // 元素值（与下标一一对应）
    std::shared_ptr<vector<float>> values_ = nullptr;
  };

  } // namespace Models
} // namespace AlibabaCloud
} // namespace HA3
#endif
