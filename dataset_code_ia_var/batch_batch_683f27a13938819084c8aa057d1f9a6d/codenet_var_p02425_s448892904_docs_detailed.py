# Déclaration des variables globales
q = int(input())  # Nombre de requêtes (opérations à réaliser)
x = 0             # Variable globale représentant l'entier manipulé comme un bitset sur 64 bits
MASK = 2 ** 64 - 1  # Masque binaire pour représenter 64 bits à 1

def x_test(i):
    """
    Vérifie si le i-ème bit de x est à 1.

    Args:
        i (int): L'indice du bit à tester (0 pour le bit de poids faible).

    Returns:
        int: 1 si le bit i est à 1, sinon 0.
    """
    return int((x & (1 << i)) > 0)

def x_set(i):
    """
    Met à 1 le i-ème bit de x.

    Args:
        i (int): L'indice du bit à modifier.
    """
    global x
    x |= 1 << i

def x_clear(i):
    """
    Met à 0 le i-ème bit de x.

    Args:
        i (int): L'indice du bit à modifier.
    """
    global x
    if x & (1 << i):
        x ^= 1 << i

def x_flip(i):
    """
    Inverse (toggle) le i-ème bit de x (met à 1 si 0, à 0 si 1).

    Args:
        i (int): L'indice du bit à modifier.
    """
    global x
    x ^= 1 << i

def x_all():
    """
    Vérifie si tous les 64 bits de x sont à 1.

    Returns:
        int: 1 si tous les bits sur 64 sont à 1, sinon 0.
    """
    return int(x & MASK == MASK)

def x_any():
    """
    Vérifie si au moins un des 64 bits de x est à 1.

    Returns:
        int: 1 si au moins un bit sur 64 est à 1, sinon 0.
    """
    return int(x & MASK > 0)

def x_none():
    """
    Vérifie si aucun des 64 bits de x n'est à 1.

    Returns:
        int: 1 si tous les bits sur 64 sont à 0, sinon 0.
    """
    return int(x & MASK == 0)

def x_count():
    """
    Compte le nombre de bits à 1 parmi les 64 bits de x.

    Returns:
        int: Le nombre de bits à 1.
    """
    # bin(x) transforme x en chaîne binaire, count("1") compte les bits 1
    return bin(x).count("1")

def x_val():
    """
    Retourne la valeur entière actuelle de x.

    Returns:
        int: La valeur de x.
    """
    return x

# Liste de fonctions correspondant aux opérations possibles, indexées par t
command = [
    x_test,   # 0 : tester un bit
    x_set,    # 1 : mettre un bit à 1
    x_clear,  # 2 : mettre un bit à 0
    x_flip,   # 3 : inverser un bit
    x_all,    # 4 : tester si tous les bits sont à 1
    x_any,    # 5 : tester si au moins un bit est à 1
    x_none,   # 6 : tester si aucun bit n'est à 1
    x_count,  # 7 : compter les bits à 1
    x_val     # 8 : obtenir la valeur de x
]

# Boucle principale pour traiter chaque requête
for j in range(q):
    # Lecture et décodage de la commande : t est le type d'opération, cmd sont les arguments éventuels
    t, *cmd = map(int, input().split())
    # Exécution de la commande, avec ses arguments le cas échéant
    ans = command[t](*cmd)
    # Affichage seulement si la commande renvoie quelque chose (pour les opérations de consultation)
    if ans is not None:
        print(ans)