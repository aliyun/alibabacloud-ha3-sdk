package com.aliyun.ha3engine.async;

import java.net.InetSocketAddress;
import java.time.Duration;
import java.util.*;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

import javax.net.ssl.KeyManager;
import javax.net.ssl.X509TrustManager;

import com.aliyun.core.http.HttpClient;
import com.aliyun.core.http.ProxyOptions;
import com.aliyun.core.utils.ParseUtil;
import com.aliyun.ha3engine.async.models.*;
import com.aliyun.httpcomponent.httpclient.ApacheAsyncHttpClientBuilder;
import com.aliyun.sdk.ha3engine.async.core.AsyncConfigInfoProvider;
import com.aliyun.teautil.Common;

import darabonba.core.client.ClientOverrideConfiguration;

/**
 * @Author maguoxin
 * @Date 2023-12-21 16:37
 **/
public class Test {

//    public static void main(String[] args) throws ExecutionException, InterruptedException {
//        AsyncConfigInfoProvider provider = AsyncConfigInfoProvider.create("zxtest", "123456");
//
//        // Configure the Client
//        AsyncClient client = AsyncClient.builder()
//                .credentialsProvider(provider)
//                .overrideConfiguration(
//                        ClientOverrideConfiguration.create()
//                                .setEndpointOverride("ha-cn-u7c3j512j02.public.ha.aliyuncs.com").setProtocol("http")
//                ).build();
//
//        //  文档推送外层结构 , 可添加对文档操作的结构体. 结构内支持 一个或多个文档操作内容.
//        ArrayList<Map<String, ?>> documentArrayList = new ArrayList<>();
//        // 更新文档内容信息, keyValue 成对匹配.
//        // field_pk 字段需与 pkField 字段配置一致.
//        for (int i = 9998; i <= 9999; i++) {
//            //  添加文档
//            Map<String, Object> add2Document = new HashMap<>();
//            Map<String, Object> add2DocumentFields = new HashMap<>();
//
//            add2DocumentFields.put("id", i);
//            add2DocumentFields.put("name", "admin");
//            List<Float> doubles = Arrays.asList(0.1912558674812317F,0.6275089979171753F);
//
//            add2DocumentFields.put("vector", doubles);
//            add2DocumentFields.put("sparse_indices", 20);
//            add2DocumentFields.put("sparse_values", 20);
//            add2DocumentFields.put("namespace", "test");
//
//            // 将文档内容添如 add2Document 结构.
//            add2Document.put("fields", add2DocumentFields);
//            //  新增对应的文档命令: add
//            add2Document.put("cmd", "add");
//            documentArrayList.add(add2Document);
//        }
//        PushDocumentsRequest request = PushDocumentsRequest.builder().body(documentArrayList).build();
//
//        //数据推送
//        CompletableFuture<PushDocumentsResponse> responseCompletableFuture = client.pushDocuments("ha-cn-u7c3j512j02_query_test", "id", request);
//        System.out.println("pushDocumentsResponseModel:\n" + responseCompletableFuture.get().getBody());
//    }

    public static void main(String[] args) throws ExecutionException, InterruptedException {
        AsyncConfigInfoProvider provider = AsyncConfigInfoProvider.create("zxtest", "123456");

        // Configure the Client
        AsyncClient client = AsyncClient.builder()
                .credentialsProvider(provider)
                .overrideConfiguration(
                        ClientOverrideConfiguration.create()
                                .setEndpointOverride("ha-cn-u7c3j512j02.public.ha.aliyuncs.com").setProtocol("http")
                ).build();

//        QueryRequest queryRequest = QueryRequest.builder().indexName("content_vec").build();
//        MultiQueryRequest multiQueryRequest = MultiQueryRequest.builder().tableName("hybrid").queries(Arrays.asList(queryRequest)).build();
//        CompletableFuture<SearchResponse> searchResponseCompletableFuture = client.multiQuery(multiQueryRequest);
//        System.out.println(searchResponseCompletableFuture.get().getBody());

        QueryRequest queryRequest = QueryRequest.builder().tableName("query_test").indexName("vector").build();
        CompletableFuture<SearchResponse> searchResponseCompletableFuture = client.query(queryRequest);
        System.out.println(searchResponseCompletableFuture.get().getBody());

    }
}
