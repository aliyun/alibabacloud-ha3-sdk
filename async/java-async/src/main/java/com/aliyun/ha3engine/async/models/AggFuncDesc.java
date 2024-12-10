// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import java.util.List;

import com.aliyun.core.annotation.Body;
import com.aliyun.core.annotation.NameInMap;
import com.aliyun.core.annotation.Validation;

import darabonba.core.TeaModel;

/**
 * {@link AggFuncDesc} extends {@link TeaModel}
 *
 * <p>AggFuncDesc</p>
 */
public class AggFuncDesc extends TeaModel {

    @Body
    @NameInMap("name")
    private String name;

    @Body
    @NameInMap("func")
    @Validation(required = true)
    private String func;

    @Body
    @NameInMap("args")
    @Validation(required = true)
    private List < String > args;

    private AggFuncDesc(Builder builder) {
        this.name = builder.name;
        this.func = builder.func;
        this.args = builder.args;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static AggFuncDesc create() {
        return builder().build();
    }

    /**
     * @return name
     */
    public String getName() {
        return this.name;
    }

    /**
     * @return func
     */
    public String getFunc() {
        return this.func;
    }

    /**
     * @return args
     */
    public List < String > getArgs() {
        return this.args;
    }

    public static final class Builder {
        private String name; 
        private String func; 
        private List < String > args;

        /**
         * 可以指定统计值在结果集中字段的名称。默认结果字段为: FUNC_NAME(args)
         */
        public Builder name(String name) {
            this.name = name;
            return this;
        }

        /**
         * 统计函数名：max, min, avg, sum, count
         */
        public Builder func(String func) {
            this.func = func;
            return this;
        }

        /**
         * 统计函数的参数
         */
        public Builder args(List < String > args) {
            this.args = args;
            return this;
        }

        public AggFuncDesc build() {
            return new AggFuncDesc(this);
        } 

    } 

}
