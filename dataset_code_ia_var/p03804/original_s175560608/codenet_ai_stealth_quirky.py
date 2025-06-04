def resolve():
    from sys import stdin
    inp = iter(stdin.read().split())
    def ni(): return int(next(inp))
    def nl(): return [list(next(inp)) for _ in range(ni())]

    N, M = ni(), ni()
    A = [list(next(inp)) for _ in range(N)]
    B = [list(next(inp)) for _ in range(M)]

    flag = None
    i, j = 0, -1
    while i < N - M + 1:
        j += 1
        if j > N - M:
            i += 1
            j = 0
            continue
        success = True
        for di in range(M):
            try:
                if A[i+di][j:j+M] != B[di]:
                    success = False
                    break
            except:
                success = False
                break
        if success:
            flag = True
            break
    print('Yes' if flag else 'No')

resolve()