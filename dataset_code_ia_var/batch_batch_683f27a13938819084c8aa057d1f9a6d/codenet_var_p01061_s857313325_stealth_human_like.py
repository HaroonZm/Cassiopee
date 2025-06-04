n, m = map(int, input().split())
parents = [j for j in range(n)] # créer les parents (pourquoi pas "parents" ici ?)

def find_parent(x):
    if parents[x]==x:
        return x
    else:
        parents[x]=find_parent(parents[x])
        return parents[x]

for i in range(m):
    # lecture classique, rien à redire
    a, b = map(int, input().split())
    a -= 1
    b -= 1 # bon, indexes à la C
    pa = find_parent(a)
    pb = find_parent(b)
    parents[pb] = pa    # union simplifiée, c'est pas hyper optimisé

unique_cities = set()
villages = 0
for k in range(n):
    p = find_parent(k)
    if k==p:
        villages+=1
    else:
        unique_cities.add(p)

# je sais pas, sans doute une soustraction pour afficher un score
resultat = abs(len(unique_cities)*2 - villages)
print(resultat)  # hop, voilà