// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import java.util.List;

import com.aliyun.core.annotation.Body;
import com.aliyun.core.annotation.NameInMap;
import com.aliyun.core.annotation.Validation;
import com.aliyun.sdk.ha3engine.async.core.models.Request;

import darabonba.core.RequestModel;


/**
 * {@link FetchRequest} extends {@link RequestModel}
 *
 * <p>FetchRequest</p>
 */
public class FetchRequest extends Request {

    @Body
    @NameInMap("tableName")
    @Validation(required = true)
    private String tableName;

    @Body
    @NameInMap("ids")
    private java.util.List < String > ids;

    @Body
    @NameInMap("filter")
    private String filter;
    @Body
    @NameInMap("sort")
    private String sort;
    @Body
    @NameInMap("limit")
    private Integer limit;
    @Body
    @NameInMap("offset")
    private Integer offset;
    @Body
    @NameInMap("includeVector")
    private Boolean includeVector;
    @Body
    @NameInMap("outputFields")
    private java.util.List < String > outputFields;

    public FetchRequest(Builder builder) {
        super(builder);
        this.tableName = builder.tableName;
        this.ids = builder.ids;
        this.filter = builder.filter;
        this.sort = builder.sort;
        this.limit = builder.limit;
        this.offset = builder.offset;
        this.includeVector = builder.includeVector;
        this.outputFields = builder.outputFields;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static FetchRequest create() {
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
     * @return ids
     */
    public java.util.List < String > getIds() {
        return this.ids;
    }

    /**
     * @return filter
     */
    public String getFilter() {
        return filter;
    }
    /**
     * @return sort
     */
    public String getSort() {
        return sort;
    }
    /**
     * @return limit
     */
    public Integer getLimit() {
        return limit;
    }
    /**
     * @return offset
     */
    public Integer getOffset() {
        return offset;
    }
    /**
     * @return includeVector
     */
    public Boolean getIncludeVector() {
        return includeVector;
    }
    /**
     * @return outputFields
     */
    public List<String> getOutputFields() {
        return outputFields;
    }

    public static final class Builder extends Request.Builder<FetchRequest, Builder> {
        private String tableName; 
        private java.util.List < String > ids;
        private String filter;
        private String sort;
        private Integer limit;
        private Integer offset;
        private Boolean includeVector;
        private java.util.List < String > outputFields;

        private Builder() {
            super();
        } 

        private Builder(FetchRequest request) {
            super(request);
            this.tableName = request.tableName;
            this.ids = request.ids;
            this.filter = request.filter;
            this.sort = request.sort;
            this.limit = request.limit;
            this.offset = request.offset;
            this.includeVector = request.includeVector;
            this.outputFields = request.outputFields;
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
         * 主键列表
         */
        public Builder ids(java.util.List < String > ids) {
            this.putBodyParameter("ids", ids);
            this.ids = ids;
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
        /**
         * 返回的数据个数
         */
        public Builder limit(Integer limit) {
            this.putBodyParameter("limit", limit);
            this.limit = limit;
            return this;
        }
        /**
         * 返回的数据开始下标，用于翻页
         */
        public Builder offset(Integer offset) {
            this.putBodyParameter("offset", offset);
            this.offset = offset;
            return this;
        }
        /**
         * 是否返回向量数据
         */
        public Builder includeVector(Boolean includeVector) {
            this.putBodyParameter("includeVector", includeVector);
            this.includeVector = includeVector;
            return this;
        }
        /**
         * 需要返回的字段，不指定默认返回所有的字段
         */
        public Builder outputFields(java.util.List < String > outputFields) {
            this.putBodyParameter("outputFields", outputFields);
            this.outputFields = outputFields;
            return this;
        }

        @Override
        public FetchRequest build() {
            return new FetchRequest(this);
        } 

    } 

}
