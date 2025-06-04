from functools import reduce
from itertools import chain, islice

N, M = map(int, input().split())
pairs = list(map(lambda s: tuple(map(int, s.split())), (input() for _ in range(M))))
A, B = zip(*pairs) if pairs else ([], [])

hits = list(map(lambda x: x >= N, A))
hit_card = sum(hits)
sorted_A = sorted(A, reverse=True)
need_money = 0

if hit_card < M - 1:
    need_hit = M - 1 - hit_card

    idxs = islice(range(hit_card, hit_card + need_hit), need_hit)
    # Use reduce to accumulate differences
    need_money = reduce(lambda acc, i: acc + (N - sorted_A[i]), idxs, 0)

print(need_money)