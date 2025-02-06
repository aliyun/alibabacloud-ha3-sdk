// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class TextQuery extends TeaModel {
    /**
     * <p>ha3 query语法，支持多个文本索引的AND、OR嵌套</p>
     */
    @NameInMap("queryString")
    @Validation(required = true)
    public String queryString;

    /**
     * <p>query查询参数：
     *       default_op: 指定在该次查询中使用的默认query 分词后的连接操作符，AND or OR。默认为AND。
     *       global_analyzer: 查询中指定全局的分词器，该分词器会覆盖schema的分词器，指定的值必须在analyzer.json里有配置。
     *       specific_index_analyzer: 查询中指定index使用另外的分词器，该分词器会覆盖global_analyzer和schema的分词器。
     *       no_token_indexes: 支持查询中指定的index不分词（除分词以外的其他流程如归一化、去停用词会正常执行），多个index之间用;分割。
     *       remove_stopwords: true or false 表示是否需要删除stop words，stop words在分词器中配置。默认true</p>
     */
    @NameInMap("queryParams")
    public java.util.Map<String, String> queryParams;

    /**
     * <p>过滤条件表达式</p>
     */
    @NameInMap("filter")
    public String filter;

    /**
     * <p>text查询结果的权重，以score * weight的结果作为该路的排序分</p>
     */
    @NameInMap("weight")
    public Float weight;

    /**
     * <p>每个分片查找满足条件的文档的最大数量。到达这个数量后，查询将提前结束，不再继续查询索引。默认为0，不设置限制。</p>
     */
    @NameInMap("terminateAfter")
    public Integer terminateAfter;

    public static TextQuery build(java.util.Map<String, ?> map) throws Exception {
        TextQuery self = new TextQuery();
        return TeaModel.build(map, self);
    }

    public TextQuery setQueryString(String queryString) {
        this.queryString = queryString;
        return this;
    }
    public String getQueryString() {
        return this.queryString;
    }

    public TextQuery setQueryParams(java.util.Map<String, String> queryParams) {
        this.queryParams = queryParams;
        return this;
    }
    public java.util.Map<String, String> getQueryParams() {
        return this.queryParams;
    }

    public TextQuery setFilter(String filter) {
        this.filter = filter;
        return this;
    }
    public String getFilter() {
        return this.filter;
    }

    public TextQuery setWeight(Float weight) {
        this.weight = weight;
        return this;
    }
    public Float getWeight() {
        return this.weight;
    }

    public TextQuery setTerminateAfter(Integer terminateAfter) {
        this.terminateAfter = terminateAfter;
        return this;
    }
    public Integer getTerminateAfter() {
        return this.terminateAfter;
    }

}
