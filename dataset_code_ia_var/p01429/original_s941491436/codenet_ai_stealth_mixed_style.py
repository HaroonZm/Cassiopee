import sys

sys.setrecursionlimit(100000)
def main():
    inp = sys.stdin.readline
    out = sys.stdout.write
    # procedural reading
    nml = inp().split()
    n, m, l = (int(x) for x in nml)
    k = [int(x) for x in inp().split()]
    s = list(map(int, inp().split()))
    # FP style: su = reduce, then imperative for-mutate
    su = [0]
    for val in s:
        su.append(su[-1] + val)
    k.sort()
    # OOP flair: object for memoization
    class Memo:
        def __init__(self, n): self.d = [[-1]*n for _ in range(n)]
        def get(self, a,b): return self.d[a][b]
        def set(self, a,b, v): self.d[a][b] = v
    memo = Memo(n)
    # Lambda + nested def
    calc = lambda x, y: (su[max(k[x],k[y])] - su[min(k[x],k[y])-1]) // l
    def dfs(i,a,b):
        if i==n: return calc(a,b)
        q = memo.get(a,b)
        if q!=-1: return q
        x = dfs(i+1,a,i) + calc(b,i)
        y = dfs(i+1,b,i) + calc(a,i)
        res = x if x<y else y
        memo.set(a,b,res)
        return res
    out(f"{dfs(1,0,0)}\n")
main()