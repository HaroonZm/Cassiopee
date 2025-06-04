class FormulaTransformer:
    class CharType:
        DIGIT = 0
        PLUS = 1

    def __init__(self, limit: int, formula: str):
        self.limit = limit
        self.original = formula
        self.length = len(formula)
        self.dp = dict()
        self.allowed_chars = [str(d) for d in range(10)] + ['+']

    def char_type(self, c: str):
        return self.CharType.PLUS if c == '+' else self.CharType.DIGIT

    def is_valid_digit(self, c: str):
        return c.isdigit()

    def valid_number(self, s: str):
        # No leading zeros unless the number is '0'
        if not s:
            return False
        if len(s) > 1 and s[0] == '0':
            return False
        return True

    def min_replacements(self):
        # We split the formula into tokens (numbers separated by +)
        # We must find a way to replace minimal characters so that the expression:
        # - Contains no unary '+' (no ++ or starts with +)
        # - Numbers have no leading zero unless zero itself
        # - Sum of numbers <= self.limit
        # We minimize replaced characters.
        # Dynamic programming approach:
        # dp[pos, prev_token_end, current_sum] = min replacements
        # But sum can be up to 1e9 and length up to 1000 => no direct sum dimension.
        # Instead, since addition order is fixed by the tokens, we try all partitions.
        # We'll use recursion with memoization on position and partial sum.
        # We'll try all possible next token splits and check validity.

        from functools import lru_cache

        @lru_cache(None)
        def solve(pos: int, sum_so_far: int) -> int:
            if pos == self.length:
                if sum_so_far <= self.limit:
                    return 0
                else:
                    return float('inf')

            res = float('inf')

            # Try all tokens starting at pos (length at least 1)
            # A token is a number, so digits only, no leading zero unless '0'
            for end in range(pos + 1, self.length + 1):
                segment = self.original[pos:end]

                # To fix segment into valid number, we may replace some chars with digits only
                # and no leading zero unless '0'
                # We'll try all possible replacements of each char
                # For performance, we guess only digits, not plus sign inside a number

                # Pre-reject segments with plus sign (since tokens are numbers only)
                if '+' in segment:
                    # We can replace '+' by digits, count cost
                    # Let's attempt to transform segment into a number of length len(segment)
                    # with no leading zero following the rules.
                    # We'll try all digits for each char and take minimal cost.
                    cost_to_digit = self.min_cost_to_number(segment)
                    if cost_to_digit is None:
                        continue
                    # Check leading zero rule for candidate digit sequences:
                    # The minimal cost solution found respects leading zero via min_cost_to_number
                    # So we consider cost_to_digit (tuple (cost, value))
                    cost, value = cost_to_digit
                    if value is None:
                        continue
                else:
                    # segment made only of digits possibly
                    # minimal cost is count chars different from original
                    cost = 0
                    for ic, c in enumerate(segment):
                        if not c.isdigit():
                            cost = None
                            break
                    if cost is None:
                        # characters inside segment should be digits
                        continue
                    # Check leading zero is valid
                    if not self.valid_number(segment):
                        # maybe replace starting char to fix leading zero
                        # Try to fix leading character to not zero if length > 1
                        # Minimal cost is replace leading char '0' to non-zero digit
                        # But this would change the string: let's try all digit replacements at leading char
                        # Compute minimal replacement cost turning segment into a number
                        res_number = self.min_cost_to_number(segment)
                        if res_number is None:
                            continue
                        cost, value = res_number

                if value is not None and sum_so_far + value <= self.limit:
                    # Then next pos: end
                    next_cost = solve(end, sum_so_far + value)
                    if next_cost != float('inf'):
                        res = min(res, cost + next_cost)
            return res

        ans = solve(0, 0)
        return ans if ans != float('inf') else -1

    def min_cost_to_number(self, segment: str):
        # Given a segment string (of digits and plus possibly),
        # find minimal cost (replacements) to make it a valid number:
        # - only digits
        # - no leading zeros unless 0
        # Return (min_cost, int_value) or None if impossible
        # Brute force approach due to digit length up to len(segment) <= 1000 can be expensive,
        # but since call is controlled, we try a DP on position

        from functools import lru_cache

        n = len(segment)

        @lru_cache(None)
        def dfs(i: int):
            if i == n:
                return [(0, "")]  # cost=0, empty number string

            results = []
            for d in range(10):
                c = str(d)
                cost_char = 0 if segment[i] == c else 1
                next_res = dfs(i + 1)
                for cost_next, num_str in next_res:
                    new_str = c + num_str
                    new_cost = cost_char + cost_next
                    results.append((new_cost, new_str))
            return results

        candidates = dfs(0)

        # Filter candidates valid by leading zero rule
        valid_candidates = []
        for cost, num_str in candidates:
            if len(num_str) == 0:
                continue
            if len(num_str) > 1 and num_str[0] == '0':
                continue
            valid_candidates.append((cost, num_str))

        if not valid_candidates:
            return None

        # Pick minimal cost candidate and convert to int
        valid_candidates.sort(key=lambda x: x[0])
        min_cost = valid_candidates[0][0]
        # Among those with min cost, select minimal numeric value
        min_candidates = [nc for nc in valid_candidates if nc[0] == min_cost]
        min_candidates.sort(key=lambda x: int(x[1]))
        chosen_num_str = min_candidates[0][1]
        return (min_cost, int(chosen_num_str))


def main():
    import sys
    sys.setrecursionlimit(10**7)
    N = int(sys.stdin.readline().strip())
    S = sys.stdin.readline().strip()
    transformer = FormulaTransformer(N, S)
    print(transformer.min_replacements())

if __name__ == "__main__":
    main()