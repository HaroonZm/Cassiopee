from itertools import product, groupby, starmap, chain
from functools import reduce, partial
from operator import add, itemgetter
from collections import defaultdict

while True:
    M,T,P,R = map(int, input().split())
    if not (M or T): break

    matrix = lambda d: [[d() for _ in range(16)] for __ in range(64)]
    time, accepted = matrix(int), matrix(int)

    tuple_inputs = list(starmap(lambda _,__=None: tuple(map(int, input().split())), [(None,)]*R))
    pipe = lambda f,*a: lambda x: f(x,*a)
    inc = lambda arr,i,j,x=1: arr[i][j] + x
    latch = lambda arr,i,j,v: arr[i].__setitem__(j, v)

    list(map(lambda args: (
        latch(accepted, args[1], args[2], 1) if not args[3] else None,
        latch(time, args[1], args[2], time[args[1]][args[2]] + args[0]) if not args[3] else latch(time, args[1], args[2], time[args[1]][args[2]] + 20)
    ), tuple_inputs))

    score = defaultdict(int)
    F = lambda t,p: accepted[t][p]*65536 - (time[t][p] if accepted[t][p] else 0)
    list(map(lambda tp: score.__setitem__(tp[0], score[tp[0]]+F(tp[0],tp[1])), chain(*[[(t,p) for p in range(1,P+1)] for t in range(1,T+1)])))

    inv_score = defaultdict(list)
    { inv_score[v].append(k) for k,v in score.items() }

    output = ",".join(
        "=".join(map(str, sorted(ts, reverse=True)))
        for v,ts in sorted(inv_score.items(), key=itemgetter(0), reverse=True)
    )
    print(output)