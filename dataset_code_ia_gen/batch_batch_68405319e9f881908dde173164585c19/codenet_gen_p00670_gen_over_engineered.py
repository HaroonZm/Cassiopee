class MagicPowerRepository:
    def __init__(self, powers):
        self._powers = powers
        self._frequency = self._build_frequency()

    def _build_frequency(self):
        freq = [0] * 101
        for p in self._powers:
            freq[p] += 1
        return freq

    def total_count(self):
        return len(self._powers)

    def frequency(self, power):
        if 1 <= power <= 100:
            return self._frequency[power]
        return 0

    def distinct_powers(self):
        return [p for p in range(1, 101) if self._frequency[p] > 0]


class EnemyPower:
    def __init__(self, power):
        self._power = power

    @property
    def value(self):
        return self._power


class PairCounter:
    def __init__(self, magic_repo: MagicPowerRepository, enemy: EnemyPower):
        self.magic_repo = magic_repo
        self.enemy = enemy

    def _count_pairs_with_different_powers(self):
        count = 0
        freq = self.magic_repo._frequency
        S = self.enemy.value
        for x in range(1, 101):
            if freq[x] == 0:
                continue
            for y in range(x + 1, 101):
                if freq[y] == 0:
                    continue
                if x + y == S:
                    # Check if one is strictly larger than the other: always true here since x != y
                    # So the pair (x,y) counts only once as (i,j) and not (j,i)
                    # Number of such pairs: freq[x] * freq[y]
                    count += freq[x] * freq[y]
        return count

    def _count_pairs_with_same_power(self):
        # When powers are equal, the sum is 2*x
        # Only count if 2*x == S and no tie condition happens, so no count for equal powers 
        # since "等しい場合は相打ちで勝ったことにならない"
        # So just return 0 explicitly
        return 0

    def count_valid_pairs(self):
        # Count pairs (i,j) i!=j, (i,j) and (j,i) same pair (not double counted)
        # Sum == enemy power, one power strictly larger than the other

        # This means sum of two powers == S
        # For pairs of distinct powers x,y with x+y=S and x != y
        # and since x != y, one is strictly bigger, so pair counts
        return self._count_pairs_with_different_powers() + self._count_pairs_with_same_power()


class InputParser:
    @staticmethod
    def parse_input_lines(lines):
        idx = 0
        cases = []
        while idx < len(lines):
            line = lines[idx].strip()
            if line == "0 0":
                break
            n, S = map(int, line.split())
            idx += 1
            powers = []
            for _ in range(n):
                powers.append(int(lines[idx].strip()))
                idx += 1
            cases.append((n, S, powers))
        return cases


class SpellcastersSolver:
    def __init__(self, input_data):
        self.input_data = input_data

    def solve(self):
        cases = InputParser.parse_input_lines(self.input_data)
        results = []
        for n, S, powers in cases:
            magic_repo = MagicPowerRepository(powers)
            enemy = EnemyPower(S)
            pair_counter = PairCounter(magic_repo, enemy)
            results.append(pair_counter.count_valid_pairs())
        return results


if __name__ == "__main__":
    import sys

    input_data = sys.stdin.read().strip().split("\n")
    solver = SpellcastersSolver(input_data)
    results = solver.solve()
    for res in results:
        print(res)