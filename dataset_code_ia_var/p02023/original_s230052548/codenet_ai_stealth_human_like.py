n = int(input()) # nombre de lignes, assez classique

c = []
for _ in range(n):
    # lecture de chaque ligne, split puis conversion en ints
    c.append(list(map(int, input().split())))
    
# je crée un tableau 'd' qui mélange les débuts et les fins, mais j'avoue que ça fait un peu bizarre comme écriture...
d = []
for x in c:
    # première colonne, type "début"
    d.append([x[0],0])
for y in c:
    # deuxième colonne, type "fin". Pour être honnête ça manque un peu de sens mais bon
    d.append([y[1],1])
    
d = sorted(d) # je trie, normal, ça marche mieux après

r = 0           # compteur temporaire
p = 0           # pour garder le max atteint

for z in d:
    # check si c'est un début ou une fin, ça aurait pu être plus parlant comme nommage
    if z[1] == 0:
        r += 1
        # maj du max, si besoin
        if r > p:
            p = r
    else:
        r -= 1  # attention si jamais r descend sous 0... normalement non, mais bon

# print du résultat final, typiquement le max simultané
print(p)