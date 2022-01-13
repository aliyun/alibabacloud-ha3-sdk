// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.models;

import com.aliyun.tea.*;

public class HaQueryAggregateClause extends TeaModel {
    // field为要进行统计的字段名，必须配置属性字段
    @NameInMap("group_key")
    @Validation(required = true)
    public String groupKey;

    // func可以为count()、sum(id)、max(id)、min(id)四种系统函数，含义分别为：文档个数、对id字段求和、取id字段最大值、取id字段最小值；支持同时进行多个函数的统计，中间用英文井号（#）分隔；sum、max、min的内容支持基本的算术运算
    @NameInMap("agg_fun")
    @Validation(required = true)
    public String aggFun;

    // 表示分段统计，可用于分布统计，只支持单个range参数。
    @NameInMap("range")
    public String range;

    // 最大返回组数
    @NameInMap("max_group")
    public String maxGroup;

    // 表示仅统计满足特定条件的文档
    @NameInMap("agg_filter")
    public String aggFilter;

    // ，抽样统计的阈值。表示该值之前的文档会依次统计，该值之后的文档会进行抽样统计；
    @NameInMap("agg_sampler_threshold")
    public String aggSamplerThresHold;

    // 抽样统计的步长，表示从agg_sampler_threshold后的文档将间隔agg_sampler_step个文档统计一次。对于sum和count类型的统计会把阈值后的抽样统计结果最后乘以步长进行估算，估算的结果再加上阈值前的统计结果就是最后的统计结果。
    @NameInMap("agg_sampler_step")
    public String aggSamplerStep;

    public static HaQueryAggregateClause build(java.util.Map<String, ?> map) throws Exception {
        HaQueryAggregateClause self = new HaQueryAggregateClause();
        return TeaModel.build(map, self);
    }

    public HaQueryAggregateClause setGroupKey(String groupKey) {
        this.groupKey = groupKey;
        return this;
    }
    public String getGroupKey() {
        return this.groupKey;
    }

    public HaQueryAggregateClause setAggFun(String aggFun) {
        this.aggFun = aggFun;
        return this;
    }
    public String getAggFun() {
        return this.aggFun;
    }

    public HaQueryAggregateClause setRange(String range) {
        this.range = range;
        return this;
    }
    public String getRange() {
        return this.range;
    }

    public HaQueryAggregateClause setMaxGroup(String maxGroup) {
        this.maxGroup = maxGroup;
        return this;
    }
    public String getMaxGroup() {
        return this.maxGroup;
    }

    public HaQueryAggregateClause setAggFilter(String aggFilter) {
        this.aggFilter = aggFilter;
        return this;
    }
    public String getAggFilter() {
        return this.aggFilter;
    }

    public HaQueryAggregateClause setAggSamplerThresHold(String aggSamplerThresHold) {
        this.aggSamplerThresHold = aggSamplerThresHold;
        return this;
    }
    public String getAggSamplerThresHold() {
        return this.aggSamplerThresHold;
    }

    public HaQueryAggregateClause setAggSamplerStep(String aggSamplerStep) {
        this.aggSamplerStep = aggSamplerStep;
        return this;
    }
    public String getAggSamplerStep() {
        return this.aggSamplerStep;
    }

}
