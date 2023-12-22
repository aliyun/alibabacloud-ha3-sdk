// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import com.aliyun.core.annotation.*;
import darabonba.core.RequestModel;
import darabonba.core.TeaModel;
import com.aliyun.sdk.ha3engine.async.core.models.Response;

/**
 * {@link SearchResponse} extends {@link TeaModel}
 *
 * <p>SearchResponse</p>
 */
public class SearchResponse extends Response {
    @NameInMap("headers")
    private java.util.Map < String, String > headers;

    @NameInMap("body")
    @Validation(required = true)
    private String body;

    private SearchResponse(BuilderImpl builder) {
        super(builder);
        this.headers = builder.headers;
        this.body = builder.body;
    }

    public static SearchResponse create() {
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

    public interface Builder extends Response.Builder<SearchResponse, Builder> {

        Builder headers(java.util.Map < String, String > headers);

        Builder body(String body);

        @Override
        SearchResponse build();

    } 

    private static final class BuilderImpl
            extends Response.BuilderImpl<SearchResponse, Builder>
            implements Builder {
        private java.util.Map < String, String > headers; 
        private String body; 

        private BuilderImpl() {
            super();
        } 

        private BuilderImpl(SearchResponse response) {
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
        public SearchResponse build() {
            return new SearchResponse(this);
        } 

    } 

}
