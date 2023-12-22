// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async.models;

import java.util.List;

import com.aliyun.core.annotation.*;
import darabonba.core.RequestModel;
import darabonba.core.TeaModel;

/**
 * {@link SparseData} extends {@link TeaModel}
 *
 * <p>SparseData</p>
 */
public class SparseData extends TeaModel {

    @Body
    @NameInMap("count")
    private java.util.List < Integer > count;

    @Body
    @NameInMap("indices")
    @Validation(required = true)
    private java.util.List < Long > indices;

    @Body
    @NameInMap("values")
    @Validation(required = true)
    private java.util.List < Float > values;

    private SparseData(Builder builder) {
        this.count = builder.count;
        this.indices = builder.indices;
        this.values = builder.values;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static SparseData create() {
        return builder().build();
    }

    /**
     * @return count
     */
    public java.util.List < Integer > getCount() {
        return this.count;
    }

    /**
     * @return indices
     */
    public java.util.List < Long > getIndices() {
        return this.indices;
    }

    /**
     * @return values
     */
    public java.util.List < Float > getValues() {
        return this.values;
    }

    public static final class Builder {
        private java.util.List < Integer > count; 
        private java.util.List < Long > indices; 
        private java.util.List < Float > values; 

        /**
         * 每个稀疏向量中包含的元素个数
         */
        public Builder count(java.util.List < Integer > count) {
            this.count = count;
            return this;
        }

        /**
         * 元素下标（需要从小到大排序）
         */
        public Builder indices(java.util.List < Long > indices) {
            this.indices = indices;
            return this;
        }

        /**
         * 元素值（与下标一一对应）
         */
        public Builder values(java.util.List < Float > values) {
            this.values = values;
            return this;
        }

        public SparseData build() {
            return new SparseData(this);
        } 

    } 

}
