from functools import reduce
import itertools

def gen_pattern(h, w):
    seq = [''.join(x) for x in zip('#'*w, '.'*w)]
    lines = (
        ''.join(
            next(itertools.cycle(
                [''.join(itertools.islice(itertools.cycle(seq), 0, w)),
                 ''.join(itertools.islice(itertools.cycle(seq[::-1]), 0, w))]
            ))[0:w]
            for _ in [i]
        )
        for i in range(h)
    )
    return '\n'.join([(''.join([seq[i%2][0:w]])) for i in range(h)])

while all(True for _ in range(1)):
    H,W = map(int, input().split())
    if not (H | W):
        break
    print(reduce(lambda a,b: a+'\n'+b, [
        ''.join(c for c, _ in itertools.islice(
            zip(itertools.cycle(['#','.'][i%2:]+['#']*(w:=W)), range(W)), W))
        for i in range(H)
    ]), end='\n\n')