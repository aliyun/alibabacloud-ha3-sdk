// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class QueryRequest extends TeaModel {
    /**
     * <p>数据源名</p>
     */
    @NameInMap("tableName")
    @Validation(required = true)
    public String tableName;

    /**
     * <p>向量数据</p>
     */
    @NameInMap("vector")
    @Validation(required = true)
    public java.util.List<Float> vector;

    /**
     * <p>查询向量的空间</p>
     */
    @NameInMap("namespace")
    public String namespace;

    /**
     * <p>返回个数</p>
     */
    @NameInMap("topK")
    public Integer topK;

    /**
     * <p>查询的索引名</p>
     */
    @NameInMap("indexName")
    public String indexName;

    /**
     * <p>查询的稀疏向量</p>
     */
    @NameInMap("sparseData")
    public SparseData sparseData;

    /**
     * <p>Query的权重</p>
     */
    @NameInMap("weight")
    public Float weight;

    /**
     * <p>需要向量化的内容</p>
     */
    @NameInMap("content")
    public String content;

    /**
     * <p>使用的模型</p>
     */
    @NameInMap("modal")
    public String modal;

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
     * <p>查询参数</p>
     */
    @NameInMap("searchParams")
    public String searchParams;

    /**
     * <p>过滤表达式</p>
     */
    @NameInMap("filter")
    public String filter;

    /**
     * <p>分数过滤， 使用欧式距离时，只返回小于scoreThreshold的结果。使用内积时，只返回大于scoreThreshold的结果</p>
     */
    @NameInMap("scoreThreshold")
    public Float scoreThreshold;

    /**
     * <p>vector字段中包含的向量个数</p>
     */
    @NameInMap("vectorCount")
    public Integer vectorCount;

    /**
     * <p>排序表达式</p>
     */
    @NameInMap("sort")
    public String sort;

    public static QueryRequest build(java.util.Map<String, ?> map) throws Exception {
        QueryRequest self = new QueryRequest();
        return TeaModel.build(map, self);
    }

    public QueryRequest setTableName(String tableName) {
        this.tableName = tableName;
        return this;
    }
    public String getTableName() {
        return this.tableName;
    }

    public QueryRequest setVector(java.util.List<Float> vector) {
        this.vector = vector;
        return this;
    }
    public java.util.List<Float> getVector() {
        return this.vector;
    }

    public QueryRequest setNamespace(String namespace) {
        this.namespace = namespace;
        return this;
    }
    public String getNamespace() {
        return this.namespace;
    }

    public QueryRequest setTopK(Integer topK) {
        this.topK = topK;
        return this;
    }
    public Integer getTopK() {
        return this.topK;
    }

    public QueryRequest setIndexName(String indexName) {
        this.indexName = indexName;
        return this;
    }
    public String getIndexName() {
        return this.indexName;
    }

    public QueryRequest setSparseData(SparseData sparseData) {
        this.sparseData = sparseData;
        return this;
    }
    public SparseData getSparseData() {
        return this.sparseData;
    }

    public QueryRequest setWeight(Float weight) {
        this.weight = weight;
        return this;
    }
    public Float getWeight() {
        return this.weight;
    }

    public QueryRequest setContent(String content) {
        this.content = content;
        return this;
    }
    public String getContent() {
        return this.content;
    }

    public QueryRequest setModal(String modal) {
        this.modal = modal;
        return this;
    }
    public String getModal() {
        return this.modal;
    }

    public QueryRequest setIncludeVector(Boolean includeVector) {
        this.includeVector = includeVector;
        return this;
    }
    public Boolean getIncludeVector() {
        return this.includeVector;
    }

    public QueryRequest setOutputFields(java.util.List<String> outputFields) {
        this.outputFields = outputFields;
        return this;
    }
    public java.util.List<String> getOutputFields() {
        return this.outputFields;
    }

    public QueryRequest setOrder(String order) {
        this.order = order;
        return this;
    }
    public String getOrder() {
        return this.order;
    }

    public QueryRequest setSearchParams(String searchParams) {
        this.searchParams = searchParams;
        return this;
    }
    public String getSearchParams() {
        return this.searchParams;
    }

    public QueryRequest setFilter(String filter) {
        this.filter = filter;
        return this;
    }
    public String getFilter() {
        return this.filter;
    }

    public QueryRequest setScoreThreshold(Float scoreThreshold) {
        this.scoreThreshold = scoreThreshold;
        return this;
    }
    public Float getScoreThreshold() {
        return this.scoreThreshold;
    }

    public QueryRequest setVectorCount(Integer vectorCount) {
        this.vectorCount = vectorCount;
        return this;
    }
    public Integer getVectorCount() {
        return this.vectorCount;
    }

    public QueryRequest setSort(String sort) {
        this.sort = sort;
        return this;
    }
    public String getSort() {
        return this.sort;
    }

}
