class LISumSolver:
    class SequenceData:
        def __init__(self, length: int, values: list[int]):
            self.length = length
            self.values = values

    class FenwickTree:
        def __init__(self, size: int):
            self.size = size
            self.data = [(0, 0)] * (self.size + 1)
            # Stores tuples (max_length, max_sum) for subsequences ending with values up to index

        def update(self, idx: int, length: int, sum_: int):
            while idx <= self.size:
                current_length, current_sum = self.data[idx]
                if length > current_length or (length == current_length and sum_ > current_sum):
                    self.data[idx] = (length, sum_)
                idx += idx & -idx

        def query(self, idx: int) -> tuple[int, int]:
            max_length = 0
            max_sum = 0
            while idx > 0:
                length, sum_ = self.data[idx]
                if length > max_length or (length == max_length and sum_ > max_sum):
                    max_length = length
                    max_sum = sum_
                idx -= idx & -idx
            return max_length, max_sum

    class AbstractSolver:
        def solve(self, seq_data: 'LISumSolver.SequenceData') -> int:
            raise NotImplementedError()

    class FenwickLISumSolver(AbstractSolver):
        def __init__(self, max_value: int):
            self.max_value = max_value

        def solve(self, seq_data: 'LISumSolver.SequenceData') -> int:
            fenw = LISumSolver.FenwickTree(self.max_value)
            max_answer = 0

            for a in seq_data.values:
                prev_len, prev_sum = fenw.query(a)
                curr_len = prev_len + 1
                curr_sum = prev_sum + a
                fenw.update(a + 1, curr_len, curr_sum)  # +1 because fenw is 1-indexed
                if curr_len > fenw.query(self.max_value)[0] or (curr_len == fenw.query(self.max_value)[0] and curr_sum > max_answer):
                    max_answer = max(max_answer, curr_sum)

            return max_answer

    class ProblemFacade:
        def __init__(self):
            self._max_A = 10**5

        def parse_input(self) -> 'LISumSolver.SequenceData':
            import sys
            input = sys.stdin.readline
            N = int(input())
            A = list(map(int, input().split()))
            return LISumSolver.SequenceData(N, A)

        def execute(self):
            seq_data = self.parse_input()
            solver = LISumSolver.FenwickLISumSolver(self._max_A)
            result = solver.solve(seq_data)
            print(result)

if __name__ == "__main__":
    problem = LISumSolver.ProblemFacade()
    problem.execute()