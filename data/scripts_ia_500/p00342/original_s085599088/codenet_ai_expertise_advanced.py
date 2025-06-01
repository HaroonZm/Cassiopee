from collections import Counter
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9 + 7

def A():
    e = list(map(int, input().split()))
    c = Counter(e)
    print("yes" if all(v == 2 for v in c.values()) else "no")

def B():
    n = int(input())
    a = sorted(map(int, input().split()))
    ans = float('-inf')
    # Precompute candidates for b and e to optimize
    for c in range(n):
        for d in range(c):
            m = a[c] - a[d]
            # Select e and b as the two largest indices different from c and d
            excluded = {c, d}
            candidates = [i for i in range(n-1, -1, -1) if i not in excluded]
            if len(candidates) < 2:
                continue
            e, b = candidates[0], candidates[1]
            val = (a[e] + a[b]) / m
            if val > ans:
                ans = val
    print(ans)

def C():
    pass

def D():
    pass

def E():
    pass

def F():
    pass

def G():
    pass

def H():
    pass

def I_():
    pass

def J():
    pass

if __name__ == "__main__":
    B()