import array
from typing import TypeVar, Generic, Sequence

T = TypeVar('T', bound=int)

class UnionFind(Generic[T]):
    __slots__ = ('parent', 'rank')

    def __init__(self, n: int, typecode: str = 'L') -> None:
        self.parent = array.array(typecode, range(n))
        self.rank = array.array(typecode, (0 for _ in range(n)))

    def find(self, x: int) -> int:
        par = self.parent
        path = []
        while par[x] != x:
            path.append(x)
            x = par[x]
        for node in path:  # Path compression in batch
            par[node] = x
        return x

    def union(self, x: int, y: int) -> bool:
        xroot, yroot = self.find(x), self.find(y)
        if xroot == yroot:
            return False
        rank = self.rank
        par = self.parent
        if rank[xroot] < rank[yroot]:
            par[xroot] = yroot
        else:
            par[yroot] = xroot
            if rank[xroot] == rank[yroot]:
                rank[xroot] += 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def roots(self) -> set[int]:
        par = self.parent
        return {self.find(i) for i in range(len(par))}

def main():
    import sys
    input_iter = iter(sys.stdin.read().split())
    n, m = int(next(input_iter)), int(next(input_iter))
    uf = UnionFind(n, "I")
    for _ in range(m):
        a, b = int(next(input_iter))-1, int(next(input_iter))-1
        uf.union(a, b)
    reps = uf.roots()
    num_components = len(reps)
    # Find number of direct "leaders" (nodes that are their own parent)
    num_leaders = sum(1 for i in range(n) if uf.parent[i] == i)
    answer = abs(num_leaders - 2 * (num_components - (num_leaders - num_components)))
    print(answer)

if __name__ == '__main__':
    main()