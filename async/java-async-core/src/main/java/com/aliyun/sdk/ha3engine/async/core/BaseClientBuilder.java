package com.aliyun.sdk.ha3engine.async.core;

import com.aliyun.sdk.ha3engine.async.core.interceptor.FinalizedOutputInterceptor;
import com.aliyun.sdk.ha3engine.async.core.interceptor.MakeMutableResponseInterceptor;
import com.aliyun.sdk.ha3engine.async.core.interceptor.ResponseBodyInterceptor;
import com.aliyun.sdk.ha3engine.async.core.interceptor.SigningInterceptor;
import com.aliyun.sdk.ha3engine.async.core.policy.UserAgentPolicy;

import darabonba.core.TeaClientBuilder;
import darabonba.core.client.ClientConfiguration;
import darabonba.core.client.ClientOption;
import darabonba.core.client.IClientBuilder;
import darabonba.core.interceptor.InterceptorChain;

public abstract class BaseClientBuilder<BuilderT extends IClientBuilder<BuilderT, ClientT>, ClientT> extends TeaClientBuilder<BuilderT, ClientT> {

    @Override
    protected String serviceName() {
        return "Ha3engine";
    }

    BuilderT serviceConfiguration(Configuration serviceConfiguration) {
        clientConfiguration.setOption(ClientOption.SERVICE_CONFIGURATION, serviceConfiguration);
        return (BuilderT) this;
    }

    @Override
    protected ClientConfiguration mergeServiceDefaults(ClientConfiguration configuration) {
        return configuration.merge(ClientConfiguration.create()
                .setOption(ClientOption.SERVICE_CONFIGURATION, Configuration.create())
                .setOption(ClientOption.USER_AGENT_SERVICE_SUFFIX, UserAgentPolicy.getDefaultUserAgentSuffix()));
    }

    @Override
    protected ClientConfiguration finalizeServiceConfiguration(ClientConfiguration configuration) {
        //interceptor
        InterceptorChain chain = InterceptorChain.create();
        chain.addHttpRequestInterceptor(new SigningInterceptor());
        chain.addResponseInterceptor(new MakeMutableResponseInterceptor());
        chain.addResponseInterceptor(new ResponseBodyInterceptor());
        chain.addOutputInterceptor(new FinalizedOutputInterceptor());
        configuration.setOption(ClientOption.INTERCEPTOR_CHAIN, chain);
        return configuration;
    }
}
