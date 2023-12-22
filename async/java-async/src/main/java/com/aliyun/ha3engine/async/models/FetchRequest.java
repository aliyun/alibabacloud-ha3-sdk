// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import com.aliyun.core.annotation.Body;
import com.aliyun.core.annotation.NameInMap;
import com.aliyun.core.annotation.Validation;
import com.aliyun.sdk.ha3engine.async.core.models.Request;

import darabonba.core.RequestModel;


/**
 * {@link FetchRequest} extends {@link RequestModel}
 *
 * <p>FetchRequest</p>
 */
public class FetchRequest extends Request {

    @Body
    @NameInMap("tableName")
    @Validation(required = true)
    private String tableName;

    @Body
    @NameInMap("ids")
    @Validation(required = true)
    private java.util.List < String > ids;

    public FetchRequest(Builder builder) {
        super(builder);
        this.tableName = builder.tableName;
        this.ids = builder.ids;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static FetchRequest create() {
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

    /**
     * @return ids
     */
    public java.util.List < String > getIds() {
        return this.ids;
    }

    public static final class Builder extends Request.Builder<FetchRequest, Builder> {
        private String tableName; 
        private java.util.List < String > ids; 

        private Builder() {
            super();
        } 

        private Builder(FetchRequest request) {
            super(request);
            this.tableName = request.tableName;
            this.ids = request.ids;
        } 

        /**
         * 数据源名
         */
        public Builder tableName(String tableName) {
            this.putBodyParameter("tableName", tableName);
            this.tableName = tableName;
            return this;
        }

        /**
         * 主键列表
         */
        public Builder ids(java.util.List < String > ids) {
            this.putBodyParameter("ids", ids);
            this.ids = ids;
            return this;
        }

        @Override
        public FetchRequest build() {
            return new FetchRequest(this);
        } 

    } 

}
