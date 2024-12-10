// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import com.aliyun.core.annotation.Body;
import com.aliyun.core.annotation.NameInMap;
import com.aliyun.core.annotation.Validation;

import darabonba.core.TeaModel;

/**
 * {@link TextQuery} extends {@link TeaModel}
 *
 * <p>TextQuery</p>
 */
public class TextQuery extends TeaModel {

    @Body
    @NameInMap("queryString")
    @Validation(required = true)
    private String queryString;

    @Body
    @NameInMap("queryParams")
    private java.util.Map < String, String > queryParams;

    @Body
    @NameInMap("filter")
    private String filter;

    @Body
    @NameInMap("weight")
    private Float weight;

    @Body
    @NameInMap("terminateAfter")
    private Integer terminateAfter;

    private TextQuery(Builder builder) {
        this.queryString = builder.queryString;
        this.queryParams = builder.queryParams;
        this.filter = builder.filter;
        this.weight = builder.weight;
        this.terminateAfter = builder.terminateAfter;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static TextQuery create() {
        return builder().build();
    }

    /**
     * @return queryString
     */
    public String getQueryString() {
        return this.queryString;
    }

    /**
     * @return queryParams
     */
    public java.util.Map < String, String > getQueryParams() {
        return this.queryParams;
    }

    /**
     * @return filter
     */
    public String getFilter() {
        return this.filter;
    }

    /**
     * @return weight
     */
    public Float getWeight() {
        return this.weight;
    }

    /**
     * @return terminateAfter
     */
    public Integer getTerminateAfter() {
        return this.terminateAfter;
    }

    public static final class Builder {
        private String queryString; 
        private java.util.Map < String, String > queryParams; 
        private String filter; 
        private Float weight; 
        private Integer terminateAfter; 

        /**
         * ha3 query语法，支持多个文本索引的AND、OR嵌套
         */
        public Builder queryString(String queryString) {
            this.queryString = queryString;
            return this;
        }

        /**
         * query查询参数：
         * <p>
         *       default_op: 指定在该次查询中使用的默认query 分词后的连接操作符，AND or OR。默认为AND。
         *       global_analyzer: 查询中指定全局的分词器，该分词器会覆盖schema的分词器，指定的值必须在analyzer.json里有配置。
         *       specific_index_analyzer: 查询中指定index使用另外的分词器，该分词器会覆盖global_analyzer和schema的分词器。
         *       no_token_indexes: 支持查询中指定的index不分词（除分词以外的其他流程如归一化、去停用词会正常执行），多个index之间用;分割。
         *       remove_stopwords: true or false 表示是否需要删除stop words，stop words在分词器中配置。默认true
         */
        public Builder queryParams(java.util.Map < String, String > queryParams) {
            this.queryParams = queryParams;
            return this;
        }

        /**
         * 过滤条件表达式
         */
        public Builder filter(String filter) {
            this.filter = filter;
            return this;
        }

        /**
         * text查询结果的权重，以score * weight的结果作为该路的排序分
         */
        public Builder weight(Float weight) {
            this.weight = weight;
            return this;
        }

        /**
         * 每个分片查找满足条件的文档的最大数量。到达这个数量后，查询将提前结束，不再继续查询索引。默认为0，不设置限制。
         */
        public Builder terminateAfter(Integer terminateAfter) {
            this.terminateAfter = terminateAfter;
            return this;
        }

        public TextQuery build() {
            return new TextQuery(this);
        } 

    } 

}
