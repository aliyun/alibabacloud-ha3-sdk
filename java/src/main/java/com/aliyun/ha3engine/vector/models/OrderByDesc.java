// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class OrderByDesc extends TeaModel {
    /**
     * <p>排序字段名称，必须指定结果集中的字段</p>
     */
    @NameInMap("field")
    @Validation(required = true)
    public String field;

    /**
     * <p>排序方向，DESC: 降序排列；ASC: 升序排列</p>
     */
    @NameInMap("direction")
    public String direction;

    public static OrderByDesc build(java.util.Map<String, ?> map) throws Exception {
        OrderByDesc self = new OrderByDesc();
        return TeaModel.build(map, self);
    }

    public OrderByDesc setField(String field) {
        this.field = field;
        return this;
    }
    public String getField() {
        return this.field;
    }

    public OrderByDesc setDirection(String direction) {
        this.direction = direction;
        return this;
    }
    public String getDirection() {
        return this.direction;
    }

}
