// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class AggregateRequest extends TeaModel {
    /**
     * <p>需要统计的表名</p>
     */
    @NameInMap("tableName")
    @Validation(required = true)
    public String tableName;

    /**
     * <p>过滤条件</p>
     */
    @NameInMap("filter")
    public String filter;

    /**
     * <p>分组统计的字段列表</p>
     */
    @NameInMap("groupKeys")
    public java.util.List<String> groupKeys;

    /**
     * <p>统计函数列表</p>
     */
    @NameInMap("aggFuncs")
    @Validation(required = true)
    public java.util.List<AggFuncDesc> aggFuncs;

    /**
     * <p>统计结果排序方式，支持多维排序</p>
     */
    @NameInMap("orderBy")
    public java.util.List<OrderByDesc> orderBy;

    /**
     * <p>超时时间，单位毫秒</p>
     */
    @NameInMap("timeout")
    public Integer timeout;

    public static AggregateRequest build(java.util.Map<String, ?> map) throws Exception {
        AggregateRequest self = new AggregateRequest();
        return TeaModel.build(map, self);
    }

    public AggregateRequest setTableName(String tableName) {
        this.tableName = tableName;
        return this;
    }
    public String getTableName() {
        return this.tableName;
    }

    public AggregateRequest setFilter(String filter) {
        this.filter = filter;
        return this;
    }
    public String getFilter() {
        return this.filter;
    }

    public AggregateRequest setGroupKeys(java.util.List<String> groupKeys) {
        this.groupKeys = groupKeys;
        return this;
    }
    public java.util.List<String> getGroupKeys() {
        return this.groupKeys;
    }

    public AggregateRequest setAggFuncs(java.util.List<AggFuncDesc> aggFuncs) {
        this.aggFuncs = aggFuncs;
        return this;
    }
    public java.util.List<AggFuncDesc> getAggFuncs() {
        return this.aggFuncs;
    }

    public AggregateRequest setOrderBy(java.util.List<OrderByDesc> orderBy) {
        this.orderBy = orderBy;
        return this;
    }
    public java.util.List<OrderByDesc> getOrderBy() {
        return this.orderBy;
    }

    public AggregateRequest setTimeout(Integer timeout) {
        this.timeout = timeout;
        return this;
    }
    public Integer getTimeout() {
        return this.timeout;
    }

}
