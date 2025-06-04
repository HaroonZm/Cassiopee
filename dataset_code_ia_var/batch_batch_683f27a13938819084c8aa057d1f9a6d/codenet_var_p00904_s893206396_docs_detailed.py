def main():
    """
    Point d'entrée du programme.
    Lit un nombre de cas de test, puis pour chaque cas,
    lit deux entiers m et n, exécute un calcul spécifique et affiche le résultat.
    """
    # Lecture du nombre de cas de test à traiter
    num_cases = int(input())
    for _ in range(num_cases):
        m, n = lire_entiers()
        count = compter_configurations_valides(m, n)
        # Affichage du résultat en fonction de la valeur de count
        if count < 5:
            print("P")
        else:
            print("C")

def lire_entiers():
    """
    Lit une ligne d'entrée standard contenant deux entiers séparés par un espace.

    Returns:
        tuple: Un tuple contenant deux entiers (m, n)
    """
    m, n = map(int, input().split())
    return m, n

def compter_configurations_valides(m, n):
    """
    Calcule le nombre de configurations (p, q) telles que p et q sont compris entre 0 et 141 (inclus),
    non tous deux nuls, p^2 + q^2 <= 20000, et satisfont les conditions arithmétiques suivantes :
      (m*p + n*q) est divisible par (p^2 + q^2)
      (n*p - m*q) est divisible par (p^2 + q^2)

    Args:
        m (int): Premier entier fourni
        n (int): Deuxième entier fourni

    Returns:
        int: Le nombre de configurations valides de (p, q) pour les paramètres donnés
    """
    count = 0
    # Parcours de toutes les p et q dans l'intervalle [0, 141]
    for p in range(142):
        for q in range(142):
            # Évite le cas où p et q sont simultanément nuls
            if p == 0 and q == 0:
                continue
            # Calcul de la somme des carrés
            pq = p * p + q * q
            # Si pq dépasse 20000, on quitte la boucle interne (toutes les q suivantes seront plus grandes)
            if pq > 20000:
                break
            # Vérifie les conditions de divisibilité
            if (m * p + n * q) % pq == 0 and (n * p - m * q) % pq == 0:
                count += 1
    return count

# Exécution du programme principal
if __name__ == "__main__":
    main()