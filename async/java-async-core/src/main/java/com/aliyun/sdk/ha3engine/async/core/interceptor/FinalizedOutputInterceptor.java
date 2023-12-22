package com.aliyun.sdk.ha3engine.async.core.interceptor;

import com.aliyun.core.utils.AttributeMap;
import darabonba.core.TeaModel;
import darabonba.core.TeaPair;
import darabonba.core.TeaResponse;
import darabonba.core.exception.TeaException;
import darabonba.core.interceptor.InterceptorContext;
import darabonba.core.interceptor.OutputInterceptor;
import darabonba.core.utils.CommonUtil;

import java.util.Map;

public class FinalizedOutputInterceptor implements OutputInterceptor {

    @Override
    public TeaModel modifyOutput(InterceptorContext context, AttributeMap attributes) {
        TeaResponse response = context.teaResponse();
        Map<String, Object> model = CommonUtil.buildMap(
                new TeaPair("body", response.deserializedBody()),
                new TeaPair("headers", response.httpResponse().getHeaders().toMap()));
        try {
            TeaModel.toModel(model, context.output());
        } catch (Exception e) {
            throw new TeaException(e);
        }
        return context.output();
    }
}
