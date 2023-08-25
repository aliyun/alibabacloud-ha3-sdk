// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class SearchVectorRequestModel extends TeaModel {
    // 数据源名
    @NameInMap("tableName")
    @Validation(required = true)
    public String tableName;

    // 向量数据
    @NameInMap("vector")
    @Validation(required = true)
    public java.util.List<Float> vector;

    // 查询向量的空间
    @NameInMap("namespace")
    public String namespace;

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

    // 查询参数
    @NameInMap("searchParams")
    public String searchParams;

    // 过滤表达式
    @NameInMap("filter")
    public String filter;

    // 分数过滤， 使用欧式距离时，只返回小于scoreThreshold的结果。使用内积时，只返回大于scoreThreshold的结果
    @NameInMap("scoreThreshold")
    public Float scoreThreshold;

    // vector字段中包含的向量个数
    @NameInMap("vectorCount")
    public Integer vectorCount;

    public static SearchVectorRequestModel build(java.util.Map<String, ?> map) throws Exception {
        SearchVectorRequestModel self = new SearchVectorRequestModel();
        return TeaModel.build(map, self);
    }

    public SearchVectorRequestModel setTableName(String tableName) {
        this.tableName = tableName;
        return this;
    }
    public String getTableName() {
        return this.tableName;
    }

    public SearchVectorRequestModel setVector(java.util.List<Float> vector) {
        this.vector = vector;
        return this;
    }
    public java.util.List<Float> getVector() {
        return this.vector;
    }

    public SearchVectorRequestModel setNamespace(String namespace) {
        this.namespace = namespace;
        return this;
    }
    public String getNamespace() {
        return this.namespace;
    }

    public SearchVectorRequestModel setTopK(Integer topK) {
        this.topK = topK;
        return this;
    }
    public Integer getTopK() {
        return this.topK;
    }

    public SearchVectorRequestModel setIncludeVector(Boolean includeVector) {
        this.includeVector = includeVector;
        return this;
    }
    public Boolean getIncludeVector() {
        return this.includeVector;
    }

    public SearchVectorRequestModel setOutputFields(java.util.List<String> outputFields) {
        this.outputFields = outputFields;
        return this;
    }
    public java.util.List<String> getOutputFields() {
        return this.outputFields;
    }

    public SearchVectorRequestModel setOrder(String order) {
        this.order = order;
        return this;
    }
    public String getOrder() {
        return this.order;
    }

    public SearchVectorRequestModel setSearchParams(String searchParams) {
        this.searchParams = searchParams;
        return this;
    }
    public String getSearchParams() {
        return this.searchParams;
    }

    public SearchVectorRequestModel setFilter(String filter) {
        this.filter = filter;
        return this;
    }
    public String getFilter() {
        return this.filter;
    }

    public SearchVectorRequestModel setScoreThreshold(Float scoreThreshold) {
        this.scoreThreshold = scoreThreshold;
        return this;
    }
    public Float getScoreThreshold() {
        return this.scoreThreshold;
    }

    public SearchVectorRequestModel setVectorCount(Integer vectorCount) {
        this.vectorCount = vectorCount;
        return this;
    }
    public Integer getVectorCount() {
        return this.vectorCount;
    }

}
