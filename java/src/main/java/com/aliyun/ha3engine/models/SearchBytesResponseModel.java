// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.models;

import com.aliyun.tea.*;

public class SearchBytesResponseModel extends TeaModel {
    // headers
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // body
    @NameInMap("body")
    @Validation(required = true)
    public byte[] body;

    public static SearchBytesResponseModel build(java.util.Map<String, ?> map) throws Exception {
        SearchBytesResponseModel self = new SearchBytesResponseModel();
        return TeaModel.build(map, self);
    }

    public SearchBytesResponseModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchBytesResponseModel setBody(byte[] body) {
        this.body = body;
        return this;
    }
    public byte[] getBody() {
        return this.body;
    }

}
