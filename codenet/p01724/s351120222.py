def main():
    N = 20; M = 15
    MP = [[-1]*M for i in range(N)]
    L = 0
    for i in range(N-1):
        s = input()
        for j in range(M):
            c = s[j]
            if c == 'O':
                sx = j; sy = i
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
        if y >= N-2:
            return 0
        r = INF
        for dx, dy in dd:
            nx = x + dx; ny = y + dy
            if not 0 <= nx < M or not 0 <= ny < N:
                continue
            k = MP[ny][nx]
            if k == -1 or state & (1 << k) == 0:
                continue
            n_state = state ^ (1 << k)
            nx += dx; ny += dy
            while 0 <= nx < M and 0 <= ny < N:
                k = MP[ny][nx]
                if k == -1 or state & (1 << k) == 0:
                    break
                n_state ^= (1 << k)
                nx += dx; ny += dy
            else:
                if (nx == -1 or nx == M) and ny == N-1:
                    return 1
                continue
            r = min(r, dfs(n_state, nx, ny) + 1)
        D[key] = r
        return D[key]
    r = dfs(2**L-1, sx, sy)
    print(r if r < INF else -1)
main()