// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class RankQuery extends TeaModel {
    /**
     * <p>查询表达式</p>
     */
    @NameInMap("rrf")
    public java.util.Map<String, String> rrf;

    public static RankQuery build(java.util.Map<String, ?> map) throws Exception {
        RankQuery self = new RankQuery();
        return TeaModel.build(map, self);
    }

    public RankQuery setRrf(java.util.Map<String, String> rrf) {
        this.rrf = rrf;
        return this;
    }
    public java.util.Map<String, String> getRrf() {
        return this.rrf;
    }

}
