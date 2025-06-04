# Utiliser la fonction input() pour lire une ligne entière depuis l'entrée standard (typiquement, le clavier de l'utilisateur).
# La méthode split() coupe la chaîne de caractères lue en sous-chaînes selon l'espace comme séparateur par défaut.
# Ensuite, map(int, ...) applique la fonction int à chaque élément résultant de split(), convertissant chaque sous-chaîne en un entier.
# Enfin, les deux valeurs entières sont simultanément affectées (assignées) aux variables A et B grâce à l'affectation multiple.
A, B = map(int, input().split())

# Vérifie si les deux valeurs A et B sont inférieures ou égales à 9 :
# max(A, B) retourne la valeur la plus grande entre A et B.
# On compare cette valeur maximale à 9 à l'aide de l'opérateur <= (inférieur ou égal).
# Si cette condition est vraie (c'est-à-dire que les deux valeurs sont ≤ 9), alors :
#   On calcule le produit de A et B (A * B).
# Sinon (au moins un des nombres est strictement supérieur à 9) :
#   On retourne -1 pour signaler une condition non acceptable selon l'énoncé.
# L'opérateur ternaire if ... else permet d'effectuer cette sélection en une ligne.
# Enfin, print(...) affiche le résultat à l'écran.
print(A * B if max(A, B) <= 9 else -1)