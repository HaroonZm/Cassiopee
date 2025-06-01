class InputReader:
    def __init__(self, source=None):
        self.source = source
        self.lines = []
        self.index = 0

    def read_all(self):
        if self.source:
            with open(self.source, 'r', encoding='utf-8') as f:
                self.lines = f.read().splitlines()
        else:
            import sys
            self.lines = sys.stdin.read().splitlines()

    def readline(self):
        line = self.lines[self.index]
        self.index += 1
        return line

class NumbersRepository:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_distinct_pairs_permutations(self):
        perms = []
        n = len(self.numbers)
        for i in range(n):
            for j in range(n):
                if i != j:
                    left = str(self.numbers[i])
                    right = str(self.numbers[j])
                    perms.append(left + right)
        return perms

class PermutationSorter:
    @staticmethod
    def sort_numerically_as_int(strings):
        return sorted(strings, key=lambda x: int(x))

class ProblemSolver:
    def __init__(self, reader):
        self.reader = reader

    def solve(self):
        self.reader.read_all()
        n = int(self.reader.readline())
        nums = []
        for _ in range(n):
            nums.append(int(self.reader.readline()))
        repo = NumbersRepository(nums)
        perms = repo.get_distinct_pairs_permutations()
        sorted_perms = PermutationSorter.sort_numerically_as_int(perms)
        print(sorted_perms[2])

if __name__ == "__main__":
    reader = InputReader()
    solver = ProblemSolver(reader)
    solver.solve()