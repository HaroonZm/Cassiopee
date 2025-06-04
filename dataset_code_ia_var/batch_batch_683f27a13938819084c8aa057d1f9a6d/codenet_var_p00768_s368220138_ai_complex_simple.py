import re
from functools import reduce
from itertools import product, groupby, chain

while True:
    *vals, = map(int, input().split())
    Time, Team, Quiz, n = vals or [0, 0, 0, 0]
    if sum(vals[:2]) == 0: break

    indices = range(Team)
    score = dict(zip(indices, [0]*Team))
    accept = dict(zip(indices, [0]*Team))
    miss = [[0]*Quiz for _ in indices]

    for _ in range(n):
        h, t, q, j = map(int, input().split())
        t, q = t-1, q-1
        [accept.__setitem__, score.__setitem__][j==0](t, (accept[t]+1, score[t]+h+miss[t][q])[j==0])
        [miss[t].__setitem__][j!=0](q, miss[t][q]+20 if j else miss[t][q])

    acc_max = max(accept.values())
    result_layers = []
    for ac in range(acc_max, -1, -1):
        subset = {k: v for k, v in score.items() if accept[k] == ac}
        stacked = sorted(subset.items(), key=lambda x: x[1])
        result_layers.append([x[0]+1 for x in stacked])

    def fancy_merge(layers):
        glue = lambda grp: reduce(lambda a,b : f"{a}={b}", map(str, grp))
        res = []
        for group in layers:
            tmp = [k for k, _ in groupby(sorted(group))]
            if not tmp: continue
            cur = []
            last = None
            for k in tmp:
                if last is not None and k == last[-1]:
                    last.append(k)
                else:
                    if last: cur.append(list(last))
                    last = [k]
            if last: cur.append(list(last))
            res.extend([glue(g) for g in cur])
        return ','.join(res)
    # flatten and group same score team numbers
    ans = ""
    flat_layers = []
    for group in result_layers:
        grouped = [list(map(str, [k for k,_ in g])) for _,g in groupby([(t,score[t]) for t in group], key=lambda x:x[1])]
        flat_layers.extend(['='.join(x) for x in grouped if x])
    ans = ','.join([str(x) for x in flat_layers if x])

    print(ans)