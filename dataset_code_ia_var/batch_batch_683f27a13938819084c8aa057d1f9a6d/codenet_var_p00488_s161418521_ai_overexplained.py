# La fonction int() convertit une chaîne de caractères en un nombre entier.
# La fonction input() lit une ligne à partir de l'entrée standard (généralement le clavier) sous forme de chaîne de caractères.
# La construction "for _ in range(3)" permet de répéter une opération trois fois.
# Le caractère "_" est couramment utilisé comme variable temporaire lorsqu'on n'a pas besoin de sa valeur dans la boucle.
# Nous allons demander trois fois à l'utilisateur de saisir un nombre entier pour créer une séquence de trois entiers.
# La syntaxe "int(input()) for _ in range(3)" génère un générateur de trois entiers lus depuis l'entrée standard.
# La fonction min() appliquée à ce générateur va retourner le plus petit des trois entiers saisis par l'utilisateur.
# On répète un schéma similaire avec "range(2)" pour obtenir le plus petit de deux nouveaux entiers lus.
# Ensuite, on additionne les deux plus petits nombres obtenus (le minimum du premier groupe de trois et le minimum du second groupe de deux).
# À la somme ainsi obtenue, on soustrait 50.
# Enfin, le résultat final est affiché à l'écran à l'aide de la fonction print().

premiere_min = min(
    int(
        input()  # Demande à l'utilisateur de saisir un entier, convertit l'entrée en entier.
    )
    for _ in range(3)  # Répète cette opération 3 fois pour recueillir 3 entiers.
)
# Le résultat de ce min sera le plus petit des 3 premiers entiers saisis.

deuxieme_min = min(
    int(
        input()  # Demande à l'utilisateur de saisir un entier, convertit l'entrée en entier.
    )
    for _ in range(2)  # Répète cette opération 2 fois pour recueillir 2 entiers.
)
# Le résultat de ce min sera le plus petit des 2 derniers entiers saisis.

resultat = premiere_min + deuxieme_min  # Additionne les deux minimums obtenus.

resultat = resultat - 50  # Soustrait 50 au résultat de l'addition.

print(
    resultat  # Affiche le résultat final à l'écran.
)