class SubstitutionRule:
    def __init__(self, pattern: str, replacement: str):
        self.pattern = pattern
        self.replacement = replacement

    def apply(self, s: str) -> str:
        parts = []
        i = 0
        length = len(s)
        p_len = len(self.pattern)
        while i < length:
            if s.startswith(self.pattern, i):
                parts.append(self.replacement)
                i += p_len
            else:
                parts.append(s[i])
                i += 1
        return ''.join(parts)


class SubstitutionSet:
    def __init__(self, rules):
        self.rules = rules  # list of SubstitutionRule

    def possible_next_states(self, s: str):
        next_states = []
        for rule in self.rules:
            result = rule.apply(s)
            if result != s:
                next_states.append(result)
        return next_states


class BFSState:
    def __init__(self, string: str, steps: int):
        self.string = string
        self.steps = steps


class SubstitutionSolver:
    MAX_STEPS = 100  # safety limit

    def __init__(self, substitution_set: SubstitutionSet, start: str, target: str):
        self.substitution_set = substitution_set
        self.start = start
        self.target = target

    def minimum_substitutions(self) -> int:
        from collections import deque

        visited = set()
        queue = deque()
        queue.append(BFSState(self.start, 0))
        visited.add(self.start)

        while queue:
            current_state = queue.popleft()
            if current_state.string == self.target:
                return current_state.steps
            if current_state.steps >= self.MAX_STEPS:
                continue
            for next_str in self.substitution_set.possible_next_states(current_state.string):
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(BFSState(next_str, current_state.steps + 1))
        return -1


class InputParser:
    def __init__(self):
        self.datasets = []

    def parse(self):
        import sys
        lines = sys.stdin.read().splitlines()
        index = 0
        while True:
            if index >= len(lines):
                break
            n_line = lines[index].strip()
            index += 1
            if n_line == '0':
                break
            n = int(n_line)
            rules = []
            for _ in range(n):
                line = lines[index].strip()
                index += 1
                alpha, beta = line.split(' ')
                rules.append(SubstitutionRule(alpha, beta))
            gamma = lines[index].strip()
            index += 1
            delta = lines[index].strip()
            index += 1
            self.datasets.append((rules, gamma, delta))


class OutputHandler:
    @staticmethod
    def output_results(results):
        for res in results:
            print(res)


def main():
    parser = InputParser()
    parser.parse()
    results = []
    for rules, gamma, delta in parser.datasets:
        substitution_set = SubstitutionSet(rules)
        solver = SubstitutionSolver(substitution_set, gamma, delta)
        res = solver.minimum_substitutions()
        results.append(res)
    OutputHandler.output_results(results)


if __name__ == '__main__':
    main()