// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.models;

import com.aliyun.tea.*;

public class Config extends TeaModel {
    @NameInMap("endpoint")
    public String endpoint;

    @NameInMap("instanceId")
    public String instanceId;

    @NameInMap("protocol")
    public String protocol;

    @NameInMap("accessUserName")
    public String accessUserName;

    @NameInMap("accessPassWord")
    public String accessPassWord;

    @NameInMap("userAgent")
    public String userAgent;

    public static Config build(java.util.Map<String, ?> map) throws Exception {
        Config self = new Config();
        return TeaModel.build(map, self);
    }

    public Config setEndpoint(String endpoint) {
        this.endpoint = endpoint;
        return this;
    }
    public String getEndpoint() {
        return this.endpoint;
    }

    public Config setInstanceId(String instanceId) {
        this.instanceId = instanceId;
        return this;
    }
    public String getInstanceId() {
        return this.instanceId;
    }

    public Config setProtocol(String protocol) {
        this.protocol = protocol;
        return this;
    }
    public String getProtocol() {
        return this.protocol;
    }

    public Config setAccessUserName(String accessUserName) {
        this.accessUserName = accessUserName;
        return this;
    }
    public String getAccessUserName() {
        return this.accessUserName;
    }

    public Config setAccessPassWord(String accessPassWord) {
        this.accessPassWord = accessPassWord;
        return this;
    }
    public String getAccessPassWord() {
        return this.accessPassWord;
    }

    public Config setUserAgent(String userAgent) {
        this.userAgent = userAgent;
        return this;
    }
    public String getUserAgent() {
        return this.userAgent;
    }

}
