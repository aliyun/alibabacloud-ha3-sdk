// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.models;

import com.aliyun.tea.*;

public class SearchRequestModel extends TeaModel {
    /**
     * <p>headers</p>
     */
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    /**
     * <p>query</p>
     */
    @NameInMap("query")
    @Validation(required = true)
    public SearchQuery query;

    /**
     * <p>body</p>
     */
    @NameInMap("body")
    public String body;

    /**
     * <p>请求方式，仅支持GET、POST两种请求方式</p>
     */
    @NameInMap("method")
    public String method;

    public static SearchRequestModel build(java.util.Map<String, ?> map) throws Exception {
        SearchRequestModel self = new SearchRequestModel();
        return TeaModel.build(map, self);
    }

    public SearchRequestModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchRequestModel setQuery(SearchQuery query) {
        this.query = query;
        return this;
    }
    public SearchQuery getQuery() {
        return this.query;
    }

    public SearchRequestModel setBody(String body) {
        this.body = body;
        return this;
    }
    public String getBody() {
        return this.body;
    }

    public SearchRequestModel setMethod(String method) {
        this.method = method;
        return this;
    }
    public String getMethod() {
        return this.method;
    }

}
