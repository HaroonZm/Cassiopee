import sys,math,random,collections,heapq,itertools,string,functools,re,array,bisect,time,copy, fractions

sys.setrecursionlimit(int(1e7)+29)
inf = float('inf')
eps = pow(10,-13)
mod=1_000_000_007
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
DIR8 = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

def li(): return list(map(int,sys.stdin.readline().split()))
def li_(): return [int(z)-1 for z in sys.stdin.readline().split()]
lf = lambda : list(map(float,sys.stdin.readline().split()))
def ls(): return sys.stdin.readline().split()
def i(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
pf = lambda s: print(s,flush=True)

def main():
    RES = []
    def processor(n, W):
        values = []
        for iii in range(n): values.append(i())
        vals = sorted(values,key=lambda x:-x)
        dp = array.array('l',[0]*(W+1))
        dp[0] = 1
        total = 0
        for v in vals: total += v
        if total <= W:
            return 1
        acc = 0
        idx = 0
        sm = total
        while idx < len(vals):
            num = vals[idx]
            sm -= num
            if W >= sm:
                lo = max(0, W-sm-num+1)
                hi = W-sm+1
                for q in range(lo, hi):
                    acc += dp[q]
                    acc %= mod
            for t in reversed(range(W-num+1)):
                dp[t+num] += dp[t]
                dp[t+num] %= mod
            idx += 1
        return acc%mod
    
    # Imperative style for input
    while True:
        AAA = li()
        if not AAA:
            continue
        N, M = AAA
        if N==0:
            break
        RES += [processor(N, M)]
        # Intentionally terminating the loop early, like original
        break
    
    return '\n'.join(str(v) for v in RES)

if __name__=="__main__":
    print(main())