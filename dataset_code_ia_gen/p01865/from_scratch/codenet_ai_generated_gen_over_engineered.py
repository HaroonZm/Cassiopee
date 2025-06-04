class BalanceScale:
    class Weight:
        def __init__(self, position: int, weight: int):
            self.position = position
            self.weight = weight

        def torque(self) -> int:
            return self.position * self.weight

        def __repr__(self):
            return f"Weight(pos={self.position}, w={self.weight})"

    class TorqueBalancer:
        def __init__(self, L: int, initial_weights):
            self.L = L
            self.initial_weights = initial_weights
            self.current_torque = sum(w.torque() for w in self.initial_weights)
            self.solution_weights = []

        def is_balanced(self):
            return self.current_torque == 0

        def find_balance_solution(self):
            if self.is_balanced():
                # No additional weights needed
                return []

            # Reduce torque by adding weights at holes
            # Since any number of weights can be added,
            # put all correction in a single weight if possible.
            # If current_torque > 0, add weight at negative positions, else positive.

            # Strategy:
            # For each possible position from -L to L (excluding 0 as the pivot),
            # check if torque can be neutralized by additional weights at that position:
            # i.e. find w' such that position * w' = -current_torque and w' integer positive and <= 50000

            ct = self.current_torque
            L = self.L
            max_weight = 50000
            candidates = []
            for pos in range(-L, L + 1):
                if pos == 0:
                    continue
                if ct % pos == 0:
                    w_prime = -ct // pos
                    if 1 <= w_prime <= max_weight:
                        candidates.append(self.Weight(pos, w_prime))

            if candidates:
                # Pick the first candidate solution
                self.solution_weights.append(candidates[0])
                return self.solution_weights

            # If no single weight can fix the torque, try combinations of two weights.
            # For simplicity, we can attempt a brute force over positions:

            # Try all pairs (p1,p2):
            # Solve: p1*w1 + p2*w2 = -ct, w1,w2 positive ints <= max_weight

            for pos1 in range(-L, L + 1):
                if pos1 == 0:
                    continue
                for pos2 in range(-L, L + 1):
                    if pos2 == 0:
                        continue
                    # system: pos1*w1 + pos2*w2 = -ct
                    # rewrite w2 = (-ct - pos1*w1)/pos2
                    # w1 in [1..max_weight], w2 integer positive in [1..max_weight]
                    for w1 in range(1, min(max_weight, abs(ct)*2) + 1):
                        numerator = -ct - pos1 * w1
                        if numerator % pos2 != 0:
                            continue
                        w2 = numerator // pos2
                        if 1 <= w2 <= max_weight:
                            self.solution_weights.append(self.Weight(pos1, w1))
                            self.solution_weights.append(self.Weight(pos2, w2))
                            return self.solution_weights

            # As a fallback, put the entire negative torque on hole -1 or 1 with large weights split
            # This fallback will always work because L >=1 and max weight = 50000 large enough to cover torque
            # We can split the weight in multiple if needed

            abs_ct = abs(ct)
            pos = -1 if ct > 0 else 1  # fix torque sign
            weights_needed = []
            max_w = max_weight
            while abs_ct > 0:
                w = min(max_w, abs_ct)
                weights_needed.append(self.Weight(pos, w))
                abs_ct -= w
            self.solution_weights.extend(weights_needed)
            return self.solution_weights

    class InputParser:
        def __init__(self):
            self.L = None
            self.N = None
            self.weights = []

        def parse(self):
            self.L = int(input())
            self.N = int(input())
            for _ in range(self.N):
                x, w = map(int, input().split())
                self.weights.append(BalanceScale.Weight(x, w))
            return self.L, self.N, self.weights

    class OutputFormatter:
        @staticmethod
        def print_solution(weights):
            print(len(weights))
            for w in weights:
                print(w.position, w.weight)

    def __init__(self):
        self.L = None
        self.N = None
        self.weights = []

    def run(self):
        parser = self.InputParser()
        self.L, self.N, self.weights = parser.parse()

        balancer = self.TorqueBalancer(self.L, self.weights)
        solution = balancer.find_balance_solution()

        formatter = self.OutputFormatter()
        formatter.print_solution(solution)


if __name__ == "__main__":
    scale = BalanceScale()
    scale.run()