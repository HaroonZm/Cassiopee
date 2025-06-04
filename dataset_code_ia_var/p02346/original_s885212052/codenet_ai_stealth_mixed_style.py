import sys

class fenwick:
    def __init__(self, n):
        self.n = n
        self.t = [0 for _ in range(n+1)]

    def update(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.t[idx] += val
            idx += (idx & -idx)

    def get(self, idx):
        res = 0
        idx += 1
        while idx > 0:
            res += self.t[idx]
            idx -= (idx & -idx)
        return res

input_ = sys.stdin
def ints(): return [int(x) for x in input_ .readline().split()]
def oneint(): return int(input_ .readline())
def strinput(): return input_ .readline().rstrip()

if __name__ == "__main__":
    a,b = ints()
    F = fenwick(a)
    for _ in range(b):
        s = input_ .readline().split()
        op = int(s[0])
        if op==0:
            F.update(int(s[1])-1, int(s[2]))
        else:
            x = int(s[1])-1
            y = int(s[2])-1
            def get_range(f,x,y): return f.get(y)-f.get(x-1)
            answer = get_range(F, x, y)
            print(answer)