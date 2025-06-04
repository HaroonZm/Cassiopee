class LinearCongruentialGenerator:
    def __init__(self, seed: int, a: int, c: int, m: int = 256):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.current = seed

    def reset(self):
        self.current = self.seed

    def next(self) -> int:
        self.current = (self.a * self.current + self.c) % self.m
        return self.current

class EntropyCalculator:
    @staticmethod
    def calculate_entropy(sequence):
        from math import log2
        n = len(sequence)
        if n == 0:
            return 0.0
        frequency = {}
        for x in sequence:
            frequency[x] = frequency.get(x, 0) + 1
        entropy = 0.0
        for count in frequency.values():
            p = count / n
            entropy -= p * log2(p)
        return entropy

class StrangeStringManipulator:
    def __init__(self, m=256):
        self.m = m

    def generate_output(self, input_seq, S, A, C):
        lcg = LinearCongruentialGenerator(seed=S, a=A, c=C, m=self.m)
        output_seq = []
        for i in range(len(input_seq)):
            r_i = lcg.next()
            val = (input_seq[i] + r_i) % self.m
            output_seq.append(val)
        return output_seq

    def find_min_entropy_params(self, input_seq):
        min_entropy = float('inf')
        best_params = (0,0,0)
        for S in range(16):
            for A in range(16):
                for C in range(16):
                    output = self.generate_output(input_seq, S, A, C)
                    entropy = EntropyCalculator.calculate_entropy(output)
                    if entropy < min_entropy or (abs(entropy - min_entropy) < 1e-15 and (S, A, C) < best_params):
                        min_entropy = entropy
                        best_params = (S, A, C)
        return best_params

class InputParser:
    @staticmethod
    def parse_input():
        import sys
        lines = sys.stdin.read().strip().split('\n')
        idx = 0
        while idx < len(lines):
            line = lines[idx].strip()
            if line == '0':
                break
            N = int(line)
            idx += 1
            inp = list(map(int, lines[idx].strip().split()))
            assert len(inp) == N
            idx += 1
            yield inp

def main():
    manipulator = StrangeStringManipulator()
    for input_seq in InputParser.parse_input():
        S, A, C = manipulator.find_min_entropy_params(input_seq)
        print(S, A, C)

if __name__ == "__main__":
    main()