class AbstractDataStructure:
    def find(self, x): raise NotImplementedError
    def unite(self, x, y, w): raise NotImplementedError
    def diff(self, x, y): raise NotImplementedError

class WeightedUnionFindTree(AbstractDataStructure):
    class _Node:
        __slots__ = ('parent', 'rank', 'weight')
        def __init__(self, parent, rank, weight):
            self.parent = parent
            self.rank = rank
            self.weight = weight

    def __init__(self, size: int):
        self._nodes = [self._Node(i, 0, 0) for i in range(size)]

    def find(self, x: int) -> int:
        node = self._nodes[x]
        if node.parent == x:
            return x
        else:
            root = self.find(node.parent)
            node.weight += self._nodes[node.parent].weight
            node.parent = root
            return root

    def unite(self, x: int, y: int, w: int) -> bool:
        # w = (a_y - a_x)
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        node_x = self._nodes[x]
        node_y = self._nodes[y]
        root_x = self._nodes[rx]
        root_y = self._nodes[ry]
        w = w + node_x.weight - node_y.weight
        if root_x.rank < root_y.rank:
            root_x.parent = ry
            root_x.weight = -w
        else:
            root_y.parent = rx
            root_y.weight = w
            if root_x.rank == root_y.rank:
                root_x.rank += 1
        return True

    def diff(self, x: int, y: int):
        if self.find(x) != self.find(y):
            return None
        return self._nodes[y].weight - self._nodes[x].weight

class QueryProcessor:
    def __init__(self, uf: AbstractDataStructure):
        self.uf = uf

    def process(self, queries):
        results = []
        for query in queries:
            op = query[0]
            if op == 0:  # relate
                _, x, y, z = query
                self.uf.unite(x, y, z)
            elif op == 1:  # diff
                _, x, y = query
                d = self.uf.diff(x, y)
                results.append(d if d is not None else '?')
            else:
                raise ValueError("Unknown operation")
        return results

class InputOutputHandler:
    def __init__(self):
        pass

    def read_input(self):
        import sys
        input = sys.stdin.readline
        n, q = map(int, input().split())
        queries = []
        for _ in range(q):
            line = input().split()
            if line[0] == '0':
                queries.append((0, int(line[1]), int(line[2]), int(line[3])))
            else:
                queries.append((1, int(line[1]), int(line[2])))
        return n, q, queries

    def write_output(self, results):
        print('\n'.join(str(r) for r in results))

def main():
    io_handler = InputOutputHandler()
    n, q, queries = io_handler.read_input()
    uf = WeightedUnionFindTree(n)
    processor = QueryProcessor(uf)
    results = processor.process(queries)
    io_handler.write_output(results)

if __name__ == "__main__":
    main()