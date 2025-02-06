// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async;

import java.util.concurrent.CompletableFuture;

import com.aliyun.ha3engine.async.models.*;
import com.aliyun.ha3engine.async.models.protobuf.VectorRequest;

public interface AsyncClient {

    static DefaultAsyncClientBuilder builder() {
        return new DefaultAsyncClientBuilder();
    }

    static AsyncClient create() {
        return builder().build();
    }

    /**
     * 向量查询
     */
    CompletableFuture<SearchResponse> query(QueryRequest request);

    /**
     * 向量查询(pb协议)
     */
    CompletableFuture<SearchResponse> query(VectorRequest.VectorSearchQuery request, boolean compress);

    /**
     * 向量预测查询
     */
    CompletableFuture<SearchResponse> inferenceQuery(QueryRequest request);

    /**
     * 向量预测查询（pb协议）
     */
    CompletableFuture<SearchResponse> inferenceQuery(VectorRequest.VectorSearchQuery request, boolean compress);

    /**
     * 多namespace查询
     */
    CompletableFuture<SearchResponse> multiQuery(MultiQueryRequest request);

    /**
     * 多namespace查询（pb协议）
     */
    CompletableFuture<SearchResponse> multiQuery(VectorRequest.VectorSearchQueries request, boolean compress);

    /**
     * 查询数据
     */
    CompletableFuture<SearchResponse> fetch(FetchRequest request);

    /**
     * 查询数据（pb协议）
     */
    CompletableFuture<SearchResponse> fetch(VectorRequest.FetchQuery request, boolean compress);

    /**
     * 文本向量混合检索
     * @param request
     * @return
     */
    CompletableFuture<SearchResponse> search(SearchRequest request);

    /**
     * 文本向量混合检索（pb协议）
     * @param request
     * @param compress 是否压缩请求体
     * @return
     */
    CompletableFuture<SearchResponse> search(VectorRequest.HybridSearchQuery request, boolean compress);

    /**
     * 向量引擎统计语法
     * @param request
     * @return
     */
    CompletableFuture<SearchResponse> aggregate(AggregateRequest request);

    /**
     * 向量引擎统计语法（pb协议）
     * @param request
     * @param compress
     * @return
     */
    CompletableFuture<SearchResponse> aggregate(VectorRequest.AggregateQuery request, boolean compress);

    /**
     * 批量查询
     * @param request
     * @return
     */
    CompletableFuture<SearchResponse> batchQuery(BatchRequest request);

    /**
     * 批量查询（pb协议）
     * @param request
     * @param compress
     * @return
     */
    CompletableFuture<SearchResponse> batchQuery(VectorRequest.VectorBatchQuery request, boolean compress);

    /**
     * 文档统计
     */
    CompletableFuture<SearchResponse> stats(StatsRequest request);

    /**
     * 文档统计（pb协议）
     */
    CompletableFuture<SearchResponse> stats(VectorRequest.StatsQuery request, boolean compress);

    /**
     * 校验网络是否通畅 检查vpc &amp; 用户名密码配置是否正确
     * @return
     */
    CompletableFuture<SearchResponse> active();

    /**
     * 支持新增、更新、删除 等操作，以及对应批量操作
     */
    CompletableFuture<PushDocumentsResponse> pushDocuments(String dataSourceName, String keyField, PushDocumentsRequest request);
}
