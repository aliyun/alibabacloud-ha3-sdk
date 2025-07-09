// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class SearchRequest extends TeaModel {
    /**
     * <p>数据源名</p>
     */
    @NameInMap("tableName")
    @Validation(required = true)
    public String tableName;

    /**
     * <p>返回结果的个数</p>
     */
    @NameInMap("size")
    public Integer size;

    /**
     * <p>从结果集的第from返回doc</p>
     */
    @NameInMap("from")
    public Integer from;

    /**
     * <p>结果排序方向:DESC: 降序排序;ASC: 升序排序</p>
     */
    @NameInMap("order")
    public String order;

    /**
     * <p>指定需要在结果中返回的字段，默认为空</p>
     */
    @NameInMap("outputFields")
    public java.util.List<String> outputFields;

    /**
     * <p>KNN查询参数</p>
     */
    @NameInMap("knn")
    public QueryRequest knn;

    /**
     * <p>text查询参数</p>
     */
    @NameInMap("text")
    public TextQuery text;

    /**
     * <p>指定两路结果融合的方式，目前支持两种策略：默认策略：两路结果中相同pk的doc的分数按权重相加。按加权后的分数排序。rrf: 使用rrf融合两路结果</p>
     */
    @NameInMap("rank")
    public RankQuery rank;

    public static SearchRequest build(java.util.Map<String, ?> map) throws Exception {
        SearchRequest self = new SearchRequest();
        return TeaModel.build(map, self);
    }

    public SearchRequest setTableName(String tableName) {
        this.tableName = tableName;
        return this;
    }
    public String getTableName() {
        return this.tableName;
    }

    public SearchRequest setSize(Integer size) {
        this.size = size;
        return this;
    }
    public Integer getSize() {
        return this.size;
    }

    public SearchRequest setFrom(Integer from) {
        this.from = from;
        return this;
    }
    public Integer getFrom() {
        return this.from;
    }

    public SearchRequest setOrder(String order) {
        this.order = order;
        return this;
    }
    public String getOrder() {
        return this.order;
    }

    public SearchRequest setOutputFields(java.util.List<String> outputFields) {
        this.outputFields = outputFields;
        return this;
    }
    public java.util.List<String> getOutputFields() {
        return this.outputFields;
    }

    public SearchRequest setKnn(QueryRequest knn) {
        this.knn = knn;
        return this;
    }
    public QueryRequest getKnn() {
        return this.knn;
    }

    public SearchRequest setText(TextQuery text) {
        this.text = text;
        return this;
    }
    public TextQuery getText() {
        return this.text;
    }

    public SearchRequest setRank(RankQuery rank) {
        this.rank = rank;
        return this;
    }
    public RankQuery getRank() {
        return this.rank;
    }

}
