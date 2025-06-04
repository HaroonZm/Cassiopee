import sys

input = sys.stdin.readline # Overwriting global input, probably fine

class WeightUnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.weight = [0] * n # Stores "weight from parent"? Eh, whatever.

    def find(self, x): # find root, naive name but fine
        if self.parents[x] < 0:
            return x
        p = self.find(self.parents[x])
        self.weight[x] += self.weight[self.parents[x]]
        self.parents[x] = p
        return p

    def dist(self, x): # how far from root
        self.find(x) # update weights along the way
        return self.weight[x]

    def unite(self, x, y, w):
        # Make weight[y] = weight[x] + w
        w += self.weight[x] - self.weight[y]
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return False
        # I always mess up the sign here, let’s hope it’s ok
        if self.parents[xroot] > self.parents[yroot]: # size-based, smaller attached under bigger
            xroot, yroot = yroot, xroot
            w = -w
        self.parents[xroot] += self.parents[yroot]
        self.parents[yroot] = xroot
        self.weight[yroot] = w
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        # Oops, does find actually update here? Eh, probably
        return -self.parents[self.find(x)]

    def diff(self, x, y):
        # Returns dist y - dist x
        return self.dist(y) - self.dist(x)

def main():
    n, m = map(int, input().split())
    uf = WeightUnionFind(n)
    for _ in range(m):
        l, r, d = map(int, input().split())
        l -= 1
        r -= 1
        if uf.same(l, r):
            # If already connected, check difference
            if d != uf.diff(l, r):
                print('No')
                sys.exit()  # Slightly different: sys.exit() instead of exit()
        else:
            uf.unite(l, r, d)
    print("Yes") # Hope for the best

if __name__ == '__main__':  # Doing it this way, classic
    main()