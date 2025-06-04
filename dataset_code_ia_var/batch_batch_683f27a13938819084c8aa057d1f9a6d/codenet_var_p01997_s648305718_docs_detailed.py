import math

def calculate_volume(a: int, b: int) -> float:
    """
    Calcule un volume spécifique basé sur la comparaison de deux entiers.
    
    Si a > b, retourne le volume égal à (2/3) * pi * a^2 * b.
    Sinon, retourne le volume égal à (4/3) * pi * b^3.

    Args:
        a (int): Premier entier.
        b (int): Deuxième entier.

    Returns:
        float: Le résultat du calcul du volume selon la condition.
    """
    if a > b:
        # Si a est supérieur à b, calcule le volume selon la première formule
        return (2 / 3) * math.pi * a ** 2 * b
    else:
        # Sinon, calcule le volume selon la seconde formule
        return (4 / 3) * math.pi * b ** 3

def main():
    """
    Fonction principale qui gère l'entrée utilisateur,
    utilise calculate_volume et affiche le résultat.
    """
    # Lit deux entiers depuis une entrée utilisateur séparés par un espace
    a, b = map(int, input().split())
    # Calcule le volume basé sur les valeurs entrées
    result = calculate_volume(a, b)
    # Affiche le résultat du calcul
    print(result)

if __name__ == "__main__":
    main()