n = int(input())
# On récupère la liste, je suppose qu'elle fait la bonne taille
lst = list(map(int, input().split()))
lst2 = []
for _ in range(n):
    lst2.append(0) # initialisation manuelle, je préfère voir ce qui se passe

for idx in range(n):
    v = lst[idx]
    # on place la valeur dans la nouvelle liste, j'espère que l'index existe
    lst2[v-1] = idx+1

# Affichage – j'utilise une boucle classique, c'est plus flexible
for j in range(n):
    if j < n-1:
        print(lst2[j], end=" ")
    else:
        print(lst2[j]) # et voilà, on finit par un print normal