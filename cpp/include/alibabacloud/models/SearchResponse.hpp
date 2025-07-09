// This file is auto-generated, don't edit it. Thanks.
#ifndef ALIBABACLOUD_MODELS_SEARCHRESPONSE_HPP_
#define ALIBABACLOUD_MODELS_SEARCHRESPONSE_HPP_
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
  class SearchResponse : public Darabonba::Model {
  public:
    friend void to_json(Darabonba::Json& j, const SearchResponse& obj) { 
      DARABONBA_PTR_TO_JSON(headers, headers_);
      DARABONBA_PTR_TO_JSON(body, body_);
    };
    friend void from_json(const Darabonba::Json& j, SearchResponse& obj) { 
      DARABONBA_PTR_FROM_JSON(headers, headers_);
      DARABONBA_PTR_FROM_JSON(body, body_);
    };
    SearchResponse() = default ;
    SearchResponse(const SearchResponse &) = default ;
    SearchResponse(SearchResponse &&) = default ;
    SearchResponse(const Darabonba::Json & obj) { from_json(obj, *this); };
    virtual ~SearchResponse() = default ;
    SearchResponse& operator=(const SearchResponse &) = default ;
    SearchResponse& operator=(SearchResponse &&) = default ;
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
    inline SearchResponse& setHeaders(const map<string, string> & headers) { DARABONBA_PTR_SET_VALUE(headers_, headers) };
    inline SearchResponse& setHeaders(map<string, string> && headers) { DARABONBA_PTR_SET_RVALUE(headers_, headers) };


    // body Field Functions 
    bool hasBody() const { return this->body_ != nullptr;};
    void deleteBody() { this->body_ = nullptr;};
    inline string body() const { DARABONBA_PTR_GET_DEFAULT(body_, "") };
    inline SearchResponse& setBody(string body) { DARABONBA_PTR_SET_VALUE(body_, body) };


  protected:
    // headers
    std::shared_ptr<map<string, string>> headers_ = nullptr;
    // body
    std::shared_ptr<string> body_ = nullptr;
  };

  } // namespace Models
} // namespace AlibabaCloud
} // namespace HA3
#endif
