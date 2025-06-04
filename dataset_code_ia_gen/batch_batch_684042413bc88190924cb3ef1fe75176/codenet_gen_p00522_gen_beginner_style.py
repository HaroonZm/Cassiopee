M,N = map(int, input().split())
P = [int(input()) for _ in range(M)]
C = []
E = []
for _ in range(N):
    c, e = map(int, input().split())
    C.append(c)
    E.append(e)

# trier les prix des manjuu decroissants
P.sort(reverse=True)

max_profit = 0
# essayer toutes les combinaisons possibles de boîtes
# comme N peut aller jusqu'à 500, on ne va pas faire de vrai combinatoire complète (2^N)
# juste une approche simple : essayer chaque boîte individuellement et prendre la meilleure

for j in range(N):
    c = C[j]
    e = E[j]
    # prendre les c manjuus les plus chers
    if c > M:
        c = M
    total_price = sum(P[:c])
    profit = total_price - e
    if profit > max_profit:
        max_profit = profit

# aussi essayer de combiner deux boites, de manière simple et non optimale
# essayer toutes paires de boites
# c'est un simple O(N^2) qui est acceptable pour N=500

for j1 in range(N):
    for j2 in range(j1+1, N):
        c1, e1 = C[j1], E[j1]
        c2, e2 = C[j2], E[j2]

        # prendre c1+c2 manjuus les plus chers
        if c1 + c2 > M:
            continue

        # pour simplicité on répartit c1 + c2 manjuus en 2 groupes:
        # on prend les c1 plus chers dans les c1+c2 manjuus pour la boite 1
        # et les c2 suivants pour la boite 2
        
        total_price_1 = sum(P[:c1])
        total_price_2 = sum(P[c1:c1+c2])
        total_price = total_price_1 + total_price_2
        profit = total_price - (e1 + e2)
        if profit > max_profit:
            max_profit = profit

print(max_profit)