// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine;

import java.util.Base64;
import java.util.UUID;
import java.nio.charset.StandardCharsets;
import com.aliyun.tea.*;
import com.aliyun.ha3engine.models.*;

public class Client {

    public String _endpoint;
    public String _protocol;
    public String _userAgent;
    public String _credential;


    private String BasicAuthStr(String username,String password){
        String auth = username + ":" + password;
        String encodedAuth = Base64.getEncoder().encodeToString((auth.getBytes(StandardCharsets.ISO_8859_1)));
        return "Basic " + encodedAuth;
    }

    private String GenXRequestID(){
        return UUID.randomUUID().toString();

    }

    public Client(Config config) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(TeaModel.buildMap(config))) {
            throw new TeaException(TeaConverter.buildMap(
                    new TeaPair("name", "ParameterMissing"),
                    new TeaPair("message", "'config' can not be unset")
            ));
        }

        this._credential = this.BasicAuthStr(config.accessUser,config.accessSecret);
        this._endpoint = config.endpoint;
        this._protocol = config.protocol;
        this._userAgent = config.userAgent;
    }

    public java.util.Map<String, ?> _request(String method, String pathname, java.util.Map<String, ?> query, java.util.Map<String, String> headers, Object body, com.aliyun.teautil.models.RuntimeOptions runtime) throws Exception {
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
                new TeaPair("timeouted", "retry"),
                new TeaPair("readTimeout", runtime.readTimeout),
                new TeaPair("connectTimeout", runtime.connectTimeout),
                new TeaPair("httpProxy", runtime.httpProxy),
                new TeaPair("httpsProxy", runtime.httpsProxy),
                new TeaPair("noProxy", runtime.noProxy),
                new TeaPair("maxIdleConns", runtime.maxIdleConns),
                new TeaPair("retry", TeaConverter.buildMap(
                        new TeaPair("retryable", runtime.autoretry),
                        new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 3))
                )),
                new TeaPair("backoff", TeaConverter.buildMap(
                        new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                        new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
                )),
                new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        long _now = System.currentTimeMillis();
        int _retryTimes = 0;
        while (Tea.allowRetry((java.util.Map<String, Object>) runtime_.get("retry"), _retryTimes, _now)) {
            if (_retryTimes > 0) {
                int backoffTime = Tea.getBackoffTime(runtime_.get("backoff"), _retryTimes);
                if (backoffTime > 0) {
                    Tea.sleep(backoffTime);
                }
            }
            _retryTimes = _retryTimes + 1;
            try {
                TeaRequest request_ = new TeaRequest();
                request_.protocol = com.aliyun.teautil.Common.defaultString(_protocol, "HTTP");
                request_.method = method;
                request_.pathname = pathname;
                request_.headers = TeaConverter.merge(String.class,
                        TeaConverter.buildMap(
                                new TeaPair("user-agent", this.getUserAgent()),
                                new TeaPair("host",_endpoint),
                                new TeaPair("x-request-id", this.GenXRequestID())
                        ),
                        headers
                );
                if (!com.aliyun.teautil.Common.isUnset(query)) {
                    request_.query = com.aliyun.teautil.Common.stringifyMapValue(query);
                }

                if (!com.aliyun.teautil.Common.isUnset(body)) {
                    String reqBody = com.aliyun.teautil.Common.toJSONString(body);
                    request_.headers.put("Content-Type", "application/json");
                    request_.body = Tea.toReadable(reqBody);
                }

                request_.headers.put("Authorization", this._credential);
                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_);

                String objStr = com.aliyun.teautil.Common.readAsString(response_.body);
                if (com.aliyun.teautil.Common.is4xx(response_.statusCode) || com.aliyun.teautil.Common.is5xx(response_.statusCode)) {
                    throw new TeaException(TeaConverter.buildMap(
                            new TeaPair("message", response_.statusMessage),
                            new TeaPair("data", objStr),
                            new TeaPair("code", response_.statusCode)
                    ));
                }

                Object obj = com.aliyun.teautil.Common.parseJSON(objStr);
                java.util.Map<String, Object> res = com.aliyun.teautil.Common.assertAsMap(obj);
                return TeaConverter.buildMap(
                        new TeaPair("body", res),
                        new TeaPair("headers", response_.headers)
                );
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    continue;
                }
                throw e;
            }
        }

        throw new TeaUnretryableException(_lastRequest);
    }

    /**
     * 系统提供了丰富的搜索语法以满足用户各种场景下的搜索需求。
     */
    public SearchResponseModel searchEx(String appName, SearchRequestModel request, com.aliyun.teautil.models.RuntimeOptions runtime) throws Exception {
        return TeaModel.toModel(this._request("GET", "/search", TeaModel.buildMap(request.query), request.headers, null, runtime), new SearchResponseModel());
    }

    /**
     * 系统提供了丰富的搜索语法以满足用户各种场景下的搜索需求。
     */
    public SearchResponseModel search(String appName, SearchRequestModel request) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = com.aliyun.teautil.models.RuntimeOptions.build(TeaConverter.buildMap(
                new TeaPair("connectTimeout", 5000),
                new TeaPair("readTimeout", 10000),
                new TeaPair("autoretry", false),
                new TeaPair("ignoreSSL", false),
                new TeaPair("maxIdleConns", 50)
        ));
        return this.searchEx(appName, request, runtime);
    }

    /**
     * 支持新增、更新、删除 等操作，以及对应批量操作
     */
    public PushDocumentResponseModel pushDocumentEx(String appName, String tableName, PushDocumentRequestModel request, com.aliyun.teautil.models.RuntimeOptions runtime) throws Exception {
        return TeaModel.toModel(this._request("POST","/update/" + tableName + "/actions/bulk", null, request.headers, request.body, runtime), new PushDocumentResponseModel());
    }

    /**
     * 支持新增、更新、删除 等操作，以及对应批量操作
     */
    public PushDocumentResponseModel pushDocument(String appName, String tableName, PushDocumentRequestModel request) throws Exception {
        com.aliyun.teautil.models.RuntimeOptions runtime = com.aliyun.teautil.models.RuntimeOptions.build(TeaConverter.buildMap(
                new TeaPair("connectTimeout", 5000),
                new TeaPair("readTimeout", 10000),
                new TeaPair("autoretry", false),
                new TeaPair("ignoreSSL", false),
                new TeaPair("maxIdleConns", 50)
        ));
        return this.pushDocumentEx(appName, tableName, request, runtime);
    }

    public void setUserAgent(String userAgent) throws Exception {
        this._userAgent = userAgent;
    }

    public void appendUserAgent(String userAgent) throws Exception {
        this._userAgent = "" + _userAgent + " " + userAgent + "";
    }

    public String getUserAgent() throws Exception {
        String userAgent = com.aliyun.teautil.Common.getUserAgent(_userAgent);
        return userAgent;
    }
}



