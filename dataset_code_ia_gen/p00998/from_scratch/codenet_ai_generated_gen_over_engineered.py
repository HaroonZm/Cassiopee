import sys
import threading
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple, Union

sys.setrecursionlimit(1 << 25)
threading.stack_size(1 << 27)

class Query(ABC):
    @abstractmethod
    def execute(self, data_structure):
        pass

class ShiftQuery(Query):
    def __init__(self, l: int, r: int):
        self.l = l
        self.r = r

    def execute(self, data_structure):
        data_structure.shift(self.l, self.r)

class MinQuery(Query):
    def __init__(self, l: int, r: int):
        self.l = l
        self.r = r

    def execute(self, data_structure):
        return data_structure.range_min(self.l, self.r)

class UpdateQuery(Query):
    def __init__(self, pos: int, val: int):
        self.pos = pos
        self.val = val

    def execute(self, data_structure):
        data_structure.point_update(self.pos, self.val)

class AbstractDataStructure(ABC):
    @abstractmethod
    def shift(self, l: int, r: int):
        pass

    @abstractmethod
    def range_min(self, l: int, r: int) -> int:
        pass

    @abstractmethod
    def point_update(self, pos: int, val: int):
        pass

class SegmentTreeRMQ(AbstractDataStructure):
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.inf = 10**15
        self.data = [self.inf] * (2 * self.size)
        for i in range(self.n):
            self.data[self.size + i] = data[i]
        for i in reversed(range(1, self.size)):
            self.data[i] = min(self.data[i << 1], self.data[(i << 1) + 1])
        self.array = data[:]  # Maintain original array for shifts

    def _update(self, pos: int, val: int):
        i = pos + self.size
        self.data[i] = val
        i >>= 1
        while i > 0:
            self.data[i] = min(self.data[i << 1], self.data[(i << 1) + 1])
            i >>= 1

    def point_update(self, pos: int, val: int):
        self.array[pos] = val
        self._update(pos, val)

    def _query(self, l: int, r: int) -> int:
        # inclusive l, r
        res = self.inf
        l += self.size
        r += self.size
        while l <= r:
            if (l & 1) == 1:
                res = min(res, self.data[l])
                l += 1
            if (r & 1) == 0:
                res = min(res, self.data[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

    def range_min(self, l: int, r: int) -> int:
        return self._query(l, r)

    def shift(self, l: int, r: int):
        # Circular shift: a[l..r] -> move a[r] to a[l], shift others right by 1
        if l >= r:
            return
        # Extract last element
        last_val = self.array[r]
        # Shift elements right from r-1 down to l
        for i in range(r, l, -1):
            self.array[i] = self.array[i - 1]
            self._update(i, self.array[i])
        self.array[l] = last_val
        self._update(l, last_val)

class QueryProcessor:
    def __init__(self, n: int, initial_array: List[int], queries: List[Query]):
        self.n = n
        self.queries = queries
        self.data_structure = SegmentTreeRMQ(initial_array)

    def process_all(self) -> List[int]:
        results = []
        for query in self.queries:
            if isinstance(query, MinQuery):
                ans = query.execute(self.data_structure)
                results.append(ans)
            else:
                query.execute(self.data_structure)
        return results

def parse_input() -> Tuple[int, int, List[int], List[Query]]:
    input = sys.stdin.readline
    n, q = map(int, input().split())
    array = [int(input()) for _ in range(n)]
    queries = []
    for _ in range(q):
        x, y, z = map(int, input().split())
        if x == 0:
            queries.append(ShiftQuery(y, z))
        elif x == 1:
            queries.append(MinQuery(y, z))
        else:
            queries.append(UpdateQuery(y, z))
    return n, q, array, queries

def main():
    n, q, array, queries = parse_input()
    processor = QueryProcessor(n, array, queries)
    results = processor.process_all()
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    threading.Thread(target=main).start()