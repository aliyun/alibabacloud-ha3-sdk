// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import com.aliyun.core.annotation.Body;
import com.aliyun.core.annotation.NameInMap;
import com.aliyun.core.annotation.Validation;
import com.aliyun.sdk.ha3engine.async.core.models.Request;

import darabonba.core.RequestModel;

/**
 * {@link MultiQueryRequest} extends {@link RequestModel}
 *
 * <p>MultiQueryRequest</p>
 */
public class MultiQueryRequest extends Request {

    @Body
    @NameInMap("tableName")
    @Validation(required = true)
    private String tableName;

    @Body
    @NameInMap("queries")
    @Validation(required = true)
    private java.util.List < QueryRequest > queries;

    @Body
    @NameInMap("topK")
    private Integer topK;

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
    @NameInMap("filter")
    private String filter;

    @Body
    @NameInMap("sort")
    private String sort;

    private MultiQueryRequest(Builder builder) {
        super(builder);
        this.tableName = builder.tableName;
        this.queries = builder.queries;
        this.topK = builder.topK;
        this.includeVector = builder.includeVector;
        this.outputFields = builder.outputFields;
        this.order = builder.order;
        this.filter = builder.filter;
        this.sort = builder.sort;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static MultiQueryRequest create() {
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
     * @return queries
     */
    public java.util.List < QueryRequest > getQueries() {
        return this.queries;
    }

    /**
     * @return topK
     */
    public Integer getTopK() {
        return this.topK;
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
     * @return filter
     */
    public String getFilter() {
        return this.filter;
    }

    /**
     * @return sort
     */
    public String getSort() {
        return sort;
    }

    public static final class Builder extends Request.Builder<MultiQueryRequest, Builder> {
        private String tableName; 
        private java.util.List < QueryRequest > queries; 
        private Integer topK; 
        private Boolean includeVector; 
        private java.util.List < String > outputFields; 
        private String order; 
        private String filter;
        private String sort;

        private Builder() {
            super();
        } 

        private Builder(MultiQueryRequest request) {
            super(request);
            this.tableName = request.tableName;
            this.queries = request.queries;
            this.topK = request.topK;
            this.includeVector = request.includeVector;
            this.outputFields = request.outputFields;
            this.order = request.order;
            this.filter = request.filter;
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
         * 多向量列表
         */
        public Builder queries(java.util.List < QueryRequest > queries) {
            this.putBodyParameter("queries", queries);
            this.queries = queries;
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
         * 过滤表达式
         */
        public Builder filter(String filter) {
            this.putBodyParameter("filter", filter);
            this.filter = filter;
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
        public MultiQueryRequest build() {
            return new MultiQueryRequest(this);
        } 

    } 

}
