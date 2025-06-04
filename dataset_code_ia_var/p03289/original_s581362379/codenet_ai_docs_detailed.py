def check_ac_string(s):
    """
    Vérifie si la chaîne fournie respecte les conditions suivantes pour être considérée comme 'AC' :
    - Le premier caractère doit être 'A'.
    - Il doit y avoir exactement un 'C' dans la sous-chaîne qui commence au troisième caractère et s'arrête à l'avant-dernier.
    - Tous les autres caractères, après avoir remplacé 'C' par 'c', doivent être des lettres minuscules.

    Args:
        s (str): La chaîne d'entrée à vérifier.

    Returns:
        str: 'AC' si la chaîne respecte toutes les conditions, sinon 'WA'.
    """
    # Vérifie que le premier caractère est 'A'
    if s[0] == "A":
        # Compte le nombre de 'C' entre le troisième caractère (inclus) et l'avant-dernier (exclus)
        c_count = s[2:-1].count("C")
        if c_count == 1:
            # Remplace tous les 'C' restants par 'c', puis vérifie si les caractères à partir du deuxième sont tous des minuscules
            if s[1:].replace("C", "c").islower():
                return "AC"
    # Retourne "WA" si l'une des conditions n'est pas respectée
    return "WA"

if __name__ == "__main__":
    # Lit la chaîne de caractères depuis l'entrée standard
    user_input = input()
    # Appelle la fonction de vérification et affiche le résultat
    print(check_ac_string(user_input))