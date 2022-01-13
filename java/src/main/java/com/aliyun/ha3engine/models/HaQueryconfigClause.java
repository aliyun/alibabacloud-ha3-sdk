// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.models;

import com.aliyun.tea.*;

public class HaQueryconfigClause extends TeaModel {
    // 从结果集中第 start_offset 开始返回 document 
    @NameInMap("start")
    @Validation(required = true)
    public String start;

    // 返回文档的最大数量
    @NameInMap("hit")
    @Validation(required = true)
    public String hit;

    // 指定用户返回数据格式. 支持 xml 和 json 类型数据返回  
    @NameInMap("format")
    @Validation(required = true)
    public String format;

    // 扩展 配置参数
    @NameInMap("customConfig")
    public java.util.Map<String, String> customConfig;

    public static HaQueryconfigClause build(java.util.Map<String, ?> map) throws Exception {
        HaQueryconfigClause self = new HaQueryconfigClause();
        return TeaModel.build(map, self);
    }

    public HaQueryconfigClause setStart(String start) {
        this.start = start;
        return this;
    }
    public String getStart() {
        return this.start;
    }

    public HaQueryconfigClause setHit(String hit) {
        this.hit = hit;
        return this;
    }
    public String getHit() {
        return this.hit;
    }

    public HaQueryconfigClause setFormat(String format) {
        this.format = format;
        return this;
    }
    public String getFormat() {
        return this.format;
    }

    public HaQueryconfigClause setCustomConfig(java.util.Map<String, String> customConfig) {
        this.customConfig = customConfig;
        return this;
    }
    public java.util.Map<String, String> getCustomConfig() {
        return this.customConfig;
    }

}
