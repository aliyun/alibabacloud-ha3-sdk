# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import zlib


class Client:
    """
    Compress data by specified compress type, use isCompressorAvailable to check if the compress type is supported.
    @param src the data to be compressed
    @param compressType the compress type
    @return the compressed data
    @throws error if the compress type is not supported or the compress failed
    """
    def __init__(self):
        pass

    @staticmethod
    def deflate_compress(
        src: bytes,
    ) -> bytes:
        encoded_str = zlib.compress(src)
        return encoded_str

    @staticmethod
    async def deflate_compress_async(
        src: bytes,
    ) -> bytes:
        encoded_str = zlib.compress(src)
        return encoded_str
