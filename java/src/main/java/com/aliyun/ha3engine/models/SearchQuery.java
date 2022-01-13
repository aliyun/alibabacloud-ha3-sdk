// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.models;

import com.aliyun.tea.*;

public class SearchQuery extends TeaModel {
    // 适配于 Ha3 类型 query. 参数支持子句关键字请参照文档
    @NameInMap("query")
    public String query;

    // 适配于 SQL 类型 query. 参数支持子句关键字请参照文档.
    @NameInMap("sql")
    public String sql;

    public static SearchQuery build(java.util.Map<String, ?> map) throws Exception {
        SearchQuery self = new SearchQuery();
        return TeaModel.build(map, self);
    }

    public SearchQuery setQuery(String query) {
        this.query = query;
        return this;
    }
    public String getQuery() {
        return this.query;
    }

    public SearchQuery setSql(String sql) {
        this.sql = sql;
        return this;
    }
    public String getSql() {
        return this.sql;
    }

}
