# Création d'une liste nommée 'li' qui contiendra 4 éléments entiers saisis par l'utilisateur.
# La liste est générée à l'aide d'une liste en compréhension, ce qui permet de construire la liste de manière concise.

li = [
    int(      # On convertit la valeur d'entrée en entier à l'aide de la fonction int(), car input() retourne une chaîne de caractères.
        input()      # On lit une ligne de texte saisie par l'utilisateur via la fonction input().
        .rstrip()    # On retire les éventuels caractères de fin de ligne ou espaces inutiles grâce à la méthode rstrip().
    )
    for x in range(4)  # Cette boucle for sera exécutée 4 fois grâce à range(4), donc pour x valant 0, 1, 2, puis 3.
    # La variable x n'est pas utilisée dans la boucle, elle sert juste à répéter l'opération ci-dessus 4 fois.
]

# Maintenant, on veut afficher la plus petite somme possible prise parmi certaines combinaisons de deux éléments de la liste.
# On utilise la fonction min() pour trouver la valeur minimale parmi quelques sommes spécifiques.
# Voici les sommes considérées :
# - li[0] + li[2] : on additionne le premier élément de la liste (index 0) avec le troisième élément (index 2),
# - li[0] + li[3] : on additionne le premier élément (index 0) avec le quatrième élément (index 3),
# - li[1] + li[2] : on additionne le deuxième élément (index 1) avec le troisième élément (index 2),
# - li[1] + li[3] : on additionne le deuxième élément (index 1) avec le quatrième élément (index 3).
# Cela donne toutes les combinaisons possibles où on prend soit li[0] ou li[1] et on additionne à li[2] ou li[3].
# On passe ces quatre sommes comme arguments à min(), qui retournera la plus petite valeur parmi elles.
# Enfin, on utilise la fonction print() pour afficher ce résultat minimal à l'utilisateur.

print(
    min(
        li[0] + li[2],  # Somme du premier et du troisième élément.
        li[0] + li[3],  # Somme du premier et du quatrième élément.
        li[1] + li[2],  # Somme du deuxième et du troisième élément.
        li[1] + li[3]   # Somme du deuxième et du quatrième élément.
    )
)