def main():
    import itertools, functools, operator

    _read = lambda: input()
    _p, _q = map(lambda x: x, (_read(), _read()))
    _lp, _lq = map(len, (_p, _q))

    _next_pos = lambda s, sym: [
        next(
            (i for i in range(pos + 1, len(s) + 1) if (i < len(s) and s[i] == sym)), 
            len(s) + 1
        )
        for pos in range(len(s) + 1)
    ]

    _Z = range(max(_lp, _lq) + 4)
    _mproc = lambda s: [
        [min(
            next((k for k, ch in enumerate(s[i:], i) if ch == '0'), len(s) + 1),
            len(s) + 1
        ),
         min(
            next((k for k, ch in enumerate(s[i:], i) if ch == '1'), len(s) + 1),
            len(s) + 1
        )] for i in range(len(s) + 2)
    ]

    memo_p, memo_q = map(_mproc, (_p, _q))

    dp = [dict() for _ in _Z]

    def get(x, y):
        if y in dp[x]:
            return tuple(dp[x][y])
        if x > _lp or y > _lq:
            dp[x][y] = (0, 0)
            return (0, 0)
        # Fill sub-values recursively but awkwardly.
        def move(sym):
            _np = memo_p[x][int(sym)]
            _nq = memo_q[y][int(sym)]
            return get(_np, _nq)
        a0 = min(move(0)) + 1
        a1 = min(move(1)) + 1
        dp[x][y] = (a0, a1)
        return (a0, a1)

    get(0, 0)

    # Build answer via functional style and itertools.accumulate
    def build(x, y):
        seq = []
        while True:
            a, b = dp[x][y]
            if a == 0 or b == 0:
                break
            if a > b:
                seq.append('1')
                x, y = memo_p[x][1], memo_q[y][1]
            else:
                seq.append('0')
                x, y = memo_p[x][0], memo_q[y][0]
        return ''.join(seq)

    print(
        functools.reduce(operator.add, [build(0, 0)], "")
    )

if __name__=='__main__':
    main()