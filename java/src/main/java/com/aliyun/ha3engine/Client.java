// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine;

import com.aliyun.tea.*;
import com.aliyun.tea.interceptor.InterceptorChain;
import com.aliyun.tea.interceptor.RuntimeOptionsInterceptor;
import com.aliyun.tea.interceptor.RequestInterceptor;
import com.aliyun.tea.interceptor.ResponseInterceptor;
import com.aliyun.ha3engine.models.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.darabonbastring.*;
import com.aliyun.darabonba.encode.*;
import com.aliyun.darabonba.map.*;

public class Client {

    private final static InterceptorChain interceptorChain = InterceptorChain.create();

    public String _endpoint;
    public String _instanceId;
    public String _protocol;
    public String _userAgent;
    public String _credential;
    public String _domainsuffix;
    public String _httpProxy;
    public Client(Config config) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(TeaModel.buildMap(config))) {
            throw new TeaException(TeaConverter.buildMap(
                new TeaPair("name", "ParameterMissing"),
                new TeaPair("message", "'config' can not be unset")
            ));
        }

        this._credential = this.getRealmSignStr(config.accessUserName, config.accessPassWord);
        this._endpoint = config.endpoint;
        this._instanceId = config.instanceId;
        this._protocol = config.protocol;
        this._userAgent = config.userAgent;
        this._domainsuffix = "ha.aliyuncs.com";
        this._httpProxy = config.httpProxy;
    }

    public java.util.Map<String, ?> _request(String method, String pathname, java.util.Map<String, ?> query, java.util.Map<String, String> headers, Object body, RuntimeOptions runtime) throws Exception {
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
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 5))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
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
                    request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(body));
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

    public java.util.Map<String, ?> _request_search_bytes(String method, String pathname, java.util.Map<String, ?> query, java.util.Map<String, String> headers, Object body, RuntimeOptions runtime) throws Exception {
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
                new TeaPair("maxAttempts", com.aliyun.teautil.Common.defaultNumber(runtime.maxAttempts, 5))
            )),
            new TeaPair("backoff", TeaConverter.buildMap(
                new TeaPair("policy", com.aliyun.teautil.Common.defaultString(runtime.backoffPolicy, "no")),
                new TeaPair("period", com.aliyun.teautil.Common.defaultNumber(runtime.backoffPeriod, 1))
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
                    request_.body = Tea.toReadable(com.aliyun.teautil.Common.toJSONString(body));
                }

                _lastRequest = request_;
                TeaResponse response_ = Tea.doAction(request_, runtime_, interceptorChain);

                byte[] objStr = com.aliyun.teautil.Common.readAsBytes(response_.body);
                if (com.aliyun.teautil.Common.is4xx(response_.statusCode) || com.aliyun.teautil.Common.is5xx(response_.statusCode)) {
                    String errorMsg = com.aliyun.teautil.Common.toString(objStr);
                    Object rawMsg = null;
                    try {
                        rawMsg = com.aliyun.teautil.Common.parseJSON(errorMsg);
                    } catch (TeaException err) {
                        rawMsg = errorMsg;
                    } catch (Exception _err) {
                        TeaException err = new TeaException(_err.getMessage(), _err);
                        rawMsg = errorMsg;
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

                if (com.aliyun.teautil.Common.isUnset(objStr)) {
                    java.util.Map<String, Object> rawbodyMap = TeaConverter.buildMap(
                        new TeaPair("status", response_.statusMessage),
                        new TeaPair("code", response_.statusCode)
                    );
                    return TeaConverter.buildMap(
                        new TeaPair("body", rawbodyMap),
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
     * 设置Client UA 配置.
     */
    public void setUserAgent(String userAgent) throws Exception {
        this._userAgent = userAgent;
    }

    /**
     * 添加Client UA 配置.
     */
    public void appendUserAgent(String userAgent) throws Exception {
        this._userAgent = "" + _userAgent + " " + userAgent + "";
    }

    /**
     * 获取Client 配置 UA 配置.
     */
    public String getUserAgent() throws Exception {
        String userAgent = com.aliyun.teautil.Common.getUserAgent(_userAgent);
        return userAgent;
    }

    /**
     * 计算用户请求识别特征, 遵循 Basic Auth 生成规范.
     */
    public String getRealmSignStr(String accessUserName, String accessPassWord) throws Exception {
        String accessUserNameStr = com.aliyun.darabonbastring.Client.trim(accessUserName);
        String accessPassWordStr = com.aliyun.darabonbastring.Client.trim(accessPassWord);
        String realmStr = "" + accessUserNameStr + ":" + accessPassWordStr + "";
        return com.aliyun.darabonba.encode.Encoder.base64EncodeToString(com.aliyun.darabonbastring.Client.toBytes(realmStr, "UTF-8"));
    }

    public String buildHaSearchQuery(HaQuery haquery) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(haquery.query)) {
            throw new TeaException(TeaConverter.buildMap(
                new TeaPair("name", "ParameterMissing"),
                new TeaPair("message", "'HaQuery.query' can not be unset")
            ));
        }

        String tempString = "query=" + haquery.query + "";
        String configStr = this.buildHaQueryconfigClauseStr(haquery.config);
        tempString = "" + tempString + "&&cluster=" + com.aliyun.teautil.Common.defaultString(haquery.cluster, "general") + "";
        tempString = "" + tempString + "&&config=" + configStr + "";
        if (!com.aliyun.teautil.Common.isUnset(haquery.filter)) {
            String filterStr = haquery.filter;
            if (!com.aliyun.teautil.Common.empty(filterStr)) {
                String fieldValueTrimed = com.aliyun.darabonbastring.Client.trim(filterStr);
                tempString = "" + tempString + "&&filter=" + fieldValueTrimed + "";
            }

        }

        if (!com.aliyun.teautil.Common.isUnset(haquery.customQuery)) {
            for (String keyField : com.aliyun.darabonba.map.Client.keySet(haquery.customQuery)) {
                String fieldValue = haquery.customQuery.get(keyField);
                if (!com.aliyun.teautil.Common.empty(fieldValue)) {
                    String fieldValueTrimed = com.aliyun.darabonbastring.Client.trim(fieldValue);
                    String keyFieldTrimed = com.aliyun.darabonbastring.Client.trim(keyField);
                    tempString = "" + tempString + "&&" + keyFieldTrimed + "=" + fieldValueTrimed + "";
                }

            }
        }

        if (!com.aliyun.teautil.Common.isUnset(haquery.sort)) {
            String sortStr = this.buildHaQuerySortClauseStr(haquery.sort);
            if (!com.aliyun.teautil.Common.empty(sortStr)) {
                tempString = "" + tempString + "&&sort=" + sortStr + "";
            }

        }

        if (!com.aliyun.teautil.Common.isUnset(haquery.aggregate)) {
            String aggregateClauseStr = this.buildHaQueryAggregateClauseStr(haquery.aggregate);
            if (!com.aliyun.teautil.Common.empty(aggregateClauseStr)) {
                tempString = "" + tempString + "&&aggregate=" + aggregateClauseStr + "";
            }

        }

        if (!com.aliyun.teautil.Common.isUnset(haquery.distinct)) {
            String distinctClauseStr = this.buildHaQueryDistinctClauseStr(haquery.distinct);
            if (!com.aliyun.teautil.Common.empty(distinctClauseStr)) {
                tempString = "" + tempString + "&&distinct=" + distinctClauseStr + "";
            }

        }

        String kvpairs = this.buildSearcKvPairClauseStr(haquery.kvpairs);
        if (!com.aliyun.teautil.Common.empty(kvpairs)) {
            tempString = "" + tempString + "&&kvpairs=" + kvpairs + "";
        }

        return tempString;
    }

    public String buildHaQueryAggregateClauseStr(java.util.List<HaQueryAggregateClause> Clause) throws Exception {
        String tempClauseString = "";
        for (HaQueryAggregateClause AggregateClause : Clause) {
            String tempAggregateClauseString = "";
            if (com.aliyun.teautil.Common.isUnset(AggregateClause.groupKey) || com.aliyun.teautil.Common.isUnset(AggregateClause.aggFun)) {
                throw new TeaException(TeaConverter.buildMap(
                    new TeaPair("name", "ParameterMissing"),
                    new TeaPair("message", "'HaQueryAggregateClause.groupKey/aggFun' can not be unset")
                ));
            }

            if (!com.aliyun.teautil.Common.empty(AggregateClause.groupKey) && !com.aliyun.teautil.Common.empty(AggregateClause.aggFun)) {
                String groupKeyTrimed = com.aliyun.darabonbastring.Client.trim(AggregateClause.groupKey);
                String aggFunTrimed = com.aliyun.darabonbastring.Client.trim(AggregateClause.aggFun);
                tempAggregateClauseString = "group_key:" + groupKeyTrimed + ",agg_fun:" + aggFunTrimed + "";
            }

            if (!com.aliyun.teautil.Common.empty(AggregateClause.range)) {
                String rangeTrimed = com.aliyun.darabonbastring.Client.trim(AggregateClause.range);
                tempAggregateClauseString = "" + tempAggregateClauseString + ",range:" + rangeTrimed + "";
            }

            if (!com.aliyun.teautil.Common.empty(AggregateClause.maxGroup)) {
                String maxGroupTrimed = com.aliyun.darabonbastring.Client.trim(AggregateClause.maxGroup);
                tempAggregateClauseString = "" + tempAggregateClauseString + ",max_group:" + maxGroupTrimed + "";
            }

            if (!com.aliyun.teautil.Common.empty(AggregateClause.aggFilter)) {
                String aggFilterTrimed = com.aliyun.darabonbastring.Client.trim(AggregateClause.aggFilter);
                tempAggregateClauseString = "" + tempAggregateClauseString + ",agg_filter:" + aggFilterTrimed + "";
            }

            if (!com.aliyun.teautil.Common.empty(AggregateClause.aggSamplerThresHold)) {
                String aggSamplerThresHoldTrimed = com.aliyun.darabonbastring.Client.trim(AggregateClause.aggSamplerThresHold);
                tempAggregateClauseString = "" + tempAggregateClauseString + ",agg_sampler_threshold:" + aggSamplerThresHoldTrimed + "";
            }

            if (!com.aliyun.teautil.Common.empty(AggregateClause.aggSamplerStep)) {
                String aggSamplerStepTrimed = com.aliyun.darabonbastring.Client.trim(AggregateClause.aggSamplerStep);
                tempAggregateClauseString = "" + tempAggregateClauseString + ",agg_sampler_step:" + aggSamplerStepTrimed + "";
            }

            if (!com.aliyun.teautil.Common.empty(tempClauseString)) {
                tempClauseString = "" + tempClauseString + ";" + tempAggregateClauseString + "";
            } else {
                tempClauseString = "" + tempAggregateClauseString + "";
            }

        }
        return tempClauseString;
    }

    public String buildHaQueryDistinctClauseStr(java.util.List<HaQueryDistinctClause> Clause) throws Exception {
        String tempClauseString = "";
        for (HaQueryDistinctClause DistinctClause : Clause) {
            String tempDistinctClauseString = "";
            if (com.aliyun.teautil.Common.isUnset(DistinctClause.distKey)) {
                throw new TeaException(TeaConverter.buildMap(
                    new TeaPair("name", "ParameterMissing"),
                    new TeaPair("message", "'HaQueryDistinctClause.distKey' can not be unset")
                ));
            }

            if (!com.aliyun.teautil.Common.empty(DistinctClause.distKey)) {
                String distKeyTrimed = com.aliyun.darabonbastring.Client.trim(DistinctClause.distKey);
                tempDistinctClauseString = "dist_key:" + distKeyTrimed + "";
            }

            if (!com.aliyun.teautil.Common.empty(DistinctClause.distCount)) {
                String distCountTrimed = com.aliyun.darabonbastring.Client.trim(DistinctClause.distCount);
                tempDistinctClauseString = "" + tempDistinctClauseString + ",dist_count:" + distCountTrimed + "";
            }

            if (!com.aliyun.teautil.Common.empty(DistinctClause.distTimes)) {
                String distTimesTrimed = com.aliyun.darabonbastring.Client.trim(DistinctClause.distTimes);
                tempDistinctClauseString = "" + tempDistinctClauseString + ",dist_times:" + distTimesTrimed + "";
            }

            if (!com.aliyun.teautil.Common.empty(DistinctClause.reserved)) {
                String reservedTrimed = com.aliyun.darabonbastring.Client.trim(DistinctClause.reserved);
                tempDistinctClauseString = "" + tempDistinctClauseString + ",reserved:" + reservedTrimed + "";
            }

            if (!com.aliyun.teautil.Common.empty(DistinctClause.distFilter)) {
                String distFilterTrimed = com.aliyun.darabonbastring.Client.trim(DistinctClause.distFilter);
                tempDistinctClauseString = "" + tempDistinctClauseString + ",dist_filter:" + distFilterTrimed + "";
            }

            if (!com.aliyun.teautil.Common.empty(DistinctClause.updateTotalHit)) {
                String updateTotalHitTrimed = com.aliyun.darabonbastring.Client.trim(DistinctClause.updateTotalHit);
                tempDistinctClauseString = "" + tempDistinctClauseString + ",update_total_hit:" + updateTotalHitTrimed + "";
            }

            if (!com.aliyun.teautil.Common.empty(DistinctClause.grade)) {
                String gradeTrimed = com.aliyun.darabonbastring.Client.trim(DistinctClause.grade);
                tempDistinctClauseString = "" + tempDistinctClauseString + ",grade:" + gradeTrimed + "";
            }

            if (!com.aliyun.teautil.Common.empty(tempClauseString)) {
                tempClauseString = "" + tempClauseString + ";" + tempDistinctClauseString + "";
            } else {
                tempClauseString = "" + tempDistinctClauseString + "";
            }

        }
        return tempClauseString;
    }

    public String buildHaQuerySortClauseStr(java.util.List<HaQuerySortClause> Clause) throws Exception {
        String tempClauseString = "";
        for (HaQuerySortClause SortClause : Clause) {
            String fieldValueTrimed = com.aliyun.darabonbastring.Client.trim(SortClause.sortOrder);
            String keyFieldTrimed = com.aliyun.darabonbastring.Client.trim(SortClause.sortKey);
            if (com.aliyun.teautil.Common.equalString(fieldValueTrimed, "+") || com.aliyun.teautil.Common.equalString(fieldValueTrimed, "-")) {
                if (!com.aliyun.teautil.Common.empty(fieldValueTrimed) && !com.aliyun.teautil.Common.empty(keyFieldTrimed)) {
                    if (com.aliyun.teautil.Common.empty(tempClauseString)) {
                        tempClauseString = "" + fieldValueTrimed + "" + keyFieldTrimed + "";
                    } else {
                        tempClauseString = "" + tempClauseString + ";" + fieldValueTrimed + "" + keyFieldTrimed + "";
                    }

                }

            }

        }
        return tempClauseString;
    }

    public String buildHaQueryconfigClauseStr(HaQueryconfigClause Clause) throws Exception {
        String tempClauseString = "";
        if (com.aliyun.teautil.Common.isUnset(TeaModel.buildMap(Clause))) {
            throw new TeaException(TeaConverter.buildMap(
                new TeaPair("name", "ParameterMissing"),
                new TeaPair("message", "'HaQueryconfigClause' can not be unset")
            ));
        }

        if (com.aliyun.teautil.Common.isUnset(Clause.start)) {
            Clause.start = null;
        }

        if (com.aliyun.teautil.Common.isUnset(Clause.hit)) {
            Clause.hit = null;
        }

        if (com.aliyun.teautil.Common.isUnset(Clause.format)) {
            Clause.format = null;
        }

        tempClauseString = "start:" + com.aliyun.teautil.Common.defaultString(Clause.start, "0") + "";
        tempClauseString = "" + tempClauseString + ",hit:" + com.aliyun.teautil.Common.defaultString(Clause.hit, "10") + "";
        tempClauseString = "" + tempClauseString + ",format:" + com.aliyun.darabonbastring.Client.toLower(com.aliyun.teautil.Common.defaultString(Clause.format, "json")) + "";
        if (!com.aliyun.teautil.Common.isUnset(Clause.customConfig)) {
            for (String keyField : com.aliyun.darabonba.map.Client.keySet(Clause.customConfig)) {
                String fieldValue = Clause.customConfig.get(keyField);
                if (!com.aliyun.teautil.Common.empty(fieldValue)) {
                    String fieldValueTrimed = com.aliyun.darabonbastring.Client.trim(fieldValue);
                    String keyFieldTrimed = com.aliyun.darabonbastring.Client.trim(keyField);
                    if (!com.aliyun.teautil.Common.empty(tempClauseString)) {
                        tempClauseString = "" + tempClauseString + "," + keyFieldTrimed + ":" + fieldValueTrimed + "";
                    } else {
                        tempClauseString = "" + keyFieldTrimed + ":" + fieldValueTrimed + "";
                    }

                }

            }
        }

        return tempClauseString;
    }

    public String buildSQLSearchQuery(SQLQuery sqlquery) throws Exception {
        if (com.aliyun.teautil.Common.isUnset(sqlquery.query)) {
            throw new TeaException(TeaConverter.buildMap(
                new TeaPair("name", "ParameterMissing"),
                new TeaPair("message", "'SQLQuery.query' can not be unset")
            ));
        }

        String tempString = "query=" + sqlquery.query + "";
        String kvpairs = this.buildSearcKvPairClauseStr(sqlquery.kvpairs);
        if (!com.aliyun.teautil.Common.empty(kvpairs)) {
            tempString = "" + tempString + "&&kvpair=" + kvpairs + "";
        }

        return tempString;
    }

    public String buildSearcKvPairClauseStr(java.util.Map<String, String> kvPair) throws Exception {
        String tempkvpairsString = "__ops_request_id:" + com.aliyun.teautil.Common.getNonce() + "";
        if (!com.aliyun.teautil.Common.isUnset(kvPair)) {
            for (String keyField : com.aliyun.darabonba.map.Client.keySet(kvPair)) {
                String fieldValue = kvPair.get(keyField);
                if (!com.aliyun.teautil.Common.empty(fieldValue)) {
                    String fieldValueTrimed = com.aliyun.darabonbastring.Client.trim(fieldValue);
                    String keyFieldTrimed = com.aliyun.darabonbastring.Client.trim(keyField);
                    tempkvpairsString = "" + tempkvpairsString + "," + keyFieldTrimed + ":" + fieldValueTrimed + "";
                }

            }
        }

        return tempkvpairsString;
    }

    /**
     * 系统提供了丰富的搜索语法以满足用户各种场景下的搜索需求。
     */
    public SearchResponseModel SearchEx(SearchRequestModel request, RuntimeOptions runtime) throws Exception {
        return TeaModel.toModel(this._request("GET", "/query", TeaModel.buildMap(request.query), request.headers, null, runtime), new SearchResponseModel());
    }

    /**
     * 系统提供了丰富的搜索语法以满足用户各种场景下的搜索需求。
     */
    public SearchResponseModel Search(SearchRequestModel request) throws Exception {
        RuntimeOptions runtime = RuntimeOptions.build(TeaConverter.buildMap(
            new TeaPair("connectTimeout", 5000),
            new TeaPair("readTimeout", 10000),
            new TeaPair("autoretry", false),
            new TeaPair("ignoreSSL", false),
            new TeaPair("maxIdleConns", 50),
            new TeaPair("httpProxy", _httpProxy)
        ));
        return this.SearchWithOptions(request, runtime);
    }

    /**
     * 系统提供了丰富的搜索语法以满足用户各种场景下的搜索需求,及传入运行时参数.
     */
    public SearchResponseModel SearchWithOptions(SearchRequestModel request, RuntimeOptions runtime) throws Exception {
        return this.SearchEx(request, runtime);
    }

    /**
     * 支持新增、更新、删除 等操作，以及对应批量操作
     */
    public PushDocumentsResponseModel pushDocumentEx(String dataSourceName, PushDocumentsRequestModel request, RuntimeOptions runtime) throws Exception {
        return TeaModel.toModel(this._request("POST", "/update/" + dataSourceName + "/actions/bulk", null, request.headers, request.body, runtime), new PushDocumentsResponseModel());
    }

    /**
     * 支持新增、更新、删除 等操作，以及对应批量操作
     */
    public PushDocumentsResponseModel pushDocuments(String dataSourceName, String keyField, PushDocumentsRequestModel request) throws Exception {
        RuntimeOptions runtime = RuntimeOptions.build(TeaConverter.buildMap(
            new TeaPair("connectTimeout", 5000),
            new TeaPair("readTimeout", 10000),
            new TeaPair("autoretry", false),
            new TeaPair("ignoreSSL", false),
            new TeaPair("maxIdleConns", 50),
            new TeaPair("httpProxy", _httpProxy)
        ));
        return this.pushDocumentsWithOptions(dataSourceName, keyField, request, runtime);
    }

    /**
     * 支持新增、更新、删除 等操作，以及对应批量操作,及传入运行时参数.
     */
    public PushDocumentsResponseModel pushDocumentsWithOptions(String dataSourceName, String keyField, PushDocumentsRequestModel request, RuntimeOptions runtime) throws Exception {
        request.headers = TeaConverter.buildMap(
            new TeaPair("X-Opensearch-Swift-PK-Field", keyField)
        );
        return this.pushDocumentEx(dataSourceName, request, runtime);
    }

    /**
     * 系统提供了丰富的搜索语法以满足用户各种场景下的搜索需求。
     */
    public SearchBytesResponseModel SearchBytesEx(SearchRequestModel request, RuntimeOptions runtime) throws Exception {
        return TeaModel.toModel(this._request_search_bytes("GET", "/query", TeaModel.buildMap(request.query), request.headers, null, runtime), new SearchBytesResponseModel());
    }

    /**
     * 系统提供了丰富的搜索语法以满足用户各种场景下的搜索需求。
     */
    public SearchBytesResponseModel SearchBytes(SearchRequestModel request) throws Exception {
        RuntimeOptions runtime = RuntimeOptions.build(TeaConverter.buildMap(
            new TeaPair("connectTimeout", 5000),
            new TeaPair("readTimeout", 10000),
            new TeaPair("autoretry", false),
            new TeaPair("ignoreSSL", false),
            new TeaPair("maxIdleConns", 50),
            new TeaPair("httpProxy", _httpProxy)
        ));
        return this.SearchBytesWithOptions(request, runtime);
    }

    /**
     * 系统提供了丰富的搜索语法以满足用户各种场景下的搜索需求,及传入运行时参数.
     */
    public SearchBytesResponseModel SearchBytesWithOptions(SearchRequestModel request, RuntimeOptions runtime) throws Exception {
        return this.SearchBytesEx(request, runtime);
    }
}
