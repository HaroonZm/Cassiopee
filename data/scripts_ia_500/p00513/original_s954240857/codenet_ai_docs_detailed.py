# Demande à l'utilisateur d'entrer un entier n qui déterminera le nombre d'itérations dans la boucle principale
n = int(input())

# Initialise un compteur ng à 0, qui sera utilisé pour compter combien des nombres générés sont premiers
ng = 0

def prime(a):
    """
    Détermine si un nombre impair a est premier.

    Args:
        a (int): Un entier impair à tester.

    Returns:
        int: 1 si a est premier, 0 sinon.
    
    Description:
        - Si a vaut 1, on considère qu'il est premier (retourne 1).
        - Ensuite, on teste les diviseurs impairs commençant par 3, 
          jusqu'à la racine carrée de a (optimisation classique pour test de primalité).
        - Si un diviseur est trouvé, retourne 0 (pas premier).
        - Sinon, retourne 1 (nombre premier).
    """
    if a == 1:
        return 1
    
    i = 3
    # On augmente i par pas de 2 (test uniquement des diviseurs impairs)
    while i <= a / i:
        if a % i == 0:
            return 0
        i += 2
    return 1

# Boucle pour n itérations
for _ in range(n):
    # Lit un entier, le multiplie par 2 et ajoute 1 pour obtenir un nombre impair
    a = 2 * int(input()) + 1
    # Ajoute 1 à ng si a est premier, sinon ajoute 0
    ng += prime(a)
    
# Affiche le nombre total de nombres premiers trouvés
print(ng)