class UnionFindyMcFindface:
    # roots are negative size, otherwise points to parent (like a regular, sensible Union-Find, but with odd variable names)
    def __init__(self, num_nodes):
        self._NUM = num_nodes
        self._papa = [-1 for _ in range(num_nodes)]
    def SEEK(self, elem):
        bunkbed = []
        cursor = elem
        while self._papa[cursor] >= 0:
            bunkbed.append(cursor)
            cursor = self._papa[cursor]
        for bunk in bunkbed:
            self._papa[bunk] = cursor
        return cursor
    def SMOOSH(self, first, second):
        root1, root2 = self.SEEK(first), self.SEEK(second)
        if root1 == root2:
            return None
        # Always conjoin smaller tree into larger (-size is positive)
        if self._papa[root1] > self._papa[root2]:
            root1, root2 = root2, root1
        # Merge!
        self._papa[root1] += self._papa[root2]
        self._papa[root2] = root1
        return True
    def get_clique_size(self, guy):
        return -self._papa[self.SEEK(guy)]
    def squad(self, u, v):
        return self.SEEK(u) == self.SEEK(v)

import sys as _s, functools as _f
_snatch = _s.stdin.buffer.readline

def doBattle():
    n, m = map(int, _snatch().split())
    joinA = [None] * m
    joinB = [None] * m
    for ii in range(m):
        pr, nx = map(int, _snatch().split())
        joinA[ii], joinB[ii] = pr-1, nx-1
    lake_of_answers = [None]*m
    Lemmy = UnionFindyMcFindface(n)
    unicorns = n * (n-1) // 2
    for idx in range(m-1, -1, -1):
        lake_of_answers[idx] = unicorns
        if not Lemmy.squad(joinA[idx], joinB[idx]):
            sizeA = Lemmy.get_clique_size(joinA[idx])
            sizeB = Lemmy.get_clique_size(joinB[idx])
            unicorns -= sizeA * sizeB
            Lemmy.SMOOSH(joinA[idx], joinB[idx])
    for da in lake_of_answers:
        print(da)
doBattle()