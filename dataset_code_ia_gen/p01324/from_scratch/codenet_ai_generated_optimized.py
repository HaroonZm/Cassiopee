import sys

sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline()

class UnionFind:
    def __init__(self):
        self.par = dict()
        self.rank = dict()
        self.diff = dict() # diff[x] = weight[x] - weight[parent[x]]

    def add(self, x):
        if x not in self.par:
            self.par[x] = x
            self.rank[x] = 0
            self.diff[x] = 0

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            p = self.par[x]
            r = self.find(p)
            self.diff[x] += self.diff[p]
            self.par[x] = r
            return r

    # unite x and y with relation: weight[y] = weight[x] + w
    # returns True if united successfully or already united consistently
    # returns False if contradictory
    def unite(self, x, y, w):
        self.add(x)
        self.add(y)
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            # Check consistency
            if self.diff[y] != self.diff[x] + w:
                return False
            else:
                return True
        else:
            if self.rank[rx] < self.rank[ry]:
                rx, ry = ry, rx
                w = -w
            self.par[ry] = rx
            self.diff[ry] = self.diff[x] + w - self.diff[y]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
            return True

def main():
    while True:
        N = int(sys.stdin.readline())
        if N == 0:
            break
        uf = UnionFind()
        contradiction = False
        for _ in range(N):
            if contradiction:
                sys.stdin.readline()
                continue
            line = sys.stdin.readline().strip()
            # line format: 1 A = 10^x B
            # parse
            parts = line.split()
            A = parts[1]
            exp = parts[3]
            x = int(exp[3:]) # skip "10^"
            B = parts[4]
            # unite A and B with weight x: 1 A = 10^x B => weight[B] = weight[A] - x
            # but our model uses: weight[y] = weight[x]+w -> here y=B, x=A, w=x means log10(B) = log10(A) + x -> but in problem, 1 A = 10^x B means A = 10^x * B => log10(A) = x + log10(B) => log10(B) = log10(A) - x
            # So weight(B) = weight(A) - x -> weight[y] = weight[x] + w => weight[B] = weight[A] + w => w = -x
            if not uf.unite(A,B, -x):
                contradiction = True
        print("No" if contradiction else "Yes")

if __name__ == "__main__":
    main()