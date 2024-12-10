// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import com.aliyun.core.annotation.Body;
import com.aliyun.core.annotation.NameInMap;
import com.aliyun.core.annotation.Validation;
import com.aliyun.sdk.ha3engine.async.core.models.Request;

import darabonba.core.RequestModel;

/**
 * {@link SearchRequest} extends {@link RequestModel}
 *
 * <p>SearchRequest</p>
 */
public class SearchRequest extends Request {

    @Body
    @NameInMap("tableName")
    @Validation(required = true)
    private String tableName;

    @Body
    @NameInMap("size")
    private Integer size;

    @Body
    @NameInMap("from")
    private Integer from;

    @Body
    @NameInMap("order")
    private String order;

    @Body
    @NameInMap("outputFields")
    private java.util.List < String > outputFields;

    @Body
    @NameInMap("knnQuery")
    private QueryRequest knn;

    @Body
    @NameInMap("textQuery")
    private TextQuery text;

    @Body
    @NameInMap("rankQuery")
    private RankQuery rank;

    private SearchRequest(Builder builder) {
        super(builder);
        this.tableName = builder.tableName;
        this.size = builder.size;
        this.from = builder.from;
        this.order = builder.order;
        this.outputFields = builder.outputFields;
        this.knn = builder.knn;
        this.text = builder.text;
        this.rank = builder.rank;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static SearchRequest create() {
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
     * @return size
     */
    public Integer getSize() {
        return this.size;
    }

    /**
     * @return from
     */
    public Integer getFrom() {
        return this.from;
    }

    /**
     * @return order
     */
    public String getOrder() {
        return this.order;
    }

    /**
     * @return outputFields
     */
    public java.util.List < String > getOutputFields() {
        return this.outputFields;
    }

    /**
     * @return knn
     */
    public QueryRequest getKnn() {
        return this.knn;
    }

    /**
     * @return text
     */
    public TextQuery getText() {
        return this.text;
    }

    /**
     * @return rank
     */
    public RankQuery getRank() {
        return this.rank;
    }

    public static final class Builder extends Request.Builder<SearchRequest, Builder> {
        private String tableName; 
        private Integer size; 
        private Integer from; 
        private String order; 
        private java.util.List < String > outputFields; 
        private QueryRequest knn; 
        private TextQuery text; 
        private RankQuery rank; 

        private Builder() {
            super();
        } 

        private Builder(SearchRequest request) {
            super(request);
            this.tableName = request.tableName;
            this.size = request.size;
            this.from = request.from;
            this.order = request.order;
            this.outputFields = request.outputFields;
            this.knn = request.knn;
            this.text = request.text;
            this.rank = request.rank;
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
         * 返回结果的个数
         */
        public Builder size(Integer size) {
            this.putBodyParameter("size", size);
            this.size = size;
            return this;
        }

        /**
         * 从结果集的第from返回doc
         */
        public Builder from(Integer from) {
            this.putBodyParameter("from", from);
            this.from = from;
            return this;
        }

        /**
         * 结果排序方向:DESC: 降序排序;ASC: 升序排序
         */
        public Builder order(String order) {
            this.putBodyParameter("order", order);
            this.order = order;
            return this;
        }

        /**
         * 指定需要在结果中返回的字段，默认为空
         */
        public Builder outputFields(java.util.List < String > outputFields) {
            this.putBodyParameter("outputFields", outputFields);
            this.outputFields = outputFields;
            return this;
        }

        /**
         * KNN查询参数
         */
        public Builder knn(QueryRequest knn) {
            this.putBodyParameter("knn", knn);
            this.knn = knn;
            return this;
        }

        /**
         * text查询参数
         */
        public Builder text(TextQuery text) {
            this.putBodyParameter("text", text);
            this.text = text;
            return this;
        }

        /**
         * 指定两路结果融合的方式，目前支持两种策略：默认策略：两路结果中相同pk的doc的分数按权重相加。按加权后的分数排序。rrf: 使用rrf融合两路结果
         */
        public Builder rank(RankQuery rank) {
            this.putBodyParameter("rank", rank);
            this.rank = rank;
            return this;
        }

        @Override
        public SearchRequest build() {
            return new SearchRequest(this);
        } 

    } 

}
