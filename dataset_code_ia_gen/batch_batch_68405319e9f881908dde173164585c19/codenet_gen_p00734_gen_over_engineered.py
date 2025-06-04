from typing import List, Optional, Tuple, Iterator
import sys

class CardSet:
    def __init__(self, scores: List[int]) -> None:
        self.scores = scores

    @property
    def total_score(self) -> int:
        return sum(self.scores)

    def __iter__(self):
        return iter(self.scores)

class ExchangeCriterion:
    def __init__(self, taro: CardSet, hanako: CardSet) -> None:
        self.taro = taro
        self.hanako = hanako
        self.difference = self.taro.total_score - self.hanako.total_score

    def feasible_pairs(self) -> Iterator[Tuple[int, int]]:
        # Find pairs (t, h) such that total after exchange is equal
        # total_t - t + h == total_h - h + t
        # rearranged: 2*(t - h) == difference
        # So, difference must be even and (t - h) == diff//2
        if self.difference % 2 != 0:
            return
        target_diff = self.difference // 2
        # Use set for Hanako's cards for fast lookup of candidates
        hanako_scores_set = set(self.hanako.scores)
        for t in self.taro.scores:
            h = t - target_diff
            if h in hanako_scores_set:
                yield (t, h)

class ExchangeDecision:
    def __init__(self, pairs: Iterator[Tuple[int,int]]) -> None:
        self.pairs = pairs

    def best_exchange(self) -> Optional[Tuple[int,int]]:
        # Select pair with minimal sum according to problem statement
        best_pair = None
        best_sum = None
        for t,h in self.pairs:
            s = t + h
            if best_sum is None or s < best_sum:
                best_sum = s
                best_pair = (t,h)
        return best_pair

class InputParser:
    def __init__(self, input_lines: List[str]) -> None:
        self.lines = input_lines
        self.index = 0

    def __iter__(self) -> Iterator[Tuple[CardSet, CardSet]]:
        while True:
            if self.index >= len(self.lines):
                break
            n_m_line = self.lines[self.index].strip()
            self.index +=1
            if n_m_line == '0 0':
                break
            n_str,m_str = n_m_line.split()
            n,m = int(n_str), int(m_str)
            taro_scores = []
            hanako_scores = []
            for _ in range(n):
                taro_scores.append(int(self.lines[self.index].strip()))
                self.index +=1
            for _ in range(m):
                hanako_scores.append(int(self.lines[self.index].strip()))
                self.index +=1
            yield CardSet(taro_scores), CardSet(hanako_scores)

class EqualTotalScoreSolver:
    def __init__(self, datasets: Iterator[Tuple[CardSet, CardSet]]) -> None:
        self.datasets = datasets

    def solve(self) -> List[str]:
        results = []
        for taro, hanako in self.datasets:
            criterion = ExchangeCriterion(taro, hanako)
            pairs = criterion.feasible_pairs()
            decision = ExchangeDecision(pairs)
            answer = decision.best_exchange()
            if answer is None:
                results.append("-1")
            else:
                results.append(f"{answer[0]} {answer[1]}")
        return results

def main() -> None:
    input_lines = sys.stdin.read().strip().split('\n')
    parser = InputParser(input_lines)
    solver = EqualTotalScoreSolver(iter(parser))
    results = solver.solve()
    print("\n".join(results))

if __name__ == "__main__":
    main()