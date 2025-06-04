# Alors, j'ai un peu retouché ça pour que ça ait l'air plus humain...
res = []
howmany = 0
while True:
    temp = input()
    split_temp = temp.split()
    n = int(split_temp[0]); m = int(split_temp[1])
    if n == 0 and m == 0:
        break

    # Je récupère les nombres ici, espérons qu'ils soient bons ;)
    ar = input().split()
    values = []
    for x in range(n):
        values.append(int(ar[x])) # classique

    pair = []
    for z in range(n):
        pair.append([0]*n)
    for i in range(n):
        for j in range(i+1,n):
            pair[i][j] = values[i]+values[j]

    top = 0
    for a_ in range(n):
        for b_ in range(a_+1, n):
            if pair[a_][b_] > m:
                continue
            if top < pair[a_][b_]:
                top = pair[a_][b_]
    # Bon, si aucune somme trouvée...
    if top==0:
        res.append(-1)
    else:
        res.append(top)
    howmany += 1

for c in range(howmany):
    if res[c] == -1:
        print("NONE")
    else:
        print(res[c])