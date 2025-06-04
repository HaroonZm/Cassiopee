# Demande à l'utilisateur de saisir une entrée. Cette instruction n'utilise pas la valeur saisie,
# elle sert seulement à attendre une entrée de l'utilisateur, ce qui est parfois utilisé pour ignorer une première ligne.
input()

# Demande à l'utilisateur de saisir une ligne d'entrée, puis sépare cette ligne en morceaux là où il y a des espaces.
# Pour chaque morceau (qui est une chaîne de caractères représentant un nombre),
# convertit la chaîne en entier avec int(x). Utilise une liste en compréhension pour créer une liste 'A' composée de tous ces entiers.
A = [int(x) for x in input().split()]

# Même opération que précédemment, mais pour une deuxième liste appelée 'B'.
B = [int(x) for x in input().split()]

# Initialise une variable nommée 'ans' à 0. Cette variable servira à stocker la réponse finale qui sera affichée à la fin.
ans = 0

# Trie la liste 'A' dans l'ordre décroissant (du plus grand au plus petit).
# L'argument reverse=True indique d'inverser l'ordre normal du tri.
A.sort(reverse=True)

# Parcourt chaque élément 'a' de la liste 'A', en commençant donc par le plus grand grâce au tri précédent.
for a in A:
    # Trie la liste 'B' dans l'ordre décroissant également, avant chaque utilisation,
    # pour s'assurer que les plus grandes valeurs de B sont utilisées en premier.
    B.sort(reverse=True)
    # On souhaite diminuer les 'a' plus grandes valeurs dans 'B' (car B a été triée).
    # Utilise une boucle for avec la variable 'i' allant de 0 à a-1 pour accéder au 'a' premiers éléments de 'B'.
    for i in range(a):
        # Diminue de 1 la valeur de B à l'indice 'i' (donc l'une des plus grandes valeurs de B).
        B[i] -= 1
    # Après avoir décrémenté les éléments de 'B', vérifie si le plus petit élément de 'B' est maintenant négatif.
    if min(B) < 0:
        # Si un élément de 'B' est devenu négatif, cela signifie que l'opération n'est pas valide.
        # On met 'ans' à 0 si ce n'était pas déjà le cas.
        ans = 0
        # On quitte immédiatement la boucle en utilisant break, car la suite n'a plus d'intérêt.
        break

# Après avoir terminé toutes les opérations précédentes (et si aucun élément de B n'est devenu négatif),
# vérifie si le plus grand élément de 'B' est exactement égal à 0. Cela signifie donc que tous les éléments de B valent 0.
if max(B) == 0:
    # Si c'est le cas, alors on a réussi à réaliser exactement ce qu'on voulait (chaque valeur de B est devenue 0)
    # donc on met la réponse finale 'ans' à 1 pour indiquer le succès.
    ans = 1

# Affiche la valeur de 'ans', qui vaut 1 si l'opération a réussi, et 0 sinon.
print(ans)