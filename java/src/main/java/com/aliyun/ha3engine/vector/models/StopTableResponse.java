// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class StopTableResponse extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("statusCode")
    public Integer statusCode;

    @NameInMap("body")
    public StopTableResponseBody body;

    public static StopTableResponse build(java.util.Map<String, ?> map) throws Exception {
        StopTableResponse self = new StopTableResponse();
        return TeaModel.build(map, self);
    }

    public StopTableResponse setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public StopTableResponse setStatusCode(Integer statusCode) {
        this.statusCode = statusCode;
        return this;
    }
    public Integer getStatusCode() {
        return this.statusCode;
    }

    public StopTableResponse setBody(StopTableResponseBody body) {
        this.body = body;
        return this;
    }
    public StopTableResponseBody getBody() {
        return this.body;
    }

}
