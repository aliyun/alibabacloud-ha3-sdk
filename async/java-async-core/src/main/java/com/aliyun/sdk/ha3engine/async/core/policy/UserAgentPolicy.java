package com.aliyun.sdk.ha3engine.async.core.policy;

import java.io.IOException;
import java.util.Properties;

public class UserAgentPolicy {
    private static String gatewayVersion = "ha3engine";

    static {
        try {
            Properties props = new Properties();
            props.load(UserAgentPolicy.class.getClassLoader().getResourceAsStream("project.properties"));
            gatewayVersion = props.getProperty("ha3engine.gateway.version");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static String getDefaultUserAgentSuffix() {
        return "aliyun-gateway-ha3engine: " + gatewayVersion;
    }
}
