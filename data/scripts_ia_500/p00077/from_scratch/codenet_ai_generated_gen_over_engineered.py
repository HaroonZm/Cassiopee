from abc import ABC, abstractmethod
from typing import List, Iterator


class DecompressionError(Exception):
    pass


class Token(ABC):
    @abstractmethod
    def decompress(self) -> str:
        pass


class LiteralToken(Token):
    def __init__(self, char: str):
        self.char = char

    def decompress(self) -> str:
        return self.char


class CompressedToken(Token):
    def __init__(self, count: int, char: str):
        if not (1 <= count <= 9):
            raise DecompressionError(f"Invalid repeat count {count}, must be 1 to 9.")
        self.count = count
        self.char = char

    def decompress(self) -> str:
        return self.char * self.count


class Tokenizer:
    def __init__(self, line: str):
        self.line = line
        self.pos = 0
        self.length = len(line)

    def __iter__(self) -> Iterator[Token]:
        return self

    def __next__(self) -> Token:
        if self.pos >= self.length:
            raise StopIteration()
        current = self.line[self.pos]
        if current == '@':
            # format: @<digit><char>
            if self.pos + 2 > self.length:
                raise DecompressionError(f"Incomplete compressed token at position {self.pos} in '{self.line}'")
            count_char = self.line[self.pos + 1]
            repeated_char = self.line[self.pos + 2]
            if not count_char.isdigit():
                raise DecompressionError(f"Expected digit after '@' at {self.pos + 1}, got '{count_char}'")
            count = int(count_char)
            # Validate repeated_char is not '@' as per problem statement
            if repeated_char == '@':
                raise DecompressionError("Decompressed string cannot contain '@' characters")
            self.pos += 3
            return CompressedToken(count, repeated_char)
        else:
            # literal char
            if current == '@':
                # should not occur here because handled above
                raise DecompressionError("Unexpected '@' character")
            self.pos += 1
            return LiteralToken(current)


class Decompressor:
    def __init__(self):
        pass

    def decompress_line(self, compressed_line: str) -> str:
        tokenizer = Tokenizer(compressed_line)
        decompressed_chars: List[str] = []
        for token in tokenizer:
            decompressed_chars.append(token.decompress())
        decompressed = ''.join(decompressed_chars)
        # confirm '@' does not exist in decompressed string as per problem statement
        if '@' in decompressed:
            raise DecompressionError("Decompressed string contains '@' character")
        return decompressed


class InputHandler:
    def __init__(self):
        self.lines: List[str] = []

    def read_lines(self) -> None:
        import sys
        count = 0
        for line in sys.stdin:
            line = line.rstrip('\n')
            if not line:
                continue
            self.lines.append(line)
            count += 1
            if count > 50:
                break


class OutputHandler:
    def __init__(self):
        pass

    def output_lines(self, lines: List[str]) -> None:
        for line in lines:
            print(line)


class MainApp:
    def __init__(self):
        self.input_handler = InputHandler()
        self.decompressor = Decompressor()
        self.output_handler = OutputHandler()

    def run(self) -> None:
        self.input_handler.read_lines()
        decompressed_lines: List[str] = []
        for line in self.input_handler.lines:
            try:
                decompressed = self.decompressor.decompress_line(line)
            except DecompressionError as e:
                decompressed = f"ERROR: {e}"
            decompressed_lines.append(decompressed)
        self.output_handler.output_lines(decompressed_lines)


if __name__ == "__main__":
    app = MainApp()
    app.run()