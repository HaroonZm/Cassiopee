# La fonction print affiche à l'écran ce qui est passé en argument.
# Ici, on va afficher le résultat d'une somme.

# sum() est une fonction intégrée de Python qui calcule la somme des éléments d'une liste ou d'un autre itérable.

# [input() for i in xrange(10)] est une liste générée par une compréhension de liste.
# Décomposons-la :
# - input() demande à l'utilisateur de saisir une valeur au clavier et renvoie cette valeur sous forme de chaîne de caractères.
# - xrange(10) est une fonction qui génère une séquence de nombres de 0 à 9 (10 nombres au total), utile pour les boucles.
# - La compréhension de liste répète donc 10 fois l'appel à input(), stockant chaque saisie dans une liste.

# Cependant, input() renvoie une chaîne de caractères. Pour sommer des valeurs numériques, il faudrait convertir ces entrées en nombres (int ou float).
# Dans ce code, tel quel, cela produira une erreur si on essaie de sommer des chaînes.
# Mais dans Python 2, input() évalue l'entrée de l'utilisateur comme une expression Python, donc si l'utilisateur saisit des nombres, ils seront traités comme int ou float.

# Finalement, la somme des 10 valeurs saisies est calculée et affichée.

print sum([input() for i in xrange(10)])