// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.models;

import com.aliyun.tea.*;

public class SearchRequestModel extends TeaModel {
    // headers
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // query
    @NameInMap("query")
    @Validation(required = true)
    public SearchQuery query;

    // body
    @NameInMap("body")
    public String body;

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

}
