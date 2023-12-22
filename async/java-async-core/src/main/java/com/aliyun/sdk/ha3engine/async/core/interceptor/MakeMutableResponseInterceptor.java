package com.aliyun.sdk.ha3engine.async.core.interceptor;

import com.aliyun.core.http.HttpResponse;
import com.aliyun.core.utils.AttributeMap;
import darabonba.core.TeaResponse;
import darabonba.core.interceptor.InterceptorContext;
import darabonba.core.interceptor.ResponseInterceptor;
import darabonba.core.utils.CommonUtil;

/**
 * @Author maguoxin
 * @Date 2023-12-21 18:43
 **/
public class MakeMutableResponseInterceptor implements ResponseInterceptor {

    @Override
    public TeaResponse modifyResponse(InterceptorContext context, AttributeMap attributes) {
        final HttpResponse httpResponse = context.httpResponse();
        TeaResponse response = new TeaResponse();
        response.setHttpResponse(httpResponse);
        response.setSuccess(CommonUtil.is2xx(httpResponse.getStatusCode()));
        return response;
    }
}
