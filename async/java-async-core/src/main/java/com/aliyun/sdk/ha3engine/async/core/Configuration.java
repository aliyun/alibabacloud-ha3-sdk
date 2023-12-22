package com.aliyun.sdk.ha3engine.async.core;

import darabonba.core.ServiceConfiguration;

public final class Configuration implements ServiceConfiguration {

    private Configuration() {
    }

    public static Configuration create() {
        return new Configuration();
    }

}

