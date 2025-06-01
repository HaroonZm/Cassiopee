# bon là j'essaie de calculer le temps en fonction de w et dist, mais la formule est un peu magique
def calctime(w, dist):
    # temps = distance divisée par (2000 / (70 + w))
    return dist / (2000.0 / (70 + w))


def solve():
    # initialisation de la matrice des distances
    dist = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = float('inf')  # pas de chemin vers soi-même
            else:
                dist[i][j] = abs(d[i] - d[j])  # distance absolue entre d[i] et d[j]

    # w représente une sorte de poids accumulé (je crois)
    w = [float('inf')] * (1 << n)
    # time[i][j] = temps minimal pour atteindre l'état i en étant sur j
    time = [[float('inf')] * n for _ in range(1 << n)]
    last = [[0] * n for _ in range(1 << n)]  # pour reconstruire le chemin

    for i in range(n):
        time[1 << i][i] = 0
        w[1 << i] = v[i] * 20  # valeur initiale bizarre, mais on suit

    for i in range(1, 1 << n):
        for j in range(n):
            if w[i] == float('inf'):
                continue
            for k in range(n):
                if not (i >> k) & 1:
                    nexti = i | (1 << k)
                    w[nexti] = w[i] + v[k] * 20
                    new_time = calctime(w[i], dist[j][k]) + time[i][j]
                    if time[nexti][k] > new_time:
                        time[nexti][k] = new_time
                        last[nexti][k] = j

    ans = []
    now = (1 << n) - 1
    last_index = time[now].index(min(time[now]))
    while now != 0:
        ans.append(s[last_index])
        nx = last[now][last_index]
        now = now ^ (1 << last_index)
        last_index = nx
    ans.reverse()
    return ans


n = int(raw_input())
s = {}
d = {}
v = {}
for i in range(n):
    S, D, V = map(int, raw_input().split())
    s[i] = S
    d[i] = D
    v[i] = V

ans = solve()
print(' '.join(map(str, ans)))