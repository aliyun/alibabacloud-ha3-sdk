// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import com.aliyun.core.annotation.*;
import darabonba.core.TeaModel;
import com.aliyun.sdk.ha3engine.async.core.models.Response;

/**
 * {@link PushDocumentsResponse} extends {@link TeaModel}
 *
 * <p>PushDocumentsResponse</p>
 */
public class PushDocumentsResponse extends Response {
    @NameInMap("headers")
    private java.util.Map < String, String > headers;

    @NameInMap("body")
    @Validation(required = true)
    private String body;

    private PushDocumentsResponse(BuilderImpl builder) {
        super(builder);
        this.headers = builder.headers;
        this.body = builder.body;
    }

    public static PushDocumentsResponse create() {
        return new BuilderImpl().build();
    }

    @Override
    public Builder toBuilder() {
        return new BuilderImpl(this);
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
    public String getBody() {
        return this.body;
    }

    public interface Builder extends Response.Builder<PushDocumentsResponse, Builder> {

        Builder headers(java.util.Map < String, String > headers);

        Builder body(String body);

        @Override
        PushDocumentsResponse build();

    } 

    private static final class BuilderImpl
            extends Response.BuilderImpl<PushDocumentsResponse, Builder>
            implements Builder {
        private java.util.Map < String, String > headers; 
        private String body; 

        private BuilderImpl() {
            super();
        } 

        private BuilderImpl(PushDocumentsResponse response) {
            super(response);
            this.headers = response.headers;
            this.body = response.body;
        } 

        /**
         * headers
         */
        @Override
        public Builder headers(java.util.Map < String, String > headers) {
            this.headers = headers;
            return this;
        }

        /**
         * body
         */
        @Override
        public Builder body(String body) {
            this.body = body;
            return this;
        }

        @Override
        public PushDocumentsResponse build() {
            return new PushDocumentsResponse(this);
        } 

    } 

}
