import zlib


def compress_string(input_string: str) -> str:
    return zlib.compress(input_string.encode("utf-8")).hex()


def decompress_string(compressed_data: str) -> str:
    return zlib.decompress(bytes.fromhex(compressed_data)).decode("utf-8")
