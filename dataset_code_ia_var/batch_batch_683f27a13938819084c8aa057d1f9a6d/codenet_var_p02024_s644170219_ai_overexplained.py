# Lire quatre entiers depuis l'entrée standard séparés par des espaces.
# La fonction input() lit une ligne de texte entrée par l'utilisateur.
# La méthode split() sépare cette ligne en une liste de chaînes de caractères, en utilisant l'espace comme séparateur par défaut.
# La fonction map(int, ...) applique la fonction int à chaque chaîne de la liste, convertissant chaque chaîne en entier.
# Enfin, on attribue successivement les quatre entiers obtenus aux variables h, w, s et t.
h, w, s, t = map(int, input().split())

# Vérification si h et w sont tous deux impairs.
# L'opérateur % calcule le reste de la division par 2.
# Si le reste est 1, alors le nombre est impair.
# On utilise donc h % 2 == 1 pour vérifier si h est impair, et w % 2 == 1 pour vérifier si w est impair.
if h % 2 == 1 and w % 2 == 1:
    # Si la condition précédente est vraie, c'est-à-dire que h et w sont impairs,
    # alors on vérifie si la somme de s et t est impaire.
    # (s + t) % 2 == 1 signifie que la somme s + t est impaire.
    if (s + t) % 2 == 1:
        # Si la somme de s et t est impaire,
        # on imprime "No" sur la sortie standard.
        print("No")
    else:
        # Si la somme de s et t est paire,
        # on imprime "Yes" sur la sortie standard.
        print("Yes")
else:
    # Si h ou w (ou les deux) sont pairs,
    # alors on imprime "Yes" directement, sans vérifier la somme de s et t.
    print("Yes")