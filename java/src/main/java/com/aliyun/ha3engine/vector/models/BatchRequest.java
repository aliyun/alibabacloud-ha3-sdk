// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class BatchRequest extends TeaModel {
    /**
     * <p>批量查询列表</p>
     */
    @NameInMap("queries")
    @Validation(required = true)
    public java.util.List<QueryRequest> queries;

    /**
     * <p>超时时间，单位毫秒</p>
     */
    @NameInMap("timeout")
    public Integer timeout;

    public static BatchRequest build(java.util.Map<String, ?> map) throws Exception {
        BatchRequest self = new BatchRequest();
        return TeaModel.build(map, self);
    }

    public BatchRequest setQueries(java.util.List<QueryRequest> queries) {
        this.queries = queries;
        return this;
    }
    public java.util.List<QueryRequest> getQueries() {
        return this.queries;
    }

    public BatchRequest setTimeout(Integer timeout) {
        this.timeout = timeout;
        return this;
    }
    public Integer getTimeout() {
        return this.timeout;
    }

}
