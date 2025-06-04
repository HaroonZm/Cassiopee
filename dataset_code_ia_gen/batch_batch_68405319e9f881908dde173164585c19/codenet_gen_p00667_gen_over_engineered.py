import sys
import threading
from abc import ABC, abstractmethod
from typing import List, Dict

MOD = 100000007

class InputReader:
    def __init__(self, stream):
        self.stream = stream

    def read_lines(self):
        for line in self.stream:
            line = line.strip()
            if line == '#':
                break
            yield line

class CharacterMapping(ABC):
    @abstractmethod
    def get_char_count(self, digit: str) -> int:
        pass

class KanaMapping(CharacterMapping):
    _mapping = {
        '1': 5,  # あいうえお
        '2': 5,  # かきくけこ
        '3': 5,  # さしすせそ
        '4': 5,  # たちつてと
        '5': 5,  # なにぬねの
        '6': 5,  # はひふへほ
        '7': 5,  # まみむめも
        '8': 3,  # やゆよ
        '9': 5,  # らりるれろ
        '0': 3,  # わをん
    }

    def get_char_count(self, digit: str) -> int:
        return self._mapping.get(digit, 0)

class PressGroup:
    def __init__(self, digit: str, length: int, char_mapping: CharacterMapping):
        self.digit = digit
        self.length = length
        self.char_mapping = char_mapping
        self.char_count = char_mapping.get_char_count(digit)

    def number_of_interpretations(self) -> int:
        # Number of ways to split 'length' presses into characters considering looping of char_count letters
        # This equals the number of ways to partition the presses modulo char_count to characters
        # Let n = length, c = char_count
        # number of ways = number of sequences of positive integers k_i where sum k_i = n and each character corresponds to k_i presses with k_i % c != 0 except for the last one which cycles.
        # Actually, we have to count ways to split length into multiples of presses that represent chars:
        # Each character corresponds to 1 to 'char_count' presses.
        # So ways to split length into sequence with parts between 1 and char_count, order matters.
        # This is a classic integer composition problem with bounded part size.

        # We'll use DP:
        # dp[i]: number of ways to decompose i presses.
        # dp[0] = 1 (empty)
        # for i in 1..length:
        #   dp[i] = sum_{k=1 to min(i, char_count)} dp[i-k]

        dp = [0] * (self.length + 1)
        dp[0] = 1
        c = self.char_count
        for i in range(1, self.length + 1):
            start = max(0, i - c)
            # sum dp[j] for j in [i-c, i-1]
            # Use sliding window for optimization

            # For efficiency on large length, do prefix sums
            # But since length can be large (up to 100000),
            # we must optimize carefully.

        # Implement sliding window sum using prefix sums
        prefix = [0] * (self.length + 1)
        prefix[0] = dp[0]
        for i in range(1, self.length + 1):
            left = i - c
            if left < 0:
                left = 0
            dp[i] = (prefix[i-1] - prefix[left-1] if left > 0 else prefix[i-1]) % MOD
            prefix[i] = (prefix[i-1] + dp[i]) % MOD
        return dp[self.length]

class InterpretationModel(ABC):
    @abstractmethod
    def parse_input(self, input_str: str) -> List[PressGroup]:
        pass

    @abstractmethod
    def count_interpretations(self, press_groups: List[PressGroup]) -> int:
        pass

class PressGroupInterpreter(InterpretationModel):
    def __init__(self, char_mapping: CharacterMapping):
        self.char_mapping = char_mapping

    def parse_input(self, input_str: str) -> List[PressGroup]:
        if not input_str:
            return []
        groups = []
        prev = input_str[0]
        count = 1
        for ch in input_str[1:]:
            if ch == prev:
                count += 1
            else:
                groups.append(PressGroup(prev, count, self.char_mapping))
                prev = ch
                count = 1
        groups.append(PressGroup(prev, count, self.char_mapping))
        return groups

    def count_interpretations(self, press_groups: List[PressGroup]) -> int:
        # Because interpretation splits only depend on single press groups (that's where forced commits can happen),
        # the total number of interpretations is product of number of ways each group can be interpreted.
        # convert under modulo
        result = 1
        for group in press_groups:
            ways = group.number_of_interpretations()
            result = (result * ways) % MOD
        return result

class Application:
    def __init__(self, reader: InputReader, interpreter: InterpretationModel):
        self.reader = reader
        self.interpreter = interpreter

    def run(self):
        outputs = []
        for line in self.reader.read_lines():
            groups = self.interpreter.parse_input(line)
            count = self.interpreter.count_interpretations(groups)
            outputs.append(count)
        return outputs

def main():
    sys.setrecursionlimit(10**7)
    input_reader = InputReader(sys.stdin)
    char_map = KanaMapping()
    interpreter = PressGroupInterpreter(char_map)
    app = Application(input_reader, interpreter)
    results = app.run()
    for r in results:
        print(r)

if __name__ == "__main__":
    threading.Thread(target=main).start()