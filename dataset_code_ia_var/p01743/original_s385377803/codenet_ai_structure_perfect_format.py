N = int(input())
A = [int(input()) for i in range(N)]
INF = 10 ** 18
N2 = 2 ** N

def dfs(i, D):
    if i == N:
        return sum(D)
    b = 1 << i
    a = A[i]
    def sel(j, state, u):
        if j == N2:
            D2 = D[:]
            for e in u:
                D2[e] -= 1
                D2[e | b] += 1
            D2[b] = a - len(u)
            return dfs(i + 1, D2)
        r = sel(j + 1, state, u)
        if D[j] > 0 and (state & j == 0) and len(u) < a:
            u.append(j)
            r = min(r, sel(j + 1, state | j, u))
            u.pop()
        return r
    return sel(0, 0, [])

print(dfs(0, [0] * N2))