# Demande à l'utilisateur de saisir deux nombres séparés par un espace sur une seule ligne.
# L'entrée utilisateur est une chaîne de caractères, comme "3 2".
user_input = input()

# La fonction split() divise la chaîne à chaque espace vide et renvoie une liste de chaînes.
# Ex: si user_input == "3 2", alors user_input.split() == ["3", "2"].
splitted_input = user_input.split()

# La fonction map(int, ...) applique la fonction int() à chaque élément de la liste,
# ce qui signifie que chaque chaîne devient un nombre entier.
# list(...) transforme le résultat en une liste de deux entiers.
# Si splitted_input == ["3", "2"], alors map(int, splitted_input) --> [3, 2].
# On affecte ces deux valeurs à N et M grâce au dépaquetage.
N, M = list(map(int, splitted_input))

# On calcule le temps d'exécution initial avec la formule : 1900 * M + 100 * (N - M).
# 1900 représente le "coût" d'une opération "difficile" exécutée M fois.
# (N-M) représente le nombre d'opérations "faciles", chacune coûtant 100 unités de temps.
# Si N == 3 et M == 2, on obtient 1900*2 + 100*(3-2) = 3800 + 100*1 = 3900.
exe_time = 1900 * M + 100 * (N - M)

# Comme il y a de la probabilité de succès à la 2^M-ème tentative en moyenne,
# on multiplie le temps par 2^M pour prendre en compte toutes les possibilités.
# pow(2, M) est équivalent à 2**M, cela signifie 2 multiplié par lui-même M fois.
# Par exemple, si M=3, alors pow(2, M) == 8.
exe_time_exp = exe_time * pow(2, M)

# On affiche le résultat final à l'utilisateur.
# print() permet d'afficher l'information à l'écran.
print(exe_time_exp)