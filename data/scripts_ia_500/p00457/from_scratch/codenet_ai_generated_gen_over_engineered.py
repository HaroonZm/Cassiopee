class Color:
    RED = 1
    BLUE = 2
    YELLOW = 3

    _all_colors = {RED, BLUE, YELLOW}

    @classmethod
    def others(cls, c):
        return cls._all_colors - {c}

class ChainReactionSimulator:
    def __init__(self, initial_sequence):
        self.initial_sequence = initial_sequence
        self.N = len(initial_sequence)

    def simulate(self, index, new_color):
        # Deep copy the sequence
        sequence = list(self.initial_sequence)
        if sequence[index] == new_color:
            # no change happens
            return len(sequence)
        sequence[index] = new_color

        return self._chain_react(sequence)

    def _chain_react(self, sequence):
        """Perform chain reaction until no 4+ consecutive same colors remain."""
        while True:
            to_remove = []
            length = len(sequence)
            start = 0
            while start < length:
                current_color = sequence[start]
                end = start + 1
                while end < length and sequence[end] == current_color:
                    end += 1
                run_length = end - start
                if run_length >= 4:
                    to_remove.extend(range(start, end))
                start = end
            if not to_remove:
                break
            # Remove characters
            new_sequence = []
            trash_set = set(to_remove)
            for i, c in enumerate(sequence):
                if i not in trash_set:
                    new_sequence.append(c)
            sequence = new_sequence
        return len(sequence)

class AbstractColorChanger:
    def __init__(self, simulator, index):
        self.simulator = simulator
        self.index = index

    def possible_new_colors(self):
        current_color = self.simulator.initial_sequence[self.index]
        for c in Color.others(current_color):
            yield c

    def calculate_min_remaining(self):
        min_remaining = self.simulator.N
        for c in self.possible_new_colors():
            remaining = self.simulator.simulate(self.index, c)
            if remaining < min_remaining:
                min_remaining = remaining
        return min_remaining

class ChainReactionSolver:
    def __init__(self, sequences):
        self.sequences = sequences

    def solve(self):
        results = []
        for sequence in self.sequences:
            simulator = ChainReactionSimulator(sequence)
            min_remain_total = simulator.N
            for idx in range(simulator.N):
                changer = AbstractColorChanger(simulator, idx)
                min_remain = changer.calculate_min_remaining()
                if min_remain < min_remain_total:
                    min_remain_total = min_remain
            results.append(min_remain_total)
        return results

def parse_input():
    import sys
    sequences = []
    lines = sys.stdin.read().strip().split('\n')
    pos = 0
    while True:
        if pos >= len(lines):
            break
        N = int(lines[pos])
        pos += 1
        if N == 0:
            break
        seq = []
        for _ in range(N):
            seq.append(int(lines[pos]))
            pos += 1
        sequences.append(seq)
    return sequences

def main():
    sequences = parse_input()
    solver = ChainReactionSolver(sequences)
    results = solver.solve()
    for res in results:
        print(res)

if __name__ == "__main__":
    main()