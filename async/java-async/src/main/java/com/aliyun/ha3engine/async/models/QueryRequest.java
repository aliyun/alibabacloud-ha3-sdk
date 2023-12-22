// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import com.aliyun.core.annotation.*;
import darabonba.core.RequestModel;
import com.aliyun.sdk.ha3engine.async.core.models.Request;

/**
 * {@link QueryRequest} extends {@link RequestModel}
 *
 * <p>QueryRequest</p>
 */
public class QueryRequest extends Request {

    @Body
    @NameInMap("tableName")
    @Validation(required = true)
    private String tableName;

    @Body
    @NameInMap("vector")
    @Validation(required = true)
    private java.util.List < Float > vector;

    @Body
    @NameInMap("namespace")
    private String namespace;

    @Body
    @NameInMap("topK")
    private Integer topK;

    @Body
    @NameInMap("indexName")
    private String indexName;

    @Body
    @NameInMap("sparseData")
    private SparseData sparseData;

    @Body
    @NameInMap("weight")
    private Float weight;

    @Body
    @NameInMap("content")
    private String content;

    @Body
    @NameInMap("modal")
    private String modal;

    @Body
    @NameInMap("includeVector")
    private Boolean includeVector;

    @Body
    @NameInMap("outputFields")
    private java.util.List < String > outputFields;

    @Body
    @NameInMap("order")
    private String order;

    @Body
    @NameInMap("searchParams")
    private String searchParams;

    @Body
    @NameInMap("filter")
    private String filter;

    @Body
    @NameInMap("scoreThreshold")
    private Float scoreThreshold;

    @Body
    @NameInMap("vectorCount")
    private Integer vectorCount;

    @Body
    @NameInMap("sort")
    private String sort;

    private QueryRequest(Builder builder) {
        super(builder);
        this.tableName = builder.tableName;
        this.vector = builder.vector;
        this.namespace = builder.namespace;
        this.topK = builder.topK;
        this.indexName = builder.indexName;
        this.sparseData = builder.sparseData;
        this.weight = builder.weight;
        this.content = builder.content;
        this.modal = builder.modal;
        this.includeVector = builder.includeVector;
        this.outputFields = builder.outputFields;
        this.order = builder.order;
        this.searchParams = builder.searchParams;
        this.filter = builder.filter;
        this.scoreThreshold = builder.scoreThreshold;
        this.vectorCount = builder.vectorCount;
        this.sort = builder.sort;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static QueryRequest create() {
        return builder().build();
    }

    @Override
    public Builder toBuilder() {
        return new Builder(this);
    }

    /**
     * @return tableName
     */
    public String getTableName() {
        return this.tableName;
    }

    /**
     * @return vector
     */
    public java.util.List < Float > getVector() {
        return this.vector;
    }

    /**
     * @return namespace
     */
    public String getNamespace() {
        return this.namespace;
    }

    /**
     * @return topK
     */
    public Integer getTopK() {
        return this.topK;
    }

    /**
     * @return indexName
     */
    public String getIndexName() {
        return this.indexName;
    }

    /**
     * @return sparseData
     */
    public SparseData getSparseData() {
        return this.sparseData;
    }

    /**
     * @return weight
     */
    public Float getWeight() {
        return this.weight;
    }

    /**
     * @return content
     */
    public String getContent() {
        return this.content;
    }

    /**
     * @return modal
     */
    public String getModal() {
        return this.modal;
    }

    /**
     * @return includeVector
     */
    public Boolean getIncludeVector() {
        return this.includeVector;
    }

    /**
     * @return outputFields
     */
    public java.util.List < String > getOutputFields() {
        return this.outputFields;
    }

    /**
     * @return order
     */
    public String getOrder() {
        return this.order;
    }

    /**
     * @return searchParams
     */
    public String getSearchParams() {
        return this.searchParams;
    }

    /**
     * @return filter
     */
    public String getFilter() {
        return this.filter;
    }

    /**
     * @return scoreThreshold
     */
    public Float getScoreThreshold() {
        return this.scoreThreshold;
    }

    /**
     * @return vectorCount
     */
    public Integer getVectorCount() {
        return this.vectorCount;
    }

    /**
     * @return sort
     */
    public String getSort() {
        return this.sort;
    }

    public static final class Builder extends Request.Builder<QueryRequest, Builder> {
        private String tableName; 
        private java.util.List < Float > vector; 
        private String namespace; 
        private Integer topK; 
        private String indexName; 
        private SparseData sparseData; 
        private Float weight; 
        private String content; 
        private String modal; 
        private Boolean includeVector; 
        private java.util.List < String > outputFields; 
        private String order; 
        private String searchParams; 
        private String filter; 
        private Float scoreThreshold; 
        private Integer vectorCount; 
        private String sort; 

        private Builder() {
            super();
        } 

        private Builder(QueryRequest request) {
            super(request);
            this.tableName = request.tableName;
            this.vector = request.vector;
            this.namespace = request.namespace;
            this.topK = request.topK;
            this.indexName = request.indexName;
            this.sparseData = request.sparseData;
            this.weight = request.weight;
            this.content = request.content;
            this.modal = request.modal;
            this.includeVector = request.includeVector;
            this.outputFields = request.outputFields;
            this.order = request.order;
            this.searchParams = request.searchParams;
            this.filter = request.filter;
            this.scoreThreshold = request.scoreThreshold;
            this.vectorCount = request.vectorCount;
            this.sort = request.sort;
        } 

        /**
         * 数据源名
         */
        public Builder tableName(String tableName) {
            this.putBodyParameter("tableName", tableName);
            this.tableName = tableName;
            return this;
        }

        /**
         * 向量数据
         */
        public Builder vector(java.util.List < Float > vector) {
            this.putBodyParameter("vector", vector);
            this.vector = vector;
            return this;
        }

        /**
         * 查询向量的空间
         */
        public Builder namespace(String namespace) {
            this.putBodyParameter("namespace", namespace);
            this.namespace = namespace;
            return this;
        }

        /**
         * 返回个数
         */
        public Builder topK(Integer topK) {
            this.putBodyParameter("topK", topK);
            this.topK = topK;
            return this;
        }

        /**
         * 查询的索引名
         */
        public Builder indexName(String indexName) {
            this.putBodyParameter("indexName", indexName);
            this.indexName = indexName;
            return this;
        }

        /**
         * 查询的稀疏向量
         */
        public Builder sparseData(SparseData sparseData) {
            this.putBodyParameter("sparseData", sparseData);
            this.sparseData = sparseData;
            return this;
        }

        /**
         * Query的权重
         */
        public Builder weight(Float weight) {
            this.putBodyParameter("weight", weight);
            this.weight = weight;
            return this;
        }

        /**
         * 需要向量化的内容
         */
        public Builder content(String content) {
            this.putBodyParameter("content", content);
            this.content = content;
            return this;
        }

        /**
         * 使用的模型
         */
        public Builder modal(String modal) {
            this.putBodyParameter("modal", modal);
            this.modal = modal;
            return this;
        }

        /**
         * 是否返回文档中的向量信息
         */
        public Builder includeVector(Boolean includeVector) {
            this.putBodyParameter("includeVector", includeVector);
            this.includeVector = includeVector;
            return this;
        }

        /**
         * 需要返回值的字段列表
         */
        public Builder outputFields(java.util.List < String > outputFields) {
            this.putBodyParameter("outputFields", outputFields);
            this.outputFields = outputFields;
            return this;
        }

        /**
         * 排序顺序, ASC：升序  DESC: 降序
         */
        public Builder order(String order) {
            this.putBodyParameter("order", order);
            this.order = order;
            return this;
        }

        /**
         * 查询参数
         */
        public Builder searchParams(String searchParams) {
            this.putBodyParameter("searchParams", searchParams);
            this.searchParams = searchParams;
            return this;
        }

        /**
         * 过滤表达式
         */
        public Builder filter(String filter) {
            this.putBodyParameter("filter", filter);
            this.filter = filter;
            return this;
        }

        /**
         * 分数过滤， 使用欧式距离时，只返回小于scoreThreshold的结果。使用内积时，只返回大于scoreThreshold的结果
         */
        public Builder scoreThreshold(Float scoreThreshold) {
            this.putBodyParameter("scoreThreshold", scoreThreshold);
            this.scoreThreshold = scoreThreshold;
            return this;
        }

        /**
         * vector字段中包含的向量个数
         */
        public Builder vectorCount(Integer vectorCount) {
            this.putBodyParameter("vectorCount", vectorCount);
            this.vectorCount = vectorCount;
            return this;
        }

        /**
         * 排序表达式
         */
        public Builder sort(String sort) {
            this.putBodyParameter("sort", sort);
            this.sort = sort;
            return this;
        }

        @Override
        public QueryRequest build() {
            return new QueryRequest(this);
        } 

    } 

}
