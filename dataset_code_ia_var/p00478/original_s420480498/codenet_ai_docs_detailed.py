def count_occurrences_with_rotation(m: str, n: int, x: list) -> int:
    """
    Compte le nombre de fois où la chaîne 'm' apparaît dans une version "rotée" 
    de chaque chaîne fournie dans 'x'. Pour chaque chaîne, elle est concaténée à ses 11 premiers caractères
    afin de simuler la rotation, puis la présence de 'm' est recherchée.

    Args:
        m (str): La chaîne à rechercher.
        n (int): Le nombre de chaînes en entrée.
        x (list): La liste des chaînes de caractères à examiner.

    Returns:
        int: Le nombre de chaînes "rotées" contenant 'm'.
    """
    c = 0  # Compteur d'occurrences

    for i in range(n):
        # Pour chaque chaîne, on ajoute ses 11 premiers caractères à la fin pour simuler la rotation
        x[i] = x[i] + x[i][:11]
        # Si la chaîne recherchée 'm' existe dans cette version étendue
        if m in x[i]:
            c += 1  # On incrémente le compteur
    return c

# Lecture de la chaîne à rechercher auprès de l'utilisateur
m = input()

# Lecture du nombre de chaînes
n = int(input())

# Lecture des différentes chaînes à traiter
x = [input() for _ in range(n)]

# Calcul du nombre de présences de 'm' avec la logique expliquée
result = count_occurrences_with_rotation(m, n, x)

# Affichage du résultat final
print(result)