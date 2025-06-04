class DigitSequence:
    def __init__(self, digits):
        self.digits = digits
        self.length = len(digits)
        self.next_pos = self._precompute_next_positions()

    def _precompute_next_positions(self):
        # For each index and each digit, store the next occurrence index of that digit
        next_pos = [{} for _ in range(self.length + 1)]
        last_occurrence = {str(d): -1 for d in range(10)}
        for i in range(self.length - 1, -1, -1):
            last_occurrence[self.digits[i]] = i
            for d in last_occurrence:
                next_pos[i][d] = last_occurrence[d]
        # For position length (beyond last digit), no further occurrences
        next_pos[self.length] = {str(d): -1 for d in range(10)}
        return next_pos

    def contains_as_subsequence(self, num_str):
        # Check if num_str appears as subsequence in self.digits using precomputed next positions
        pos = 0
        for ch in num_str:
            pos = self.next_pos[pos].get(ch, -1)
            if pos == -1:
                return False
            pos += 1
        return True


class IntegerSearcher:
    def __init__(self, digit_sequence):
        self.digit_sequence = digit_sequence

    def find_min_absent_integer(self):
        # We search from 0 upwards for the smallest integer not appearing as subsequence
        # Given n<=1000 digits, the missing integer won't be absurdly large
        candidate = 0
        while True:
            if not self.digit_sequence.contains_as_subsequence(str(candidate)):
                return candidate
            candidate += 1


class ProblemSolver:
    def __init__(self):
        self.input_reader = InputReader()
        self.digit_sequence = None
        self.searcher = None

    def solve(self):
        self.digit_sequence = DigitSequence(self.input_reader.read_digits())
        self.searcher = IntegerSearcher(self.digit_sequence)
        result = self.searcher.find_min_absent_integer()
        print(result)


class InputReader:
    def __init__(self):
        self.n = 0
        self.digits = []

    def read_digits(self):
        import sys
        lines = sys.stdin.read().strip().split()
        self.n = int(lines[0])
        digits = lines[1:]
        if len(digits) != self.n:
            raise ValueError("Number of digits does not match n")
        return digits


if __name__ == "__main__":
    solver = ProblemSolver()
    solver.solve()