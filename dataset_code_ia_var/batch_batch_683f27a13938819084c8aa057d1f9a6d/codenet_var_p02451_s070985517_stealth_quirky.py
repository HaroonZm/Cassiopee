import bisect as b
_0 = int(input())
__ = list(map(int, input().split()))
__.insert(-0, 10**9 + 1)
for _q in [*range(int(input()))]:
    k = int(input())
    p = b.bisect_left(__, k)
    print(int(__[p] == k))