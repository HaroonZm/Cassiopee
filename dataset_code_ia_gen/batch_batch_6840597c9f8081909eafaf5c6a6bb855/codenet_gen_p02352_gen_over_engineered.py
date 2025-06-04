class AbstractSegmentTreeOperation:
    def combine_node_values(self, left, right):
        raise NotImplementedError()

    def apply_update(self, node_value, update_value, segment_length):
        raise NotImplementedError()

    def combine_updates(self, old_update, new_update):
        raise NotImplementedError()

    def default_node_value(self):
        raise NotImplementedError()

    def default_update_value(self):
        raise NotImplementedError()

class MinWithAddOperation(AbstractSegmentTreeOperation):
    def combine_node_values(self, left, right):
        return min(left, right)

    def apply_update(self, node_value, update_value, segment_length):
        return node_value + update_value

    def combine_updates(self, old_update, new_update):
        return old_update + new_update

    def default_node_value(self):
        # Because array values and updates can be negative, use large positive
        return float('inf')

    def default_update_value(self):
        return 0

class LazySegmentTree:
    def __init__(self, size, operation: AbstractSegmentTreeOperation):
        self._n = 1
        while self._n < size:
            self._n <<= 1
        self._operation = operation
        self._data = [self._operation.default_node_value()] * (2 * self._n)
        self._lazy = [self._operation.default_update_value()] * (2 * self._n)
        self._has_lazy = [False] * (2 * self._n)

    def _apply(self, idx, val, length):
        self._data[idx] = self._operation.apply_update(self._data[idx], val, length)
        if idx < self._n:
            self._lazy[idx] = self._operation.combine_updates(self._lazy[idx], val)
            self._has_lazy[idx] = True

    def _push(self, idx, length):
        if self._has_lazy[idx]:
            self._apply(idx * 2, self._lazy[idx], length // 2)
            self._apply(idx * 2 + 1, self._lazy[idx], length // 2)
            self._lazy[idx] = self._operation.default_update_value()
            self._has_lazy[idx] = False

    def _recalc(self, idx):
        self._data[idx] = self._operation.combine_node_values(self._data[idx * 2], self._data[idx * 2 + 1])

    def build(self):
        for i in reversed(range(1, self._n)):
            self._recalc(i)

    def _update(self, left, right, val, idx, l, r):
        if right < l or r < left:
            return
        if left <= l and r <= right:
            self._apply(idx, val, r - l + 1)
            return
        self._push(idx, r - l + 1)
        mid = (l + r) // 2
        self._update(left, right, val, idx * 2, l, mid)
        self._update(left, right, val, idx * 2 + 1, mid + 1, r)
        self._recalc(idx)

    def update(self, left, right, val):
        self._update(left, right, val, 1, 0, self._n - 1)

    def _query(self, left, right, idx, l, r):
        if right < l or r < left:
            return self._operation.default_node_value()
        if left <= l and r <= right:
            return self._data[idx]
        self._push(idx, r - l + 1)
        mid = (l + r) // 2
        left_res = self._query(left, right, idx * 2, l, mid)
        right_res = self._query(left, right, idx * 2 + 1, mid + 1, r)
        return self._operation.combine_node_values(left_res, right_res)

    def query(self, left, right):
        return self._query(left, right, 1, 0, self._n - 1)

def main():
    import sys
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    n, q = map(int, input().split())
    operation = MinWithAddOperation()
    segtree = LazySegmentTree(n, operation)
    segtree.build()

    class QueryProcessor:
        def __init__(self, segtree):
            self.segtree = segtree

        def process_add(self, s, t, x):
            self.segtree.update(s, t, x)

        def process_find(self, s, t):
            return self.segtree.query(s, t)

    processor = QueryProcessor(segtree)

    class QueryDispatcher:
        def __init__(self, processor):
            self.processor = processor

        def dispatch(self, query):
            if query[0] == 0:
                _, s, t, x = query
                self.processor.process_add(s, t, x)
            else:
                _, s, t = query
                res = self.processor.process_find(s, t)
                print(res)

    dispatcher = QueryDispatcher(processor)

    for _ in range(q):
        line = input().split()
        if line[0] == '0':
            query = (0, int(line[1]), int(line[2]), int(line[3]))
        else:
            query = (1, int(line[1]), int(line[2]))
        dispatcher.dispatch(query)

if __name__ == '__main__':
    main()