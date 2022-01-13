// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.models;

import com.aliyun.tea.*;

public class PushDocumentsResponseModel extends TeaModel {
    // headers
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // body
    @NameInMap("body")
    @Validation(required = true)
    public String body;

    public static PushDocumentsResponseModel build(java.util.Map<String, ?> map) throws Exception {
        PushDocumentsResponseModel self = new PushDocumentsResponseModel();
        return TeaModel.build(map, self);
    }

    public PushDocumentsResponseModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public PushDocumentsResponseModel setBody(String body) {
        this.body = body;
        return this;
    }
    public String getBody() {
        return this.body;
    }

}
