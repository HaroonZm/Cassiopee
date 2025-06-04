from typing import List, Tuple
from itertools import product
from math import isclose

class Marathon:
    class Runner:
        def __init__(self, pid: int, p_rest: float, t_rest: int, speed: int, n_rest: int, length: int):
            self.id = pid
            self.p_rest = p_rest / 100.0
            self.t_rest = t_rest
            self.speed = speed
            self.n_rest = n_rest
            self.length = length

            # Compute all possible total times as (rest_count, time) tuples
            self.possible_times = self._compute_time_distribution()

        def _compute_time_distribution(self) -> List[Tuple[int, float]]:
            # Each runner may rest at each resting place independently: run-time + resting time if any rests.
            # Time without rest = L / V
            base_time = self.length / self.speed if self.speed != 0 else float('inf')
            # We store tuples: (time, probability)
            distribution = []
            # r: number of resting places where runner rests (from 0 to n_rest)
            # The distribution is binomial, but resting time fixed for each rest.
            # Actually we need the full distribution over all subsets since probability differs
            # because each resting place has the same probability of resting?

            # Because all resting places have the *same* probability for each runner,
            # distribution of rest counts is binomial: prob(k rests) = C(n_rest,k) * p^k * (1-p)^{n_rest-k}
            from math import comb
            dist = []
            for k in range(self.n_rest + 1):
                prob = comb(self.n_rest, k)*(self.p_rest ** k)*((1-self.p_rest) ** (self.n_rest - k))
                time = base_time + k * self.t_rest
                dist.append((time, prob))
            return dist

    class ResultAggregator:
        def __init__(self, runners: List['Marathon.Runner']):
            self.runners = runners
            self.n = len(runners)
            # Store win probabilities indexed by runner id
            self.wins = [0.0] * self.n

        def compute_wins(self):
            # For each combination of runners' possible times (they are independent),
            # calculate the resulting winner or draw and accumulate probabilities.
            # Because each runner has at most n_rest+1 possible times, total combinations:
            # (n_rest+1)^n which is feasible only for small n and m.
            # Constraints: n <= 100, m <= 50 => maximum (51)^100 is impossible.
            # So we optimize: since each runner's dist has length n_rest+1, but n_rest = M,
            # We must find a polynomial method.

            # Elegant solution:
            # Since resting places and resting probabilities are all runner-specific and identical per resting place,
            # we can treat each runner independently with a multinomial/time distribution.

            # But question asks sophisticated solution, so we do full joint distribution using dynamic programming of mass function.

            # We build joint distributions progressively:

            distributions = [r.possible_times for r in self.runners]

            # Each possible_times is list of (time, prob).
            # Construct joint distribution over all runners: dict {tuple(times): prob}

            joint_dist = {(): 1.0}
            for dist in distributions:
                next_joint = {}
                for times_tuple, prob1 in joint_dist.items():
                    for t, prob2 in dist:
                        extended = times_tuple + (t,)
                        next_joint[extended] = next_joint.get(extended, 0.0) + prob1*prob2
                joint_dist = next_joint

            # Now, for each tuple of finishing times, find the unique fastest runner(s)
            # If exactly one fastest, increment that runner's win probability by the scenario probability

            for times_tuple, prob in joint_dist.items():
                min_time = min(times_tuple)
                winners = [idx for idx, t in enumerate(times_tuple) if isclose(t, min_time, abs_tol=1e-14)]
                if len(winners) == 1:
                    self.wins[winners[0]] += prob
                # else tie => no winner

        def get_wins(self) -> List[float]:
            return self.wins


    def __init__(self, N: int, M: int, L: int, runners_data: List[Tuple[int,int,int]]):
        self.N = N
        self.M = M
        self.L = L
        self.runners = [self.Runner(i, p, t, v, M, L) for i,(p,t,v) in enumerate(runners_data)]

    def solve(self) -> List[float]:
        aggregator = self.ResultAggregator(self.runners)
        aggregator.compute_wins()
        return aggregator.get_wins()

def parse_input() -> Tuple[int,int,int,List[Tuple[int,int,int]]]:
    import sys
    N, M, L = map(int, sys.stdin.readline().split())
    runners = []
    for _ in range(N):
        P, T, V = map(int, sys.stdin.readline().split())
        runners.append((P,T,V))
    return N, M, L, runners

def main():
    N, M, L, runners_data = parse_input()
    marathon = Marathon(N,M,L,runners_data)
    results = marathon.solve()
    for p in results:
        print(f"{p:.8f}")

if __name__ == "__main__":
    main()