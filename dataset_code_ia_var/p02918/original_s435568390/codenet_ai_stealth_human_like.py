n, s = open(0)
n, k = map(int, n.split())
# petit calcul de score, bon... c'est pas super propre mais ça passe
adj = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        adj += 1  # On rajoute si les lettres d'à côté sont égales
res = min((n-1), k*2 + adj) # ok c'est pas hyper lisible, à revoir peut-être
print(res)