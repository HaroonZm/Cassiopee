from abc import ABC, abstractmethod
from decimal import Decimal, getcontext

# Augmenter la précision pour éviter toute erreur d'arrondi
getcontext().prec = 50

class BitStream:
    def __init__(self, hex_str: str):
        # Stocke le flux binaire sur 32 bits
        self.bits = ''.join(f'{int(c,16):04b}' for c in hex_str)
        if len(self.bits) != 32:
            raise ValueError("La chaîne d'entrée doit être exactement 32 bits")

    def get_bit(self, index: int) -> int:
        # index de 1 à 32 (b1 à b32)
        return int(self.bits[index - 1])

    def __str__(self):
        return self.bits

class FixedPointRepresentation(ABC):
    @abstractmethod
    def parse(self, bitstream: BitStream):
        pass

    @abstractmethod
    def to_decimal(self) -> Decimal:
        pass

class KongouType32(FixedPointRepresentation):
    def __init__(self):
        self.sign_bit = 0
        self.integer_part_bits = []
        self.fractional_part_bits = []

    def parse(self, bitstream: BitStream):
        # b1 = signe
        self.sign_bit = bitstream.get_bit(1)
        # b2 à b25 = partie entière (24 bits)
        self.integer_part_bits = [bitstream.get_bit(i) for i in range(2, 26)]
        # b26 à b32 = partie fractionnaire (7 bits)
        self.fractional_part_bits = [bitstream.get_bit(i) for i in range(26, 33)]

    def _integer_value(self) -> int:
        # Somme des bits pondérés selon 2^(position - 1) (avec position commençant à 1 pour b2)
        value = 0
        for power, bit in enumerate(reversed(self.integer_part_bits)):
            value += bit * (2 ** power)
        return value

    def _fractional_value(self) -> Decimal:
        value = Decimal(0)
        for power, bit in enumerate(self.fractional_part_bits, 1):
            if bit == 1:
                value += Decimal(0.5) ** power
        return value

    def to_decimal(self) -> Decimal:
        integer_value = self._integer_value()
        fractional_value = self._fractional_value()
        magnitude = Decimal(integer_value) + fractional_value
        # (-1)^sign
        sign = Decimal((-1) ** self.sign_bit)
        return sign * magnitude

class Formatter(ABC):
    @abstractmethod
    def format(self, value: Decimal) -> str:
        pass

class DecimalFormatter(Formatter):
    def format(self, value: Decimal) -> str:
        sign_str = '-' if value.is_signed() and value != 0 else ''
        abs_val = abs(value)
        integer_part = int(abs_val)
        fractional_part = abs_val - Decimal(integer_part)
        if fractional_part == 0:
            # Fraction nulle, afficher '0' dans la partie fractionnaire
            return f"{sign_str}{integer_part}.0"
        else:
            # Extract fractional digits en base 10 en évitant les zéros inutiles
            digits = []
            frac = fractional_part
            max_digits = 50  # limite arbitraire pour éviter boucle infinie
            for _ in range(max_digits):
                frac *= 10
                digit = int(frac)
                digits.append(str(digit))
                frac -= digit
                if frac == 0:
                    break
            # Enlever les zéros finaux inutiles
            while digits and digits[-1] == '0':
                digits.pop()
            frac_str = ''.join(digits)
            return f"{sign_str}{integer_part}.{frac_str}"

class ParserController:
    def __init__(self, rep: FixedPointRepresentation, formatter: Formatter):
        self.rep = rep
        self.formatter = formatter

    def process(self, hex_string: str) -> str:
        bitstream = BitStream(hex_string)
        self.rep.parse(bitstream)
        val = self.rep.to_decimal()
        return self.formatter.format(val)

def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    parser = ParserController(KongouType32(), DecimalFormatter())
    for _ in range(Q):
        hex_str = input().strip()
        print(parser.process(hex_str))

if __name__ == '__main__':
    main()