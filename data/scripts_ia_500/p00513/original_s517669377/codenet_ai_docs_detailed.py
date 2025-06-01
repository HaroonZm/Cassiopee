def p(x):
    """
    Vérifie si un nombre entier x est un nombre premier.

    Un nombre premier est un nombre entier supérieur à 1 qui n'a pas d'autres diviseurs
    entiers que 1 et lui-même.

    Args:
        x (int): Le nombre entier à tester pour la primalité.

    Returns:
        int: 1 si x est premier, 0 sinon.
    """
    # On considère que les nombres pairs ne sont pas premiers (sauf 2).
    # Ici, si x est pair, on retourne immédiatement 0 (non premier).
    if x % 2 == 0:
        return 0
    
    # On teste tous les diviseurs impairs de 3 jusqu'à la racine carrée de x (inclus),
    # car si x a un diviseur supérieur à sa racine carrée, il a aussi un diviseur inférieur.
    for i in range(3, int(x ** 0.5 + 1), 2):
        # Si i divise x, x n'est pas premier.
        if x % i == 0:
            return 0

    # Si aucun diviseur n'a été trouvé, x est premier.
    return 1


# Lecture du nombre d'itérations à effectuer
n = int(input())

# Somme des résultats de la fonction p appliquée à 2*input + 1, répété n fois
# Pour chaque itération, on lit un entier, on calcule 2*x + 1,
# puis on teste si ce nombre est premier avec la fonction p.
result = sum(p(int(input()) * 2 + 1) for _ in range(n))

# Affichage du total des nombres premiers détectés
print(result)