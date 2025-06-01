class StampSequenceAnalyzer:
    class StampCounts:
        def __init__(self, circle=0, cross=0, circle_cross=0):
            self.circle = circle
            self.cross = cross
            self.circle_cross = circle_cross

        def total_stamps_used(self):
            return self.circle + self.cross + self.circle_cross

        def __repr__(self):
            return f"StampCounts(circle={self.circle}, cross={self.cross}, circle_cross={self.circle_cross})"

    class SequenceInfo:
        def __init__(self, sequence: str):
            self.sequence = sequence
            self.length = len(sequence)
            # Count single O's and X's to later deduce possible counts of single stamps and double stamps
            self.single_O = 0
            self.single_X = 0
            self.adjacent_OX = 0
            self.adjacent_XO = 0
            self._analyze_sequence()

        def _analyze_sequence(self):
            for i in range(self.length):
                if self.length == 1:
                    # Only one character, no adjacent pairs
                    continue
                if i < self.length - 1:
                    pair = self.sequence[i:i+2]
                    if pair == "OX":
                        self.adjacent_OX += 1
                    elif pair == "XO":
                        self.adjacent_XO += 1

            # Calculate single O and X that are not part of any possible double stamps
            # We will deduce these later, but keeping these as placeholders
            # Actually, final counts will be derived in analyzer main function

        def __repr__(self):
            return (f"SequenceInfo(length={self.length}, adjacent_OX={self.adjacent_OX}, "
                    f"adjacent_XO={self.adjacent_XO})")

    def __init__(self, sequence: str):
        self.sequence_info = self.SequenceInfo(sequence)
        self.sequence = sequence

    def maximum_circle_cross_stamps(self) -> int:
        # The key insight:
        # Let:
        #   a = count of 'OX' pairs we use as "circle-cross" stamp oriented as O then X
        #   b = count of 'XO' pairs we use as "circle-cross" stamp oriented as X then O
        # Then total circle-cross stamps = a + b
        # After using them, remaining characters must come from single circle or cross stamps
        # The number of 'O' in sequence = total_O
        # The number of 'X' in sequence = total_X
        # Each 'circle-cross' stamp covers one O and one X
        # So:
        #   total_O = (number of single circle stamps) + (a + b)
        #   total_X = (number of single cross stamps) + (a + b)
        # All stamps used exactly once, so total stamps used = N - (a + b) (joined pairs)
        #
        # We want to maximize (a + b), the number of circle-cross stamps used
        #
        # But (a + b) cannot exceed min(number of OX pairs, number of XO pairs), but actually it can be at most the total pairs of adjacent characters that can form circle-cross stamps.
        # Actually, the number of circle-cross stamps cannot exceed the number of adjacent pairs in sequence.
        #
        # Actually, circle-cross stamps correspond exactly to adjacent pairs that can be used either "OX" or "XO".
        # The maximum number is bounded by the minimum of total 'OX' adjacent pairs + 'XO' adjacent pairs.
        #
        # Since each circle-cross stamp consumes exactly two characters, one O and one X, in adjacent positions, and they can be used in either orientation.
        #
        # Since JOI uses each stamp exactly once, if we choose k circle-cross stamps, they correspond to k adjacent pairs in sequence
        #
        # The problem reduces to counting the maximum number of disjoint adjacent pairs in sequence that are either 'OX' or 'XO' we can use as circle-cross stamps without overlapping.

        # We implement a greedy matching on the sequence:
        # - Iterate from left to right:
        # - When we find 'OX' or 'XO' pair starting at index i, consume pair as one circle-cross stamp
        # - Skip next index (i+1) as it's consumed by this circle-cross stamp
        # - Continue until end of sequence
        # This will yield the maximum number of circle-cross stamps

        used = [False] * self.sequence_info.length
        max_circle_cross = 0
        i = 0
        while i < self.sequence_info.length - 1:
            if not used[i] and not used[i+1]:
                pair = self.sequence[i:i+2]
                if pair == "OX" or pair == "XO":
                    # use this pair as a circle-cross stamp
                    used[i] = True
                    used[i+1] = True
                    max_circle_cross += 1
                    i += 2
                    continue
            i += 1
        return max_circle_cross


def main():
    import sys

    class IOManager:
        def __init__(self):
            self.raw_input = sys.stdin.read().strip().split('\n')
            self.current_line = 0

        def input(self):
            line = self.raw_input[self.current_line]
            self.current_line += 1
            return line

    io = IOManager()

    N = int(io.input())
    S = io.input()

    analyzer = StampSequenceAnalyzer(S)
    result = analyzer.maximum_circle_cross_stamps()
    print(result)


if __name__ == "__main__":
    main()