// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_MODELS_RANKQUERY_HPP_
#define ALIBABACLOUD_MODELS_RANKQUERY_HPP_
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
  class RankQuery : public Darabonba::Model {
  public:
    friend void to_json(Darabonba::Json& j, const RankQuery& obj) { 
      DARABONBA_PTR_TO_JSON(rrf, rrf_);
    };
    friend void from_json(const Darabonba::Json& j, RankQuery& obj) { 
      DARABONBA_PTR_FROM_JSON(rrf, rrf_);
    };
    RankQuery() = default ;
    RankQuery(const RankQuery &) = default ;
    RankQuery(RankQuery &&) = default ;
    RankQuery(const Darabonba::Json & obj) { from_json(obj, *this); };
    virtual ~RankQuery() = default ;
    RankQuery& operator=(const RankQuery &) = default ;
    RankQuery& operator=(RankQuery &&) = default ;
    virtual void validate() const override {
    };
    virtual void fromMap(const Darabonba::Json &obj) override { from_json(obj, *this); validate(); };
    virtual Darabonba::Json toMap() const override { Darabonba::Json obj; to_json(obj, *this); return obj; };
    virtual bool empty() const override { this->rrf_ != nullptr; };
    // rrf Field Functions 
    bool hasRrf() const { return this->rrf_ != nullptr;};
    void deleteRrf() { this->rrf_ = nullptr;};
    inline const map<string, string> & rrf() const { DARABONBA_PTR_GET_CONST(rrf_, map<string, string>) };
    inline map<string, string> rrf() { DARABONBA_PTR_GET(rrf_, map<string, string>) };
    inline RankQuery& setRrf(const map<string, string> & rrf) { DARABONBA_PTR_SET_VALUE(rrf_, rrf) };
    inline RankQuery& setRrf(map<string, string> && rrf) { DARABONBA_PTR_SET_RVALUE(rrf_, rrf) };


  protected:
    // 查询表达式
    std::shared_ptr<map<string, string>> rrf_ = nullptr;
  };

  } // namespace Models
} // namespace AlibabaCloud
} // namespace HA3
#endif
