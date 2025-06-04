import string

def factorize_number(n, primes):
    """
    Décompose le nombre n en facteurs premiers parmi la liste 'primes'.
    Retourne une liste contenant les exposants correspondants à chaque nombre premier.
    
    Args:
        n (int): Le nombre à factoriser.
        primes (list of int): La liste des nombres premiers parmi lesquels factoriser.
    
    Returns:
        list of int: Les exposants des facteurs premiers pour n (alignés à la liste primes).
    """
    # Initialiser la liste des exposants à 0 pour chaque nombre premier
    exponents = [0 for _ in primes]
    # Parcourir chaque nombre premier
    for i in range(len(primes)):
        current = n
        # Compter combien de fois 'primes[i]' divise n
        while current % primes[i] == 0 and current > 0:
            current /= primes[i]
            exponents[i] += 1
    return exponents

def baseN_to_decimal(s, base, symbols):
    """
    Convertit une chaîne s représentant un nombre dans une certaine base en décimal.
    
    Args:
        s (str): Le nombre sous forme de chaîne, potentiellement dans une base quelconque.
        base (int): La base dans laquelle s est exprimée.
        symbols (str): Les caractères représentant les chiffres dans la base.
    
    Returns:
        int: La valeur décimale du nombre représenté par s.
    """
    decimal_value = 0
    length = len(s)
    # Parcourir chaque caractère de droite à gauche (position déterminée par i)
    for i in range(1, length + 1):
        c = s[-i]
        digit_value = symbols.index(c)
        decimal_value += digit_value * (base ** (i - 1))
    return decimal_value

def min_k_factorial_divisible(n, l_decimal, primes, exponents):
    """
    Détermine la plus grande valeur entière k telle que N^k divise L! où
    N est la base, L la valeur décimale à traiter.
    
    Args:
        n (int): La base N.
        l_decimal (int): La valeur décimale correspondant à l'entrée M.
        primes (list of int): Liste des nombres premiers.
        exponents (list of int): Exposants des facteurs premiers de N.
    
    Returns:
        int: Le plus grand entier k tel que N^k divise L!.
    """
    # Une valeur très grande pour l'initialisation du minimum
    min_ans = float('inf')
    # Parcourir chaque facteur premier
    for i in range(len(primes)):
        p = primes[i]
        if exponents[i] != 0:
            # Calculer le nombre de fois où p apparaît dans la décomposition de L!
            k = 1
            total = 0
            while p ** k <= l_decimal:
                e = l_decimal // (p ** k)
                total += e
                k += 1
            # Diviser par le nombre d’occurrences de ce facteur dans N (multiplicité)
            total //= exponents[i]
            min_ans = min(min_ans, total)
    return min_ans

def main():
    """
    Point d'entrée principal du programme : lit les entrées utilisateurs,
    exécute le traitement principal et affiche les résultats.
    """
    S = string.digits + string.ascii_uppercase  # Symboles pour les bases jusqu'à 36
    # Liste des nombres premiers utilisés pour factoriser N
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    while True:
        try:
            # Lecture et découpage de l'entrée utilisateur
            line = raw_input()
        except EOFError:
            # Si fin de fichier, arrêter le programme
            break
        if not line.strip():
            # Ligne vide, on passe à la suivante
            continue
        N_str, M = line.strip().split()
        N = int(N_str)
        if N == 0:
            # Condition d'arrêt du programme
            break
        
        # Décomposition de N en facteurs premiers
        exponents = factorize_number(N, primes)
        
        # Conversion de M (en base N) vers une valeur décimale L
        L = baseN_to_decimal(M, N, S)
        
        # Calcul de la réponse minimale pour L!
        ans = min_k_factorial_divisible(N, L, primes, exponents)
        
        # Affichage du résultat
        print ans

# Lancement du programme principal
if __name__ == "__main__":
    main()