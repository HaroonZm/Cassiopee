b = [1] * 500000  # Initialise une liste b de 500000 éléments à 1. Cette liste sert pour le crible d'Ératosthène.

for i in range(3, 999, 2):  # On itère uniquement sur les nombres impairs de 3 à 998 (exclus).
    if b[i // 2]:  # Si l'élément correspondant à i//2 est encore marqué comme premier (valeur 1).
        # On met à zéro tous les multiples de i au carré, en sautant par i (filtrage des non-premiers)
        b[i * i // 2::i] = [0] * len(b[i * i // 2::i])

def p(x):
    """
    Fonction qui détermine si un nombre est premier.
    Pour x < 500000, la réponse est donnée par le crible pré-calculé b.
    Pour x >= 500000, un test de primalité classique est effectué.
    
    Args:
        x (int): Le nombre à tester
    
    Returns:
        int: 1 si x est premier, 0 sinon
    """
    if x < 5 * 1e5:
        return b[int(x)]  # Pour les petits nombres, retourne directement le résultat du crible

    # Pour les grands nombres, on effectue un test de primalité classique
    x = 2 * x + 1  # On considère seulement les nombres impairs car b représente seulement les impairs
    limite = int(x ** 0.5) + 1
    for i in range(3, limite, 2):
        if x % i == 0:
            return 0
    return 1

# Lecture du nombre de tests à effectuer
nombre_de_tests = int(input())

# Pour chaque test, on lit un entier, teste s'il est premier via p, et on somme les résultats
resultat = sum(p(int(input())) for _ in range(nombre_de_tests))

print(resultat)  # Affiche le nombre total de nombres premiers détectés parmi les entrées données