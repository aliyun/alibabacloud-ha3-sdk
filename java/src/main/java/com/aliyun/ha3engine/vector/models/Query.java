// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class Query extends TeaModel {
    // 查询的向量数据，多个向量可以平铺开
    @NameInMap("vector")
    @Validation(required = true)
    public java.util.List<Float> vector;

    // vector字段中向量的个数
    @NameInMap("vectorCount")
    public Integer vectorCount;

    // 返回个数
    @NameInMap("topK")
    public Integer topK;

    // 查询向量的空间
    @NameInMap("namespace")
    public String namespace;

    // 向量查询参数
    @NameInMap("searchParams")
    public String searchParams;

    // 分数过滤， 使用欧式距离时，只返回小于scoreThreshold的结果。使用内积时，只返回大于scoreThreshold的结果
    @NameInMap("scoreThreshold")
    public Float scoreThreshold;

    public static Query build(java.util.Map<String, ?> map) throws Exception {
        Query self = new Query();
        return TeaModel.build(map, self);
    }

    public Query setVector(java.util.List<Float> vector) {
        this.vector = vector;
        return this;
    }
    public java.util.List<Float> getVector() {
        return this.vector;
    }

    public Query setVectorCount(Integer vectorCount) {
        this.vectorCount = vectorCount;
        return this;
    }
    public Integer getVectorCount() {
        return this.vectorCount;
    }

    public Query setTopK(Integer topK) {
        this.topK = topK;
        return this;
    }
    public Integer getTopK() {
        return this.topK;
    }

    public Query setNamespace(String namespace) {
        this.namespace = namespace;
        return this;
    }
    public String getNamespace() {
        return this.namespace;
    }

    public Query setSearchParams(String searchParams) {
        this.searchParams = searchParams;
        return this;
    }
    public String getSearchParams() {
        return this.searchParams;
    }

    public Query setScoreThreshold(Float scoreThreshold) {
        this.scoreThreshold = scoreThreshold;
        return this;
    }
    public Float getScoreThreshold() {
        return this.scoreThreshold;
    }

}
