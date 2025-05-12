import sys
input = sys.stdin.readline

def Solve():
    ans = 0
    for i in range(n):
        if V[i]:
            continue
        cur = i
        S, an = 0, 0
        m = VMAX
        while True:
            V[cur] = True
            an += 1
            v = A[cur]
            m = min(m, v)
            S += v
            cur = T[v]
            if V[cur]:
                break
        ans += min(S + (an - 2) * m, m + S + (an + 1) * s)
    return ans

MAX = 1000
VMAX = 10000

n = int(input())
A = [int(x) for x in input().split()]
s = min(A)
B = sorted(A)
T = [0] * (VMAX + 1)
for i, b in enumerate(B):
    T[b] = i
V =[False] * MAX
ans = Solve()
print(ans)