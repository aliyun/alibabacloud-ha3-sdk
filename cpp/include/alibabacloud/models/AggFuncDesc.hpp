// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_MODELS_AGGFUNCDESC_HPP_
#define ALIBABACLOUD_MODELS_AGGFUNCDESC_HPP_
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
  class AggFuncDesc : public Darabonba::Model {
  public:
    friend void to_json(Darabonba::Json& j, const AggFuncDesc& obj) { 
      DARABONBA_PTR_TO_JSON(name, name_);
      DARABONBA_PTR_TO_JSON(func, func_);
      DARABONBA_PTR_TO_JSON(args, args_);
    };
    friend void from_json(const Darabonba::Json& j, AggFuncDesc& obj) { 
      DARABONBA_PTR_FROM_JSON(name, name_);
      DARABONBA_PTR_FROM_JSON(func, func_);
      DARABONBA_PTR_FROM_JSON(args, args_);
    };
    AggFuncDesc() = default ;
    AggFuncDesc(const AggFuncDesc &) = default ;
    AggFuncDesc(AggFuncDesc &&) = default ;
    AggFuncDesc(const Darabonba::Json & obj) { from_json(obj, *this); };
    virtual ~AggFuncDesc() = default ;
    AggFuncDesc& operator=(const AggFuncDesc &) = default ;
    AggFuncDesc& operator=(AggFuncDesc &&) = default ;
    virtual void validate() const override {
        DARABONBA_VALIDATE_REQUIRED(func_);
        DARABONBA_VALIDATE_REQUIRED(args_);
    };
    virtual void fromMap(const Darabonba::Json &obj) override { from_json(obj, *this); validate(); };
    virtual Darabonba::Json toMap() const override { Darabonba::Json obj; to_json(obj, *this); return obj; };
    virtual bool empty() const override { this->name_ != nullptr
        && this->func_ != nullptr && this->args_ != nullptr; };
    // name Field Functions 
    bool hasName() const { return this->name_ != nullptr;};
    void deleteName() { this->name_ = nullptr;};
    inline string name() const { DARABONBA_PTR_GET_DEFAULT(name_, "") };
    inline AggFuncDesc& setName(string name) { DARABONBA_PTR_SET_VALUE(name_, name) };


    // func Field Functions 
    bool hasFunc() const { return this->func_ != nullptr;};
    void deleteFunc() { this->func_ = nullptr;};
    inline string func() const { DARABONBA_PTR_GET_DEFAULT(func_, "") };
    inline AggFuncDesc& setFunc(string func) { DARABONBA_PTR_SET_VALUE(func_, func) };


    // args Field Functions 
    bool hasArgs() const { return this->args_ != nullptr;};
    void deleteArgs() { this->args_ = nullptr;};
    inline const vector<string> & args() const { DARABONBA_PTR_GET_CONST(args_, vector<string>) };
    inline vector<string> args() { DARABONBA_PTR_GET(args_, vector<string>) };
    inline AggFuncDesc& setArgs(const vector<string> & args) { DARABONBA_PTR_SET_VALUE(args_, args) };
    inline AggFuncDesc& setArgs(vector<string> && args) { DARABONBA_PTR_SET_RVALUE(args_, args) };


  protected:
    // 可以指定统计值在结果集中字段的名称。默认结果字段为: FUNC_NAME(args)
    std::shared_ptr<string> name_ = nullptr;
    // 统计函数名：max, min, avg, sum, count
    std::shared_ptr<string> func_ = nullptr;
    // 统计函数的参数
    std::shared_ptr<vector<string>> args_ = nullptr;
  };

  } // namespace Models
} // namespace AlibabaCloud
} // namespace HA3
#endif
