import bisect

LENGTH = 1000000

def eratosthenes(length):
    """
    Génère une liste indiquant la primalité des nombres jusqu'à 'length' inclus
    en utilisant le crible d'Ératosthène.

    Args:
        length (int): La limite supérieure jusqu'à laquelle on teste la primalité.

    Returns:
        list of bool: Une liste où l'indice correspond au nombre et la valeur booléenne
        indique si ce nombre est premier (True) ou non (False).
    """
    from math import sqrt

    def is_prime_number(num):
        """
        Vérifie si un nombre impair 'num' est premier en testant la divisibilité par
        des nombres impairs jusqu'à la racine carrée de 'num'.

        Args:
            num (int): Le nombre à tester (impair).

        Returns:
            bool: True si 'num' est premier, False sinon.
        """
        limit = int(sqrt(num)) + 1

        for lp in range(3, limit, 2):
            if num % lp == 0:
                return False

        return True

    # Initialisation d'une liste pour marquer la primalité: True potentiellement premier
    is_prime_number_list = [True] * (LENGTH + 1)
    # 0 et 1 ne sont pas premiers
    is_prime_number_list[0] = False
    is_prime_number_list[1] = False
    # 2 est un nombre premier
    is_prime_number_list[2] = True

    # Élimine tous les nombres pairs >= 4
    for index in range(4, length + 1, 2):
        is_prime_number_list[index] = False

    limit = int(sqrt(length)) + 1

    # Pour tous les nombres impairs jusqu'à sqrt(length),
    # si le nombre est premier, éliminer ses multiples
    for lp in range(3, limit, 2):
        if is_prime_number(lp):
            # Balayer tous les multiples et les marquer comme non premiers
            for index in range(lp * 2, length + 1, lp):
                is_prime_number_list[index] = False

    return is_prime_number_list

# Génère la liste des booléens indiquant si un nombre est premier jusqu'à LENGTH
is_prime_number_list = eratosthenes(LENGTH)

# Crée une liste des nombres premiers à partir de la liste booléenne
prime_number_list = [index for index, item in enumerate(is_prime_number_list) if item]

while True:
    # Lit le nombre d'entrées à traiter
    input_count = int(input())

    # Condition d'arrêt: dès que l'entrée est 0, quitter la boucle
    if input_count == 0:
        break

    pay = 0  # Initialise la somme des "paiements"

    # Traite chaque paire (p, m)
    for _ in range(input_count):
        p, m = [int(item) for item in input().split(" ")]

        # Calcule les bornes inférieure et supérieure en tenant compte des limites
        lower = p - m if 0 < p - m else 0
        upper = p + m if p + m < LENGTH else LENGTH

        # Recherche de l'index de la borne inférieure dans la liste des nombres premiers
        lower_index = bisect.bisect_left(prime_number_list, lower)
        # Recherche de l'index de la borne supérieure dans la liste des nombres premiers
        upper_index = bisect.bisect_right(prime_number_list, upper)

        # Le nombre de nombres premiers dans cet intervalle est la différence des indices
        prize = upper_index - lower_index

        # On ajoute (prize - 1) au total (logique métier spécifique)
        pay += prize - 1

    # Affiche le montant total calculé pour cette série d'entrées
    print(pay)