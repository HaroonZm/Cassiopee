# Utilisation d'une fonction intégrée Python appelée 'print' pour afficher des résultats à l'écran.
# Ici, nous allons afficher le résultat de la somme d'une liste de nombres entiers.

# La fonction 'sum' est une fonction intégrée qui calcule la somme de tous les éléments d'un itérable (comme une liste).
print(
    # Appel de la fonction 'sum' sur une liste générée par compréhension.
    sum(
        # Création d'une liste grâce à une compréhension de liste.
        # Une compréhension de liste est une syntaxe compacte pour créer des listes en une seule ligne.
        [   
            # Pour chaque itération, nous appelons la fonction 'input()' qui attend que l'utilisateur entre une donnée au clavier.
            # L'entrée reçue est à l'origine une chaîne de caractères (string).
            # On convertit cette chaîne en un entier grâce à la fonction 'int()' afin de pouvoir effectuer des opérations numériques.
            int(input())
            # La variable 'i' est une variable de boucle qui prend les valeurs successives données par la fonction 'range(10)'.
            # 'range(10)' génère une séquence de nombres allant de 0 à 9 inclusivement, ce qui signifie que la boucle va s'exécuter 10 fois.
            for i in range(10)
        ]
    )
)