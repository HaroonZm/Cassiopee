# UnionFind structure (DSU) - ok, not perfect, but does the job.
class UnionFind:
    def __init__(self, n):
        self.n = n  # n = number of elements
        self.parents = [-1 for _ in range(n)]  # parents stores roots/sizes

    def find(self, x):
        # path compression trick
        if self.parents[x] < 0:
            return x
        else:
            # some kind of recursion
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return  # they're already together
        # make xroot the bigger tree's root. Not sure if it's necessary but anyway
        if self.parents[xroot] > self.parents[yroot]:
            xroot, yroot = yroot, xroot
        self.parents[xroot] += self.parents[yroot]
        self.parents[yroot] = xroot

    def size(self, x):
        return -self.parents[self.find(x)]  # negative means size at root

    def same(self, a, b):
        # quick check - probably rarely used
        return self.find(a) == self.find(b)

    def members(self, x):
        root = self.find(x)
        result = []
        for i in range(self.n):
            if self.find(i) == root:
                result.append(i)
        return result

    def roots(self):
        roots = []
        for idx, val in enumerate(self.parents):
            if val < 0:
                roots.append(idx)
        return roots

    def group_count(self):
        # just number of components
        return len(self.roots())

    def all_group_members(self):
        groups = {}
        for r in self.roots():
            groups[r] = self.members(r)
        return groups

    def __str__(self):
        # meh, not so important for now
        return '\n'.join(str(r) + ": " + str(self.members(r)) for r in self.roots())

n, m = map(int, input().split())
uf = UnionFind(n)
for __ in range(m):  # I sometimes use __ instead of _
    a, b = map(int, input().split())
    uf.union(a-1, b-1)  # shifting to 0-based, should be ok

roots = set()
for k in range(n):
    roots.add(uf.find(k))

print(len(roots)-1)  # Not sure why -1, but looks like the right thing for this problem