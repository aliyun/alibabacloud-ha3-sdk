// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class SearchResponseModel extends TeaModel {
    // headers
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // body
    @NameInMap("body")
    @Validation(required = true)
    public String body;

    public static SearchResponseModel build(java.util.Map<String, ?> map) throws Exception {
        SearchResponseModel self = new SearchResponseModel();
        return TeaModel.build(map, self);
    }

    public SearchResponseModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchResponseModel setBody(String body) {
        this.body = body;
        return this;
    }
    public String getBody() {
        return this.body;
    }

}
