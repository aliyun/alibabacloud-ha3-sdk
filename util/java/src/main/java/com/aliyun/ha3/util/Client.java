// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ha3.util;

import java.io.ByteArrayOutputStream;
import java.util.zip.Deflater;

public class Client {

    public static byte[] deflateCompress(byte[] src) throws Exception {
        int len;
        Deflater defl = new Deflater();
        defl.setInput(src);
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
