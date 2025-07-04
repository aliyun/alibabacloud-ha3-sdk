// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_MODELS_SORT_HPP_
#define ALIBABACLOUD_MODELS_SORT_HPP_
#include <darabonba/Core.hpp>
using namespace std;
using json = nlohmann::json;
namespace AlibabaCloud
{
namespace HA3
{
namespace Models
{
  class Sort : public Darabonba::Model {
  public:
    friend void to_json(Darabonba::Json& j, const Sort& obj) { 
      DARABONBA_PTR_TO_JSON(order, order_);
      DARABONBA_PTR_TO_JSON(expression, expression_);
    };
    friend void from_json(const Darabonba::Json& j, Sort& obj) { 
      DARABONBA_PTR_FROM_JSON(order, order_);
      DARABONBA_PTR_FROM_JSON(expression, expression_);
    };
    Sort() = default ;
    Sort(const Sort &) = default ;
    Sort(Sort &&) = default ;
    Sort(const Darabonba::Json & obj) { from_json(obj, *this); };
    virtual ~Sort() = default ;
    Sort& operator=(const Sort &) = default ;
    Sort& operator=(Sort &&) = default ;
    virtual void validate() const override {
    };
    virtual void fromMap(const Darabonba::Json &obj) override { from_json(obj, *this); validate(); };
    virtual Darabonba::Json toMap() const override { Darabonba::Json obj; to_json(obj, *this); return obj; };
    virtual bool empty() const override { this->order_ != nullptr
        && this->expression_ != nullptr; };
    // order Field Functions 
    bool hasOrder() const { return this->order_ != nullptr;};
    void deleteOrder() { this->order_ = nullptr;};
    inline string order() const { DARABONBA_PTR_GET_DEFAULT(order_, "") };
    inline Sort& setOrder(string order) { DARABONBA_PTR_SET_VALUE(order_, order) };


    // expression Field Functions 
    bool hasExpression() const { return this->expression_ != nullptr;};
    void deleteExpression() { this->expression_ = nullptr;};
    inline string expression() const { DARABONBA_PTR_GET_DEFAULT(expression_, "") };
    inline Sort& setExpression(string expression) { DARABONBA_PTR_SET_VALUE(expression_, expression) };


  protected:
    // 排序顺序, ASC：升序  DESC: 降序
    std::shared_ptr<string> order_ = nullptr;
    // 表达式
    std::shared_ptr<string> expression_ = nullptr;
  };

  } // namespace Models
} // namespace AlibabaCloud
} // namespace HA3
#endif
