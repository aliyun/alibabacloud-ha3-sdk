// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class PushDocumentsRequestModel extends TeaModel {
    // headers
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // body
    @NameInMap("body")
    @Validation(required = true)
    public java.util.List<java.util.Map<String, ?>> body;

    public static PushDocumentsRequestModel build(java.util.Map<String, ?> map) throws Exception {
        PushDocumentsRequestModel self = new PushDocumentsRequestModel();
        return TeaModel.build(map, self);
    }

    public PushDocumentsRequestModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public PushDocumentsRequestModel setBody(java.util.List<java.util.Map<String, ?>> body) {
        this.body = body;
        return this;
    }
    public java.util.List<java.util.Map<String, ?>> getBody() {
        return this.body;
    }

}
