def somme_modulo_24(a: int, b: int) -> int:
    """
    Calcule la somme de deux entiers modulo 24.

    Args:
        a (int): Premier entier représentant une heure, par exemple.
        b (int): Deuxième entier représentant une durée ou une heure.

    Returns:
        int: Le résultat de (a + b) modulo 24, garantissant une valeur dans l'intervalle [0, 23].
    """
    # Additionne les deux nombres, puis applique le modulo 24
    return (a + b) % 24

def main():
    """
    Lit deux entiers à partir de l'entrée standard, les additionne et affiche le résultat modulo 24.
    """
    # Demande à l'utilisateur de saisir deux entiers séparés par un espace
    a, b = map(int, input().split())
    # Calcule la somme modulo 24 à l'aide de la fonction dédiée
    resultat = somme_modulo_24(a, b)
    # Affiche le résultat final
    print(resultat)

# Exécution du programme principal
if __name__ == "__main__":
    main()