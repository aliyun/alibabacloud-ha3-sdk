// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import com.aliyun.core.annotation.Body;
import com.aliyun.core.annotation.NameInMap;

import darabonba.core.TeaModel;

/**
 * {@link RankQuery} extends {@link TeaModel}
 *
 * <p>RankQuery</p>
 */
public class RankQuery extends TeaModel {

    @Body
    @NameInMap("rrf")
    private java.util.Map < String, String > rrf;

    private RankQuery(Builder builder) {
        this.rrf = builder.rrf;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static RankQuery create() {
        return builder().build();
    }

    /**
     * @return rrf
     */
    public java.util.Map < String, String > getRrf() {
        return this.rrf;
    }

    public static final class Builder {
        private java.util.Map < String, String > rrf; 

        /**
         * 查询表达式
         */
        public Builder rrf(java.util.Map < String, String > rrf) {
            this.rrf = rrf;
            return this;
        }

        public RankQuery build() {
            return new RankQuery(this);
        } 

    } 

}
