def max_value_after_operations():
    """
    Lit deux entiers 'n' et 'm' depuis l'entrée standard, puis lit 'n' lignes contenant chacune deux entiers.
    Pour chaque ligne, met à jour la valeur 'm' en ajoutant la différence entre le premier et le deuxième entier.
    Si à un moment 'm' devient négatif, affiche 0 et arrête l'exécution.
    Sinon, affiche la valeur maximale atteinte par 'm' au cours des mises à jour.

    Cela peut être interprété comme un suivi de score ou de ressource,
    vérifiant que la ressource ne devient jamais négative,
    et enregistrant la valeur la plus élevée obtenue.
    """
    # Lecture de l'entier n : le nombre de paires à lire
    n = int(input())
    # Lecture de l'entier m : la valeur initiale
    m = int(input())

    # Initialisation de 'sm' à la valeur initiale m pour garder la trace du maximum atteint
    sm = m
    # Initialisation d'une liste vide pour stocker les paires d'entiers
    C = []

    # Boucle de saisie des n lignes, chaque ligne contient deux entiers
    for _ in range(n):
        # Lire une ligne, la découper en entiers et les ajouter à la liste C
        C.append(list(map(int, input().split())))

    # Parcours de chaque paire dans la liste C
    for i in C:
        # Mise à jour de m en ajoutant la différence entre le premier et le deuxième élément
        m += i[0] - i[1]

        # Si m devient négatif, cela signifie une condition d'échec
        if m < 0:
            # Affiche 0 puis termine le programme immédiatement
            print(0)
            exit()

        # Met à jour sm si la nouvelle valeur de m est plus grande que l'actuel maximum
        sm = max(m, sm)

    # Si la boucle s'est terminée sans que m devienne négatif,
    # affiche la valeur maximale atteinte par m
    print(sm)


# Appel de la fonction principale pour exécuter le programme
max_value_after_operations()