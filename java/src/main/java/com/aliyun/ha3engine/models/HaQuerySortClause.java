// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.models;

import com.aliyun.tea.*;

public class HaQuerySortClause extends TeaModel {
    /**
     * <p>field为要进行统计的字段名，必须配置属性字段</p>
     */
    @NameInMap("sortKey")
    @Validation(required = true)
    public String sortKey;

    /**
     * <p>+为按字段值升序排序，-为降序排序</p>
     */
    @NameInMap("sortOrder")
    @Validation(required = true)
    public String sortOrder;

    public static HaQuerySortClause build(java.util.Map<String, ?> map) throws Exception {
        HaQuerySortClause self = new HaQuerySortClause();
        return TeaModel.build(map, self);
    }

    public HaQuerySortClause setSortKey(String sortKey) {
        this.sortKey = sortKey;
        return this;
    }
    public String getSortKey() {
        return this.sortKey;
    }

    public HaQuerySortClause setSortOrder(String sortOrder) {
        this.sortOrder = sortOrder;
        return this;
    }
    public String getSortOrder() {
        return this.sortOrder;
    }

}
