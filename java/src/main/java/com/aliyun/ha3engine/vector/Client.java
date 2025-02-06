// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector;

import com.aliyun.tea.*;
import com.aliyun.tea.interceptor.InterceptorChain;
import com.aliyun.tea.interceptor.RuntimeOptionsInterceptor;
import com.aliyun.tea.interceptor.RequestInterceptor;
import com.aliyun.tea.interceptor.ResponseInterceptor;
import com.aliyun.ha3engine.vector.models.*;

public class Client {

    private final static InterceptorChain interceptorChain = InterceptorChain.create();

    public String _endpoint;
    public String _instanceId;
    public String _protocol;
    public String _userAgent;
    public String _credential;
    public String _domainsuffix;
    public com.aliyun.teautil.models.RuntimeOptions _runtimeOptions;
    public Client(Config config) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(config)) {
            throw new TeaException(TeaConverter.buildMap(
                new TeaPair("name", "ParameterMissing"),
                new TeaPair("message", "'config' can not be unset")
            ));
        }

        if (!com.aliyun.teautil.Common.empty(config.accessUserName) && !com.aliyun.teautil.Common.empty(config.accessPassWord)) {
            this._credential = this.getRealmSignStr(config.accessUserName, config.accessPassWord);
        }

        this._endpoint = this.getEndpoint(config.endpoint);
        this._instanceId = config.instanceId;
        this._protocol = config.protocol;
        this._userAgent = config.userAgent;
        this._domainsuffix = "ha.aliyuncs.com";
        this._runtimeOptions = this.buildRuntimeOptions(config.runtimeOptions);
    }

    public java.util.Map<String, ?> _request(String method, String pathname, java.util.Map<String, ?> query, java.util.Map<String, String> headers, Object body, com.aliyun.teautil.models.RuntimeOptions runtime) throws Exception {
        java.util.Map<String, Object> runtime_ = TeaConverter.buildMap(
            new TeaPair("timeouted", "retry"),
            new TeaPair("readTimeout", runtime.readTimeout),
            new TeaPair("connectTimeout", runtime.connectTimeout),
            new TeaPair("httpsProxy", runtime.httpsProxy),
            new TeaPair("noProxy", runtime.noProxy),
            new TeaPair("maxIdleConns", runtime.maxIdleConns),
            new TeaPair("retry", TeaConverter.buildMap(
                new TeaPair("retryable", runtime.autoretry),
                new TeaPair("maxAttempts", runtime.maxAttempts)
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", runtime.backoffPolicy),
                new TeaPair("period", runtime.backoffPeriod)
            )),
            new TeaPair("ignoreSSL", runtime.ignoreSSL)
        );

        TeaRequest _lastRequest = null;
        Exception _lastException = null;
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
                        new TeaPair("host", com.aliyun.teautil.Common.defaultString(_endpoint, "" + _instanceId + "." + _domainsuffix + "")),
                        new TeaPair("authorization", "Basic " + _credential + ""),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                    ),
                    headers
                );
                if (!com.aliyun.teautil.Common.isUnset(query)) {
                    request_.query = com.aliyun.teautil.Common.stringifyMapValue(query);
                    request_.headers.put("X-Opensearch-Request-ID", com.aliyun.teautil.Common.getNonce());
                }

                if (!com.aliyun.teautil.Common.isUnset(body)) {
                    request_.headers.put("X-Opensearch-Swift-Request-ID", com.aliyun.teautil.Common.getNonce());
                    if (com.aliyun.darabonbastring.Client.equals("deflate", request_.headers.get("Content-Encoding")) && !com.aliyun.darabonbastring.Client.contains(pathname, "actions/bulk")) {
                        byte[] compressed = com.aliyun.ha3.util.Client.deflateCompress(com.aliyun.darabonbastring.Client.toBytes(com.aliyun.teautil.Common.toJSONString(body), "UTF-8"));
                        request_.body = Tea.toReadable(compressed);
                    } else {
                        request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(body));
                    }

                }

                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_, interceptorChain);

                String objStr = com.aliyun.teautil.Common.readAsString(response_.body);
                if (com.aliyun.teautil.Common.is4xx(response_.statusCode) || com.aliyun.teautil.Common.is5xx(response_.statusCode)) {
                    Object rawMsg = null;
                    try {
                        rawMsg = com.aliyun.teautil.Common.parseJSON(objStr);
                    } catch (TeaException err) {
                        rawMsg = objStr;
                    } catch (Exception _err) {
                        TeaException err = new TeaException(_err.getMessage(), _err);
                        rawMsg = objStr;
                    }                    
                    java.util.Map<String, Object> rawMap = TeaConverter.buildMap(
                        new TeaPair("errors", rawMsg)
                    );
                    throw new TeaException(TeaConverter.buildMap(
                        new TeaPair("message", response_.statusMessage),
                        new TeaPair("data", rawMap),
                        new TeaPair("code", response_.statusCode)
                    ));
                }

                if (com.aliyun.teautil.Common.empty(objStr)) {
                    java.util.Map<String, Object> rawbodyMap = TeaConverter.buildMap(
                        new TeaPair("status", response_.statusMessage),
                        new TeaPair("code", response_.statusCode)
                    );
                    return TeaConverter.buildMap(
                        new TeaPair("body", com.aliyun.teautil.Common.toJSONString(rawbodyMap)),
                        new TeaPair("headers", response_.headers)
                    );
                }

                return TeaConverter.buildMap(
                    new TeaPair("body", objStr),
                    new TeaPair("headers", response_.headers)
                );
            } catch (Exception e) {
                if (Tea.isRetryable(e)) {
                    _lastException = e;
                    continue;
                }
                throw e;
            }
        }
        throw new TeaUnretryableException(_lastRequest, _lastException);
    }

    public void addRuntimeOptionsInterceptor(RuntimeOptionsInterceptor interceptor) {
        interceptorChain.addRuntimeOptionsInterceptor(interceptor);
    }

    public void addRequestInterceptor(RequestInterceptor interceptor) {
        interceptorChain.addRequestInterceptor(interceptor);
    }

    public void addResponseInterceptor(ResponseInterceptor interceptor) {
        interceptorChain.addResponseInterceptor(interceptor);
    }

    /**
     * <b>description</b> :
     * <p>如果endpoint 配置以 http:// 或 https:// 开头，则去掉头部的 http:// 或 https://, 否则直接返回</p>
     */
    public String getEndpoint(String endpoint) throws Exception {
        if (com.aliyun.darabonbastring.Client.hasPrefix(endpoint, "http://")) {
            return com.aliyun.darabonbastring.Client.replace(endpoint, "http://", "", 1);
        }

        if (com.aliyun.darabonbastring.Client.hasPrefix(endpoint, "https://")) {
            return com.aliyun.darabonbastring.Client.replace(endpoint, "https://", "", 1);
        }

        return endpoint;
    }

    /**
     * <b>description</b> :
     * <p>设置Client UA 配置.</p>
     */
    public void setUserAgent(String userAgent) throws Exception {
        this._userAgent = userAgent;
    }

    /**
     * <b>description</b> :
     * <p>添加Client UA 配置.</p>
     */
    public void appendUserAgent(String userAgent) throws Exception {
        this._userAgent = "" + _userAgent + " " + userAgent + "";
    }

    /**
     * <b>description</b> :
     * <p>获取Client 配置 UA 配置.</p>
     */
    public String getUserAgent() throws Exception {
        String userAgent = com.aliyun.teautil.Common.getUserAgent(_userAgent);
        return userAgent;
    }

    /**
     * <b>description</b> :
     * <p>计算用户请求识别特征, 遵循 Basic Auth 生成规范.</p>
     */
    public String getRealmSignStr(String accessUserName, String accessPassWord) throws Exception {
        String accessUserNameStr = com.aliyun.darabonbastring.Client.trim(accessUserName);
        String accessPassWordStr = com.aliyun.darabonbastring.Client.trim(accessPassWord);
        String realmStr = "" + accessUserNameStr + ":" + accessPassWordStr + "";
        return com.aliyun.darabonba.encode.Encoder.base64EncodeToString(com.aliyun.darabonbastring.Client.toBytes(realmStr, "UTF-8"));
    }

    /**
     * <b>description</b> :
     * <p>向量查询</p>
     */
    public SearchResponse query(QueryRequest request) throws Exception {
        java.util.Map<String, String> headers = this.getHeadersFromRunTimeOption();
        return TeaModel.toModel(this._request("POST", "/vector-service/query", null, headers, com.aliyun.teautil.Common.toJSONString(request), _runtimeOptions), new SearchResponse());
    }

    /**
     * <b>description</b> :
     * <p>向量预测查询</p>
     */
    public SearchResponse inferenceQuery(QueryRequest request) throws Exception {
        java.util.Map<String, String> headers = this.getHeadersFromRunTimeOption();
        return TeaModel.toModel(this._request("POST", "/vector-service/inference-query", null, headers, com.aliyun.teautil.Common.toJSONString(request), _runtimeOptions), new SearchResponse());
    }

    /**
     * <b>description</b> :
     * <p>多namespace查询</p>
     */
    public SearchResponse multiQuery(MultiQueryRequest request) throws Exception {
        java.util.Map<String, String> headers = this.getHeadersFromRunTimeOption();
        return TeaModel.toModel(this._request("POST", "/vector-service/multi-query", null, headers, com.aliyun.teautil.Common.toJSONString(request), _runtimeOptions), new SearchResponse());
    }

    /**
     * <b>description</b> :
     * <p>查询数据</p>
     */
    public SearchResponse fetch(FetchRequest request) throws Exception {
        java.util.Map<String, String> headers = this.getHeadersFromRunTimeOption();
        return TeaModel.toModel(this._request("POST", "/vector-service/fetch", null, headers, com.aliyun.teautil.Common.toJSONString(request), _runtimeOptions), new SearchResponse());
    }

    /**
     * <b>description</b> :
     * <p>文本向量混合检索</p>
     */
    public SearchResponse search(SearchRequest request) throws Exception {
        java.util.Map<String, String> headers = this.getHeadersFromRunTimeOption();
        return TeaModel.toModel(this._request("POST", "/vector-service/search", null, headers, com.aliyun.teautil.Common.toJSONString(request), _runtimeOptions), new SearchResponse());
    }

    /**
     * <b>description</b> :
     * <p>向量引擎统计语法</p>
     */
    public SearchResponse aggregate(AggregateRequest request) throws Exception {
        java.util.Map<String, String> headers = this.getHeadersFromRunTimeOption();
        return TeaModel.toModel(this._request("POST", "/vector-service/aggregate", null, headers, com.aliyun.teautil.Common.toJSONString(request), _runtimeOptions), new SearchResponse());
    }

    /**
     * <b>description</b> :
     * <p>批量查询</p>
     */
    public SearchResponse batchQuery(BatchRequest request) throws Exception {
        java.util.Map<String, String> headers = this.getHeadersFromRunTimeOption();
        return TeaModel.toModel(this._request("POST", "/vector-service/batch-query", null, headers, com.aliyun.teautil.Common.toJSONString(request), _runtimeOptions), new SearchResponse());
    }

    /**
     * <b>description</b> :
     * <p>文档统计</p>
     */
    public SearchResponse stats(String tableName) throws Exception {
        java.util.Map<String, Object> body = TeaConverter.buildMap(
            new TeaPair("tableName", tableName)
        );
        return TeaModel.toModel(this._request("POST", "/vector-service/stats", null, null, com.aliyun.teautil.Common.toJSONString(body), _runtimeOptions), new SearchResponse());
    }

    /**
     * <b>description</b> :
     * <p>校验网络是否通畅
     * 检查vpc &amp; 用户名密码配置是否正确</p>
     */
    public SearchResponse active() throws Exception {
        return TeaModel.toModel(this._request("GET", "/network/active", null, null, null, _runtimeOptions), new SearchResponse());
    }

    /**
     * <b>description</b> :
     * <p>支持新增、更新、删除 等操作，以及对应批量操作</p>
     */
    public PushDocumentsResponse pushDocuments(String dataSourceName, String keyField, PushDocumentsRequest request) throws Exception {
        request.headers = TeaConverter.merge(String.class,
            TeaConverter.buildMap(
                new TeaPair("X-Opensearch-Swift-PK-Field", keyField)
            ),
            request.headers
        );
        return TeaModel.toModel(this._request("POST", "/update/" + dataSourceName + "/actions/bulk", null, request.headers, request.body, _runtimeOptions), new PushDocumentsResponse());
    }

    /**
     * <b>description</b> :
     * <p>构建RuntimeOptions</p>
     */
    public com.aliyun.teautil.models.RuntimeOptions buildRuntimeOptions(com.aliyun.teautil.models.RuntimeOptions runtimeOptions) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(runtimeOptions)) {
            return com.aliyun.teautil.models.RuntimeOptions.build(TeaConverter.buildMap(
                new TeaPair("readTimeout", 10000),
                new TeaPair("connectTimeout", 5000),
                new TeaPair("autoretry", false),
                new TeaPair("ignoreSSL", false),
                new TeaPair("maxIdleConns", 50)
            ));
        }

        if (com.aliyun.teautil.Common.isUnset(runtimeOptions.readTimeout)) {
            runtimeOptions.readTimeout = 10000;
        }

        if (com.aliyun.teautil.Common.isUnset(runtimeOptions.connectTimeout)) {
            runtimeOptions.connectTimeout = 5000;
        }

        if (com.aliyun.teautil.Common.isUnset(runtimeOptions.maxIdleConns)) {
            runtimeOptions.maxIdleConns = 50;
        }

        if (com.aliyun.teautil.Common.isUnset(runtimeOptions.maxAttempts)) {
            runtimeOptions.maxAttempts = 5;
        }

        if (com.aliyun.teautil.Common.isUnset(runtimeOptions.backoffPolicy)) {
            runtimeOptions.backoffPolicy = "no";
        }

        if (com.aliyun.teautil.Common.isUnset(runtimeOptions.backoffPeriod)) {
            runtimeOptions.backoffPeriod = 1;
        }

        return runtimeOptions;
    }

    /**
     * <b>description</b> :
     * <p>从runtimeoptions中获取headers</p>
     */
    public java.util.Map<String, String> getHeadersFromRunTimeOption() throws Exception {
        com.aliyun.teautil.models.RuntimeOptions options = _runtimeOptions;
        java.util.Map<String, String> headers = new java.util.HashMap<>();
        if (!com.aliyun.teautil.Common.isUnset(options.extendsParameters) && !com.aliyun.teautil.Common.isUnset(options.extendsParameters.headers) && !com.aliyun.teautil.Common.empty(options.extendsParameters.headers.get("Content-Encoding"))) {
            String contentEncoding = options.extendsParameters.headers.get("Content-Encoding");
            if (com.aliyun.darabonbastring.Client.equals("deflate", contentEncoding)) {
                headers.put("Content-Encoding", "deflate");
            }

        }

        return headers;
    }
}
