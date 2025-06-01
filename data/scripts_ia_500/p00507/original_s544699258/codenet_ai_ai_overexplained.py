import itertools  # Importation de la bibliothèque itertools, qui contient des fonctions créant des itérateurs efficaces et complexes

# Dans la ligne suivante, nous allons décomposer plusieurs opérations imbriquées dans une compréhension de liste,
# puis trier ces résultats et enfin extraire un élément spécifique.

# Étape 1: Exécution de int(input()) qui demande à l'utilisateur d'entrer un nombre,
# puis on utilise ce nombre pour répéter un certain nombre de fois une opération.
# Plus précisément, [0]*int(input()) crée une liste de zéros dont la longueur est égale à ce nombre entré.

# Étape 2: Pour chaque élément de cette liste (dont les valeurs sont toutes 0 mais ici on s'en fiche, on s'en sert juste pour répéter),
# on demande à nouveau un input, qu'on convertit en entier avec int(input()).
# Cela crée une liste d'entiers dont la longueur est égale au nombre entré lors de la première input.

# Étape 3: On trie cette liste d'entiers grâce à sorted(...), ce qui organise les éléments du plus petit au plus grand.

# Étape 4: On prend les 4 premiers éléments de cette liste triée avec [:4].
# Cela signifie qu'on ne prendra qu'au maximum les 4 éléments les plus petits parmi ceux entrés.

# Étape 5: On utilise itertools.permutations(..., 2) pour générer toutes les permutations possibles de longueur 2
# (c'est-à-dire des paires ordonnées) parmi ces 4 éléments.
# Par exemple, si les 4 éléments sont [1,2,3,4], permutations de 2 seront toutes les combinaisons possibles sans répétition
# d'ordre des éléments : (1,2), (1,3), (1,4), (2,1), etc.

# Étape 6: Pour chaque paire (c,d) générée par permutations, on crée une chaîne de caractères f'{c}{d}',
# ce qui concatène les deux chiffres en une chaîne comme "12" si c=1 et d=2.
# Ensuite, on convertit cette chaîne en entier avec int(...), ce qui transforme "12" en nombre 12.

# Étape 7: On crée une liste de tous ces entiers résultants, puis on utilise sorted(...) pour trier cette liste en ordre croissant.

# Étape 8: Enfin, l'expression [2] à la fin sélectionne le troisième élément de cette liste triée (en raison de l'indexation qui 
# commence à 0).
# Cela signifie que parmi toutes ces permutations converties en nombres, on récupère le troisième plus petit.
 
print(sorted([int(f'{c}{d}') for c,d in itertools.permutations(sorted([int(input()) for _ in [0]*int(input())])[:4],2)])[2])