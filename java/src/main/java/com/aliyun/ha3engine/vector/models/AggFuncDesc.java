// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class AggFuncDesc extends TeaModel {
    /**
     * <p>可以指定统计值在结果集中字段的名称。默认结果字段为: FUNC_NAME(args)</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>统计函数名：max, min, avg, sum, count</p>
     */
    @NameInMap("func")
    @Validation(required = true)
    public String func;

    /**
     * <p>统计函数的参数</p>
     */
    @NameInMap("args")
    @Validation(required = true)
    public java.util.List<String> args;

    public static AggFuncDesc build(java.util.Map<String, ?> map) throws Exception {
        AggFuncDesc self = new AggFuncDesc();
        return TeaModel.build(map, self);
    }

    public AggFuncDesc setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public AggFuncDesc setFunc(String func) {
        this.func = func;
        return this;
    }
    public String getFunc() {
        return this.func;
    }

    public AggFuncDesc setArgs(java.util.List<String> args) {
        this.args = args;
        return this;
    }
    public java.util.List<String> getArgs() {
        return this.args;
    }

}
