// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class StartTableResponse extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("statusCode")
    public Integer statusCode;

    @NameInMap("body")
    public StartTableResponseBody body;

    public static StartTableResponse build(java.util.Map<String, ?> map) throws Exception {
        StartTableResponse self = new StartTableResponse();
        return TeaModel.build(map, self);
    }

    public StartTableResponse setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public StartTableResponse setStatusCode(Integer statusCode) {
        this.statusCode = statusCode;
        return this;
    }
    public Integer getStatusCode() {
        return this.statusCode;
    }

    public StartTableResponse setBody(StartTableResponseBody body) {
        this.body = body;
        return this;
    }
    public StartTableResponseBody getBody() {
        return this.body;
    }

}
