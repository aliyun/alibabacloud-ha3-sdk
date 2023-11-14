// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.models;

import com.aliyun.tea.*;

public class HaQuery extends TeaModel {
    /**
     * <p>搜索主体，不能为空.并且可以指定多个查询条件及其之间的关系.</p>
     */
    @NameInMap("query")
    @Validation(required = true)
    public String query;

    /**
     * <p>cluster部分用于指定要查询的集群的名字。它不仅可以同时指定多个集群，还可以指定到集群中的哪些partition获取结果。</p>
     */
    @NameInMap("cluster")
    public String cluster;

    /**
     * <p>config部分可以指定查询结果的起始位置、返回结果的数量、展现结果的格式、参与精排表达式文档个数等。</p>
     */
    @NameInMap("config")
    @Validation(required = true)
    public HaQueryconfigClause config;

    /**
     * <p>过滤功能支持用户根据查询条件，筛选出用户感兴趣的文档。会在通过query子句查找到的文档进行进一步的过滤，以返回最终所需结果。</p>
     */
    @NameInMap("filter")
    public String filter;

    /**
     * <p>为便于通过查询语句传递信息给具体的特征函数，用户可以在kvpairs子句中对排序表达式中的可变部分进行参数定义。</p>
     */
    @NameInMap("kvpairs")
    public java.util.Map<String, String> kvpairs;

    /**
     * <p>用户可以通过查询语句控制结果的排序方式，包括指定排序的字段和升降序。field为要排序的字段，+为按字段值升序排序，-为降序排序</p>
     */
    @NameInMap("sort")
    public java.util.List<HaQuerySortClause> sort;

    /**
     * <p>一个关键词查询后可能会找到数以万计的文档，用户不太可能浏览所有的文档来获取自己需要的信息，有些情况下用户感兴趣的可能是一些统计的信息。</p>
     */
    @NameInMap("aggregate")
    public java.util.List<HaQueryAggregateClause> aggregate;

    /**
     * <p>打散子句可以在一定程度上保证展示结果的多样性，以提升用户体验。如一次查询可以查出很多的文档，但是如果某个用户的多个文档分值都比较高，则都排在了前面，导致一页中所展示的结果几乎都属于同一用户，这样既不利于结果展示也不利于用户体验。对此，打散子句可以对每个用户的文档进行抽取，使得每个用户都有展示文档的机会。</p>
     */
    @NameInMap("distinct")
    public java.util.List<HaQueryDistinctClause> distinct;

    /**
     * <p>扩展 配置参数</p>
     */
    @NameInMap("customConfig")
    public java.util.Map<String, String> customQuery;

    public static HaQuery build(java.util.Map<String, ?> map) throws Exception {
        HaQuery self = new HaQuery();
        return TeaModel.build(map, self);
    }

    public HaQuery setQuery(String query) {
        this.query = query;
        return this;
    }
    public String getQuery() {
        return this.query;
    }

    public HaQuery setCluster(String cluster) {
        this.cluster = cluster;
        return this;
    }
    public String getCluster() {
        return this.cluster;
    }

    public HaQuery setConfig(HaQueryconfigClause config) {
        this.config = config;
        return this;
    }
    public HaQueryconfigClause getConfig() {
        return this.config;
    }

    public HaQuery setFilter(String filter) {
        this.filter = filter;
        return this;
    }
    public String getFilter() {
        return this.filter;
    }

    public HaQuery setKvpairs(java.util.Map<String, String> kvpairs) {
        this.kvpairs = kvpairs;
        return this;
    }
    public java.util.Map<String, String> getKvpairs() {
        return this.kvpairs;
    }

    public HaQuery setSort(java.util.List<HaQuerySortClause> sort) {
        this.sort = sort;
        return this;
    }
    public java.util.List<HaQuerySortClause> getSort() {
        return this.sort;
    }

    public HaQuery setAggregate(java.util.List<HaQueryAggregateClause> aggregate) {
        this.aggregate = aggregate;
        return this;
    }
    public java.util.List<HaQueryAggregateClause> getAggregate() {
        return this.aggregate;
    }

    public HaQuery setDistinct(java.util.List<HaQueryDistinctClause> distinct) {
        this.distinct = distinct;
        return this;
    }
    public java.util.List<HaQueryDistinctClause> getDistinct() {
        return this.distinct;
    }

    public HaQuery setCustomQuery(java.util.Map<String, String> customQuery) {
        this.customQuery = customQuery;
        return this;
    }
    public java.util.Map<String, String> getCustomQuery() {
        return this.customQuery;
    }

}
