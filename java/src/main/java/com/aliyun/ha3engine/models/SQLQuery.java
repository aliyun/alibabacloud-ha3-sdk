// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.models;

import com.aliyun.tea.*;

public class SQLQuery extends TeaModel {
    // 搜索主体，不能为空.
    @NameInMap("query")
    @Validation(required = true)
    public String query;

    // cluster部分用于指定要查询的集群的名字。它不仅可以同时指定多个集群，还可以指定到集群中的哪些partition获取结果。
    @NameInMap("kvpairs")
    public java.util.Map<String, String> kvpairs;

    public static SQLQuery build(java.util.Map<String, ?> map) throws Exception {
        SQLQuery self = new SQLQuery();
        return TeaModel.build(map, self);
    }

    public SQLQuery setQuery(String query) {
        this.query = query;
        return this;
    }
    public String getQuery() {
        return this.query;
    }

    public SQLQuery setKvpairs(java.util.Map<String, String> kvpairs) {
        this.kvpairs = kvpairs;
        return this;
    }
    public java.util.Map<String, String> getKvpairs() {
        return this.kvpairs;
    }

}
