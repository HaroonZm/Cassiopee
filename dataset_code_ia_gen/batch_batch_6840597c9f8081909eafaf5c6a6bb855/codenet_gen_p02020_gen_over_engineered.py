class TeaPartyProblem:
    def __init__(self, bread_sets):
        self.bread_sets = bread_sets
        self.n = len(bread_sets)
        self.total_breads = sum(bread_sets)
        self.dp_table = [[False] * (self.total_breads + 1) for _ in range(self.n + 1)]
        self.dp_table[0][0] = True

    def _build_dp(self):
        for i in range(1, self.n + 1):
            bread = self.bread_sets[i - 1]
            for j in range(self.total_breads + 1):
                if self.dp_table[i-1][j]:
                    self.dp_table[i][j] = True  # Not taking current set
                    if j + bread <= self.total_breads:
                        self.dp_table[i][j + bread] = True  # Taking current set

    def _find_max_even_sum(self):
        # Find the maximum even sum <= total_breads that can be formed
        max_even_sum = 0
        for s in range(0, self.total_breads + 1, 2):
            if self.dp_table[self.n][s]:
                if s > max_even_sum:
                    max_even_sum = s
        return max_even_sum

    def max_sandwiches(self):
        self._build_dp()
        max_even_sum = self._find_max_even_sum()
        # Return the maximum number of sandwiches (pairs)
        return max_even_sum // 2


class TeaPartyController:
    def __init__(self, input_reader, output_writer):
        self.input_reader = input_reader
        self.output_writer = output_writer

    def execute(self):
        n = int(self.input_reader.read_line())
        breads = list(map(int, self.input_reader.read_line().split()))
        problem = TeaPartyProblem(breads)
        result = problem.max_sandwiches()
        self.output_writer.write_line(str(result))


class InputReader:
    def read_line(self):
        return input()


class OutputWriter:
    def write_line(self, line):
        print(line, end='\n')


if __name__ == "__main__":
    input_reader = InputReader()
    output_writer = OutputWriter()
    controller = TeaPartyController(input_reader, output_writer)
    controller.execute()