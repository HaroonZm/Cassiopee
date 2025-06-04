def min_attacks_to_defeat_monster(H, A):
    """
    Calcule le nombre minimal d'attaques nécessaires pour vaincre un monstre.

    Cette fonction utilise la division entière pour déterminer combien d'attaques
    d'une puissance A sont nécessaires pour réduire les PV du monstre H à 0 ou moins.

    Args:
        H (int): Nombre initial de points de vie (PV) du monstre.
        A (int): Dégâts infligés par une attaque.

    Returns:
        int: Nombre minimal d'attaques nécessaires pour vaincre le monstre.
    """
    # Utilisation de la "division plafond" pour déterminer le nombre d'attaques :
    # (H + A - 1) // A équivaut à math.ceil(H / A) sans importer de bibliothèque.
    return (H + A - 1) // A

# Lecture de l'entrée utilisateur et conversion des valeurs en entiers
H, A = map(int, input().split())

# Calcul et affichage du résultat
print(min_attacks_to_defeat_monster(H, A))