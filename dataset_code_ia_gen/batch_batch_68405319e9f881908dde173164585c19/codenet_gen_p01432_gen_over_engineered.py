import sys
from abc import ABC, abstractmethod
from math import gcd
from functools import lru_cache
from typing import Tuple, Optional

class InputParser(ABC):
    @abstractmethod
    def parse(self) -> Tuple[int, int, int]:
        pass

class StdInputParser(InputParser):
    def parse(self) -> Tuple[int, int, int]:
        line = sys.stdin.readline().strip()
        S_str, N_str, K_str = line.split()
        return int(S_str), int(N_str), int(K_str)

class ProbabilityDistribution(ABC):
    @abstractmethod
    def probability(self, value: int) -> float:
        pass
    @abstractmethod
    def support(self) -> Tuple[int, int]:
        pass

class UniformSumDistribution(ProbabilityDistribution):
    def __init__(self, N: int, K: int):
        self.N = N
        self.K = K
        self._min = K * 1
        self._max = K * N
        self._counts = None
        self._total = N ** K
        self._init_distribution_counts()

    def _init_distribution_counts(self):
        # Compute distribution_counts[x] = number of combinations summing to x
        # x ranges from K to K*N
        # Use dynamic programming for the counts
        counts_prev = [0] * (self._max + 1)
        for i in range(1, self.N + 1):
            counts_prev[i] = 1
        for _ in range(2, self.K + 1):
            counts_curr = [0] * (self._max + 1)
            cum = 0
            for s in range(self._max + 1):
                if s - 1 >= 0:
                    cum += counts_prev[s - 1]
                if s - self.N - 1 >= 0:
                    cum -= counts_prev[s - self.N - 1]
                counts_curr[s] = cum
            counts_prev = counts_curr
        self._counts = counts_prev

    def probability(self, value: int) -> float:
        if value < self._min or value > self._max:
            return 0.0
        return self._counts[value] / self._total

    def support(self) -> Tuple[int, int]:
        return self._min, self._max

class JumpModel:
    def __init__(self, S: int, N: int, K: int):
        self.S = S
        self.N = N
        self.K = K
        self.distribution = UniformSumDistribution(N, K)
        self.R = abs(S)
        self.direction = -1 if S > 0 else 1  # Jump direction toward witch at 0

    def can_reach(self) -> bool:
        # The possible jump step sizes are from distribution.support()
        min_step, max_step = self.distribution.support()
        d = self._gcd_of_support()
        return self.R % d == 0

    def _gcd_of_support(self) -> int:
        # The jump length is sum of K numbers each in 1..N
        # So support is {K .. K*N}, consecutive integers, thus gcd=1 always
        # but let's keep for extension or change cases
        return 1

    def expected_jumps(self) -> Optional[float]:
        if not self.can_reach():
            return None
        # We solve E(r) = 1 + sum_p E(r - s) for s in support, E(0) = 0
        # where r from 0 to R
        # The distribution is symmetric and the problem reduces to a linear
        # equation system which due to Markov property we solve by DP
        #
        # Here, since R can be huge (up to 10^9), direct DP impossible.
        #
        # But the problem is classic: For a random walk with steps in support,
        # expected hitting time at 0 starting from R = R / mean step length.
        #
        # So expected number of jumps = R / expected_step
        #
        # But need to check if expected value finite: only if mean step > 0
        mean_step = sum(s * self.distribution.probability(s) for s in range(self.N * self.K + 1))
        if mean_step <= 0:
            return None
        # The step is always positive, since sum of positive integers between 1 and N
        # So expected_jumps = R / mean_step
        return self.R / mean_step

class OutputFormatter(ABC):
    @abstractmethod
    def format(self, value: Optional[float]) -> str:
        pass

class ConsoleOutputFormatter(OutputFormatter):
    def format(self, value: Optional[float]) -> str:
        if value is None:
            return "-1"
        else:
            return f"{value:.9f}"

def main():
    parser = StdInputParser()
    S, N, K = parser.parse()
    model = JumpModel(S, N, K)
    result = model.expected_jumps()
    formatter = ConsoleOutputFormatter()
    print(formatter.format(result))

if __name__ == "__main__":
    main()