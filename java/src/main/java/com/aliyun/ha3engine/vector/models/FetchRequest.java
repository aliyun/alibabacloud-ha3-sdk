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
     * <p>主键列表</p>
     */
    @NameInMap("ids")
    @Validation(required = true)
    public java.util.List<String> ids;

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

}
