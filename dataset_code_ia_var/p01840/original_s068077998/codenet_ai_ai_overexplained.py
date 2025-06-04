# Lire la première ligne d'entrée utilisateur, la diviser selon les espaces, convertir chaque élément en entier,
# puis stocker les valeurs dans les variables N, M et T respectivement.
N, M, T = list(map(int, input().split()))

# Lire la deuxième ligne d'entrée utilisateur, la diviser selon les espaces,
# convertir chaque élément en entier et les stocker dans une liste 'a'.
a = list(map(int, input().split()))

# Créer une nouvelle liste 'b' qui commencera avec la première valeur de 'a'.
b = [a[0]]

# Boucle pour calculer les différences entre les éléments consécutifs dans la liste 'a'.
# On commence par l'indice 1 puisque la différence avec l'élément précédent est nécessaire.
for i in range(1, N):
    # Ajouter la différence entre l'élément courant de 'a' et l'élément précédent à la liste 'b'.
    b.append(a[i] - a[i-1])

# Après avoir bouclé sur tous les éléments, ajouter la différence entre la valeur 'T' et le dernier élément de 'a'.
# Cela complète la liste des intervalles entre les positions spécifiées.
b.append(T - a[N-1])

# Initialiser une variable 'ans' à 0 pour stocker la réponse finale.
ans = 0

# Calculer la première partie de la réponse.
# Soustraire la valeur de M de la première valeur de la liste 'b', puis ajouter le résultat à 'ans'.
ans += b[0] - M

# Boucle pour traiter tous les intervalles internes, c'est-à-dire du deuxième élément (indice 1) au dernier mais un.
for i in range(1, N):
    # Calculer la valeur b[i] - 2*M.
    # Si cette valeur est négative, la fonction max(0, b[i] - 2*M) prendra 0, sinon elle prendra la valeur positive.
    # Ajouter ce résultat à 'ans'.
    ans += max(0, b[i] - 2*M)

# Pour le dernier intervalle de la liste 'b', calculer b[N] - M.
# Si la valeur est négative, max(0, b[N] - M) prendra 0, sinon la valeur elle-même.
# Ajouter ce résultat à 'ans'.
ans += max(0, b[N] - M)

# Afficher la valeur finale de 'ans' sur la sortie standard.
print(ans)