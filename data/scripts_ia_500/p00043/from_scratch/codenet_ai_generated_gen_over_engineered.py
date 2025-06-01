from collections import Counter
from typing import List, Tuple


class PuzzleState:
    def __init__(self, digits: List[int]):
        self.digits = digits
        self.counter = Counter(digits)
        # Check if any digit appears more than 4 times (invalid state)
        if any(v > 4 for v in self.counter.values()):
            self.valid = False
        else:
            self.valid = True

    def add_digit(self, d: int) -> 'PuzzleState':
        new_digits = self.digits.copy()
        new_digits.append(d)
        return PuzzleState(new_digits)

    def can_use_digit(self, d: int) -> bool:
        return self.counter[d] < 4

    def frequencies(self) -> List[int]:
        # frequencies for digits 1 to 9 (index 0 = digit 1)
        return [self.counter[i] for i in range(1, 10)]


class AbstractGroup:
    def is_match(self, group: List[int]) -> bool:
        raise NotImplementedError


class PairGroup(AbstractGroup):
    def is_match(self, group: List[int]) -> bool:
        return len(group) == 2 and group[0] == group[1]


class TripleGroup(AbstractGroup):
    def is_match(self, group: List[int]) -> bool:
        if len(group) != 3:
            return False
        # Either all three same
        if group[0] == group[1] == group[2]:
            return True
        # Or three consecutive increasing
        s = sorted(group)
        # Consecutive means s[1] = s[0]+1 and s[2]=s[1]+1
        if s[0] + 1 == s[1] and s[1] + 1 == s[2]:
            return True
        return False


class PuzzleVerifier:
    def __init__(self):
        self.pair_group = PairGroup()
        self.triple_group = TripleGroup()

    def can_complete(self, digits: List[int]) -> bool:
        # digits length is 14, must split into 1 pair + 4 triples
        # We try all possible pairs indices
        digits_sorted = sorted(digits)
        freq = Counter(digits_sorted)

        # Check no digit more than 4 times
        if any(v > 4 for v in freq.values()):
            return False

        # We must find exactly one pair (two identical digits)
        pairs = [d for d, c in freq.items() if c >= 2]
        if not pairs:
            return False  # no possible pair to start

        # We'll attempt all possible pairs:
        for p in pairs:
            # Remove 2 of digit p to form pair:
            freq_copy = freq.copy()
            freq_copy[p] -= 2

            # From the remaining 12 digits, try to split into four triples each valid triple

            # Build a sorted list of remaining digits:
            rest = []
            for d in range(1, 10):
                rest.extend([d]*freq_copy[d])

            if self._can_split_into_triples(rest):
                return True
        return False

    def _can_split_into_triples(self, digits: List[int]) -> bool:
        # Recursive backtracking to split digits (len 12) into four triples each valid
        if not digits:
            return True
        if len(digits) % 3 != 0:
            return False

        counter = Counter(digits)

        # Try triple of three identical digits
        for d in counter:
            if counter[d] >= 3:
                new_counter = counter.copy()
                new_counter[d] -= 3
                if new_counter[d] == 0:
                    del new_counter[d]
                new_digits = list(new_counter.elements())
                if self._can_split_into_triples(new_digits):
                    return True

        # Try triple of three consecutive digits
        # Because digits sorted, get unique digits sorted
        unique_digits = sorted(counter.keys())
        for d in unique_digits:
            if d + 1 in counter and d + 2 in counter:
                # check if can take one instance each
                new_counter = counter.copy()
                new_counter[d] -= 1
                new_counter[d+1] -= 1
                new_counter[d+2] -= 1
                if new_counter[d] == 0:
                    del new_counter[d]
                if new_counter[d+1] == 0:
                    del new_counter[d+1]
                if new_counter[d+2] == 0:
                    del new_counter[d+2]
                new_digits = list(new_counter.elements())
                if self._can_split_into_triples(new_digits):
                    return True
        return False


class PuzzleSolver:
    def __init__(self):
        self.verifier = PuzzleVerifier()

    def solve_for_input(self, input_line: str) -> List[int]:
        digits_list = [int(c) for c in input_line.strip()]
        if len(digits_list) != 13:
            # invalid input length, rule out
            return [0]
        ps = PuzzleState(digits_list)
        if not ps.valid:
            return [0]

        valid_additions = []
        for d in range(1, 10):
            # can only add if current count < 4 (max 4 allowed)
            if ps.can_use_digit(d):
                ps_new = ps.add_digit(d)
                if self.verifier.can_complete(ps_new.digits):
                    valid_additions.append(d)
        if not valid_additions:
            return [0]
        return valid_additions


def main():
    import sys
    solver = PuzzleSolver()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        result = solver.solve_for_input(line)
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()