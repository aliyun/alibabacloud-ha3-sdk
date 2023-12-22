// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import java.util.Map;
import java.util.Set;

import com.aliyun.core.annotation.*;
import darabonba.core.RequestModel;
import darabonba.core.utils.CommonUtil;

import com.aliyun.sdk.ha3engine.async.core.models.Request;

/**
 * {@link PushDocumentsRequest} extends {@link RequestModel}
 *
 * <p>PushDocumentsRequest</p>
 */
public class PushDocumentsRequest extends Request {

    @NameInMap("headers")
    private java.util.Map < String, String > headers;

    @Body
    @NameInMap("body")
    @Validation(required = true)
    private java.util.List < java.util.Map<String, ?>> body;

    private PushDocumentsRequest(Builder builder) {
        super(builder);
        this.headers = builder.headers;
        this.body = builder.body;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static PushDocumentsRequest create() {
        return builder().build();
    }

    @Override
    public Builder toBuilder() {
        return new Builder(this);
    }

    /**
     * @return headers
     */
    public java.util.Map < String, String > getHeaders() {
        return this.headers;
    }

    /**
     * @return body
     */
    public java.util.List < java.util.Map<String, ?>> getBody() {
        return this.body;
    }

    public static final class Builder extends Request.Builder<PushDocumentsRequest, Builder> {
        private java.util.Map < String, String > headers; 
        private java.util.List < java.util.Map<String, ?>> body; 

        private Builder() {
            super();
        } 

        private Builder(PushDocumentsRequest request) {
            super(request);
            this.headers = request.headers;
            this.body = request.body;
        } 

        /**
         * headers
         */
        public Builder headers(java.util.Map < String, String > headers) {
            if (!CommonUtil.isUnset(headers)) {
                for (Map.Entry<String, String> entry : headers.entrySet()) {
                    this.putHeaderParameter(entry.getKey(), entry.getValue());
                }
            }
            this.headers = headers;
            return this;
        }

        /**
         * body
         */
        public Builder body(java.util.List < java.util.Map<String, ?>> body) {
            this.putBodyParameter("body", body);
            this.body = body;
            return this;
        }

        @Override
        public PushDocumentsRequest build() {
            return new PushDocumentsRequest(this);
        } 

    } 

}
