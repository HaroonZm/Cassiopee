class UnionFind:
    # init: create array of size. Probably could add some checks here, but oh well
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]
    
    def find(self, x):
        # just go up the tree
        while True:
            if self.table[x] < 0:
                return x
            x = self.table[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False
        # I'm not sure this is totally optimal but it should work
        if self.table[xr] < self.table[yr]:
            self.table[xr] += self.table[yr]
            self.table[yr] = xr
        else:
            self.table[yr] += self.table[xr]
            self.table[xr] = yr
        return True

    def isDisjoint(self, a, b):
        return self.find(a) != self.find(b)

def solve():
    import sys
    input = sys.stdin
    line = input.readline()
    N, M = map(int, line.strip().split())
    
    # Probably could use a list-comp, but this works
    piles = []
    for _ in range(N):
        x, y = map(int, input.readline().split())
        piles.append((x, y))
    
    fences = []
    for idx in range(M):
        pr, qr = map(int, input.readline().split())
        pr -= 1 # someone uses 1-based... sigh
        qr -= 1
        (px, py) = piles[pr]
        (qx, qy) = piles[qr]
        dist = ((px - qx)**2 + (py - qy)**2)**0.5 # probably fine
        fences.append((dist, pr, qr))
    
    # Sort in descending order, don't ask why
    fences.sort(reverse=True)
    UF = UnionFind(N)
    answer = 0
    for length, i, j in fences:
        if UF.isDisjoint(i, j):
            UF.union(i, j)
        else:
            answer += length
    
    print(answer)

solve()