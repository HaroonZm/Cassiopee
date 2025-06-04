def number_to_alphabet_string():
    """
    Lis un entier depuis l'entrée standard et le convertit en une chaîne composée de lettres minuscules,
    en suivant une logique similaire à celle du système de numérotation des colonnes Excel, mais avec des lettres minuscules.
    Par exemple, 1 -> 'a', 26 -> 'z', 27 -> 'aa', etc.
    Affiche le résultat.
    """
    # Lire l'entier depuis l'entrée utilisateur
    N = int(input("Entrez un entier : "))
    
    # Initialiser la chaîne de résultat vide
    S = ""
    
    # Boucle de conversion jusqu'à ce que N atteigne 0
    while N > 0:
        # Décrémenter N de 1 pour ajuster l'indexation de 1-26 à 0-25
        N -= 1

        # Trouver la lettre correspondant au chiffre le moins significatif
        # N % 26 donne un nombre entre 0 et 25. On ajoute ord('a') pour obtenir le code ASCII
        # correspondant à la lettre minuscule appropriée, puis on convertit en caractère.
        S += chr(ord('a') + N % 26)

        # Réduire N pour traiter le prochain chiffre/le reste
        N //= 26

    # À la fin, S contient les lettres dans l'ordre inverse
    # On inverse S pour obtenir la chaîne correcte et on l'affiche
    print(S[::-1])