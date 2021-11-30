// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.models;

import com.aliyun.tea.*;

public class SearchQuery extends TeaModel {
    @NameInMap("query")
    @Validation(required = true)
    public String query;

    public static SearchQuery build(java.util.Map<String, ?> map) throws Exception {
        SearchQuery self = new SearchQuery();
        return TeaModel.build(map, self);
    }

}
