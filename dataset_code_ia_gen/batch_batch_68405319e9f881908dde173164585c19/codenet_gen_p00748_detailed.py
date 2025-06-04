import sys

# Fonction pour calculer les nombres tétraédriques jusqu'à une certaine limite
def generate_tetrahedral_numbers(limit):
    tetra = []
    n = 1
    while True:
        val = n * (n + 1) * (n + 2) // 6
        if val > limit:
            break
        tetra.append(val)
        n += 1
    return tetra

# Fonction pour générer uniquement les nombres tétraédriques impairs jusqu'à une limite
def generate_odd_tetrahedral_numbers(limit):
    tetra = []
    n = 1
    while True:
        val = n * (n + 1) * (n + 2) // 6
        if val > limit:
            break
        if val % 2 == 1:  # nombre tétraédrique impair
            tetra.append(val)
        n += 1
    return tetra

# Fonction pour calculer le nombre minimal de termes pour représenter target
# avec les nombres donnés dans numbers (par programmation dynamique)
def min_count_numbers(target, numbers):
    # On initialise la liste dp avec une valeur élevée indiquant "non réalisable"
    # dp[x] informera du minimum de nombres nécessaires pour constituer x
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # 0 peut être représenté par 0 nombres
    
    for x in range(1, target + 1):
        # On essaie de prendre chaque nombre tétraédrique possible
        for num in numbers:
            if num > x:
                break  # les nombres tétraédriques sont triés, pas besoin de continuer
            # Mise à jour si on trouve une meilleure combinaison
            if dp[x - num] + 1 < dp[x]:
                dp[x] = dp[x - num] + 1
    return dp[target]

# Programme principal
def main():
    input_numbers = []
    max_input = 0

    # Lecture des entrées
    for line in sys.stdin:
        n = line.strip()
        if n == '0':
            break
        val = int(n)
        input_numbers.append(val)
        if val > max_input:
            max_input = val

    # Génération de toutes les listes nécessaires au maximum des entrées
    tetrahedral_numbers = generate_tetrahedral_numbers(max_input)
    odd_tetrahedral_numbers = generate_odd_tetrahedral_numbers(max_input)

    # Pour optimiser, on va faire un calcul DP une fois par cas, mais cela
    # serait trop couteux pour max_input=10^6 (mémoire et temps).
    # En fait, la solution demande de répondre pour chaque entrée,
    # donc on procède entrée par entrée en dynamique.
    # Comme max_input peut aller jusqu'à 10^6, un dp complet est très gros.
    # Il faut une autre stratégie : faire un calcul par entrée avec un DP optimisé
    # en respectant la complexité.

    # Pour la limite 10^6 et la taille des nombres tétraédriques (~175),
    # il est possible de faire un DP complet : dp array de taille 10^6 ~ 1 million éléments,
    # ce qui est faisable en mémoire, mais un double DP pour tous les inputs serait lourd.
    # Solution : calculer une fois pour max_input et réutiliser les résultats.

    # Calcul DP complet pour nombres tétraédriques
    dp_tetra = [float('inf')] * (max_input + 1)
    dp_tetra[0] = 0
    for x in range(1, max_input + 1):
        for t in tetrahedral_numbers:
            if t > x:
                break
            val = dp_tetra[x - t] + 1
            if val < dp_tetra[x]:
                dp_tetra[x] = val

    # Calcul DP complet pour nombres tétraédriques impairs
    dp_odd = [float('inf')] * (max_input + 1)
    dp_odd[0] = 0
    for x in range(1, max_input + 1):
        for t in odd_tetrahedral_numbers:
            if t > x:
                break
            val = dp_odd[x - t] + 1
            if val < dp_odd[x]:
                dp_odd[x] = val

    # Affichage des résultats pour chaque entrée
    for val in input_numbers:
        print(dp_tetra[val], dp_odd[val])

if __name__ == '__main__':
    main()