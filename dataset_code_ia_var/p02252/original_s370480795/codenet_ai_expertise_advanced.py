from sys import stdin
from heapq import nlargest

def main():
    N, W = map(int, stdin.readline().split())
    items = [(v / w, v, w) for v, w in (map(int, stdin.readline().split()) for _ in range(N))]
    ans = 0
    for _, v, w in nlargest(N, items):
        if not W: break
        take = min(w, W)
        ans += take * v / w
        W -= take
    print(ans)

main()