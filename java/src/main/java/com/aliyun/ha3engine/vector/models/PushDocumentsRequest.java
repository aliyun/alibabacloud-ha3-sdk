// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class PushDocumentsRequest extends TeaModel {
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
    public java.util.List<java.util.Map<String, ?>> body;

    public static PushDocumentsRequest build(java.util.Map<String, ?> map) throws Exception {
        PushDocumentsRequest self = new PushDocumentsRequest();
        return TeaModel.build(map, self);
    }

    public PushDocumentsRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public PushDocumentsRequest setBody(java.util.List<java.util.Map<String, ?>> body) {
        this.body = body;
        return this;
    }
    public java.util.List<java.util.Map<String, ?>> getBody() {
        return this.body;
    }

}
