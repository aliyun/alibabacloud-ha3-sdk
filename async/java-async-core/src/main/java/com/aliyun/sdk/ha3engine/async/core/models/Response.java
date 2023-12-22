// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sdk.ha3engine.async.core.models;

import darabonba.core.TeaModel;

public abstract class Response extends TeaModel {

    protected Response(BuilderImpl<?, ?> builder) {
    }

    public abstract Builder toBuilder();

    public interface Builder<ProviderT extends Response, BuilderT extends Builder> {

        ProviderT build();

    }

    protected abstract static class BuilderImpl<ProviderT extends Response, BuilderT extends Builder>
            implements Builder<ProviderT, BuilderT> {

        protected BuilderImpl() {
        }

        protected BuilderImpl(Response response) {
        }

    }

}
