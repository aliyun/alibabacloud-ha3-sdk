package com.aliyun.sdk.ha3engine.async.core.interceptor;

import com.aliyun.core.utils.AttributeMap;
import com.aliyun.tea.TeaConverter;
import com.aliyun.tea.TeaException;
import com.aliyun.tea.TeaPair;

import darabonba.core.TeaResponse;
import darabonba.core.exception.ClientException;
import darabonba.core.interceptor.InterceptorContext;
import darabonba.core.interceptor.ResponseInterceptor;

public class ResponseBodyInterceptor implements ResponseInterceptor {

    @Override
    public TeaResponse modifyResponse(InterceptorContext context, AttributeMap attributes) {
        TeaResponse response = context.teaResponse();

        try {
            // 处理response body
            handleResponseBody(response);
        } catch (TeaException e) {
            response.setException(new ClientException(com.aliyun.teautil.Common.toJSONString(e.getData()), e));
        }
        return response;
    }

    private void handleResponseBody(TeaResponse response) {
        int statusCode = response.httpResponse().getStatusCode();
        String responseBody = response.httpResponse().getBodyAsString();
        if (com.aliyun.teautil.Common.is4xx(statusCode) || com.aliyun.teautil.Common.is5xx(statusCode)) {
            java.util.Map<String, Object> rawMap = TeaConverter.buildMap(new TeaPair("errors", responseBody));
            throw new TeaException(TeaConverter.buildMap(
                    new TeaPair("message", "FAIL"),
                    new TeaPair("data", rawMap),
                    new TeaPair("code", statusCode)
            ));
        }

        if (com.aliyun.teautil.Common.empty(responseBody)) {
            java.util.Map<String, Object> responseMap = TeaConverter.buildMap(
                    new TeaPair("status", "OK"),
                    new TeaPair("code", statusCode)
            );
            response.setDeserializedBody(com.aliyun.teautil.Common.toJSONString(responseMap));
            return;
        }

        if (response.success()) {
            response.setDeserializedBody(responseBody);
        }
    }
}
