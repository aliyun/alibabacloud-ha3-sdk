// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class PushDocumentsResponse extends TeaModel {
    /**
     * <p>headers</p>
     */
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    /**
     * <p>body</p>
     */
    @NameInMap("body")
    @Validation(required = true)
    public String body;

    public static PushDocumentsResponse build(java.util.Map<String, ?> map) throws Exception {
        PushDocumentsResponse self = new PushDocumentsResponse();
        return TeaModel.build(map, self);
    }

    public PushDocumentsResponse setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public PushDocumentsResponse setBody(String body) {
        this.body = body;
        return this;
    }
    public String getBody() {
        return this.body;
    }

}
