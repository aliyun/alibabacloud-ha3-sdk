// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import com.aliyun.core.annotation.Body;
import com.aliyun.core.annotation.NameInMap;
import com.aliyun.core.annotation.Validation;

import darabonba.core.TeaModel;

/**
 * {@link OrderByDesc} extends {@link TeaModel}
 *
 * <p>OrderByDesc</p>
 */
public class OrderByDesc extends TeaModel {

    @Body
    @NameInMap("field")
    @Validation(required = true)
    private String field;

    @Body
    @NameInMap("direction")
    private String direction;

    private OrderByDesc(Builder builder) {
        this.field = builder.field;
        this.direction = builder.direction;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static OrderByDesc create() {
        return builder().build();
    }

    /**
     * @return field
     */
    public String getField() {
        return this.field;
    }

    /**
     * @return direction
     */
    public String getDirection() {
        return this.direction;
    }

    public static final class Builder {
        private String field; 
        private String direction; 

        /**
         * 排序字段名称，必须指定结果集中的字段
         */
        public Builder field(String field) {
            this.field = field;
            return this;
        }

        /**
         * 排序方向，DESC: 降序排列；ASC: 升序排列
         */
        public Builder direction(String direction) {
            this.direction = direction;
            return this;
        }

        public OrderByDesc build() {
            return new OrderByDesc(this);
        } 

    } 

}
