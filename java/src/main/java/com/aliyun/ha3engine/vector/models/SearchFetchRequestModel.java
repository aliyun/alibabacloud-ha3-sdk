// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class SearchFetchRequestModel extends TeaModel {
    // 数据源名
    @NameInMap("tableName")
    @Validation(required = true)
    public String tableName;

    // 主键列表
    @NameInMap("ids")
    @Validation(required = true)
    public java.util.List<String> ids;

    public static SearchFetchRequestModel build(java.util.Map<String, ?> map) throws Exception {
        SearchFetchRequestModel self = new SearchFetchRequestModel();
        return TeaModel.build(map, self);
    }

    public SearchFetchRequestModel setTableName(String tableName) {
        this.tableName = tableName;
        return this;
    }
    public String getTableName() {
        return this.tableName;
    }

    public SearchFetchRequestModel setIds(java.util.List<String> ids) {
        this.ids = ids;
        return this;
    }
    public java.util.List<String> getIds() {
        return this.ids;
    }

}
