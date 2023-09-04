// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class MultiQueryRequest extends TeaModel {
    /**
     * <p>数据源名</p>
     */
    @NameInMap("tableName")
    @Validation(required = true)
    public String tableName;

    /**
     * <p>多向量列表</p>
     */
    @NameInMap("queries")
    @Validation(required = true)
    public java.util.List<QueryRequest> queries;

    /**
     * <p>返回个数</p>
     */
    @NameInMap("topK")
    public Integer topK;

    /**
     * <p>是否返回文档中的向量信息</p>
     */
    @NameInMap("includeVector")
    public Boolean includeVector;

    /**
     * <p>需要返回值的字段列表</p>
     */
    @NameInMap("outputFields")
    public java.util.List<String> outputFields;

    /**
     * <p>排序顺序, ASC：升序  DESC: 降序</p>
     */
    @NameInMap("order")
    public String order;

    /**
     * <p>过滤表达式</p>
     */
    @NameInMap("filter")
    public String filter;

    public static MultiQueryRequest build(java.util.Map<String, ?> map) throws Exception {
        MultiQueryRequest self = new MultiQueryRequest();
        return TeaModel.build(map, self);
    }

    public MultiQueryRequest setTableName(String tableName) {
        this.tableName = tableName;
        return this;
    }
    public String getTableName() {
        return this.tableName;
    }

    public MultiQueryRequest setQueries(java.util.List<QueryRequest> queries) {
        this.queries = queries;
        return this;
    }
    public java.util.List<QueryRequest> getQueries() {
        return this.queries;
    }

    public MultiQueryRequest setTopK(Integer topK) {
        this.topK = topK;
        return this;
    }
    public Integer getTopK() {
        return this.topK;
    }

    public MultiQueryRequest setIncludeVector(Boolean includeVector) {
        this.includeVector = includeVector;
        return this;
    }
    public Boolean getIncludeVector() {
        return this.includeVector;
    }

    public MultiQueryRequest setOutputFields(java.util.List<String> outputFields) {
        this.outputFields = outputFields;
        return this;
    }
    public java.util.List<String> getOutputFields() {
        return this.outputFields;
    }

    public MultiQueryRequest setOrder(String order) {
        this.order = order;
        return this;
    }
    public String getOrder() {
        return this.order;
    }

    public MultiQueryRequest setFilter(String filter) {
        this.filter = filter;
        return this;
    }
    public String getFilter() {
        return this.filter;
    }

}
