from functools import reduce
from operator import itemgetter
from itertools import count, chain, cycle, starmap, takewhile

N = int(input())
indices = list(range(N))
LRs = list(starmap(lambda l, r, i: (l, r, i), 
                   (map(int, input().split()) + (i,) for i in indices)))
Ls = sorted(LRs, key=itemgetter(0))
Rs = sorted(LRs, key=itemgetter(1))

def traverse(direction):
    done = set()
    pos = 0
    score = 0
    iL, iR = N-1, 0

    cycle_getters = [
        lambda: ( # negative direction
            ((pos, Rs[j][1], Rs[j][2]) for j in range(iR, N) if Rs[j][2] not in done),
            lambda j: N if j == N else next(x[1] for x in Rs[j:])
        ),
        lambda: ( # positive direction
            ((pos, Ls[j][0], Ls[j][2]) for j in range(iL, -1, -1) if Ls[j][2] not in done),
            lambda j: -1 if j < 0 else next(x[1] for x in Ls[:j+1][::-1])
        )
    ]

    pointers = [lambda: (iR, N, 1), lambda: (iL, -1, -1)]
    seqidx = 0 if direction == 'neg' else 1

    for k in count():
        # Move in current direction
        total, step, step_sign = pointers[seqidx%2]()
        seq = (Rs if seqidx%2 == 0 else Ls)
        getter = [itemgetter(1), itemgetter(0)][seqidx % 2]
        # Skip done
        while 0 <= total < N and seq[total][2] in done:
            total += step_sign
        if total < 0 or total >= N:
            break
        xNext = getter(seq[total])
        if (seqidx % 2 == 0 and pos < xNext) or (seqidx % 2 == 1 and pos > xNext):
            break
        score += abs(pos - xNext)
        pos = xNext
        done.add(seq[total][2])
        if seqidx %2 == 0:
            iR = total + 1
        else:
            iL = total - 1
        seqidx += 1
    return score + abs(pos)

ans = max(traverse('neg'), traverse('pos'))
print(ans)