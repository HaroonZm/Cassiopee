# Boucle infinie : la condition 'while 1' signifie que la boucle va tourner indéfiniment,
# car '1' est toujours évalué comme 'True' en Python.
while 1:
    # Demande à l'utilisateur d'entrer une chaîne de caractères,
    # en utilisant la fonction 'input()', qui lit la saisie clavier
    # et retourne la chaîne saisie sans le saut de ligne final.
    a = input()

    # Condition pour vérifier si la chaîne entrée est exactement "END OF INPUT"
    # Les guillemets délimitent une chaîne littérale à comparer avec l'entrée utilisateur.
    if a == "END OF INPUT":
        # Si la condition précédente est vraie, on quitte la boucle 'while'
        # en utilisant l'instruction 'break', ce qui arrête l'exécution
        # de la boucle la plus proche.
        break
    else:
        # Sinon (si l'entrée n'est pas "END OF INPUT"), on exécute le bloc suivant.
        # Initialisation de la variable 'c' à 0. Cette variable servira à compter,
        # pour chaque mot, le nombre de caractères qui le composent.
        c = 0
        # Boucle 'for' qui itère sur chaque caractère 'i' de la chaîne 'a'.
        for i in a:
            # Condition qui vérifie si le caractère courant 'i' est un espace (caractère ' ').
            if i == ' ':
                # Si le caractère courant est un espace, cela signifie la fin d'un mot.
                # On affiche donc le nombre de caractères 'c' accumulé jusque-là,
                # sans saut de ligne final grâce à 'end=""' dans 'print'.
                print(c, end = "")
                # Après avoir affiché la longueur du mot, on réinitialise le compteur 'c' à 0
                # pour commencer à compter le mot suivant.
                c = 0
            else:
                # Si le caractère courant n'est pas un espace,
                # cela signifie qu'il fait partie d'un mot.
                # On incrémente alors le compteur 'c' de 1 pour compter ce caractère.
                c += 1
        # Après la fin de la boucle sur la chaîne 'a', il reste un mot dont la longueur
        # est stockée dans 'c' (le dernier mot de la ligne, qui n'est pas suivi d'un espace).
        # On l'affiche, cette fois-ci avec un retour à la ligne par défaut,
        # car la fonction 'print' sans paramètre 'end' ajoute un saut de ligne.
        print(c)