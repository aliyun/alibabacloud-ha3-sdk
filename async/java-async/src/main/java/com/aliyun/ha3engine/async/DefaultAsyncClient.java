// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.CompletableFuture;

import com.aliyun.core.http.BodyType;
import com.aliyun.core.http.HttpMethod;
import com.aliyun.ha3engine.async.models.*;

import darabonba.core.RequestStyle;
import darabonba.core.TeaAsyncHandler;
import darabonba.core.TeaRequest;
import darabonba.core.client.ClientConfiguration;
import darabonba.core.client.ClientExecutionParams;


/**
 * <p>Main client.</p>
 */
public final class DefaultAsyncClient implements AsyncClient {

    protected final TeaRequest REQUEST;
    protected final TeaAsyncHandler handler;

    protected DefaultAsyncClient(ClientConfiguration configuration) {
        this.handler = new TeaAsyncHandler(configuration);
        this.REQUEST = TeaRequest.create();
    }

    /**
     * 向量查询
     */
    @Override
    public CompletableFuture<SearchResponse> query(QueryRequest request) {
        try {
            TeaRequest teaRequest = REQUEST.copy()
                    .setStyle(RequestStyle.RESTFUL)
                    .setAction("Query")
                    .setMethod(HttpMethod.POST)
                    .setPathRegex("/vector-service/query")
                    .setBodyType(BodyType.JSON)
                    .setBodyIsForm(false)
                    .setReqBodyType(BodyType.JSON)
                    .formModel(request);
            ClientExecutionParams params = new ClientExecutionParams().withInput(request).withRequest(teaRequest).withOutput(SearchResponse.create());
            return this.handler.execute(params);
        } catch (Exception e) {
            CompletableFuture<SearchResponse> future = new CompletableFuture<>();
            future.completeExceptionally(e);
            return future;
        }
    }

    /**
     * 向量预测查询
     */
    @Override
    public CompletableFuture<SearchResponse> inferenceQuery(QueryRequest request) {
        try {
            TeaRequest teaRequest = REQUEST.copy()
                    .setStyle(RequestStyle.RESTFUL)
                    .setAction("InferenceQuery")
                    .setMethod(HttpMethod.POST)
                    .setPathRegex("/vector-service/inference-query")
                    .setBodyType(BodyType.JSON)
                    .setBodyIsForm(false)
                    .setReqBodyType(BodyType.JSON)
                    .formModel(request);
            ClientExecutionParams params = new ClientExecutionParams().withInput(request).withRequest(teaRequest).withOutput(SearchResponse.create());
            return this.handler.execute(params);
        } catch (Exception e) {
            CompletableFuture<SearchResponse> future = new CompletableFuture<>();
            future.completeExceptionally(e);
            return future;
        }
    }

    /**
     * 多namespace查询
     */
    @Override
    public CompletableFuture<SearchResponse> multiQuery(MultiQueryRequest request) {
        try {
            TeaRequest teaRequest = REQUEST.copy()
                    .setStyle(RequestStyle.RESTFUL)
                    .setAction("MultiQuery")
                    .setMethod(HttpMethod.POST)
                    .setPathRegex("/vector-service/multi-query")
                    .setBodyType(BodyType.JSON)
                    .setBodyIsForm(false)
                    .setReqBodyType(BodyType.JSON)
                    .formModel(request);
            ClientExecutionParams params = new ClientExecutionParams().withInput(request).withRequest(teaRequest).withOutput(SearchResponse.create());
            return this.handler.execute(params);
        } catch (Exception e) {
            CompletableFuture<SearchResponse> future = new CompletableFuture<>();
            future.completeExceptionally(e);
            return future;
        }
    }

    /**
     * 查询数据
     */
    @Override
    public CompletableFuture<SearchResponse> fetch(FetchRequest request) {
        try {
            TeaRequest teaRequest = REQUEST.copy()
                    .setStyle(RequestStyle.RESTFUL)
                    .setAction("Fetch")
                    .setMethod(HttpMethod.POST)
                    .setPathRegex("/vector-service/fetch")
                    .setBodyType(BodyType.JSON)
                    .setBodyIsForm(false)
                    .setReqBodyType(BodyType.JSON)
                    .formModel(request);
            ClientExecutionParams params = new ClientExecutionParams().withInput(request).withRequest(teaRequest).withOutput(SearchResponse.create());
            return this.handler.execute(params);
        } catch (Exception e) {
            CompletableFuture<SearchResponse> future = new CompletableFuture<>();
            future.completeExceptionally(e);
            return future;
        }
    }

    /**
     * 文档统计
     */
    @Override
    public CompletableFuture<SearchResponse> stats(StatsRequest request) {
        try {
            TeaRequest teaRequest = REQUEST.copy()
                    .setStyle(RequestStyle.RESTFUL)
                    .setAction("Stats")
                    .setMethod(HttpMethod.POST)
                    .setPathRegex("/vector-service/stats")
                    .setBodyType(BodyType.JSON)
                    .setBodyIsForm(false)
                    .setReqBodyType(BodyType.JSON)
                    .formModel(request);
            ClientExecutionParams params = new ClientExecutionParams().withInput(request).withRequest(teaRequest).withOutput(SearchResponse.create());
            return this.handler.execute(params);
        } catch (Exception e) {
            CompletableFuture<SearchResponse> future = new CompletableFuture<>();
            future.completeExceptionally(e);
            return future;
        }
    }

    /**
     * 支持新增、更新、删除 等操作，以及对应批量操作
     */
    @Override
    public CompletableFuture<PushDocumentsResponse> pushDocuments(String dataSourceName, String keyField, PushDocumentsRequest request) {
        try {
            Map<String, String> headers = null == request.getHeaders() || request.getHeaders().isEmpty() ? new HashMap<>() : request.getHeaders();
            headers.put("X-Opensearch-Swift-PK-Field", keyField);
            PushDocumentsRequest build = request.toBuilder().headers(headers).body(request.getBody()).build();
            TeaRequest teaRequest = REQUEST.copy()
                    .setStyle(RequestStyle.RESTFUL)
                    .setAction("PushDocuments")
                    .setMethod(HttpMethod.POST)
                    .setPathRegex("/update/" + dataSourceName + "/actions/bulk")
                    .setBodyType(BodyType.JSON)
                    .setBodyIsForm(false)
                    .setReqBodyType(BodyType.JSON)
                    .formModel(build);
            ClientExecutionParams params = new ClientExecutionParams().withInput(request).withRequest(teaRequest).withOutput(PushDocumentsResponse.create());
            return this.handler.execute(params);
        } catch (Exception e) {
            CompletableFuture<PushDocumentsResponse> future = new CompletableFuture<>();
            future.completeExceptionally(e);
            return future;
        }
    }

    /**
     * 用于内网环境的新增、更新、删除 等操作，以及对应批量操作
     */
    @Override
    public CompletableFuture<PushDocumentsResponse> pushDocumentsWithSwift(String dataSourceName, String keyField, String topic, String swift, PushDocumentsRequest request) {
        try {
            Map<String, String> headers = new HashMap<>();
            headers.put("X-Opensearch-Swift-PK-Field", keyField);
            headers.put("X-Opensearch-Swift-Topic", topic);
            headers.put("X-Opensearch-Swift-Swift", swift);
            PushDocumentsRequest build = request.toBuilder().headers(headers).body(request.getBody()).build();
            TeaRequest teaRequest = REQUEST.copy()
                    .setStyle(RequestStyle.RESTFUL)
                    .setAction("PushDocumentsWithSwift")
                    .setMethod(HttpMethod.POST)
                    .setPathRegex("/update/" + dataSourceName + "/actions/bulk")
                    .setBodyType(BodyType.JSON)
                    .setBodyIsForm(false)
                    .setReqBodyType(BodyType.JSON)
                    .formModel(build);
            ClientExecutionParams params = new ClientExecutionParams().withInput(request).withRequest(teaRequest).withOutput(PushDocumentsResponse.create());
            return this.handler.execute(params);
        } catch (Exception e) {
            CompletableFuture<PushDocumentsResponse> future = new CompletableFuture<>();
            future.completeExceptionally(e);
            return future;
        }
    }

}
