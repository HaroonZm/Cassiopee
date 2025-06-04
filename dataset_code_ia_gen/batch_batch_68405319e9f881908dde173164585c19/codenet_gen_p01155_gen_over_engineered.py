class FactorizationStrategy:
    def factor_pairs(self, n: int) -> list[tuple[int, int]]:
        raise NotImplementedError

class BruteForceFactorization(FactorizationStrategy):
    def factor_pairs(self, n: int) -> list[tuple[int, int]]:
        factors = []
        limit = int(n**0.5)
        for i in range(1, limit + 1):
            if n % i == 0:
                factors.append((i, n // i))
        return factors

class SequenceGenerator:
    def __init__(self, a: int, b: int, factorization_strategy: FactorizationStrategy):
        self.a = a
        self.b = b
        self.factorization_strategy = factorization_strategy
        
    def generate_all_sequences(self) -> list[list[int]]:
        a_factors = self.factorization_strategy.factor_pairs(self.a)
        b_factors = self.factorization_strategy.factor_pairs(self.b)
        sequences = []
        for a1, a2 in a_factors:
            for b1, b2 in b_factors:
                seq = [a1, a2, b1, b2]
                seq.sort()
                sequences.append(seq)
        return sequences

class CostEvaluator:
    @staticmethod
    def evaluate_sequence(seq: list[int]) -> int:
        return sum((seq[i+1] - seq[i])**2 for i in range(len(seq)-1))

class MinimalCostFinder:
    def __init__(self, sequence_generator: SequenceGenerator, cost_evaluator: CostEvaluator):
        self.sequence_generator = sequence_generator
        self.cost_evaluator = cost_evaluator
        
    def find_min_cost(self) -> int:
        sequences = self.sequence_generator.generate_all_sequences()
        min_cost = None
        for seq in sequences:
            cost = self.cost_evaluator.evaluate_sequence(seq)
            if min_cost is None or cost < min_cost:
                min_cost = cost
        return min_cost

class RuinsSolver:
    def __init__(self, factorization_strategy: FactorizationStrategy):
        self.factorization_strategy = factorization_strategy
        
    def solve(self, a: int, b: int) -> int:
        sequence_generator = SequenceGenerator(a, b, self.factorization_strategy)
        cost_evaluator = CostEvaluator()
        finder = MinimalCostFinder(sequence_generator, cost_evaluator)
        return finder.find_min_cost()

def main():
    import sys
    factorization_strategy = BruteForceFactorization()
    solver = RuinsSolver(factorization_strategy)
    for line in sys.stdin:
        a_str, b_str = line.split()
        a, b = int(a_str), int(b_str)
        if a == 0 and b == 0:
            break
        result = solver.solve(a, b)
        print(result)

if __name__ == "__main__":
    main()