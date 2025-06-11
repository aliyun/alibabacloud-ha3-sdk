// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class Sort extends TeaModel {
    /**
     * <p>排序顺序, ASC：升序  DESC: 降序</p>
     */
    @NameInMap("order")
    public String order;

    /**
     * <p>表达式</p>
     */
    @NameInMap("expression")
    public String expression;

    public static Sort build(java.util.Map<String, ?> map) throws Exception {
        Sort self = new Sort();
        return TeaModel.build(map, self);
    }

    public Sort setOrder(String order) {
        this.order = order;
        return this;
    }
    public String getOrder() {
        return this.order;
    }

    public Sort setExpression(String expression) {
        this.expression = expression;
        return this;
    }
    public String getExpression() {
        return this.expression;
    }

}
