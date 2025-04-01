// This file is auto-generated, don't edit it
/**
 * @remarks
 * Compress data by specified compress type, use isCompressorAvailable to check if the compress type is supported.
 *
 * @param src - the data to be compressed
 * @param compressType - the compress type
 * @returns the compressed data
 *
 * @throws error if the compress type is not supported or the compress failed
 */
import * as zlib from 'zlib';
import {promisify} from 'util';

// 将 zlib.deflate 转换为 Promise 基础异步函数
const deflateAsync = promisify(zlib.deflate);

export default class Client {
  static async deflateCompress(src: Buffer): Promise<Buffer> {
      try {
          // 调用异步压缩方法
          return await deflateAsync(src);
      } catch (error) {
          throw new Error(`Compression failed: ${error.message}`);
      }
  }
}