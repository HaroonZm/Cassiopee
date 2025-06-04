def main():
    N = 20
    M = 15
    MP = [[-1] * M for _ in range(N)]
    L = 0
    for i in range(N - 1):
        s = input()
        for j in range(M):
            c = s[j]
            if c == 'O':
                sx = j
                sy = i
            elif c == 'X':
                MP[i][j] = L
                L += 1

    dd = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))

    INF = 30
    D = {}

    def dfs(state, x, y):
        key = (state, x, y)
        if key in D:
            return D[key]
        if y >= N - 2:
            return 0
        r = INF
        for dx, dy in dd:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < M and 0 <= ny < N):
                continue
            k = MP[ny][nx]
            if k == -1 or (state & (1 << k)) == 0:
                continue
            n_state = state ^ (1 << k)
            tx = nx + dx
            ty = ny + dy
            tmp_state = n_state
            while 0 <= tx < M and 0 <= ty < N:
                kk = MP[ty][tx]
                if kk == -1 or (state & (1 << kk)) == 0:
                    break
                tmp_state ^= (1 << kk)
                tx += dx
                ty += dy
            else:
                if (tx == -1 or tx == M) and ty == N - 1:
                    return 1
                continue
            r = min(r, dfs(tmp_state, tx, ty) + 1)
        D[key] = r
        return r

    r = dfs((1 << L) - 1, sx, sy)
    print(r if r < INF else -1)

main()