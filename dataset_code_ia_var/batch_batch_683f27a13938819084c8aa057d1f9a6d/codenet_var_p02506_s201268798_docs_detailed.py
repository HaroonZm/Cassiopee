def count_word_occurrences():
    """
    Demande à l'utilisateur un mot à rechercher, puis lit des lignes de texte depuis l'entrée standard.
    Compte et affiche le nombre d'occurrences du mot spécifié (insensible à la casse) jusqu'à ce que 'END_OF_TEXT' soit rencontré en début de ligne.

    Entrée :
        - La première ligne : le mot à rechercher (insensible à la casse)
        - Les lignes suivantes : du texte à analyser ; le mot END_OF_TEXT seul sur une ligne termine la saisie

    Sortie :
        - Un entier affiché à l'écran, représentant le nombre d'occurrences du mot recherché parmi toutes les lignes lues (comparaison sans tenir compte de la casse)
    """
    cou = 0  # Compteur pour le nombre d'occurrences du mot recherché
    i = input().lower()  # Lecture du mot à rechercher et conversion en minuscules

    while True:
        # Lecture d'une ligne de texte, découpée en mots
        j = input().split()

        # Si le premier mot de la ligne est 'END_OF_TEXT', la boucle s'arrête
        if j[0] == "END_OF_TEXT":
            break

        # Conversion de tous les mots de la ligne en minuscules pour comparaison insensible à la casse
        k = [x.lower() for x in j]

        # Incrémentation du compteur par le nombre de fois où le mot recherché apparaît dans cette ligne
        cou += k.count(i)

    # Affichage du résultat final : nombre total d'occurrences trouvées
    print(cou)

# Appel de la fonction principale pour lancer le programme
count_word_occurrences()