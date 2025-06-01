def main():
    """
    Programme qui lit des paires d'entiers (m, n) depuis l'entrée standard,
    calcule m^n et affiche le résultat selon un format spécifique avec des unités japonaises
    si la valeur est suffisamment grande.

    Le programme s'arrête lorsque la somme de m et n est nulle (m + n == 0).
    """

    while True:
        # Lecture de deux entiers m et n séparés par un espace
        m, n = map(int, input().split())

        # Condition d'arrêt : si la somme de m et n est 0, on sort de la boucle
        if m + n == 0:
            break

        # Calcul de la puissance m^n
        result = m ** n

        # Si le résultat est inférieur à 10 000, on l'affiche directement
        if result < 10000:
            print(result)
            continue  # Passer à la prochaine itération

        # Conversion du résultat en chaîne de caractères pour traitement par groupe de 4 chiffres
        s = str(result)

        # Ajout de zéros en tête pour que la longueur de la chaîne soit un multiple de 4
        while len(s) % 4 > 0:
            s = "0" + s

        # Liste des unités correspondant aux puissances de 10^4 japonaise
        # L'index 0 est vide car les 4 derniers chiffres n'ont pas d'unité assignée
        units = [
            "",       # 10^0
            "Man",    # 10^4
            "Oku",    # 10^8
            "Cho",    # 10^12
            "Kei",    # 10^16
            "Gai",    # 10^20
            "Jo",     # 10^24
            "Jou",    # 10^28
            "Ko",     # 10^32
            "Kan",    # 10^36
            "Sei",    # 10^40
            "Sai",    # 10^44
            "Gok",    # 10^48
            "Ggs",    # 10^52
            "Asg",    # 10^56
            "Nyt",    # 10^60
            "Fks",    # 10^64
            "Mts"     # 10^68
        ]

        # Parcours de la chaîne par blocs de 4 caractères, correspondants à 4 chiffres
        for i in range(0, len(s), 4):
            # Extraction d'un bloc de 4 chiffres converti en entier
            x = int(s[i:i + 4])

            # Si le bloc est 0, on ne l'affiche pas car il n'apporte pas d'information
            if x == 0:
                continue

            # Calcul de l'indice de l'unité correspondant au groupe de chiffres
            # (len(s) - i) // 4 donne le numéro du groupe en partant de la gauche
            unit_index = (len(s) - i) // 4 - 1

            # Affichage sans espace ni retour à la ligne, concaténation du chiffre et de l'unité
            print(str(x) + units[unit_index], end="")

        # Saut de ligne après avoir affiché toutes les parties du nombre
        print()

if __name__ == "__main__":
    main()