from heapq import nlargest

def croad():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    diffs = [b - a for a, b in zip(x, x[1:])]
    if k >= n:
        print(0)
        return
    print(sum(diffs) - sum(nlargest(k - 1, diffs)))

for _ in range(int(input())):
    croad()