from functools import reduce
from itertools import cycle, accumulate, islice, count, takewhile

N, K = map(int, input().split())
P = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

def loop_data(start, perm, score):
    def iterator():
        idx = start
        while True:
            yield idx
            idx = perm[idx]
    first = next(islice(iterator(), 1))
    seq = [start]
    idx = perm[start]
    while idx != start:
        seq.append(idx)
        idx = perm[idx]
    scores = [score[x] for x in seq]
    return seq, scores, sum(scores)

inspector = lambda iterable, func: reduce(lambda acc, x: acc if acc else func(x), iterable, None)

def stepper(K, seq, scores, loop_sum):
    M = len(seq)
    reverie = [0] + scores * ((K + M - 1) // M + 2)
    best = -10**9
    strides = accumulate(reverie)
    def inner():
        for o in range(M):
            for t in range(1, min(M, K)+1):
                walks = t + (K - t) // M * M
                if walks > K or o+t>len(reverie): continue
                loops_full = (K - t) // M
                v = strides.__copy__()
                cur = sum(scores[:t])
                bonus = max(0, loop_sum) * loops_full
                yield cur + bonus
            next(strides)
    return max(inner())

candid = ((i, *loop_data(i, P, C)) for i in range(1, N+1))
outcome = max(stepper(K, seq, scores, loop_sum) for i, seq, scores, loop_sum in candid)
print(outcome)