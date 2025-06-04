from itertools import accumulate
from bisect import bisect_right as br
n = int(input())
alst = sorted(map(int, input().split()))
acc = list(accumulate(alst))
m = int(input())
blst = list(map(int, input().split()))
clst = list(map(int, input().split()))
for b, c in zip(blst, clst):
    index = br(alst, b)
    print(["No", "Yes"][(acc[index - 1] if index > 0 else 0) >= c])