// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_MODELS_CONFIG_HPP_
#define ALIBABACLOUD_MODELS_CONFIG_HPP_
#include <darabonba/Core.hpp>
#include <darabonba/Runtime.hpp>
using namespace std;
using json = nlohmann::json;
namespace AlibabaCloud
{
namespace HA3
{
namespace Models
{
  class Config : public Darabonba::Model {
  public:
    friend void to_json(Darabonba::Json& j, const Config& obj) { 
      DARABONBA_PTR_TO_JSON(endpoint, endpoint_);
      DARABONBA_PTR_TO_JSON(instanceId, instanceId_);
      DARABONBA_PTR_TO_JSON(protocol, protocol_);
      DARABONBA_PTR_TO_JSON(accessUserName, accessUserName_);
      DARABONBA_PTR_TO_JSON(accessPassWord, accessPassWord_);
      DARABONBA_PTR_TO_JSON(userAgent, userAgent_);
      DARABONBA_PTR_TO_JSON(runtimeOptions, runtimeOptions_);
    };
    friend void from_json(const Darabonba::Json& j, Config& obj) { 
      DARABONBA_PTR_FROM_JSON(endpoint, endpoint_);
      DARABONBA_PTR_FROM_JSON(instanceId, instanceId_);
      DARABONBA_PTR_FROM_JSON(protocol, protocol_);
      DARABONBA_PTR_FROM_JSON(accessUserName, accessUserName_);
      DARABONBA_PTR_FROM_JSON(accessPassWord, accessPassWord_);
      DARABONBA_PTR_FROM_JSON(userAgent, userAgent_);
      DARABONBA_PTR_FROM_JSON(runtimeOptions, runtimeOptions_);
    };
    Config() = default ;
    Config(const Config &) = default ;
    Config(Config &&) = default ;
    Config(const Darabonba::Json & obj) { from_json(obj, *this); };
    virtual ~Config() = default ;
    Config& operator=(const Config &) = default ;
    Config& operator=(Config &&) = default ;
    virtual void validate() const override {
    };
    virtual void fromMap(const Darabonba::Json &obj) override { from_json(obj, *this); validate(); };
    virtual Darabonba::Json toMap() const override { Darabonba::Json obj; to_json(obj, *this); return obj; };
    virtual bool empty() const override { this->endpoint_ != nullptr
        && this->instanceId_ != nullptr && this->protocol_ != nullptr && this->accessUserName_ != nullptr && this->accessPassWord_ != nullptr && this->userAgent_ != nullptr
        && this->runtimeOptions_ != nullptr; };
    // endpoint Field Functions 
    bool hasEndpoint() const { return this->endpoint_ != nullptr;};
    void deleteEndpoint() { this->endpoint_ = nullptr;};
    inline string endpoint() const { DARABONBA_PTR_GET_DEFAULT(endpoint_, "") };
    inline Config& setEndpoint(string endpoint) { DARABONBA_PTR_SET_VALUE(endpoint_, endpoint) };


    // instanceId Field Functions 
    bool hasInstanceId() const { return this->instanceId_ != nullptr;};
    void deleteInstanceId() { this->instanceId_ = nullptr;};
    inline string instanceId() const { DARABONBA_PTR_GET_DEFAULT(instanceId_, "") };
    inline Config& setInstanceId(string instanceId) { DARABONBA_PTR_SET_VALUE(instanceId_, instanceId) };


    // protocol Field Functions 
    bool hasProtocol() const { return this->protocol_ != nullptr;};
    void deleteProtocol() { this->protocol_ = nullptr;};
    inline string protocol() const { DARABONBA_PTR_GET_DEFAULT(protocol_, "") };
    inline Config& setProtocol(string protocol) { DARABONBA_PTR_SET_VALUE(protocol_, protocol) };


    // accessUserName Field Functions 
    bool hasAccessUserName() const { return this->accessUserName_ != nullptr;};
    void deleteAccessUserName() { this->accessUserName_ = nullptr;};
    inline string accessUserName() const { DARABONBA_PTR_GET_DEFAULT(accessUserName_, "") };
    inline Config& setAccessUserName(string accessUserName) { DARABONBA_PTR_SET_VALUE(accessUserName_, accessUserName) };


    // accessPassWord Field Functions 
    bool hasAccessPassWord() const { return this->accessPassWord_ != nullptr;};
    void deleteAccessPassWord() { this->accessPassWord_ = nullptr;};
    inline string accessPassWord() const { DARABONBA_PTR_GET_DEFAULT(accessPassWord_, "") };
    inline Config& setAccessPassWord(string accessPassWord) { DARABONBA_PTR_SET_VALUE(accessPassWord_, accessPassWord) };


    // userAgent Field Functions 
    bool hasUserAgent() const { return this->userAgent_ != nullptr;};
    void deleteUserAgent() { this->userAgent_ = nullptr;};
    inline string userAgent() const { DARABONBA_PTR_GET_DEFAULT(userAgent_, "") };
    inline Config& setUserAgent(string userAgent) { DARABONBA_PTR_SET_VALUE(userAgent_, userAgent) };


    // runtimeOptions Field Functions 
    bool hasRuntimeOptions() const { return this->runtimeOptions_ != nullptr;};
    void deleteRuntimeOptions() { this->runtimeOptions_ = nullptr;};
    inline const Darabonba::RuntimeOptions & runtimeOptions() const { DARABONBA_PTR_GET_CONST(runtimeOptions_, Darabonba::RuntimeOptions) };
    inline Darabonba::RuntimeOptions runtimeOptions() { DARABONBA_PTR_GET(runtimeOptions_, Darabonba::RuntimeOptions) };
    inline Config& setRuntimeOptions(const Darabonba::RuntimeOptions & runtimeOptions) { DARABONBA_PTR_SET_VALUE(runtimeOptions_, runtimeOptions) };
    inline Config& setRuntimeOptions(Darabonba::RuntimeOptions && runtimeOptions) { DARABONBA_PTR_SET_RVALUE(runtimeOptions_, runtimeOptions) };


  protected:
    std::shared_ptr<string> endpoint_ = nullptr;
    std::shared_ptr<string> instanceId_ = nullptr;
    std::shared_ptr<string> protocol_ = nullptr;
    std::shared_ptr<string> accessUserName_ = nullptr;
    std::shared_ptr<string> accessPassWord_ = nullptr;
    std::shared_ptr<string> userAgent_ = nullptr;
    std::shared_ptr<Darabonba::RuntimeOptions> runtimeOptions_ = nullptr;
  };

  } // namespace Models
} // namespace AlibabaCloud
} // namespace HA3
#endif
