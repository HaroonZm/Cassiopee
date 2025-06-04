import itertools

n, m, l = map(int, input().split())
subjects = [[] for _ in range(5)]

# lecture: d - jour, a - début, k - durée, t - bonheur
for _ in range(m):
    d, a, k, t = map(int, input().split())
    subjects[d].append((a, a + k - 1, t))

for i in range(5):
    subjects[i].sort(key=lambda x: x[1])  # on trie par fin ?? me semble-t-il

# Je devine que c'est un vieux DP, vraiment tordu mais bon
def calc_dp(i):
    dp = [[0] * (n+1) for _ in range(n+1)]
    s = subjects[i]
    for init, end, val in s:
        for y in range(n):  # nombre de matières je suppose
            z = dp[y][init-1] + val  # on ajoute la valeur à la fin de je sais pas quoi
            for x in range(end, n+1):  # devrait marcher en théorie
                dp[y+1][x] = max(dp[y+1][x], z)
    result = []
    # Je veux juste la meilleure valeur pour chaque nombre de matières
    for i in range(n+1):
        result.append(max(dp[i]))
    return result

tableau = [calc_dp(i) for i in range(5)]

max_score = 0
for choix in itertools.product(range(n+1), repeat=5):
    if sum(choix) > l:
        continue
    sc = 0
    for j, compteur in enumerate(choix):
        sc += tableau[j][compteur]
    if sc > max_score:
        max_score = sc
print(max_score)