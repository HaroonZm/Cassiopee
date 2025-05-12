import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n, func, e, arrange=None):
        self.init(n)
        self.func = func
        self.e = e
        self.make_arrange(arrange)
    
    def init(self, n):
        self.inf = pow(2, 32)
        self.n = n
        self.N = 1
        while self.N < self.n:
            self.N *= 2
        self.size = self.N * 2 - 1
        self.N -= 1
    
    def make_arrange(self, arrange):
        self.set_arrange(arrange)
        self.construct(arrange)

    def set_arrange(self, arrange):
        if arrange == None:
            self.segment = [self.e]*(self.size)
            return
        self.segment = [0]*(self.N) + arrange + [self.e]*(self.size-self.N-self.n)
    
    def construct(self, arrange):
        if arrange == None:
            return
        for i in range(self.N-1, -1, -1):
            self.segment[i] = self.func(self.segment[2*i+1], self.segment[2*i+2])
    
    def update(self, i, x):
        i += (self.N-1)
        self.segment[i] = x
        while i > 0:
            i = (i-1)//2
            self.segment[i] = self.func(self.segment[2*i+1], self.segment[2*i+2])
    
    def find(self, a, b, k, l, r):
        if r <= a or b <= l:
            return self.e
        elif a <= l and r <= b:
            return self.segment[k]
        else:
            find_l = self.find(a, b, 2*k+1, l, (l+r)//2)
            find_r = self.find(a, b, 2*k+2, (l+r)//2, r)
            res = self.func(find_l, find_r)
            return res

    def count(self, l, r):
        return self.find(l-1, r, 0, 0, self.size-self.N)
    
    def bisect_sub(self, a, b, k, l, r, x):
        if r <= a or b <= l:
            return b+1
        if self.segment[k] < x:
            return b+1
        if k >= self.N:
            return r
        
        find_l = self.bisect_sub(a, b, 2*k+1, l, (l+r)//2, x)
        if find_l <= b:
            return find_l

        find_r = self.bisect_sub(a, b, 2*k+2, (l+r)//2, r, x)
        return find_r

        

    def bisect(self, l, r, x):
        return self.bisect_sub(l-1, r, 0, 0, self.size-self.N, x)
    

def main():
    n, q = map(int, input().split())
    p = list(map(int, input().split()))
    seg = SegmentTree(n, max, 0, arrange=p)

    res = []
    for i in range(q):
        a, b, c = list(map(int, input().split()))
        if a == 1:
            seg.update(b, c)
        elif a == 2:
            ans = seg.count(b, c)
            res.append(ans)
        else:
            ans = seg.bisect(b, n, c)
            res.append(ans)

    print(*res, sep="\n")
            

    
if __name__ == "__main__":
    main()