from typing import List, Tuple, Dict, Iterator
from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True)
class ProblemParameters:
    region_count: int
    days: int
    max_burden: int
    max_multi_live_days: int


@dataclass(frozen=True)
class LiveData:
    expected_profit: List[List[int]]  # [region][day]
    burden: List[List[int]]  # [region][day]


@dataclass(frozen=True)
class ScheduleState:
    day: int
    burden_used: int
    multi_live_days_used: int
    last_regions_bitset: int  # bitmask of regions visited today to avoid repeat within same day


class LiveScheduleSolver:
    def __init__(self, parameters: ProblemParameters, data: LiveData):
        self.p = parameters
        self.data = data
        # Precompute adjacency for regions
        self.adjacency_map = self._build_adjacency_map(self.p.region_count)

    @staticmethod
    def _build_adjacency_map(region_count: int) -> Dict[int, List[int]]:
        adjacency = {i: [] for i in range(region_count)}
        for i in range(region_count):
            if i > 0:
                adjacency[i].append(i - 1)
            if i < region_count - 1:
                adjacency[i].append(i + 1)
        return adjacency

    def solve(self) -> int:
        # Since multiple lives per day must be adjacent regions and cannot repeat same region same day,
        # we need to consider all sequences of regions (sets) per day with adjacency,
        # but this would be huge.
        # Instead, we consider combinations encoded as bitsets, but that too is large.
        # To reduce complexity, we do a stateful DP:
        # State: day, burden used, multi-live-days used
        # Transition: For each subset of regions on today's live (0 or more, but if more than 1 then adjacency and no duplicates)
        # We handle the condition of at most one multi-live day per state.

        # Given constraints:
        # C <= 15, D <= 30, W <= 50, X <= 5
        # We will enumerate for each day all valid "live sets" respecting adjacency and no duplicate regions same day

        valid_live_sets = self._generate_valid_live_sets()

        @lru_cache(maxsize=None)
        def dp(day: int, burden_left: int, multi_live_days_left: int) -> int:
            if day == self.p.days:
                return 0

            best_profit = 0
            # Try all valid live sets on this day
            for live_set in valid_live_sets:
                burden_sum = 0
                profit_sum = 0
                count_lives = bin(live_set).count('1')
                if count_lives == 0:
                    # skip no live (allowed?), problem states max 1 live per day principal, 0 live allowed is doubtful. Let's allow no live no burden no profit.
                    profit_sum = 0
                    burden_sum = 0
                    needed_multi = 0
                else:
                    needed_multi = 1 if count_lives > 1 else 0
                    if needed_multi > multi_live_days_left:
                        continue
                    # Sum burden and profit for selected regions
                    valid = True
                    for r in range(self.p.region_count):
                        if (live_set & (1 << r)) != 0:
                            e = self.data.expected_profit[r][day]
                            f = self.data.burden[r][day]
                            if e == 0:
                                valid = False
                                break
                            profit_sum += e
                            burden_sum += f
                    if not valid:
                        continue
                if burden_sum > burden_left:
                    continue
                candidate = profit_sum + dp(day + 1, burden_left - burden_sum, multi_live_days_left - needed_multi)
                if candidate > best_profit:
                    best_profit = candidate
            return best_profit

        return dp(0, self.p.max_burden, self.p.max_multi_live_days)

    def _generate_valid_live_sets(self) -> List[int]:
        # Generate all subsets of regions that are valid to be performed in one day:
        # - no duplicate region obviously (sets)
        # - if multiple regions, they form a connected chain by adjacency
        # Max regions = 15 -> 2^15 = 32768 subsets possible

        # We'll cache region adjacency bitmasks for quick checking
        adj_masks = []
        for i in range(self.p.region_count):
            mask = 0
            for adj in self.adjacency_map[i]:
                mask |= (1 << adj)
            adj_masks.append(mask)

        valid_sets = []
        # We rely on the fact that subsets with 0 or 1 region always valid
        # For > 1 region, must be connected adj.

        def is_connected_subset(s: int) -> bool:
            # BFS starting from any set bit
            if s == 0:
                return True
            # Find first set bit index
            start = (s & (-s)).bit_length() - 1
            visited = 0
            queue = [start]
            visited |= (1 << start)
            while queue:
                v = queue.pop()
                neighbors = adj_masks[v]
                # neighbors intersect s (regions in subset) not yet visited
                nbrs_in_s = neighbors & s & (~visited)
                # expand visited with nbrs_in_s
                while nbrs_in_s:
                    nxt = (nbrs_in_s & (-nbrs_in_s)).bit_length() - 1
                    nbrs_in_s &= ~(1 << nxt)
                    visited |= (1 << nxt)
                    queue.append(nxt)

            return visited == s

        for subset in range(1 << self.p.region_count):
            # check connectedness if size > 1
            if bin(subset).count('1') <= 1:
                valid_sets.append(subset)
            else:
                if is_connected_subset(subset):
                    valid_sets.append(subset)
        return valid_sets


class InputParser:
    def __init__(self, lines: Iterator[str]):
        self.lines = lines

    def parse_next_case(self) -> Tuple[ProblemParameters, LiveData]:
        # parse header line
        while True:
            header_line = next(self.lines).strip()
            if header_line:
                break
        C, D, W, X = map(int, header_line.split())
        if (C, D, W, X) == (0, 0, 0, 0):
            return None, None

        # parse E: C rows * D columns each (for profit)
        expected_profit = []
        for _ in range(C):
            profit_line = next(self.lines).strip()
            while not profit_line:
                profit_line = next(self.lines).strip()
            row = list(map(int, profit_line.split()))
            # There could be multiple lines if data array split per day?
            # Problem shows E i,j in lines, but sample input is presented concatenated.
            # We'll consider each line is C integers for a day (?), the sample input seems tricky.
            # Actually, from problem description, E i,j lines are C*D lines.
            # Each line is a single integer (expect profit) for region i and day j.
            # So we read C*D lines (not a single line).
            # Correction: we must read C * D lines, each line one integer.

        # Due to problem description structure, we must read C*D lines with one integer each for expected profit, then same for burden
        # So rewrite parsing accordingly

        # Rewind parsing for E:
        e_profit = [[0]*D for _ in range(C)]
        for i in range(C):
            for j in range(D):
                line = next(self.lines).strip()
                while not line:
                    line = next(self.lines).strip()
                e_profit[i][j] = int(line)

        # then F burden similarly
        f_burden = [[0]*D for _ in range(C)]
        for i in range(C):
            for j in range(D):
                line = next(self.lines).strip()
                while not line:
                    line = next(self.lines).strip()
                f_burden[i][j] = int(line)

        return ProblemParameters(C, D, W, X), LiveData(e_profit, f_burden)


class LiveScheduleProcessor:
    def __init__(self):
        self.results: List[int] = []

    def process(self, lines: Iterator[str]):
        parser = InputParser(lines)
        while True:
            params, data = parser.parse_next_case()
            if params is None:
                break
            solver = LiveScheduleSolver(params, data)
            ans = solver.solve()
            self.results.append(ans)

    def output_results(self):
        for res in self.results:
            print(res)


def main():
    import sys
    processor = LiveScheduleProcessor()
    processor.process(iter(sys.stdin))
    processor.output_results()


if __name__ == "__main__":
    main()