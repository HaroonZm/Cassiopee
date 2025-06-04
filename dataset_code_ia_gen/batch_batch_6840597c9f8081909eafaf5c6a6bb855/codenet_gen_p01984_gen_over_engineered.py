class ShortNumberGenerator:
    def __init__(self):
        # Cache to store generated short numbers by length for optimization and possible future extensions
        self.cache = {}

    class ShortNumber:
        def __init__(self, digits):
            self.digits = digits

        def __lt__(self, other):
            if len(self.digits) == len(other.digits):
                return self.digits < other.digits
            return len(self.digits) < len(other.digits)

        def to_int(self):
            return int(''.join(map(str, self.digits)))

        def __repr__(self):
            return ''.join(map(str, self.digits))

    @staticmethod
    def digit_pairs():
        # Generate all distinct pairs of digits (a,b), 0 <= a < b <= 9
        return [(a, b) for a in range(10) for b in range(a + 1, 10)]

    def generate_by_length_and_pair(self, length, a, b):
        """
        Generate all short numbers of given length using exactly digits {a,b}
        with no leading zero.
        Return sorted list of ShortNumber objects.
        """

        if length == 1:
            # For length 1, possible numbers are a or b if nonzero
            candidates = []
            if a != 0:
                candidates.append(self.ShortNumber([a]))
            if b != 0:
                candidates.append(self.ShortNumber([b]))
            return candidates

        # We'll generate all sequences of length with digits a,b, no leading zero (so first digit !=0)
        # Using bitmasks or product is not tractable for huge length.
        # So we implement an iterator with a binary representation interpretation.

        # Since the digits are two, we can consider each number as a bitmask length digits,
        # digit = a if bit=0, digit=b if bit=1, but first digit must not be zero

        # For first digit:
        # If a != 0: first digit can be a or b
        # Else a=0, we must have first digit=b (b!=0 since a<b)
        #
        # Total combinations: 2^(length-1) for each pair (except care for zeros)

        from itertools import product

        digits = [a, b]

        results = []
        # Handle which digit can be first digit to not be zero
        first_digit_candidates = []
        if a != 0:
            first_digit_candidates.append(a)
        if b != 0:
            first_digit_candidates.append(b)

        # For large length, this explodes so we generate generator instead.
        # But problem constraints require N up to 10^18/indexed overall numbers across lengths.

        # We will do a binary-tree inspired iterator:
        # Generate all combinations of length-1 remaining digits from digits,
        # then prepend each first_digit in first_digit_candidates.

        # Use yield to reduce memory if needed
        def gen():
            for first_digit in first_digit_candidates:
                for pattern in product(digits, repeat=length - 1):
                    yield self.ShortNumber([first_digit] + list(pattern))

        return gen()

    def count_by_length_and_pair(self, length, a, b):
        # Count how many short numbers of length with digits {a,b} exist
        # no leading zero
        # possible first digits:
        first_digit_count = 0
        if a != 0:
            first_digit_count += 1
        if b != 0:
            first_digit_count += 1
        if first_digit_count == 0:
            return 0
        # The other length-1 positions can be either digit:
        return first_digit_count * (2 ** (length - 1))

    def count_up_to_length(self, length):
        # Count total number of short numbers up to given length inclusive (all digit pairs)
        count = 0
        for l in range(1, length + 1):
            for a, b in self.digit_pairs():
                count += self.count_by_length_and_pair(l, a, b)
        return count

    def nth_short_number(self, n):
        # Using the strategy:
        # iterate over number length from 1 upwards
        # for each length, all pairs (a,b), calculate how many short numbers
        # if n > total count for length, subtract and continue
        # else generate numbers of that length and pair, and find nth

        # To optimize, precompute counts by length and digit pairs
        # We'll iterate length 1..max (max 60 to be safe because digits can reach large lengths)

        # For very large n and length, we must be careful to not overkill memory.

        # max length possibly needed:
        max_len = 60
        remaining = n

        for length in range(1, max_len + 1):
            for a, b in self.digit_pairs():
                c = self.count_by_length_and_pair(length, a, b)
                if remaining > c:
                    remaining -= c
                else:
                    # Found correct length and pair
                    # Generate the remaining-th number
                    # The order is ascending by integer value
                    # So numbers sorted lex order of digits (equivalent)

                    # Generate all numbers length-long with digits {a,b} no leading zero sorted ascending

                    # If a < b, then binary mask maps 0->a, 1->b, so numbers in ascending order of bits represent ascending numbers

                    # Create mapping bit -> digit:
                    digit_map = [a, b]

                    # first digit cannot be zero:
                    first_digit_candidates = []
                    if a != 0:
                        first_digit_candidates.append(a)
                    if b != 0:
                        first_digit_candidates.append(b)

                    # There are 2^(length-1) sequences for fixed first digit

                    # We must find which first digit block remaining belongs to

                    n_in_block = remaining

                    for first_digit in sorted(first_digit_candidates):
                        block_size = 2 ** (length - 1)
                        if n_in_block > block_size:
                            n_in_block -= block_size
                        else:
                            # generate n_in_block-th number with this first digit and bits
                            # bits length = length-1, bits from 0 to 2^(length-1)-1

                            index = n_in_block - 1  # zero-based

                            bits = []
                            for i in range(length - 1):
                                bits.append((index >> (length - 2 - i)) & 1)

                            digits = [first_digit] + [digit_map[b] for b in bits]

                            return int(''.join(map(str, digits)))

        # If not found (should not happen)
        return -1


def main():
    import sys
    gen = ShortNumberGenerator()
    for line in sys.stdin:
        line=line.strip()
        if line == '0':
            break
        n = int(line)
        print(gen.nth_short_number(n))


if __name__ == "__main__":
    main()