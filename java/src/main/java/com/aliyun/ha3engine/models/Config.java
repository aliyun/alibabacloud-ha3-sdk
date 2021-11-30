// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.models;

import com.aliyun.tea.*;

public class Config extends TeaModel {
    @NameInMap("endpoint")
    public String endpoint;

    @NameInMap("protocol")
    public String protocol;

    @NameInMap("type")
    public String type;

    @NameInMap("accessUser")
    public String accessUser;

    @NameInMap("accessSecret")
    public String accessSecret;

    @NameInMap("userAgent")
    public String userAgent;

    public static Config build(java.util.Map<String, ?> map) throws Exception {
        Config self = new Config();
        return TeaModel.build(map, self);
    }

}
