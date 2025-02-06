// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.CompletableFuture;
import java.util.zip.Deflater;

import com.aliyun.core.http.BodyType;
import com.aliyun.core.http.HttpHeaders;
import com.aliyun.core.http.HttpMethod;
import com.aliyun.ha3engine.async.models.*;
import com.aliyun.ha3engine.async.models.protobuf.VectorRequest;
import com.aliyun.sdk.ha3engine.async.core.models.Request;

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
            compressRequest(request);

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
     * 向量查询(pb协议)
     */
    public CompletableFuture<SearchResponse> query(VectorRequest.VectorSearchQuery request, boolean compress) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.set("Content-Type", "application/protobuf");

            TeaRequest teaRequest = REQUEST.copy()
                .setStyle(RequestStyle.RESTFUL)
                .setAction("Query")
                .setMethod(HttpMethod.POST)
                .setPathname("/vector-service/query")
                .setBodyType(BodyType.JSON)
                .setBodyIsForm(false)
                .setHeaders(headers)
                .setQuery(new HashMap<>())
                .setReqBodyType(BodyType.BINARY);
            teaRequest.setBody(request.toByteArray());
            compressPbRequest(teaRequest, compress);

            ClientExecutionParams params = new ClientExecutionParams().withRequest(teaRequest).withOutput(SearchResponse.create());
            return this.handler.execute(params);
        } catch (Exception e) {
            CompletableFuture<SearchResponse> future = new CompletableFuture<>();
            future.completeExceptionally(e);
            return future;
        }
    }

    /**
     * 向量预测查询(pb)
     */
    @Override
    public CompletableFuture<SearchResponse> inferenceQuery(VectorRequest.VectorSearchQuery request, boolean compress) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.set("Content-Type", "application/protobuf");

            TeaRequest teaRequest = REQUEST.copy()
                .setStyle(RequestStyle.RESTFUL)
                .setAction("InferenceQuery")
                .setMethod(HttpMethod.POST)
                .setPathname("/vector-service/inference-query")
                .setBodyType(BodyType.JSON)
                .setBodyIsForm(false)
                .setHeaders(headers)
                .setQuery(new HashMap<>())
                .setReqBodyType(BodyType.BINARY);
            teaRequest.setBody(request.toByteArray());

            compressPbRequest(teaRequest, compress);

            ClientExecutionParams params = new ClientExecutionParams().withRequest(teaRequest).withOutput(SearchResponse.create());
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
            compressRequest(request);

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
            compressRequest(request);

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
     * 多namespace查询（pb协议）
     */
    @Override
    public CompletableFuture<SearchResponse> multiQuery(VectorRequest.VectorSearchQueries request, boolean compress) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.set("Content-Type", "application/protobuf");

            TeaRequest teaRequest = REQUEST.copy()
                .setStyle(RequestStyle.RESTFUL)
                .setAction("MultiQuery")
                .setMethod(HttpMethod.POST)
                .setPathname("/vector-service/multi-query")
                .setBodyType(BodyType.JSON)
                .setBodyIsForm(false)
                .setHeaders(headers)
                .setQuery(new HashMap<>())
                .setReqBodyType(BodyType.BINARY);
            teaRequest.setBody(request.toByteArray());

            compressPbRequest(teaRequest, compress);

            ClientExecutionParams params = new ClientExecutionParams().withRequest(teaRequest).withOutput(SearchResponse.create());
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
            compressRequest(request);

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
     * 查询数据（pb协议）
     */
    @Override
    public CompletableFuture<SearchResponse> fetch(VectorRequest.FetchQuery request, boolean compress) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.set("Content-Type", "application/protobuf");

            TeaRequest teaRequest = REQUEST.copy()
                .setStyle(RequestStyle.RESTFUL)
                .setAction("Fetch")
                .setMethod(HttpMethod.POST)
                .setPathname("/vector-service/fetch")
                .setBodyType(BodyType.JSON)
                .setBodyIsForm(false)
                .setHeaders(headers)
                .setQuery(new HashMap<>())
                .setReqBodyType(BodyType.BINARY);
            teaRequest.setBody(request.toByteArray());

            compressPbRequest(teaRequest, compress);

            ClientExecutionParams params = new ClientExecutionParams().withRequest(teaRequest).withOutput(SearchResponse.create());
            return this.handler.execute(params);
        } catch (Exception e) {
            CompletableFuture<SearchResponse> future = new CompletableFuture<>();
            future.completeExceptionally(e);
            return future;
        }
    }

    /**
     * 文本向量混合检索
     * @param request
     * @return
     */
    @Override
    public CompletableFuture<SearchResponse> search(SearchRequest request) {
        try {
            compressRequest(request);

            TeaRequest teaRequest = REQUEST.copy()
                .setStyle(RequestStyle.RESTFUL)
                .setAction("Search")
                .setMethod(HttpMethod.POST)
                .setPathRegex("/vector-service/search")
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
     * 文本向量混合检索（pb协议）
     * @param request
     * @param compress 是否压缩请求体
     * @return
     */
    @Override
    public CompletableFuture<SearchResponse> search(VectorRequest.HybridSearchQuery request, boolean compress) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.set("Content-Type", "application/protobuf");

            TeaRequest teaRequest = REQUEST.copy()
                .setStyle(RequestStyle.RESTFUL)
                .setAction("Search")
                .setMethod(HttpMethod.POST)
                .setPathname("/vector-service/search")
                .setBodyType(BodyType.JSON)
                .setBodyIsForm(false)
                .setHeaders(headers)
                .setQuery(new HashMap<>())
                .setReqBodyType(BodyType.BINARY);
            teaRequest.setBody(request.toByteArray());

            compressPbRequest(teaRequest, compress);

            ClientExecutionParams params = new ClientExecutionParams().withRequest(teaRequest).withOutput(SearchResponse.create());
            return this.handler.execute(params);
        } catch (Exception e) {
            CompletableFuture<SearchResponse> future = new CompletableFuture<>();
            future.completeExceptionally(e);
            return future;
        }
    }

    /**
     * 向量引擎统计语法
     * @param request
     * @return
     */
    @Override
    public CompletableFuture<SearchResponse> aggregate(AggregateRequest request) {
        try {
            compressRequest(request);

            TeaRequest teaRequest = REQUEST.copy()
                .setStyle(RequestStyle.RESTFUL)
                .setAction("Aggregate")
                .setMethod(HttpMethod.POST)
                .setPathRegex("/vector-service/aggregate")
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
     * 向量引擎统计语法（pb协议）
     * @param request
     * @param compress
     * @return
     */
    @Override
    public CompletableFuture<SearchResponse> aggregate(VectorRequest.AggregateQuery request, boolean compress) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.set("Content-Type", "application/protobuf");

            TeaRequest teaRequest = REQUEST.copy()
                .setStyle(RequestStyle.RESTFUL)
                .setAction("Aggregate")
                .setMethod(HttpMethod.POST)
                .setPathname("/vector-service/aggregate")
                .setBodyType(BodyType.JSON)
                .setBodyIsForm(false)
                .setHeaders(headers)
                .setQuery(new HashMap<>())
                .setReqBodyType(BodyType.BINARY);
            teaRequest.setBody(request.toByteArray());

            compressPbRequest(teaRequest, compress);

            ClientExecutionParams params = new ClientExecutionParams().withRequest(teaRequest).withOutput(SearchResponse.create());
            return this.handler.execute(params);
        } catch (Exception e) {
            CompletableFuture<SearchResponse> future = new CompletableFuture<>();
            future.completeExceptionally(e);
            return future;
        }
    }

    /**
     * 批量查询
     * @param request
     * @return
     */
    @Override
    public CompletableFuture<SearchResponse> batchQuery(BatchRequest request) {
        try {
            compressRequest(request);

            TeaRequest teaRequest = REQUEST.copy()
                .setStyle(RequestStyle.RESTFUL)
                .setAction("BatchQuery")
                .setMethod(HttpMethod.POST)
                .setPathRegex("/vector-service/batch-query")
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
     * 批量查询（pb协议）
     * @param request
     * @param compress
     * @return
     */
    @Override
    public CompletableFuture<SearchResponse> batchQuery(VectorRequest.VectorBatchQuery request, boolean compress) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.set("Content-Type", "application/protobuf");

            TeaRequest teaRequest = REQUEST.copy()
                .setStyle(RequestStyle.RESTFUL)
                .setAction("BatchQuery")
                .setMethod(HttpMethod.POST)
                .setPathname("/vector-service/batch-query")
                .setBodyType(BodyType.JSON)
                .setBodyIsForm(false)
                .setHeaders(headers)
                .setQuery(new HashMap<>())
                .setReqBodyType(BodyType.BINARY);
            teaRequest.setBody(request.toByteArray());

            compressPbRequest(teaRequest, compress);

            ClientExecutionParams params = new ClientExecutionParams().withRequest(teaRequest).withOutput(SearchResponse.create());
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
            compressRequest(request);

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
     * 文档统计（pb协议）
     */
    @Override
    public CompletableFuture<SearchResponse> stats(VectorRequest.StatsQuery request, boolean compress) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.set("Content-Type", "application/protobuf");

            TeaRequest teaRequest = REQUEST.copy()
                .setStyle(RequestStyle.RESTFUL)
                .setAction("Stats")
                .setMethod(HttpMethod.POST)
                .setPathname("/vector-service/stats")
                .setBodyType(BodyType.JSON)
                .setBodyIsForm(false)
                .setHeaders(headers)
                .setQuery(new HashMap<>())
                .setReqBodyType(BodyType.BINARY);
            teaRequest.setBody(request.toByteArray());

            compressPbRequest(teaRequest, compress);

            ClientExecutionParams params = new ClientExecutionParams().withRequest(teaRequest).withOutput(SearchResponse.create());
            return this.handler.execute(params);
        } catch (Exception e) {
            CompletableFuture<SearchResponse> future = new CompletableFuture<>();
            future.completeExceptionally(e);
            return future;
        }
    }

    /**
     * 校验网络是否通畅 检查vpc &amp; 用户名密码配置是否正确
     * @return
     */
    @Override
    public CompletableFuture<SearchResponse> active() {
        try {
            TeaRequest teaRequest = REQUEST.copy()
                .setStyle(RequestStyle.RESTFUL)
                .setAction("Active")
                .setMethod(HttpMethod.GET)
                .setPathname("/network/active")
                .setQuery(new HashMap<>())
                .setHeaders(new HttpHeaders());
            ClientExecutionParams params = new ClientExecutionParams().withRequest(teaRequest).withOutput(SearchResponse.create());
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
            request.getHeaderParameters().put("X-Opensearch-Swift-PK-Field", keyField);
            TeaRequest teaRequest = REQUEST.copy()
                    .setStyle(RequestStyle.RESTFUL)
                    .setAction("PushDocuments")
                    .setMethod(HttpMethod.POST)
                    .setPathRegex("/update/" + dataSourceName + "/actions/bulk")
                    .setBodyType(BodyType.JSON)
                    .setBodyIsForm(false)
                    .setReqBodyType(BodyType.JSON)
                    .formModel(request);
            ClientExecutionParams params = new ClientExecutionParams().withInput(request).withRequest(teaRequest).withOutput(PushDocumentsResponse.create());
            return this.handler.execute(params);
        } catch (Exception e) {
            CompletableFuture<PushDocumentsResponse> future = new CompletableFuture<>();
            future.completeExceptionally(e);
            return future;
        }
    }

    /**
     * 对pb request进行压缩
     * @param teaRequest
     * @param compress
     * @throws IOException
     */
    public void compressPbRequest(TeaRequest teaRequest, boolean compress) throws IOException {
        if (compress) {
            byte[] bytes = deflateCompress((byte[]) teaRequest.body());
            teaRequest.headers().set("Content-Encoding", "deflate");
            teaRequest.setBody(bytes);
        }
    }

    /**
     * 对request进行压缩
     * @param request
     * @throws IOException
     */
    public void compressRequest(Request request) throws IOException {
        String contentEncoding = (String)request.getHeaderParameters().get("Content-Encoding");
        if ("deflate".equals(contentEncoding)) {
            Map<String, Object> requestParams = request.getBodyParameters();
            String str = com.aliyun.teautil.Common.toJSONString(requestParams);
            byte[] bytes = deflateCompress(str.getBytes());
            request.getBodyParameters().put("body", bytes);
        }
    }


    /**
     * 对请求体进行gzip压缩
     * @param bytes byte[]
     * @return
     * @throws IOException
     */
    public static byte[] deflateCompress(byte[] bytes) throws IOException {
        int len;
        Deflater defl = new Deflater();
        defl.setInput(bytes);
        defl.finish();
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        byte[] outputByte = new byte[1024];
        try {
            while (!defl.finished()) {
                // 压缩并将压缩后的内容输出到字节输出流bos中
                len = defl.deflate(outputByte);
                bos.write(outputByte, 0, len);
            }
            defl.end();
        } finally {
            bos.close();
        }
        return bos.toByteArray();
    }
}
