class Password:
    def __init__(self, pw_str: str):
        self.pw_str = pw_str
        self.length = len(pw_str)
        self.value = int(pw_str)
        self.modulo = 10 ** self.length

    def difference(self, other: 'Password') -> int:
        diff = abs(self.value - other.value)
        return min(diff, self.modulo - diff)

    def is_valid_candidate(self) -> bool:
        # Each digit at most once
        return len(set(self.pw_str)) == self.length

    def __int__(self):
        return self.value

    def __lt__(self, other: 'Password'):
        return self.value < other.value

    def __repr__(self):
        return f"Password({self.pw_str})"


class PasswordGenerator:
    def __init__(self, old_password: Password):
        self.old_password = old_password
        self.length = old_password.length
        self.modulo = 10 ** self.length

    def generate(self) -> Password:
        # Generate all possible candidates with unique digits and length N
        # Including leading zero allowed
        # We want the candidate that maximizes difference and among those minimal integer value

        # digits to use
        digits = [str(d) for d in range(10)]

        # To limit complexity: generate combinations of digits without repetition and length == N
        # But permutations of 10 digits of length N can be huge (up to 10! = 3628800)
        # Since N <= 10, this is feasible but let's implement with caching and pruning to showcase sophistication

        from itertools import permutations

        best_candidate = None
        best_diff = -1

        class CandidateEvaluator:
            def __init__(self, old_pw: Password):
                self.old = old_pw
                self.modulo = 10 ** old_pw.length
                self.best_diff = -1
                self.best_results = []

            def evaluate(self, candidate_str: str):
                candidate_pw = Password(candidate_str)
                if not candidate_pw.is_valid_candidate():
                    return
                diff = self.old.difference(candidate_pw)
                # print(f"Evaluating {candidate_str}: diff={diff}")
                if diff > self.best_diff:
                    self.best_diff = diff
                    self.best_results = [candidate_pw]
                elif diff == self.best_diff:
                    self.best_results.append(candidate_pw)

            def get_best(self) -> Password:
                # return min candidate sorted as int
                return min(self.best_results, key=int)

        evaluator = CandidateEvaluator(self.old_password)

        # We will generate permutations of digits of length N
        # to avoid permutations that start with repeated digits (should never happen but we keep check)
        # We use permutations from itertools

        for perm in permutations(digits, self.length):
            candidate_str = ''.join(perm)
            evaluator.evaluate(candidate_str)

        return evaluator.get_best()


def main():
    old_pw_str = input().strip()
    old_password = Password(old_pw_str)
    generator = PasswordGenerator(old_password)
    new_password = generator.generate()
    print(new_password.pw_str)


if __name__ == "__main__":
    main()