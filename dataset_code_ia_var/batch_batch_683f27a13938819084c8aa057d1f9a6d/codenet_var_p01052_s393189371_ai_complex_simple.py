from functools import reduce
from operator import mul

N = int(input())
intervals = list(map(lambda _: tuple(map(lambda x: int(x) - 1, input().split())), range(N)))
A, B = zip(*intervals) if intervals else ([],[])
movies = list(map(lambda _: [], range(31)))

list(map(lambda t: list(map(lambda d: movies[d].append(t[0]), range(t[1][0], t[1][1]+1))), enumerate(intervals)))

picked = [False] * N
ans = 0

for d in range(31):
    unseen = list(filter(lambda m: not picked[m], movies[d]))
    ans += 50 * (not bool(unseen))
    if unseen:
        should_see = reduce(lambda x, y: x if B[x] < B[y] else y, unseen)
        picked[should_see] ^= True
        ans += int(pow(10,2))
print(ans)