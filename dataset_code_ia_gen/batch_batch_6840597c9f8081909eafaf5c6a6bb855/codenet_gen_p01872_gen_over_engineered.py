class MyNumberValidator:
    def __init__(self, number_str):
        self.number_str = number_str
        self.length = 12
        self.weights = self._compute_weights()
        self.unknown_index = self._find_unknown_index()
        self.digits = self._parse_digits()

    def _compute_weights(self):
        weights = []
        for n in range(1, 12):
            if 1 <= n <= 6:
                weights.append(n + 1)
            else:
                weights.append(n - 5)
        return weights

    def _find_unknown_index(self):
        count_unknown = self.number_str.count('?')
        if count_unknown != 1:
            raise ValueError("Input must contain exactly one '?' character")
        return self.number_str.index('?')

    def _parse_digits(self):
        digits = []
        for ch in self.number_str:
            if ch == '?':
                digits.append(None)
            else:
                digits.append(int(ch))
        return digits

    def _checksum_modulo(self, digits11):
        total = 0
        for p, q in zip(digits11, self.weights):
            total += p * q
        return total % 11

    def _compute_check_digit(self, digits11):
        r = self._checksum_modulo(digits11)
        if r <= 1:
            return 0
        return 11 - r

    def _validate_with_candidate(self, candidate_digit):
        trial_digits = self.digits[:]
        trial_digits[self.unknown_index] = candidate_digit
        digits11 = trial_digits[:-1]
        expected_check_digit = self._compute_check_digit(digits11)
        actual_check_digit = trial_digits[-1]
        return expected_check_digit == actual_check_digit

    def solve(self):
        valid_candidates = []
        for candidate in range(10):
            if self.unknown_index == 11:
                # Unknown digit is check digit:
                # We can compute expected check digit for given digits11 and see if candidate matches it
                digits11 = self.digits[:-1]
                if None in digits11:
                    # Should not happen as only one unknown digit per problem statement
                    continue
                expected_check_digit = self._compute_check_digit(digits11)
                if candidate == expected_check_digit:
                    valid_candidates.append(candidate)
            else:
                # Unknown digit is one of digits11
                # Substitute candidate then check consistency with check digit
                if self._validate_with_candidate(candidate):
                    valid_candidates.append(candidate)

        if len(valid_candidates) == 1:
            print(valid_candidates[0])
        else:
            print("MULTIPLE")

def main():
    input_str = input().rstrip('\n')
    validator = MyNumberValidator(input_str)
    validator.solve()

if __name__ == "__main__":
    main()