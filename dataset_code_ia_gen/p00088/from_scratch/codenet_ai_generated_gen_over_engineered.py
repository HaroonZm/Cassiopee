class Encoder:
    def __init__(self):
        self.char_to_code = {
            ' ': '101',
            "'": '000000',
            ',': '000011',
            '-': '10010001',
            '.': '010001',
            '?': '000001',
            'A': '100101',
            'B': '10011010',
            'C': '0101',
            'D': '0001',
            'E': '110',
            'F': '01001',
            'G': '10011011',
            'H': '010000',
            'I': '0111',
            'J': '10011000',
            'K': '0110',
            'L': '00100',
            'M': '10011001',
            'N': '10011110',
            'O': '00101',
            'P': '111',
            'Q': '10011111',
            'R': '1000',
            'S': '00110',
            'T': '00111',
            'U': '10011100',
            'V': '10011101',
            'W': '000010',
            'X': '10010010',
            'Y': '10010011',
            'Z': '10010000',
        }

    def encode(self, text: str) -> str:
        encoded_bits = ''.join(self.char_to_code[ch] for ch in text)
        # パディングで5文字区切り
        remainder = len(encoded_bits) % 5
        if remainder != 0:
            encoded_bits += '0' * (5 - remainder)
        return encoded_bits

class Decoder:
    def __init__(self):
        self.code_to_char = {
            '00000': 'A',
            '00001': 'B',
            '00010': 'C',
            '00011': 'D',
            '00100': 'E',
            '00101': 'F',
            '00110': 'G',
            '00111': 'H',
            '01000': 'I',
            '01001': 'J',
            '01010': 'K',
            '01011': 'L',
            '01100': 'M',
            '01101': 'N',
            '01110': 'O',
            '01111': 'P',
            '10000': 'Q',
            '10001': 'R',
            '10010': 'S',
            '10011': 'T',
            '10100': 'U',
            '10101': 'V',
            '10110': 'W',
            '10111': 'X',
            '11000': 'Y',
            '11001': 'Z',
            '11010': ' ',
            '11011': '.',
            '11100': ',',
            '11101': '-',
            '11110': "'",
            '11111': '?',
        }

    def decode(self, bits: str) -> str:
        output_chars = []
        for i in range(0, len(bits), 5):
            chunk = bits[i:i+5]
            char = self.code_to_char.get(chunk, '')
            output_chars.append(char)
        return ''.join(output_chars)

class PeterPiperCipher:
    def __init__(self):
        self.encoder = Encoder()
        self.decoder = Decoder()

    def transform(self, text: str) -> str:
        # 1. Encode input text chars into variable length code bits.
        encoded_bits = self.encoder.encode(text)
        # 2. Split into 5-bit chunks is already represented by encoded_bits padded.
        # 3. Decode each 5-bit chunk using second table.
        return self.decoder.decode(encoded_bits)

def main():
    import sys
    cipher = PeterPiperCipher()
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        # Input line uppercase is guaranteed per problem statement, otherwise enforce:
        result = cipher.transform(line.upper())
        print(result)

if __name__ == "__main__":
    main()