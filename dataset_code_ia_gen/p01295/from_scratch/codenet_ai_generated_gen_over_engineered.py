class DigitSource:
    def digit_at(self, position: int) -> str:
        raise NotImplementedError()

    def digits(self, start: int, count: int) -> str:
        return ''.join(self.digit_at(pos) for pos in range(start, start + count))


class ChampernowneConstant(DigitSource):
    def __init__(self):
        # Precompute powers for digit lengths (1 to 10)
        self._digit_length_buckets = []
        # Each bucket: (start_position, digit_length, count_of_numbers)
        # Accumulated number of digits covered
        self._init_buckets()

    def _init_buckets(self):
        # Since N can be up to 10^9, we need buckets covering positions up to that
        # We'll prepare buckets with numbers of length 1 to 10 digits
        start_pos = 1
        for digit_len in range(1, 11):
            count_numbers = 9 * (10 ** (digit_len - 1))
            digits_in_bucket = count_numbers * digit_len
            self._digit_length_buckets.append({
                'start_pos': start_pos,
                'digit_len': digit_len,
                'count_numbers': count_numbers,
                'digits_in_bucket': digits_in_bucket
            })
            start_pos += digits_in_bucket

    def digit_at(self, position: int) -> str:
        bucket = self._find_bucket(position)
        within_bucket_pos = position - bucket['start_pos']
        number_index = within_bucket_pos // bucket['digit_len']
        digit_index = within_bucket_pos % bucket['digit_len']

        number = (10 ** (bucket['digit_len'] - 1)) + number_index
        return str(number)[digit_index]

    def _find_bucket(self, position: int) -> dict:
        # Binary search for bucket
        low, high = 0, len(self._digit_length_buckets) - 1
        while low <= high:
            mid = (low + high) // 2
            b = self._digit_length_buckets[mid]
            if b['start_pos'] <= position < b['start_pos'] + b['digits_in_bucket']:
                return b
            elif position < b['start_pos']:
                high = mid - 1
            else:
                low = mid + 1
        # If none found, fallback to last bucket (should not happen given constraints)
        return self._digit_length_buckets[-1]


class InputParser:
    def __init__(self):
        self._lines = []

    def feed_line(self, line: str):
        self._lines.append(line.strip())

    def parse(self):
        for raw_line in self._lines:
            if raw_line == '0 0':
                break
            parts = raw_line.split()
            if len(parts) != 2:
                continue
            N, K = parts
            yield int(N), int(K)


class OutputFormatter:
    @staticmethod
    def format_digits(digits: str) -> str:
        return digits


class ChampernowneSolver:
    def __init__(self):
        self._constant = ChampernowneConstant()
        self._parser = InputParser()
        self._formatter = OutputFormatter()

    def feed_input_line(self, line: str):
        self._parser.feed_line(line)

    def solve_all(self):
        results = []
        for N, K in self._parser.parse():
            digits = self._constant.digits(N, K)
            results.append(self._formatter.format_digits(digits))
        return results


def main():
    import sys
    solver = ChampernowneSolver()
    for line in sys.stdin:
        if line.strip() == '0 0':
            break
        solver.feed_input_line(line)
    # Feed the terminating line to parser for completeness, although parse() stops on '0 0'
    solver.feed_input_line('0 0')
    for output in solver.solve_all():
        print(output)


if __name__ == '__main__':
    main()