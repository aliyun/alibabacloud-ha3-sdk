// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.vector.models;

import com.aliyun.tea.*;

public class SparseData extends TeaModel {
    /**
     * <p>每个稀疏向量中包含的元素个数</p>
     */
    @NameInMap("count")
    public java.util.List<Integer> count;

    /**
     * <p>元素下标（需要从小到大排序）</p>
     */
    @NameInMap("indices")
    @Validation(required = true)
    public java.util.List<Long> indices;

    /**
     * <p>元素值（与下标一一对应）</p>
     */
    @NameInMap("values")
    @Validation(required = true)
    public java.util.List<Float> values;

    public static SparseData build(java.util.Map<String, ?> map) throws Exception {
        SparseData self = new SparseData();
        return TeaModel.build(map, self);
    }

    public SparseData setCount(java.util.List<Integer> count) {
        this.count = count;
        return this;
    }
    public java.util.List<Integer> getCount() {
        return this.count;
    }

    public SparseData setIndices(java.util.List<Long> indices) {
        this.indices = indices;
        return this;
    }
    public java.util.List<Long> getIndices() {
        return this.indices;
    }

    public SparseData setValues(java.util.List<Float> values) {
        this.values = values;
        return this;
    }
    public java.util.List<Float> getValues() {
        return this.values;
    }

}
