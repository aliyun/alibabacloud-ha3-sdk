// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_MODELS_ORDERBYDESC_HPP_
#define ALIBABACLOUD_MODELS_ORDERBYDESC_HPP_
#include <darabonba/Core.hpp>
using namespace std;
using json = nlohmann::json;
namespace AlibabaCloud
{
namespace HA3
{
namespace Models
{
  class OrderByDesc : public Darabonba::Model {
  public:
    friend void to_json(Darabonba::Json& j, const OrderByDesc& obj) { 
      DARABONBA_PTR_TO_JSON(field, field_);
      DARABONBA_PTR_TO_JSON(direction, direction_);
    };
    friend void from_json(const Darabonba::Json& j, OrderByDesc& obj) { 
      DARABONBA_PTR_FROM_JSON(field, field_);
      DARABONBA_PTR_FROM_JSON(direction, direction_);
    };
    OrderByDesc() = default ;
    OrderByDesc(const OrderByDesc &) = default ;
    OrderByDesc(OrderByDesc &&) = default ;
    OrderByDesc(const Darabonba::Json & obj) { from_json(obj, *this); };
    virtual ~OrderByDesc() = default ;
    OrderByDesc& operator=(const OrderByDesc &) = default ;
    OrderByDesc& operator=(OrderByDesc &&) = default ;
    virtual void validate() const override {
        DARABONBA_VALIDATE_REQUIRED(field_);
    };
    virtual void fromMap(const Darabonba::Json &obj) override { from_json(obj, *this); validate(); };
    virtual Darabonba::Json toMap() const override { Darabonba::Json obj; to_json(obj, *this); return obj; };
    virtual bool empty() const override { this->field_ != nullptr
        && this->direction_ != nullptr; };
    // field Field Functions 
    bool hasField() const { return this->field_ != nullptr;};
    void deleteField() { this->field_ = nullptr;};
    inline string field() const { DARABONBA_PTR_GET_DEFAULT(field_, "") };
    inline OrderByDesc& setField(string field) { DARABONBA_PTR_SET_VALUE(field_, field) };


    // direction Field Functions 
    bool hasDirection() const { return this->direction_ != nullptr;};
    void deleteDirection() { this->direction_ = nullptr;};
    inline string direction() const { DARABONBA_PTR_GET_DEFAULT(direction_, "") };
    inline OrderByDesc& setDirection(string direction) { DARABONBA_PTR_SET_VALUE(direction_, direction) };


  protected:
    // 排序字段名称，必须指定结果集中的字段
    std::shared_ptr<string> field_ = nullptr;
    // 排序方向，DESC: 降序排列；ASC: 升序排列
    std::shared_ptr<string> direction_ = nullptr;
  };

  } // namespace Models
} // namespace AlibabaCloud
} // namespace HA3
#endif
