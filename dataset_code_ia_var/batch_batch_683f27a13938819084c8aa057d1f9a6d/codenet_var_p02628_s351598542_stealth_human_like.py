# Bon, on commence par récupérer n et k (je suppose)
params = input().split()
n = int(params[0])
k = int(params[1])

# Ensuite on prend la liste des prix
prix = list(map(int, input().split()))

# un tri pour prendre les moins chers
prix = sorted(prix)

# initialise le total (ici j'utilise fruit comme dans le code original)
total = 0
for j in range(k):  # je suppose que k est toujours <= n
    total += prix[j] # on ajoute au total le prix du fruit

#print le total final, normalement ça marche
print(total)