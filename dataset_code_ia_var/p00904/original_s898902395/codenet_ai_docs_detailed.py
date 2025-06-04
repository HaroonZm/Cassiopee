def check_condition(p, q):
    """
    Vérifie si les conditions données sont satisfaites pour moins de 5 cas,
    en parcourant toutes les combinaisons possibles de i et j de 0 à 141 inclus.

    Args:
        p (int): Le premier entier de l'entrée.
        q (int): Le deuxième entier de l'entrée.

    Returns:
        bool: True si le nombre de cas trouvés est inférieur à 5, False sinon.
    """
    count = 0
    # Parcourt toutes les valeurs possibles de i
    for i in range(142):
        # Parcourt toutes les valeurs possibles de j
        for j in range(142):
            # On évite la division par zéro ou le cas trivial où i et j sont tous les deux nuls
            if i > 0 or j > 0:
                denominator = j * j + i * i
                # Vérifie les deux conditions de divisibilité spécifiées
                if ((j * p + i * q) % denominator == 0) and ((j * q - i * p) % denominator == 0):
                    count += 1
    # Retourne True si moins de 5 cas ont été trouvés, sinon False
    return count < 5

def process_test_cases():
    """
    Traite plusieurs cas de test. Pour chaque cas, lit deux entiers et imprime 'P' si la fonction de vérification renvoie True,
    sinon imprime 'C'.
    """
    # Lit le nombre total de cas de test à traiter
    num_cases = int(input())
    for _ in range(num_cases):
        # Lit et convertit les deux entiers p et q fournis pour le cas actuel
        p, q = map(int, input().split())
        # Applique la condition logicielle et imprime le résultat approprié
        if check_condition(p, q):
            print('P')
        else:
            print('C')

# Lancement du traitement des cas de test
process_test_cases()