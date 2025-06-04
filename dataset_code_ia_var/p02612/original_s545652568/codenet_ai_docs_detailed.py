def compute_result():
    """
    Lit une entrée utilisateur et traite les trois derniers caractères comme un nombre.
    Si les trois derniers caractères sont '000', retourne 0.
    Sinon, retourne 1000 moins la valeur entière de ces trois caractères.
    Affiche le résultat final.
    """
    # Prend une entrée utilisateur, convertit en chaîne de caractères et extrait les 3 derniers caractères
    user_input = input()
    last_three = user_input[-3:]

    # Si les trois derniers caractères sont "000", le résultat est 0
    # Sinon, on soustrait la valeur entière de ces 3 caractères à 1000
    if last_three == "000":
        result = 0
    else:
        result = 1000 - int(last_three)

    # Affiche le résultat final
    print(result)

# Appel de la fonction principale
compute_result()