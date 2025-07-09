// This file is auto-generated, don't edit it. Thanks.
/**
 * Compress data by specified compress type, use isCompressorAvailable to check if the compress type is supported.
 * @param src the data to be compressed
 * @param compressType the compress type
 * @return the compressed data
 * @throws error if the compress type is not supported or the compress failed
 */
package client

import (
	"bytes"
	"compress/zlib"
)


func DeflateCompress (src []byte) (_result []byte, _err error) {
	var buf bytes.Buffer
	writer := zlib.NewWriter(&buf)
	_, err := writer.Write(src)
	if err != nil {
		return nil, err
	}
	err = writer.Close()
	if err != nil {
		return nil, err
	}

	return buf.Bytes(), nil
}

