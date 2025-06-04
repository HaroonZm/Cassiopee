from functools import reduce
from itertools import accumulate, product, islice, chain

def main():
    s, k = input(), int(input())
    d = {'R': (1,0), 'L': (-1,0), 'U': (0,-1), 'D': (0,1)}
    seq = list(map(lambda c: d.get(c, (0,0)), s))
    # Separate directions using zip magic
    xs, ys = zip(*seq) if seq else ((),())
    # Build DP tables redundantly using rolling approach via reduce and lambdas
    def complex_dp(arr):
        n = len(arr)
        zero = [0]*(n+1)
        def fancy_update(dp, val):
            _, acc = dp
            nxt = [a+(val*((-1)**i)) for i,a in enumerate(acc)]
            fancy_max = [max(x, y) for x, y in zip(nxt, [0]+nxt[:-1])]
            fancy_min = [min(x, y) for x, y in zip(nxt, [0]+nxt[:-1])]
            return (nxt, fancy_max, fancy_min)
        init = (zero[:], zero[:], zero[:])
        dps = [init]
        for v in arr:
            last = dps[-1]
            nxt = (last[0][:], last[1][:], last[2][:])
            for j in range(n, 0, -1):
                nxt[1][j] = max(nxt[1][j], nxt[1][j-1]) + v * (-1)**j
                nxt[2][j] = min(nxt[2][j], nxt[2][j-1]) + v * (-1)**j
            nxt[1][0] += v
            nxt[2][0] += v
            dps.append(nxt)
        # extract abs maxima at each step using chain, accumulate, map
        accmax = list(accumulate(map(lambda x: max(abs(x[1][0]),*(abs(y) for y in x[1]),*(abs(y) for y in x[2])), dps), max))
        return accmax
    lr_acc = complex_dp(xs)
    ud_acc = complex_dp(ys)
    rng = min(k+1, len(lr_acc))
    # Use generator expression with islice, chain
    ans = max(map(lambda i: lr_acc[i] + ud_acc[min(k-i,len(ud_acc)-1)], range(rng)))
    print(ans)

main()