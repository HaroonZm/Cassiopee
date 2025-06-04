class FenwickTree:
    def __init__(self, size):
        self._size = size
        self._tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self._size:
            self._tree[index] += delta
            index += index & -index

    def prefix_sum(self, index):
        result = 0
        while index > 0:
            result += self._tree[index]
            index -= index & -index
        return result

    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

class SequenceInterface:
    def add(self, i, x):
        raise NotImplementedError()

    def get_sum(self, s, t):
        raise NotImplementedError()

class FenwickSequence(SequenceInterface):
    def __init__(self, n):
        self._fenwick = FenwickTree(n)

    def add(self, i, x):
        self._fenwick.update(i, x)

    def get_sum(self, s, t):
        return self._fenwick.range_sum(s, t)

class QueryProcessor:
    def __init__(self, sequence: SequenceInterface):
        self._sequence = sequence
        self._results = []

    def process_query(self, com, x, y):
        if com == 0:
            self._sequence.add(x, y)
        elif com == 1:
            res = self._sequence.get_sum(x, y)
            self._results.append(res)

    def output_results(self):
        for res in self._results:
            print(res)

class InputParser:
    @staticmethod
    def parse_ints(line):
        return list(map(int, line.strip().split()))

    @classmethod
    def parse_first_line(cls):
        import sys
        line = sys.stdin.readline()
        return cls.parse_ints(line)

    @classmethod
    def parse_queries(cls, q):
        import sys
        for _ in range(q):
            line = sys.stdin.readline()
            yield cls.parse_ints(line)

class Application:
    def __init__(self):
        self.n = 0
        self.q = 0
        self.processor = None

    def run(self):
        self.n, self.q = InputParser.parse_first_line()
        sequence = FenwickSequence(self.n)
        self.processor = QueryProcessor(sequence)
        for com, x, y in InputParser.parse_queries(self.q):
            self.processor.process_query(com, x, y)
        self.processor.output_results()

if __name__ == "__main__":
    app = Application()
    app.run()