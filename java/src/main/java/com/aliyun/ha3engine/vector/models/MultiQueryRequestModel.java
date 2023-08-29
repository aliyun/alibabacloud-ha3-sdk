// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class MultiQueryRequestModel extends TeaModel {
    // 数据源名
    @NameInMap("tableName")
    @Validation(required = true)
    public String tableName;

    // 多向量列表
    @NameInMap("queries")
    @Validation(required = true)
    public java.util.List<Query> queries;

    // 返回个数
    @NameInMap("topK")
    public Integer topK;

    // 是否返回文档中的向量信息
    @NameInMap("includeVector")
    public Boolean includeVector;

    // 需要返回值的字段列表
    @NameInMap("outputFields")
    public java.util.List<String> outputFields;

    // 排序顺序, ASC：升序  DESC: 降序
    @NameInMap("order")
    public String order;

    // 过滤表达式
    @NameInMap("filter")
    public String filter;

    public static MultiQueryRequestModel build(java.util.Map<String, ?> map) throws Exception {
        MultiQueryRequestModel self = new MultiQueryRequestModel();
        return TeaModel.build(map, self);
    }

    public MultiQueryRequestModel setTableName(String tableName) {
        this.tableName = tableName;
        return this;
    }
    public String getTableName() {
        return this.tableName;
    }

    public MultiQueryRequestModel setQueries(java.util.List<Query> queries) {
        this.queries = queries;
        return this;
    }
    public java.util.List<Query> getQueries() {
        return this.queries;
    }

    public MultiQueryRequestModel setTopK(Integer topK) {
        this.topK = topK;
        return this;
    }
    public Integer getTopK() {
        return this.topK;
    }

    public MultiQueryRequestModel setIncludeVector(Boolean includeVector) {
        this.includeVector = includeVector;
        return this;
    }
    public Boolean getIncludeVector() {
        return this.includeVector;
    }

    public MultiQueryRequestModel setOutputFields(java.util.List<String> outputFields) {
        this.outputFields = outputFields;
        return this;
    }
    public java.util.List<String> getOutputFields() {
        return this.outputFields;
    }

    public MultiQueryRequestModel setOrder(String order) {
        this.order = order;
        return this;
    }
    public String getOrder() {
        return this.order;
    }

    public MultiQueryRequestModel setFilter(String filter) {
        this.filter = filter;
        return this;
    }
    public String getFilter() {
        return this.filter;
    }

}
