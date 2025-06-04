class PokeBellDecoder:
    class ConversionTable:
        def __init__(self):
            self._mapping = {
                '11': 'a', '12': 'b', '13': 'c', '14': 'd', '15': 'e',
                '21': 'f', '22': 'g', '23': 'h', '24': 'i', '25': 'j',
                '31': 'k', '32': 'l', '33': 'm', '34': 'n', '35': 'o',
                '41': 'p', '42': 'q', '43': 'r', '44': 's', '45': 't',
                '51': 'u', '52': 'v', '53': 'w', '54': 'x', '55': 'y',
                '56': 'z',
                '61': '.', '62': '?', '63': '!', '64': ' '
            }

        def decode_pair(self, pair):
            return self._mapping.get(pair, None)

    class MessageValidator:
        def __init__(self, conversion_table):
            self.table = conversion_table

        def is_valid(self, message):
            if len(message) % 2 != 0:
                return False
            for i in range(0, len(message), 2):
                if self.table.decode_pair(message[i:i+2]) is None:
                    return False
            return True

    class MessageDecoder:
        def __init__(self, conversion_table):
            self.table = conversion_table

        def decode(self, message):
            decoded_chars = []
            for i in range(0, len(message), 2):
                char = self.table.decode_pair(message[i:i+2])
                if char is None:
                    return None
                decoded_chars.append(char)
            return ''.join(decoded_chars)

    class MessageProcessor:
        def __init__(self):
            self.conversion_table = PokeBellDecoder.ConversionTable()
            self.validator = PokeBellDecoder.MessageValidator(self.conversion_table)
            self.decoder = PokeBellDecoder.MessageDecoder(self.conversion_table)

        def process_message(self, message):
            if not self.validator.is_valid(message):
                return "NA"
            result = self.decoder.decode(message)
            if result is None:
                return "NA"
            return result

    @staticmethod
    def run():
        import sys
        processor = PokeBellDecoder.MessageProcessor()
        input_lines = []
        count = 0
        for line in sys.stdin:
            line = line.rstrip('\n')
            if not line:
                continue
            input_lines.append(line)
            count += 1
            if count >= 50:
                break
        for message in input_lines:
            print(processor.process_message(message))

if __name__ == "__main__":
    PokeBellDecoder.run()