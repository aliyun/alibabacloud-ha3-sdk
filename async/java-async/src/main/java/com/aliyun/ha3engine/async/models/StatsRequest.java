// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import com.aliyun.core.annotation.*;
import darabonba.core.RequestModel;
import darabonba.core.TeaModel;
import com.aliyun.sdk.ha3engine.async.core.models.Request;

/**
 * {@link StatsRequest} extends {@link RequestModel}
 *
 * <p>StatsRequest</p>
 */
public class StatsRequest extends Request {

    @Body
    @NameInMap("tableName")
    @Validation(required = true)
    private String tableName;

    private StatsRequest(Builder builder) {
        super(builder);
        this.tableName = builder.tableName;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static StatsRequest create() {
        return builder().build();
    }

    @Override
    public Builder toBuilder() {
        return new Builder(this);
    }

    /**
     * @return tableName
     */
    public String getTableName() {
        return this.tableName;
    }

    public static final class Builder extends Request.Builder<StatsRequest, Builder> {
        private String tableName; 

        private Builder() {
            super();
        } 

        private Builder(StatsRequest request) {
            super(request);
            this.tableName = request.tableName;
        } 

        /**
         * 数据源名
         */
        public Builder tableName(String tableName) {
            this.putBodyParameter("tableName", tableName);
            this.tableName = tableName;
            return this;
        }

        @Override
        public StatsRequest build() {
            return new StatsRequest(this);
        } 

    } 

}
