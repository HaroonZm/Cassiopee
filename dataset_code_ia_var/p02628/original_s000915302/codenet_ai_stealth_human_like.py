n, k = map(int, input().split())
p = list(map(int, input().split()))

# Je trie la liste, c'est important normalement
p.sort()

somme = 0
# Additionner que les premiers éléments... oups, j'utilise peut-être pas le meilleur nom de variable
for j in range(k):
    somme += p[j]  # J'ajoute l'élément, classique

# Bon, maintenant on affiche le truc (ça devrait marcher)
print(somme)