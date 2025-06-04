# Solution utilisant une approche gloutonne (greedy) optimisée
# L'approche gloutonne est valide ici car les pièces sont celles du système monétaire US classique (1,5,10,25)
# et on a une infinité de chaque pièce.
# On commence par utiliser le maximum de pièces de 25, puis de 10, puis de 5 et enfin de 1.

def minimum_coins(n):
    # Liste des pièces disponibles, triée par valeur décroissante
    coins = [25, 10, 5, 1]
    count = 0  # Nombre total de pièces utilisées

    for coin in coins:
        # Nombre maximal de pièces de cette valeur que l'on peut utiliser
        count += n // coin
        # Réduit n du montant couvert par les pièces utilisées
        n = n % coin
        # Si n devient zero, on peut arrêter la boucle tôt
        if n == 0:
            break

    return count

if __name__ == "__main__":
    import sys
    # Lire la valeur entière n depuis l'entrée standard
    n = int(sys.stdin.readline().strip())
    # Calculer et afficher le nombre minimum de pièces
    print(minimum_coins(n))