# Démarre une boucle infinie qui ne s'arrête jamais sauf si une instruction "break" est rencontrée.
while True:
    # Demande à l'utilisateur d'entrer une ligne de texte depuis la console et la stocke dans la variable 's'.
    s = input()  # 'input()' lit la saisie utilisateur et retourne une chaîne de caractères.

    # Vérifie si la chaîne saisie est exactement "END OF INPUT".
    if s == "END OF INPUT":
        # Si c'est le cas, on quitte la boucle avec 'break'.
        break

    # Ajoute un espace à la fin de la chaîne.
    # Cela garantit que le dernier mot sera pris en compte lors de la séparation par espaces dans la suite du programme.
    s += " "

    # Initialise un compteur 'c' à 0. Ce compteur servira pour compter le nombre de caractères dans chaque mot.
    c = 0

    # Commence une boucle qui va de 0 jusqu'à la longueur de la chaîne 's' (non incluse).
    # 'range(len(s))' crée une séquence de tous les indices valides pour accéder aux caractères de 's'.
    for i in range(len(s)):
        # Vérifie si le caractère actuel 's[i]' est un espace.
        if s[i] == ' ':
            # Si c'est un espace, cela signifie qu'un mot vient de se terminer.
            # On affiche la valeur actuelle de 'c', c'est-à-dire la longueur du mot précédent, sans ajouter de saut de ligne à la fin.
            print(c, end="")

            # Réinitialise le compteur 'c' à 0 pour commencer à compter la longueur du prochain mot.
            c = 0

            # Utilise 'continue' pour passer immédiatement à l'itération suivante de la boucle,
            # sans exécuter le reste des instructions dans cette itération.
            continue

        # Si le caractère actuel n'est pas un espace, cela signifie qu'il fait partie d'un mot.
        # On incrémente le compteur 'c' de 1 pour compter ce caractère.
        c += 1

    # Après avoir traité tous les caractères de la chaîne (c'est-à-dire après la fin de la boucle for),
    # on affiche un saut de ligne afin que la prochaine ligne de sortie commence sur une nouvelle ligne.
    print("")