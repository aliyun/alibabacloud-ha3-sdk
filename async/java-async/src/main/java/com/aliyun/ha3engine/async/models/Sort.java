// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import com.aliyun.core.annotation.Body;
import com.aliyun.tea.NameInMap;
import com.aliyun.tea.TeaModel;

public class Sort extends TeaModel {
    /**
     * <p>排序顺序, ASC：升序  DESC: 降序</p>
     */
    @Body
    @NameInMap("order")
    private String order;

    /**
     * <p>表达式</p>
     */
    @Body
    @NameInMap("expression")
    private String expression;

    private Sort(Builder builder) {
        this.order = builder.order;
        this.expression = builder.expression;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Sort create() {
        return builder().build();
    }

    public String getOrder() {
        return this.order;
    }

    public String getExpression() {
        return this.expression;
    }

    public static final class Builder {
        private String order;
        private String expression;

        /**
         * 排序顺序, ASC：升序  DESC: 降序
         */
        public Builder order(String order) {
            this.order = order;
            return this;
        }

        /**
         * 表达式
         */
        public Builder expression(String expression) {
            this.expression = expression;
            return this;
        }

        public Sort build() {
            return new Sort(this);
        }
    }
}
