from abc import ABC, abstractmethod

class BitStream:
    def __init__(self, hex_string: str):
        # 16 hex chars representing 32 bits
        self.hex_string = hex_string
        self.value = int(hex_string, 16)

    def get_bit(self, pos: int) -> int:
        # pos: 1-based bit index from left (MSB)
        if not (1 <= pos <= 32):
            raise ValueError("Bit position must be between 1 and 32.")
        shift = 32 - pos
        return (self.value >> shift) & 1

    def __repr__(self):
        return f"BitStream({self.hex_string})"

class Component(ABC):
    @abstractmethod
    def extract_bits(self, bitstream: BitStream):
        pass

    @abstractmethod
    def value(self) -> int or float:
        pass

class SignBit(Component):
    def __init__(self):
        self.bit = 0

    def extract_bits(self, bitstream: BitStream):
        self.bit = bitstream.get_bit(1)

    def value(self) -> int:
        # (-1)^bit
        return (-1) ** self.bit

    def __repr__(self):
        return f"SignBit(bit={self.bit})"

class IntegerPart(Component):
    def __init__(self):
        self.bits = []

    def extract_bits(self, bitstream: BitStream):
        # Bits 8 to 31 (24 bits)
        self.bits = [bitstream.get_bit(i) for i in range(8, 32)]

    def value(self) -> int:
        total = 0
        # b8 is LSB of integer part or MSB? The problem states:
        # integer value = b8 + 2^1 * b9 + 2^2 * b10 ... 2^23 * b31
        # So b8 is 2^0 place
        for i, bit in enumerate(self.bits):
            total += bit << i  # bit * 2^i
        return total

    def __repr__(self):
        return f"IntegerPart(bits={self.bits})"

class FractionalPart(Component):
    def __init__(self):
        self.bits = []

    def extract_bits(self, bitstream: BitStream):
        # Bits 2 to 7 (6 bits for fraction)
        # But problem states 7 bits fractional part: bits 2 to 8 or 1 to 7 from right?
        # The problem states: rightmost 7 bits are fraction (b1 to b7),
        # so bits 32 to 26 are fractional bits?
        # Bits 1 to 7 (from left to right) are from right is b1 to b7. But bit 1 is sign bit by problem.
        # Re-check problem indexing:
        # b1 ... b32 are bits, bit1 is MSB (sign)
        # integer part = b8 to b31 (24 bits)
        # fractional part = b1 to b7 (7 bits)
        # So fractional bits are the lowest 7 bits, thus bits 25 to 31 or 26 to 32 from left?
        # Bits from left : 1 (MSB) .. 32 (LSB)
        # Fractional bits: b1 to b7 are **rightmost 7 bits** => bits 32 (b1) to 26 (b7).
        # So fractional bits are bits 26 to 32 from left, reversed order b1..b7 from right:
        # b1 = bit 32, b2=bit31,...,b7=bit26
        self.bits = [bitstream.get_bit(i) for i in range(26, 33)]

    def value(self) -> float:
        # Sum (0.5)^i * b_i for i=1..7, with b1 is rightmost bit (bit 32)
        total = 0.0
        for i, bit in enumerate(reversed(self.bits), start=1):
            total += bit * (0.5 ** i)
        return total

    def __repr__(self):
        return f"FractionalPart(bits={self.bits})"

class KongoFloat:
    def __init__(self, hex_string: str):
        self.bitstream = BitStream(hex_string)
        self.sign = SignBit()
        self.integer = IntegerPart()
        self.fraction = FractionalPart()

        # Extract all parts.
        self.sign.extract_bits(self.bitstream)
        self.integer.extract_bits(self.bitstream)
        self.fraction.extract_bits(self.bitstream)

    def to_decimal_str(self) -> str:
        # calculate float value exactly
        sign_val = self.sign.value()
        int_val = self.integer.value()
        frac_val = self.fraction.value()
        total_val = sign_val * (int_val + frac_val)

        # format output as requested
        # - omit trailing zeros in fraction
        # - output fraction as "0" if fractional part is zero
        # Use exact arithmetic for fractional part:
        # The fractional part can be converted to fraction for exactness:
        # Since fractional part is sum of (b_i * 1/2^i), denominator is power of two.
        # Use fractions to avoid float rounding errors.
        from fractions import Fraction
        frac_fraction = Fraction(0)
        for i, bit in enumerate(reversed(self.fraction.bits), start=1):
            if bit == 1:
                frac_fraction += Fraction(1, 2**i)

        int_fraction = Fraction(self.integer.value())
        val_fraction = int_fraction + frac_fraction

        if sign_val == -1:
            val_fraction = -val_fraction

        # Now convert fraction to decimal string without approximation:
        # convert numerator and denominator to decimal string
        numerator = val_fraction.numerator
        denominator = val_fraction.denominator

        # If denominator is 1, integer number
        if denominator == 1:
            result = str(numerator) + ".0"
            return result

        # else decimal with fraction part
        # convert fraction to decimal with exact representation (denominator is power of 2)
        # denominator is 2^{k}, k<=31

        # generate decimal digits of fractional part:
        # total_val = integer part + fractional part

        # separate integer and fractional parts:
        abs_frac = val_fraction if val_fraction >= 0 else -val_fraction
        integer_part = abs_frac.numerator // abs_frac.denominator
        fractional_part = abs_frac - integer_part

        # convert fractional_part to decimal digits until exact or trailing zeros
        # max 7 decimal places enough or until fractional part zero.
        # However, we must generate exactly to not lose information and avoid floating point errors.

        # actually, denominator divides 2^7=128
        # but integer part can be larger, so longest fraction decimal length can be estimated.

        # We'll generate decimal fraction digits as long as fractional_part !=0:

        digits = []
        frac = fractional_part
        max_digits = 20  # more than enough for denominator power of 2 up to 2^31

        for _ in range(max_digits):
            frac *= 10
            digit = frac.numerator // frac.denominator
            digits.append(str(digit))
            frac -= digit
            if frac == 0:
                break

        # strip trailing zeros
        while digits and digits[-1] == '0':
            digits.pop()

        if not digits:
            # fractional part zero
            frac_str = "0"
        else:
            frac_str = "".join(digits)

        sign_str = "-" if val_fraction < 0 else ""

        return f"{sign_str}{integer_part}.{frac_str}"

def main():
    import sys

    class InputReader:
        def __init__(self):
            self.Q = int(sys.stdin.readline().strip())
            self.bitstrings = [sys.stdin.readline().strip() for _ in range(self.Q)]

    input_data = InputReader()

    for bitstr in input_data.bitstrings:
        kf = KongoFloat(bitstr)
        print(kf.to_decimal_str())

if __name__ == "__main__":
    main()