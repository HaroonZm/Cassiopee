# Demande à l'utilisateur de saisir une ligne sur l'entrée standard (habituellement le clavier).
# La fonction 'input()' lit cette ligne en tant que chaîne de caractères (string).
# 'split()' sépare cette chaîne en une liste de sous-chaînes, ici en utilisant l'espace comme séparateur par défaut.
# Par exemple, si l'utilisateur saisit "8 3", alors input().split() devient ['8', '3'].
# La fonction 'map(int, ...)' applique la fonction 'int' à chaque élément de la liste
# résultant en des entiers : map(int, ['8', '3']) donne un itérable équivalent à [8, 3].
# L'affectation multiple 'a, b = ...' permet d'attribuer respectivement le premier élément à 'a' et le second à 'b'.
a, b = map(int, input().split())

# On calcule la valeur de la variable 'gap', qui correspond à la différence entre
# 'a' et deux fois la valeur de 'b'. Cela s'écrit : gap = a - 2 * b.
gap = a - 2 * b

# La structure conditionnelle 'if' permet d'exécuter un bloc de code si une condition est vérifiée.
# Ici, on teste si 'gap' est strictement supérieur à 0.
if gap > 0:
    # Si la condition précédente est vraie, on affiche la valeur de 'gap' avec la fonction 'print'.
    print(gap)
else:
    # Si la condition précédente est fausse (gap <= 0), l'instruction après 'else' s'exécute.
    # On affiche alors la valeur 0.
    print(0)