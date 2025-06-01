from abc import ABC, abstractmethod
from typing import List, Tuple, Optional


class ParticleEnergyCalculator(ABC):
    @abstractmethod
    def compute_energy(self, bm: int, bw: int) -> int:
        pass


class BParticleEnergyCalculator(ParticleEnergyCalculator):
    def compute_energy(self, bm: int, bw: int) -> int:
        diff = abs(bm - bw)
        return diff * (diff - 30) ** 2


class Microbe(ABC):
    def __init__(self, b_particles: int):
        self.b_particles = b_particles

    def get_b_particles(self) -> int:
        return self.b_particles


class MaleMicrobe(Microbe):
    pass


class FemaleMicrobe(Microbe):
    pass


class MicrobePopulation:
    def __init__(self, males: List[MaleMicrobe], females: List[FemaleMicrobe]):
        self.males = males
        self.females = females


class MaxEnergyEvaluator(ABC):
    @abstractmethod
    def evaluate(self, population: MicrobePopulation) -> int:
        pass


class BipartiteMaximumWeightMatching(MaxEnergyEvaluator):
    def __init__(self, energy_calculator: ParticleEnergyCalculator):
        self.energy_calculator = energy_calculator

    def evaluate(self, population: MicrobePopulation) -> int:
        males = population.males
        females = population.females
        M = len(males)
        W = len(females)

        # Build cost matrix (negative weights since we want max weight matching)
        cost_matrix = [[0] * W for _ in range(M)]
        for i, male in enumerate(males):
            for j, female in enumerate(females):
                energy = self.energy_calculator.compute_energy(male.get_b_particles(), female.get_b_particles())
                cost_matrix[i][j] = -energy  # negative for Hungarian minimization

        # Hungarian algorithm implementation for minimum weight matching
        return -self._hungarian(cost_matrix)

    def _hungarian(self, cost_matrix: List[List[int]]) -> int:
        # This implementation assumes rectangular matrix MxN with M <= N
        # If M > N, pad to make M <= N, since problem constraints allow up to 12 for each
        M = len(cost_matrix)
        N = len(cost_matrix[0]) if M > 0 else 0
        if M == 0 or N == 0:
            return 0
        # Pad the matrix if needed
        size = max(M, N)
        cost = [[0]*size for _ in range(size)]
        for i in range(M):
            for j in range(N):
                cost[i][j] = cost_matrix[i][j]

        u = [0]* (size+1)
        v = [0]* (size+1)
        p = [0]* (size+1)
        way = [0]* (size+1)
        INF = 10**9
        for i in range(1, size+1):
            p[0] = i
            j0 = 0
            minv = [INF]*(size+1)
            used = [False]*(size+1)
            while True:
                used[j0] = True
                i0 = p[j0]
                j1 = 0
                delta = INF
                for j in range(1,size+1):
                    if not used[j]:
                        cur = cost[i0-1][j-1]-u[i0]-v[j]
                        if cur < minv[j]:
                            minv[j] = cur
                            way[j] = j0
                        if minv[j] < delta:
                            delta = minv[j]
                            j1 = j
                for j in range(size+1):
                    if used[j]:
                        u[p[j]] += delta
                        v[j] -= delta
                    else:
                        minv[j] -= delta
                j0 = j1
                if p[j0] == 0:
                    break
            # augmenting path
            while True:
                j1 = way[j0]
                p[j0] = p[j1]
                j0 = j1
                if j0 == 0:
                    break
        # p[j]: male matched to female j
        result = 0
        for j in range(1,size+1):
            i = p[j]
            if i <= M and j <= N:
                result += cost[i-1][j-1]
        return result


class InputParser:
    def parse(self, raw_input: str) -> List[MicrobePopulation]:
        lines = [line.strip() for line in raw_input.strip().splitlines()]
        populations = []
        i = 0
        while i < len(lines):
            if lines[i] == '0 0':
                break
            # parse M, W
            M, W = map(int, lines[i].split())
            i += 1
            # parse bm
            bm_list = list(map(int, lines[i].split()))
            while len(bm_list) < M:
                i += 1
                bm_list.extend(map(int, lines[i].split()))
            i += 1
            # parse bw
            bw_list = list(map(int, lines[i].split()))
            while len(bw_list) < W:
                i += 1
                bw_list.extend(map(int, lines[i].split()))
            i += 1

            males = [MaleMicrobe(bm) for bm in bm_list[:M]]
            females = [FemaleMicrobe(bw) for bw in bw_list[:W]]
            populations.append(MicrobePopulation(males, females))
        return populations


class OutputFormatter:
    def format(self, results: List[int]) -> str:
        return '\n'.join(str(r) for r in results)


class MicrobeEnergyMaximizerApp:
    def __init__(self,
                 parser: InputParser,
                 evaluator: MaxEnergyEvaluator,
                 formatter: OutputFormatter):
        self.parser = parser
        self.evaluator = evaluator
        self.formatter = formatter

    def run(self, raw_input: Optional[str] = None) -> str:
        if raw_input is None:
            raw_input = self._read_stdin()
        populations = self.parser.parse(raw_input)
        results = [self.evaluator.evaluate(pop) for pop in populations]
        return self.formatter.format(results)

    @staticmethod
    def _read_stdin() -> str:
        import sys
        return sys.stdin.read()


if __name__ == "__main__":
    app = MicrobeEnergyMaximizerApp(
        parser=InputParser(),
        evaluator=BipartiteMaximumWeightMatching(BParticleEnergyCalculator()),
        formatter=OutputFormatter()
    )
    print(app.run())