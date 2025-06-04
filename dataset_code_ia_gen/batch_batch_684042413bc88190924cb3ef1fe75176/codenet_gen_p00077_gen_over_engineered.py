from abc import ABC, abstractmethod
from typing import List, Iterator


class DecompressionError(Exception):
    pass


class Token(ABC):
    @abstractmethod
    def expand(self) -> str:
        pass


class LiteralToken(Token):
    def __init__(self, char: str):
        self.char = char

    def expand(self) -> str:
        return self.char


class CompressedToken(Token):
    def __init__(self, count: int, char: str):
        self.count = count
        self.char = char

    def expand(self) -> str:
        return self.char * self.count


class Tokenizer:
    def __init__(self, data: str):
        self.data = data
        self.pos = 0
        self.length = len(data)

    def __iter__(self) -> Iterator[Token]:
        while self.pos < self.length:
            ch = self.data[self.pos]
            if ch == '@':
                yield self._consume_compressed()
            else:
                yield self._consume_literal()
        return

    def _consume_literal(self) -> Token:
        ch = self.data[self.pos]
        if ch == '@':
            raise DecompressionError("Unexpected @ in literal consumption")
        self.pos += 1
        return LiteralToken(ch)

    def _consume_compressed(self) -> Token:
        # Current pos points to '@'
        self.pos += 1  # consume '@'
        count_str = ''
        while self.pos < self.length and self.data[self.pos].isdigit():
            count_str += self.data[self.pos]
            self.pos += 1
        if count_str == '':
            raise DecompressionError("Missing count number after @")
        if self.pos >= self.length:
            raise DecompressionError("Missing character after count")
        count = int(count_str)
        ch = self.data[self.pos]
        if ch == '@':
            raise DecompressionError("Decompressed string cannot contain '@'")
        self.pos += 1
        return CompressedToken(count, ch)


class Decompressor:
    def __init__(self, compressed: str):
        self.compressed = compressed

    def decompress(self) -> str:
        tokenizer = Tokenizer(self.compressed)
        tokens = list(tokenizer)
        return ''.join(token.expand() for token in tokens)


class Processor:
    def __init__(self, lines: List[str]):
        self.lines = lines

    def process(self) -> List[str]:
        output = []
        for line in self.lines:
            decompressor = Decompressor(line)
            decompressed = decompressor.decompress()
            output.append(decompressed)
        return output


def main():
    import sys
    lines = [line.rstrip('\n') for line in sys.stdin if line.strip()]
    processor = Processor(lines)
    results = processor.process()
    for result in results:
        print(result)


if __name__ == "__main__":
    main()