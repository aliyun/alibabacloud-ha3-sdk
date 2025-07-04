// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_MODELS_PUSHDOCUMENTSREQUEST_HPP_
#define ALIBABACLOUD_MODELS_PUSHDOCUMENTSREQUEST_HPP_
#include <darabonba/Core.hpp>
#include <map>
#include <vector>
using namespace std;
using json = nlohmann::json;
namespace AlibabaCloud
{
namespace HA3
{
namespace Models
{
  class PushDocumentsRequest : public Darabonba::Model {
  public:
    friend void to_json(Darabonba::Json& j, const PushDocumentsRequest& obj) { 
      DARABONBA_PTR_TO_JSON(headers, headers_);
      DARABONBA_PTR_TO_JSON(body, body_);
    };
    friend void from_json(const Darabonba::Json& j, PushDocumentsRequest& obj) { 
      DARABONBA_PTR_FROM_JSON(headers, headers_);
      DARABONBA_PTR_FROM_JSON(body, body_);
    };
    PushDocumentsRequest() = default ;
    PushDocumentsRequest(const PushDocumentsRequest &) = default ;
    PushDocumentsRequest(PushDocumentsRequest &&) = default ;
    PushDocumentsRequest(const Darabonba::Json & obj) { from_json(obj, *this); };
    virtual ~PushDocumentsRequest() = default ;
    PushDocumentsRequest& operator=(const PushDocumentsRequest &) = default ;
    PushDocumentsRequest& operator=(PushDocumentsRequest &&) = default ;
    virtual void validate() const override {
        DARABONBA_VALIDATE_REQUIRED(body_);
    };
    virtual void fromMap(const Darabonba::Json &obj) override { from_json(obj, *this); validate(); };
    virtual Darabonba::Json toMap() const override { Darabonba::Json obj; to_json(obj, *this); return obj; };
    virtual bool empty() const override { this->headers_ != nullptr
        && this->body_ != nullptr; };
    // headers Field Functions 
    bool hasHeaders() const { return this->headers_ != nullptr;};
    void deleteHeaders() { this->headers_ = nullptr;};
    inline const map<string, string> & headers() const { DARABONBA_PTR_GET_CONST(headers_, map<string, string>) };
    inline map<string, string> headers() { DARABONBA_PTR_GET(headers_, map<string, string>) };
    inline PushDocumentsRequest& setHeaders(const map<string, string> & headers) { DARABONBA_PTR_SET_VALUE(headers_, headers) };
    inline PushDocumentsRequest& setHeaders(map<string, string> && headers) { DARABONBA_PTR_SET_RVALUE(headers_, headers) };


    // body Field Functions 
    bool hasBody() const { return this->body_ != nullptr;};
    void deleteBody() { this->body_ = nullptr;};
    inline const vector<Darabonba::Json> & body() const { DARABONBA_PTR_GET_CONST(body_, vector<Darabonba::Json>) };
    inline vector<Darabonba::Json> body() { DARABONBA_PTR_GET(body_, vector<Darabonba::Json>) };
    inline PushDocumentsRequest& setBody(const vector<Darabonba::Json> & body) { DARABONBA_PTR_SET_VALUE(body_, body) };
    inline PushDocumentsRequest& setBody(vector<Darabonba::Json> && body) { DARABONBA_PTR_SET_RVALUE(body_, body) };


  protected:
    // headers
    std::shared_ptr<map<string, string>> headers_ = nullptr;
    // body
    std::shared_ptr<vector<Darabonba::Json>> body_ = nullptr;
  };

  } // namespace Models
} // namespace AlibabaCloud
} // namespace HA3
#endif
