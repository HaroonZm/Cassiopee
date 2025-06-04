import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop, heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')

while True:
    line = sys.stdin.readline()
    if not line:
        break
    parts = line.strip().split()
    if not parts:
        continue
    n, m = map(int, parts)
    if n == 0 and m == 0:
        quit()
    recipe = []
    for _ in range(n):
        c = list(map(int, list(sys.stdin.readline().strip())))
        s = 0
        t = 1
        for i in range(m):
            s += c[m - i - 1] * t
            t *= 2
        recipe.append(s)
    dp = defaultdict(int)
    dp[0] = 0
    for r in recipe:
        dp1 = defaultdict(int)
        for j in dp:
            dp1[j] = dp[j]
        for j in dp:
            dp1[j ^ r] = max(dp1[j ^ r], dp[j] + 1)
        dp = dp1
    print(dp[0])