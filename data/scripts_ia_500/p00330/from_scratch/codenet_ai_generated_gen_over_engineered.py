class Bits:
    __bits_per_word = 32

    def __init__(self, word_count: int):
        self._validate_word_count(word_count)
        self._word_count = word_count

    @classmethod
    def _validate_word_count(cls, word_count):
        if not isinstance(word_count, int):
            raise TypeError("Word count must be an integer")
        if not (0 <= word_count <= 100):
            raise ValueError("Word count must be between 0 and 100 inclusive")

    @property
    def total_bits(self) -> int:
        return self._word_count * self.__bits_per_word


class InputParser:
    @staticmethod
    def parse(input_str: str) -> int:
        try:
            return int(input_str.strip())
        except ValueError as e:
            raise ValueError("Invalid input: must be an integer") from e


class BitsConverter:
    def __init__(self, bits_representation: Bits):
        self._bits = bits_representation

    def to_bit_string(self) -> str:
        return str(self._bits.total_bits)


class Application:
    def __init__(self, parser, converter_cls, bits_cls):
        self._parser = parser
        self._converter_cls = converter_cls
        self._bits_cls = bits_cls

    def run(self, input_data: str) -> str:
        word_count = self._parser.parse(input_data)
        bits_obj = self._bits_cls(word_count)
        converter = self._converter_cls(bits_obj)
        return converter.to_bit_string()


if __name__ == "__main__":
    import sys
    app = Application(InputParser, BitsConverter, Bits)
    input_line = sys.stdin.readline()
    print(app.run(input_line))