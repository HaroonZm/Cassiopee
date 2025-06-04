import bisect

def generate_primes(limit):
    """
    Génère une liste de nombres premiers jusqu'à une limite donnée.
    
    Args:
        limit (int): La borne supérieure pour rechercher les nombres premiers (exclue).
        
    Returns:
        list: Une liste de nombres premiers jusqu'à 'limit'.
    """
    primes = []
    for i in range(2, limit):
        # Tester si i est un nombre premier en vérifiant la divisibilité de 2 à sqrt(i)
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                # i n'est pas premier, arrêter de vérifier ce nombre.
                break
        else:
            # Si aucune division n'était exacte alors i est premier
            primes.append(i)
    return primes

def find_nth_sum_of_consecutive_primes(n, p, primes):
    """
    Calcule la p-ième plus petite somme de deux nombres premiers consécutifs après n.

    Args:
        n (int): La borne inférieure, seuls les nombres premiers strictement supérieurs à n sont considérés.
        p (int): L'indice (1-based) de la somme recherchée dans la liste triée des sommes possibles.
        primes (list): La liste complète des nombres premiers précalculés.

    Returns:
        int: La p-ième plus petite valeur de pr[i] + pr[j], avec i <= j, i et j compris dans l'intervalle choisi.
    """
    # Trouver l'index où débuter en recherchant le premier nombre premier strictement supérieur à n
    start_idx = bisect.bisect_right(primes, n)
    # Sélectionner le sous-ensemble de p nombres premiers après n
    selected_primes = primes[start_idx:start_idx + p]
    # Calculer toutes les sommes pr[i] + pr[j] pour i <= j dans ce sous-ensemble
    sums = []
    for i in range(p):
        for j in range(i, p):
            sums.append(selected_primes[i] + selected_primes[j])
    # Trier les sommes, puis retourner la p-ième plus petite somme (indices sont 0-based)
    sums.sort()
    return sums[p - 1]

def main():
    """
    Fonction principale du programme.
    Génère les nombres premiers, puis lit les entrées utilisateur pour effectuer les calculs
    demandés jusqu'à ce que l'utilisateur saisisse une valeur négative pour n.
    """
    # Générer la liste des nombres premiers jusqu'à 110000 (non inclus)
    primes = generate_primes(110000)

    while True:
        # Lire les valeurs de n et p depuis l'entrée standard, séparées par un espace
        n, p = map(int, input().split())
        # Si n est négatif, arrêter la boucle
        if n < 0:
            break
        # Calculer et afficher le résultat souhaité
        result = find_nth_sum_of_consecutive_primes(n, p, primes)
        print(result)

# Appeler la fonction principale lorsque le script est exécuté
if __name__ == "__main__":
    main()