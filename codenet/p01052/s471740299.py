import sys
import heapq
# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

n = II()
M = [LI() for _ in range(n)]
for a in zip(* M):
    start = set(a)
    break
M.sort()
# print(start)

ans = 0
index = 0
hq = []
for i in range(31):
    if i + 1 in start:
        while i + 1 in start and M[index][0] == i + 1:
            heapq.heappush(hq, M[index][1])
            index += 1
            if index >= n:
                break

    while hq and hq[0] < i + 1:
        if hq:
            tmp = heapq.heappop(hq)
        else:
            break

    if hq:
        ans += 100
        tmp = heapq.heappop(hq)
    else:
        ans += 50

    # print(i+1, ans, hq)

print(ans)