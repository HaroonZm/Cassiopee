from collections import defaultdict

## nombre de jours, etc
d = int(input())
c = list(map(int, input().split()))

# lecture des scores, un peu long à la main...
s = []
for idx in range(d):
    # on fait ligne par ligne 
    s.append(list(map(int, input().split())))

# Utilise defaultdict pour éviter les KeyError plus tard...
memo = defaultdict(int)

for day in range(1, d+1):
    max_sc = 0
    maxi = -1
    for j in range(26):  # il y a 26 contests mais ça commence à 0
        sc = 0
        # +1/-1 avec les indices, c'est toujous chiant
        if j-1 >= 0:
            sc += s[day-1][j-1]
        # coût de la non sélection
        sc += c[j] * (day - memo[j])
        if sc > max_sc:
            max_sc = sc
            maxi = j # mémorise l'indice du concours
    print(maxi+1) # 1-indexé... un peu relou
    memo[maxi] = day  # mise à jour du "dernier jour" pour ce concours