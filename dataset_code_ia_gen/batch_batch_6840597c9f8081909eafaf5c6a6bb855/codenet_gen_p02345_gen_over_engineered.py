class AbstractDataStructure:
    def query(self, left: int, right: int):
        raise NotImplementedError

    def update(self, index: int, value: int):
        raise NotImplementedError

class RangeMinimumQuery(AbstractDataStructure):
    def __init__(self, size: int, default_value: int):
        self.n = size
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.default = default_value
        self.data = [self.default] * (2 * self.size)

    def build(self):
        for i in reversed(range(1, self.size)):
            self.data[i] = min(self.data[i << 1], self.data[(i << 1) + 1])

    def update(self, index: int, value: int):
        pos = index + self.size
        self.data[pos] = value
        while pos > 1:
            pos >>= 1
            self.data[pos] = min(self.data[pos << 1], self.data[(pos << 1) + 1])

    def query(self, left: int, right: int) -> int:
        # inclusive range [left, right]
        res = self.default
        l = left + self.size
        r = right + self.size
        while l <= r:
            if l & 1:
                res = min(res, self.data[l])
                l += 1
            if not (r & 1):
                res = min(res, self.data[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

class Query:
    def __init__(self, command: int, x: int, y: int):
        self.command = command  # 0 = update, 1 = query
        self.x = x
        self.y = y

class RMQProcessor:
    def __init__(self, n: int, q: int, queries: list[Query]):
        self.n = n
        self.q = q
        self.queries = queries
        self.default_value = (1 << 31) - 1  # 2^31 - 1
        self.rmq = RangeMinimumQuery(self.n, self.default_value)

    def process(self):
        # Initially the array is all default values which is already set
        # No need to build since no initial updates before queries
        output = []
        for query in self.queries:
            if query.command == 0:
                # update(x, y)
                self.rmq.update(query.x, query.y)
            elif query.command == 1:
                # find(x, y): minimum in [x, y]
                left, right = query.x, query.y
                if left > right:
                    left, right = right, left
                ans = self.rmq.query(left, right)
                output.append(ans)
        return output

def main():
    import sys
    input = sys.stdin.readline
    n, q = map(int, input().split())
    queries = []
    for _ in range(q):
        com, x, y = map(int, input().split())
        queries.append(Query(com, x, y))
    processor = RMQProcessor(n, q, queries)
    results = processor.process()
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()