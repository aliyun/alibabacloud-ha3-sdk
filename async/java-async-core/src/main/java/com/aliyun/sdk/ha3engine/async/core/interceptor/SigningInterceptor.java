package com.aliyun.sdk.ha3engine.async.core.interceptor;

import java.util.Map;
import java.util.Optional;
import java.util.Properties;

import com.aliyun.core.http.HttpHeaders;
import com.aliyun.core.http.HttpRequest;
import com.aliyun.core.utils.AttributeMap;
import com.aliyun.sdk.ha3engine.async.core.AsyncConfigInfoProvider;
import com.aliyun.tea.TeaException;

import darabonba.core.TeaConfiguration;
import darabonba.core.TeaPair;
import darabonba.core.TeaRequest;
import darabonba.core.client.ClientOption;
import darabonba.core.interceptor.HttpRequestInterceptor;
import darabonba.core.interceptor.InterceptorContext;
import darabonba.core.utils.CommonUtil;
import darabonba.core.utils.ModelUtil;

public class SigningInterceptor implements HttpRequestInterceptor {

    @Override
    public HttpRequest modifyHttpRequest(InterceptorContext context, AttributeMap attributes) {
        TeaRequest request = context.teaRequest();
        TeaConfiguration configuration = context.configuration();
        AsyncConfigInfoProvider provider = (AsyncConfigInfoProvider) configuration.clientConfiguration().option(ClientOption.CREDENTIALS_PROVIDER);

        Map<String, String> headers = CommonUtil.merge(String.class, CommonUtil.buildMap(
                        new TeaPair("user-agent", getUserAgent()),
                        new TeaPair("host", configuration.endpoint()),
                        new TeaPair("authorization", "Basic " + getRealmSignStr(provider.getUsername(), provider.getPassword()) + ""),
                        new TeaPair("content-type", "application/json; charset=utf-8")
                ),
                request.headers().toMap()
        );
        if (!com.aliyun.teautil.Common.isUnset(request.query())) {
            headers.put("X-Opensearch-Request-ID", com.aliyun.teautil.Common.getNonce());
        }
        if (!com.aliyun.teautil.Common.isUnset(request.body())) {
            headers.put("X-Opensearch-Swift-Request-ID", com.aliyun.teautil.Common.getNonce());
        }

        HttpHeaders httpHeaders = new HttpHeaders(headers);

        HttpRequest httpRequest = new HttpRequest(Optional.ofNullable(configuration.method()).orElseGet(request::method),
                ModelUtil.composeUrl(configuration.endpoint(), request.query(), configuration.protocol(), request.pathname()));
        httpRequest.setHeaders(httpHeaders);
        httpRequest.setBody(com.aliyun.teautil.Common.toJSONString(request.body()));
        return httpRequest;
    }

    /**
     * 计算用户请求识别特征, 遵循 Basic Auth 生成规范.
     */
    private String getRealmSignStr(String accessUserName, String accessPassWord) {
        try {
            String accessUserNameStr = com.aliyun.darabonbastring.Client.trim(accessUserName);
            String accessPassWordStr = com.aliyun.darabonbastring.Client.trim(accessPassWord);
            String realmStr = "" + accessUserNameStr + ":" + accessPassWordStr + "";
            return com.aliyun.darabonba.encode.Encoder.base64EncodeToString(com.aliyun.darabonbastring.Client.toBytes(realmStr, "UTF-8"));
        } catch (Exception e) {
            throw new TeaException();
        }
    }

    private String getUserAgent() {
        Properties sysProps = System.getProperties();
        return String.format("AlibabaCloud (%s; %s) Java/%s %s/%s TeaDSL/1", sysProps.getProperty("os.name"), sysProps.getProperty("os.arch"), sysProps.getProperty("java.runtime.version"), "tea-util", "0.2.21");
    }
}
