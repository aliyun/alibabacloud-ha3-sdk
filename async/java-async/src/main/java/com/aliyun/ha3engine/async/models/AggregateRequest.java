// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import com.aliyun.core.annotation.Body;
import com.aliyun.core.annotation.NameInMap;
import com.aliyun.core.annotation.Validation;
import com.aliyun.sdk.ha3engine.async.core.models.Request;

import darabonba.core.RequestModel;

/**
 * {@link AggregateRequest} extends {@link RequestModel}
 *
 * <p>AggregateRequest</p>
 */
public class AggregateRequest extends Request {

    @Body
    @NameInMap("tableName")
    @Validation(required = true)
    private String tableName;

    @Body
    @NameInMap("filter")
    private String filter;

    @Body
    @NameInMap("groupKeys")
    private java.util.List < String > groupKeys;

    @Body
    @NameInMap("aggFuncs")
    @Validation(required = true)
    private java.util.List < AggFuncDesc > aggFuncs;

    @Body
    @NameInMap("orderBy")
    private java.util.List < OrderByDesc > orderBy;

    @Body
    @NameInMap("timeout")
    private Integer timeout;

    private AggregateRequest(Builder builder) {
        super(builder);
        this.tableName = builder.tableName;
        this.filter = builder.filter;
        this.groupKeys = builder.groupKeys;
        this.aggFuncs = builder.aggFuncs;
        this.orderBy = builder.orderBy;
        this.timeout = builder.timeout;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static AggregateRequest create() {
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
     * @return filter
     */
    public String getFilter() {
        return this.filter;
    }

    /**
     * @return groupKeys
     */
    public java.util.List < String > getGroupKeys() {
        return this.groupKeys;
    }

    /**
     * @return aggFuncs
     */
    public java.util.List < AggFuncDesc > getAggFuncs() {
        return this.aggFuncs;
    }

    /**
     * @return orderBy
     */
    public java.util.List < OrderByDesc > getOrderBy() {
        return this.orderBy;
    }

    /**
     * @return timeout
     */
    public Integer getTimeout() {
        return this.timeout;
    }

    public static final class Builder extends Request.Builder<AggregateRequest, Builder> {
        private String tableName; 
        private String filter; 
        private java.util.List < String > groupKeys; 
        private java.util.List < AggFuncDesc > aggFuncs; 
        private java.util.List < OrderByDesc > orderBy; 
        private Integer timeout; 

        private Builder() {
            super();
        } 

        private Builder(AggregateRequest request) {
            super(request);
            this.tableName = request.tableName;
            this.filter = request.filter;
            this.groupKeys = request.groupKeys;
            this.aggFuncs = request.aggFuncs;
            this.orderBy = request.orderBy;
            this.timeout = request.timeout;
        } 

        /**
         * 需要统计的表名
         */
        public Builder tableName(String tableName) {
            this.putBodyParameter("tableName", tableName);
            this.tableName = tableName;
            return this;
        }

        /**
         * 过滤条件
         */
        public Builder filter(String filter) {
            this.putBodyParameter("filter", filter);
            this.filter = filter;
            return this;
        }

        /**
         * 分组统计的字段列表
         */
        public Builder groupKeys(java.util.List < String > groupKeys) {
            this.putBodyParameter("groupKeys", groupKeys);
            this.groupKeys = groupKeys;
            return this;
        }

        /**
         * 统计函数列表
         */
        public Builder aggFuncs(java.util.List < AggFuncDesc > aggFuncs) {
            this.putBodyParameter("aggFuncs", aggFuncs);
            this.aggFuncs = aggFuncs;
            return this;
        }

        /**
         * 统计结果排序方式，支持多维排序
         */
        public Builder orderBy(java.util.List < OrderByDesc > orderBy) {
            this.putBodyParameter("orderBy", orderBy);
            this.orderBy = orderBy;
            return this;
        }

        /**
         * 超时时间，单位毫秒
         */
        public Builder timeout(Integer timeout) {
            this.putBodyParameter("timeout", timeout);
            this.timeout = timeout;
            return this;
        }

        @Override
        public AggregateRequest build() {
            return new AggregateRequest(this);
        } 

    } 

}
