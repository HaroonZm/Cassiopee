class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.total = 0
        self.lazy_val = None  # For range assignment
        self.length = end - start + 1

    def apply(self, val):
        self.total = val * self.length
        self.lazy_val = val

    def push_down(self):
        if self.lazy_val is not None and self.left and self.right:
            self.left.apply(self.lazy_val)
            self.right.apply(self.lazy_val)
            self.lazy_val = None


class AbstractSegmentTree:
    def __init__(self, n):
        self.n = n
        self.root = self._build(0, n - 1)

    def _build(self, start, end):
        raise NotImplementedError

    def update(self, start, end, val):
        self._update(self.root, start, end, val)

    def _update(self, node, start, end, val):
        raise NotImplementedError

    def query(self, start, end):
        return self._query(self.root, start, end)

    def _query(self, node, start, end):
        raise NotImplementedError


class RangeUpdateRangeSumSegmentTree(AbstractSegmentTree):
    def _build(self, start, end):
        node = SegmentTreeNode(start, end)
        if start < end:
            mid = (start + end) // 2
            node.left = self._build(start, mid)
            node.right = self._build(mid + 1, end)
        return node

    def _update(self, node, start, end, val):
        if node.start > end or node.end < start:
            return
        if start <= node.start and node.end <= end:
            node.apply(val)
            return
        node.push_down()
        self._update(node.left, start, end, val)
        self._update(node.right, start, end, val)
        node.total = node.left.total + node.right.total

    def _query(self, node, start, end):
        if node.start > end or node.end < start:
            return 0
        if start <= node.start and node.end <= end:
            return node.total
        node.push_down()
        return self._query(node.left, start, end) + self._query(node.right, start, end)


class QueryProcessor:
    def __init__(self, n):
        self.tree = RangeUpdateRangeSumSegmentTree(n)

    def process_queries(self, queries):
        results = []
        for query in queries:
            if query[0] == 0:
                _, s, t, x = query
                self.tree.update(s, t, x)
            elif query[0] == 1:
                _, s, t = query
                results.append(self.tree.query(s, t))
        return results


class Parser:
    def __init__(self, input_source):
        self.input_source = input_source

    def parse(self):
        n, q = map(int, self.input_source.readline().split())
        queries = []
        for _ in range(q):
            parts = self.input_source.readline().strip().split()
            if parts[0] == '0':
                queries.append((0, int(parts[1]), int(parts[2]), int(parts[3])))
            else:
                queries.append((1, int(parts[1]), int(parts[2])))
        return n, queries


class Application:
    def __init__(self, input_source):
        self.parser = Parser(input_source)
        self.query_processor = None

    def run(self):
        n, queries = self.parser.parse()
        self.query_processor = QueryProcessor(n)
        results = self.query_processor.process_queries(queries)
        for res in results:
            print(res)


import sys

if __name__ == "__main__":
    app = Application(sys.stdin)
    app.run()