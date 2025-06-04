class BitwiseOperation:
    """A bitwise operation abstraction to facilitate XOR computations."""
    @staticmethod
    def xor(a: int, b: int) -> int:
        return a ^ b


class ModularArithmetic:
    """Handles addition modulo 2^32."""
    MODULO = 2 ** 32

    @classmethod
    def add(cls, a: int, b: int) -> int:
        return (a + b) % cls.MODULO


class Chunk:
    """Represents a 32-bit integer chunk with hexadecimal parsing and output."""
    def __init__(self, value: int):
        self.value = value & 0xFFFFFFFF  # ensure 32-bit

    @classmethod
    def from_hex(cls, hex_str: str) -> 'Chunk':
        return cls(int(hex_str, 16))

    def xor(self, other: 'Chunk') -> 'Chunk':
        return Chunk(BitwiseOperation.xor(self.value, other.value))

    def __add__(self, other: 'Chunk') -> 'Chunk':
        return Chunk(ModularArithmetic.add(self.value, other.value))

    def lowest_bit(self) -> int:
        return self.value & 1

    def to_hex(self) -> str:
        # no leading zeros
        return hex(self.value)[2:]


class Dataset:
    """Encapsulates a dataset containing exactly nine chunks."""
    def __init__(self, chunks: list[Chunk]):
        if len(chunks) != 9:
            raise ValueError("A dataset must contain exactly 9 chunks")
        self.chunks = chunks

    def compute_checksum(self) -> Chunk:
        # sum first 8 chunks modulo 2^32
        total = Chunk(0)
        for i in range(8):
            total += self.chunks[i]
        return total

    def encoded_checksum(self, key: Chunk) -> Chunk:
        return self.compute_checksum().xor(key)

    def encoded_ninth_chunk(self, key: Chunk) -> Chunk:
        return self.chunks[8].xor(key)


class KeyFinder:
    """Responsible for discovering the 32-bit key used for encoding."""
    def __init__(self, dataset: Dataset):
        self.dataset = dataset

    def find_lowest_bit_key(self) -> int:
        # Following logic in problem: determine the lowest bit k0 of key
        encoded_checksum_lowest = (self.dataset.compute_checksum().value) & 1
        encoded_ninth_lowest = (self.dataset.chunks[8].value) & 1
        if encoded_checksum_lowest == encoded_ninth_lowest:
            return 0
        else:
            return 1

    def find_full_key(self) -> Chunk:
        # The key is found by:
        # K = (sum of first 8 chunks) XOR ninth chunk
        sum_first_8 = self.dataset.compute_checksum()
        ninth = self.dataset.chunks[8]
        key = sum_first_8.xor(ninth)
        return key


class InputParser:
    """Parses input lines and produces dataset objects."""
    def __init__(self, lines: list[str]):
        self.lines = lines
        self.datasets = []

    def parse(self):
        s = int(self.lines[0].strip())
        hex_values = []
        idx = 1
        while len(hex_values) < s * 9:
            line = self.lines[idx].strip()
            if not line:
                idx += 1
                continue
            parts = line.split()
            hex_values.extend(parts)
            idx += 1
        # chunk hex_values into datasets of 9 each
        for i in range(s):
            chunk_hexes = hex_values[i*9:(i+1)*9]
            chunks = [Chunk.from_hex(h) for h in chunk_hexes]
            self.datasets.append(Dataset(chunks))


class LeakyCryptanalysis:
    """Driver class coordinating the cryptanalysis process."""
    def __init__(self, datasets: list[Dataset]):
        self.datasets = datasets

    def analyze(self) -> list[str]:
        keys_hex = []
        for dataset in self.datasets:
            finder = KeyFinder(dataset)
            key = finder.find_full_key()
            keys_hex.append(key.to_hex())
        return keys_hex


def main():
    import sys
    parser = InputParser(sys.stdin.readlines())
    parser.parse()
    cryptanalysis = LeakyCryptanalysis(parser.datasets)
    keys = cryptanalysis.analyze()
    for key in keys:
        print(key)


if __name__=="__main__":
    main()