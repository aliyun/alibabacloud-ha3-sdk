import json
import unittest
from unittest.mock import patch

from alibabacloud_ha3engine_vector.client import Client
from alibabacloud_ha3engine_vector.models import (
    BatchRequest,
    Config,
    MultiQueryRequest,
    QueryRequest,
    SearchRequest,
)


class NsExpressionTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(Config(endpoint="localhost", instance_id="test"))
        self.expression = "cate_id=1&color_id=2|color_id=3"

    def request_body(self, call, request):
        with patch.object(self.client, "_request", return_value={"body": "{}"}) as send:
            call(request)
        return json.loads(send.call_args[0][4])

    def test_query_and_inference_send_expression_unchanged(self):
        query = QueryRequest(table_name="docs", ns_expression=self.expression)
        for call in (self.client.query, self.client.inference_query):
            with self.subTest(method=call.__name__):
                self.assertEqual(self.request_body(call, query)["nsExpression"], self.expression)

    def test_nested_requests_put_expression_on_each_vector_query(self):
        query = QueryRequest(table_name="docs", ns_expression=self.expression)
        legacy = QueryRequest("docs", [1.0], "legacy", 3)
        search = self.request_body(self.client.search, SearchRequest(knn=query))
        self.assertEqual(search["knn"]["nsExpression"], self.expression)
        self.assertNotIn("nsExpression", search)

        cases = (
            (self.client.multi_query, MultiQueryRequest(table_name="docs", queries=[query, legacy])),
            (self.client.batch_query, BatchRequest(queries=[query, legacy])),
        )
        for call, request in cases:
            with self.subTest(method=call.__name__):
                body = self.request_body(call, request)
                self.assertNotIn("nsExpression", body)
                self.assertEqual(body["queries"][0]["nsExpression"], self.expression)
                self.assertEqual(body["queries"][1]["namespace"], "legacy")
                self.assertEqual(body["queries"][1]["topK"], 3)
                self.assertNotIn("nsExpression", body["queries"][1])
