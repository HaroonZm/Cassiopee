# Solution complète en Python avec commentaires détaillés

# L'idée est de déterminer le coût minimum pour acheter au moins X millilitres d'eau,
# en combinant des bouteilles de 1 litre (1000 millilitres) et de 0.5 litre (500 millilitres).
# On souhaite minimiser le coût total.

# Approche:
# - On itère sur le nombre possible de bouteilles de 1 litre (de 0 à un maximum suffisant).
# - Pour chaque nombre de bouteilles de 1 litre, on calcule la quantité restante à couvrir.
# - On calcule alors le nombre minimal de bouteilles de 0.5 litre nécessaires (en arrondissant vers le haut).
# - On calcule le coût total pour cette combinaison.
# - On garde la meilleure solution (coût minimum) trouvée.

# Cette approche est efficace puisque X ≤ 20000 et le nombre maximum de bouteilles de 1 litre est au plus 20.

def main():
    # Lecture des entrées : prix A (1L), prix B (0.5L), et quantité X en millilitres
    A, B, X = map(int, input().split())

    # Initialisation du coût minimum à une valeur très haute
    cost_min = float('inf')

    # Nombre maximum potentiel de bouteilles 1L à considérer :
    # On peut acheter jusqu'à X//1000+2 bouteilles de 1L pour couvrir la quantité demandée, +2 pour marge.
    max_1L = X // 1000 + 2

    for count_1L in range(max_1L + 1):
        # Quantité couverte par les bouteilles 1L
        quantity_1L = count_1L * 1000

        # Quantité encore nécessaire après utilisation des bouteilles 1L
        leftover = max(0, X - quantity_1L)

        # Nombre minimal de bouteilles 0.5L pour couvrir leftover
        # Chaque bouteille 0.5L couvre 500ml, on divise en arrondissant vers le haut
        count_halfL = (leftover + 499) // 500  # Technique d'arrondi supérieur

        # Calcul du coût total pour cette combinaison
        total_cost = count_1L * A + count_halfL * B

        # On met à jour la solution minimale si meilleur coût trouvé
        if total_cost < cost_min:
            cost_min = total_cost

    print(cost_min)

if __name__ == "__main__":
    main()