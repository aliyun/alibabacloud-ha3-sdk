// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3engine.async;

import java.util.concurrent.CompletableFuture;

import com.aliyun.ha3engine.async.models.*;

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
     * 向量预测查询
     */
    CompletableFuture<SearchResponse> inferenceQuery(QueryRequest request);

    /**
     * 多namespace查询
     */
    CompletableFuture<SearchResponse> multiQuery(MultiQueryRequest request);

    /**
     * 查询数据
     */
    CompletableFuture<SearchResponse> fetch(FetchRequest request);

    /**
     * 文档统计
     */
    CompletableFuture<SearchResponse> stats(StatsRequest request);

    /**
     * 支持新增、更新、删除 等操作，以及对应批量操作
     */
    CompletableFuture<PushDocumentsResponse> pushDocuments(String dataSourceName, String keyField, PushDocumentsRequest request);

    /**
     * 用于内网环境的新增、更新、删除 等操作，以及对应批量操作
     */
    CompletableFuture<PushDocumentsResponse> pushDocumentsWithSwift(String dataSourceName, String keyField, String topic, String swift, PushDocumentsRequest request);

}
