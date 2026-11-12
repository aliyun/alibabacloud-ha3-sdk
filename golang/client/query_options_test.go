package client

import (
	"bytes"
	"compress/zlib"
	"encoding/json"
	"io"
	"net/http"
	"net/http/httptest"
	"reflect"
	"testing"

	util "github.com/alibabacloud-go/tea-utils/v2/service"
	"github.com/alibabacloud-go/tea/tea"
)

func TestQueryOptionsOnWire(t *testing.T) {
	const knn = `{"tableName":"items","vector":[1.5],"topK":0,"includeVector":false,"sparseData":{"indices":[9007199254740993],"values":[2]}}`
	for _, test := range []struct {
		name       string
		path       string
		onlyIDs    *bool
		compressed bool
		wantHeader string
		wantJSON   string
	}{
		{"query omitted", "query", nil, false, "", knn},
		{"query false", "query", tea.Bool(false), false, "", knn[:len(knn)-1] + `,"onlyIds":false}`},
		{"query true", "query", tea.Bool(true), false, "", knn[:len(knn)-1] + `,"onlyIds":true}`},
		{"inference with deflate", "inference-query", tea.Bool(true), true, "inference-route", knn},
		{"search with nested options", "search", tea.Bool(true), false, "search-route", `{"tableName":"items","knn":` + knn + `}`},
		{"multi-query with nested options", "multi-query", tea.Bool(true), false, "", `{"tableName":"items","queries":[` + knn + `]}`},
		{"batch-query with nested options", "batch-query", tea.Bool(true), false, "", `{"queries":[` + knn + `]}`},
	} {
		t.Run(test.name, func(t *testing.T) {
			query := &QueryRequest{
				TableName:     tea.String("items"),
				Vector:        []*float32{tea.Float32(1.5)},
				TopK:          tea.Int(0),
				IncludeVector: tea.Bool(false),
				SparseData: &SparseData{
					Indices: []*int64{tea.Int64(9007199254740993)},
					Values:  []*float32{tea.Float32(2)},
				},
				OnlyIds: test.onlyIDs,
				Headers: map[string]*string{
					"X-Source-Id":     tea.String("inference-route"),
					"X-Custom-Header": tea.String("inference-custom"),
				},
			}
			var request interface{} = query
			var invoke func(*Client) (*SearchResponse, error)
			switch test.path {
			case "query":
				invoke = func(sdk *Client) (*SearchResponse, error) { return sdk.Query(query) }
			case "inference-query":
				invoke = func(sdk *Client) (*SearchResponse, error) { return sdk.InferenceQuery(query) }
			case "search":
				search := &SearchRequest{
					TableName: tea.String("items"),
					Knn:       query,
					Headers: map[string]*string{
						"X-Source-Id":     tea.String("search-route"),
						"X-Custom-Header": tea.String("search-custom"),
					},
				}
				request = search
				invoke = func(sdk *Client) (*SearchResponse, error) { return sdk.Search(search) }
			case "multi-query":
				multi := &MultiQueryRequest{TableName: tea.String("items"), Queries: []*QueryRequest{query}}
				request = multi
				invoke = func(sdk *Client) (*SearchResponse, error) { return sdk.MultiQuery(multi) }
			case "batch-query":
				batch := &BatchRequest{Queries: []*QueryRequest{query}}
				request = batch
				invoke = func(sdk *Client) (*SearchResponse, error) { return sdk.BatchQuery(batch) }
			}
			before, err := json.Marshal(request)
			if err != nil {
				t.Fatal(err)
			}
			wire := captureQueryOptionsRequest(t, invoke, test.compressed)
			after, err := json.Marshal(request)
			if err != nil {
				t.Fatal(err)
			}
			if !bytes.Equal(before, after) {
				t.Errorf("request changed: before %s, after %s", before, after)
			}
			if want := "/vector-service/" + test.path; wire.method != http.MethodPost || wire.path != want || wire.query != "" {
				t.Errorf("got %s %s?%s, want POST %s without query parameters", wire.method, wire.path, wire.query, want)
			}
			if test.wantHeader == "" {
				if len(wire.header.Values("X-Source-Id")) != 0 || len(wire.header.Values("X-Custom-Header")) != 0 {
					t.Errorf("unexpected request headers: %v", wire.header)
				}
			} else {
				if got := wire.header.Get("X-Source-Id"); got != test.wantHeader {
					t.Errorf("X-Source-Id = %q, want %q", got, test.wantHeader)
				}
				wantCustom := "inference-custom"
				if test.path == "search" {
					wantCustom = "search-custom"
				}
				if got := wire.header.Get("X-Custom-Header"); got != wantCustom {
					t.Errorf("X-Custom-Header = %q, want %q", got, wantCustom)
				}
			}
			body := wire.body
			if test.compressed {
				if got := wire.header.Get("Content-Encoding"); got != "deflate" {
					t.Fatalf("Content-Encoding = %q, want deflate", got)
				}
				reader, err := zlib.NewReader(bytes.NewReader(body))
				if err != nil {
					t.Fatal(err)
				}
				defer reader.Close()
				body, err = io.ReadAll(reader)
				if err != nil {
					t.Fatal(err)
				}
			}
			if got, want := decodeQueryOptionsJSON(t, body), decodeQueryOptionsJSON(t, []byte(test.wantJSON)); !reflect.DeepEqual(got, want) {
				t.Errorf("JSON body = %s\nwant %s", body, test.wantJSON)
			}
		})
	}
}

type queryOptionsWireRequest struct {
	method string
	path   string
	query  string
	header http.Header
	body   []byte
}

func captureQueryOptionsRequest(t *testing.T, invoke func(*Client) (*SearchResponse, error), compressed bool) queryOptionsWireRequest {
	t.Helper()
	received := make(chan queryOptionsWireRequest, 1)
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		body, err := io.ReadAll(r.Body)
		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}
		select {
		case received <- queryOptionsWireRequest{r.Method, r.URL.Path, r.URL.RawQuery, r.Header.Clone(), body}:
		default:
		}
		w.Header().Set("Content-Type", "application/json")
		_, _ = w.Write([]byte(`{}`))
	}))
	defer server.Close()
	config := (&Config{}).SetEndpoint(server.URL).SetProtocol("http")
	if compressed {
		config.SetRuntimeOptions(&util.RuntimeOptions{ExtendsParameters: &util.ExtendsParameters{
			Headers: map[string]*string{"Content-Encoding": tea.String("deflate")},
		}})
	}
	sdk, err := NewClient(config)
	if err != nil {
		t.Fatal(err)
	}
	if _, err := invoke(sdk); err != nil {
		t.Fatal(err)
	}
	select {
	case wire := <-received:
		return wire
	default:
		t.Fatal("server did not receive an HTTP request")
		return queryOptionsWireRequest{}
	}
}

func decodeQueryOptionsJSON(t *testing.T, body []byte) interface{} {
	t.Helper()
	decoder := json.NewDecoder(bytes.NewReader(body))
	decoder.UseNumber()
	var result interface{}
	if err := decoder.Decode(&result); err != nil {
		t.Fatalf("decode JSON body %q: %v", body, err)
	}
	return result
}
