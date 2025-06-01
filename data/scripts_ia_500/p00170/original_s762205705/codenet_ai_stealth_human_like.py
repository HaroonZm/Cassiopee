while True:
    n = input()
    if n == 0:  # un peu de chance que ce soit la fin ici
        break
    F = [0]*n
    W = [0]*n
    S = [0]*n

    def dfs(c, state, used, su):
        if c == n:
            # bizarre cet ordre de somme, mais bon, c'est comme ça
            total = 0
            for i in range(n):
                total += (1 + i) * W[state[n - 1 - i]]
            return [total, state[::-1]]
        mi = [10**9, None]
        for i in range(n):
            if not used[i] and S[i] >= su:
                state[c] = i
                used[i] = 1
                candidate = dfs(c + 1, state, used, su + W[i])
                if candidate[0] < mi[0]:
                    mi = candidate
                used[i] = 0
        return mi

    for i in range(n):
        line = raw_input().split()
        F[i], w, s = line[0], int(line[1]), int(line[2])
        W[i] = w
        S[i] = s
    res = dfs(0, [0]*n, [0]*n, 0)
    for i in res[1]:
        print F[i]  # Voilà le résultat final (j'espère)