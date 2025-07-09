// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class FetchRequest extends TeaModel {
    /**
     * <p>数据源名</p>
     */
    @NameInMap("tableName")
    @Validation(required = true)
    public String tableName;

    /**
     * <p>主键列表，如果传了主键列表，下面的条件参数不生效</p>
     */
    @NameInMap("ids")
    public java.util.List<String> ids;

    /**
     * <p>过滤表达式</p>
     */
    @NameInMap("filter")
    public String filter;

    /**
     * <p>排序表达式</p>
     */
    @NameInMap("sort")
    public String sort;

    /**
     * <p>返回的数据个数</p>
     */
    @NameInMap("limit")
    public Integer limit;

    /**
     * <p>返回的数据开始下标，用于翻页</p>
     */
    @NameInMap("offset")
    public Integer offset;

    /**
     * <p>是否返回向量数据</p>
     */
    @NameInMap("includeVector")
    public Boolean includeVector;

    /**
     * <p>需要返回的字段，不指定默认返回所有的字段</p>
     */
    @NameInMap("outputFields")
    public java.util.List<String> outputFields;

    /**
     * <p>kvpairs</p>
     */
    @NameInMap("kvpairs")
    public java.util.Map<String, String> kvpairs;

    public static FetchRequest build(java.util.Map<String, ?> map) throws Exception {
        FetchRequest self = new FetchRequest();
        return TeaModel.build(map, self);
    }

    public FetchRequest setTableName(String tableName) {
        this.tableName = tableName;
        return this;
    }
    public String getTableName() {
        return this.tableName;
    }

    public FetchRequest setIds(java.util.List<String> ids) {
        this.ids = ids;
        return this;
    }
    public java.util.List<String> getIds() {
        return this.ids;
    }

    public FetchRequest setFilter(String filter) {
        this.filter = filter;
        return this;
    }
    public String getFilter() {
        return this.filter;
    }

    public FetchRequest setSort(String sort) {
        this.sort = sort;
        return this;
    }
    public String getSort() {
        return this.sort;
    }

    public FetchRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public FetchRequest setOffset(Integer offset) {
        this.offset = offset;
        return this;
    }
    public Integer getOffset() {
        return this.offset;
    }

    public FetchRequest setIncludeVector(Boolean includeVector) {
        this.includeVector = includeVector;
        return this;
    }
    public Boolean getIncludeVector() {
        return this.includeVector;
    }

    public FetchRequest setOutputFields(java.util.List<String> outputFields) {
        this.outputFields = outputFields;
        return this;
    }
    public java.util.List<String> getOutputFields() {
        return this.outputFields;
    }

    public FetchRequest setKvpairs(java.util.Map<String, String> kvpairs) {
        this.kvpairs = kvpairs;
        return this;
    }
    public java.util.Map<String, String> getKvpairs() {
        return this.kvpairs;
    }

}
