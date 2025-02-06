package com.aliyun.ha3engine.async.models;

import com.aliyun.core.annotation.Body;
import com.aliyun.sdk.ha3engine.async.core.models.Request;
import com.aliyun.tea.NameInMap;
import com.aliyun.tea.Validation;

public class BatchRequest extends Request {
    /**
     * <p>批量查询列表</p>
     */
    @Body
    @NameInMap("queries")
    @Validation(required = true)
    public java.util.List<QueryRequest> queries;

    /**
     * <p>超时时间，单位毫秒</p>
     */
    @Body
    @NameInMap("timeout")
    public Integer timeout;

    public BatchRequest(Builder builder) {
        super(builder);
        this.queries = builder.queries;
        this.timeout = builder.timeout;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static BatchRequest create() {
        return builder().build();
    }

    @Override
    public Builder toBuilder() {
        return new Builder(this);
    }

    public java.util.List<QueryRequest> getQueries() {
        return this.queries;
    }

    public Integer getTimeout() {
        return this.timeout;
    }

    public static final class Builder extends Request.Builder<BatchRequest, Builder> {
        private java.util.List<QueryRequest> queries;
        private Integer timeout;

        private Builder() {
            super();
        }

        private Builder(BatchRequest request) {
            super(request);
            this.queries = request.queries;
            this.timeout = request.timeout;
        }

        /**
         * 批量查询列表
         */
        public Builder queries(java.util.List<QueryRequest> queries) {
            this.putBodyParameter("queries", queries);
            this.queries = queries;
            return this;
        }

        /**
         * 超时时间，单位毫秒
         */
        public Builder timeout(Integer timeout) {
            this.putBodyParameter("timeout", timeout);
            this.timeout = timeout;
            return this;
        }

        @Override
        public BatchRequest build() {
            return new BatchRequest(this);
        }
    }
}
