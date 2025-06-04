# Solution complète pour le problème "Discounts of Buckwheat"

# L'idée est de déterminer la combinaison optimale d'achats entre les trois boutiques A, B et C
# pour obtenir la quantité exacte de farine demandée au moindre coût, en prenant en compte
# les remises par lots.

# Chaque boutique vend une farine avec :
# - une quantité fixe par sac
# - un prix unitaire par sac
# - une réduction aplicable par lots de sacs achetés

# Méthode proposée :
# Puisqu'on doit trouver la combinaison minimale de sacs dont la somme des quantités fait exactement
# a, avec des remises appliquées sur certains multiples d’unités,
# on peut faire un parcours sur toutes les combinaisons possibles de sacs (naïvement),
# mais la quantité maximale est 5000, on peut limiter la recherche avec une programmation dynamique
# sur la quantité de farine.

# Étapes :
# 1. Définir pour chaque boutique une fonction qui calcule le coût total pour un nombre donné de sacs.
# 2. Utiliser la programmation dynamique pour calculer le coût minimum pour chaque quantité de farine
#    de 0 à a.
# 3. Pour chaque quantité intermédiaire, on essaie d'ajouter un sac d’une des boutiques pour mettre à jour
#    le coût minimum.

# Résultat final : dp[a] contient le coût minimum pour obtenir exactement a grammes.

import sys

# Définition des données des boutiques
shops = {
    'A': {
        'amount': 200,      # en grammes
        'price': 380,       # prix unitaire (yen) par sac
        'discount_units': 5,
        'discount_rate': 0.20
    },
    'B': {
        'amount': 300,
        'price': 550,
        'discount_units': 4,
        'discount_rate': 0.15
    },
    'C': {
        'amount': 500,
        'price': 850,
        'discount_units': 3,
        'discount_rate': 0.12
    }
}

def cost_for_bags(shop_key, bags):
    """
    Calcule le prix total pour un nombre donné de sacs achetés dans une boutique donnée en tenant compte
    des remises par lots.
    
    Paramètres :
    shop_key : clé de la boutique ('A', 'B' ou 'C')
    bags : nombre de sacs
    
    Retourne :
    Le coût total en yen (int)
    """
    shop = shops[shop_key]
    full_discount_batches = bags // shop['discount_units']    # nombre de lots complets permettant la remise
    remaining_bags = bags % shop['discount_units']            # sacs non réduits
    
    # Coût pour les lots complets avec réduction
    cost_discounted = full_discount_batches * shop['discount_units'] * shop['price'] * (1 - shop['discount_rate'])
    # Coût pour les sacs restants sans réduction
    cost_remaining = remaining_bags * shop['price']
    
    total_cost = cost_discounted + cost_remaining
    
    # conversion en int car yen (sans centimes)
    return int(total_cost + 0.5)  # arrondi à l'entier le plus proche

def solve_for_amount(amount):
    """
    Utilise la programmation dynamique pour trouver le coût minimum pour obtenir exactement 'amount' grammes.
    
    Paramètre :
    amount (int): quantité demandée en grammes
    
    Retourne :
    Le coût minimal (int)
    """
    # dp[i] = coût minimal pour i grammes
    # On initialise avec une valeur très grande sauf dp[0]
    INF = 10**9
    dp = [INF] * (amount + 1)
    dp[0] = 0
    
    # Pour chaque quantité de farine de 0 à amount,
    # on essaie d'ajouter un sac de chaque boutique si ça ne dépasse pas amount
    for i in range(amount + 1):
        if dp[i] == INF:
            continue  # impossible d'atteindre cette quantité, ignorer
        for shop_key in shops:
            s = shops[shop_key]
            next_amount = i + s['amount']
            if next_amount <= amount:
                # On doit connaitre combien de sacs déjà achetés dans cette boutique pour calculer la remise
                # Mais ici dp est global, on ne connait pas la composition.
                # Donc on doit changer d'approche :
                # Il faut mémoriser pour chaque quantité le nombre de sacs par boutique.
                # Comme la quantité max est 5000, on peut mettre une structure supplémentaire dans dp.
                pass

    # L'approche précédente ne permet pas de calculer correctement les remises car on ne connaît pas le 
    # nombre de sacs achetés dans chaque boutique pour cette quantité intermédiaire.

    # Nouvelle approche :
    # On peut représenter chaque état dp[i][a][b][c] représentant le coût pour i grammes en ayant acheté
    # a sacs chez A, b chez B et c chez C.
    # Mais cela serait trop grand (la complexité explose).

    # Autre idée :
    # Chaque sac a un poids fixe donc on peut calculer le nombre maximum de sacs nécessaires pour chaque boutique.
    # Les nombres max de sacs pour atteindre au max 5000 grammes:
    max_a = amount // shops['A']['amount'] + 1
    max_b = amount // shops['B']['amount'] + 1
    max_c = amount // shops['C']['amount'] + 1

    min_cost = 10**9
    
    # On va essayer toutes les combinaisons possibles de sacs des boutiques A, B, et C
    # qui totalisent exactement 'amount' grammes.
    # L'optimisation possible est de réduire le domaine des boucles en fonction de amount.
    for a in range(max_a):
        for b in range(max_b):
            weight_ab = a * shops['A']['amount'] + b * shops['B']['amount']
            if weight_ab > amount:
                # trop de poids, skip
                continue
            c_needed = (amount - weight_ab)
            # pour que c_needed soit divisible par 500 (poids des sacs C)
            if c_needed % shops['C']['amount'] != 0:
                continue
            c = c_needed // shops['C']['amount']
            if c >= max_c:
                continue
            
            # Calculer le coût total
            cost_a = cost_for_bags('A', a)
            cost_b = cost_for_bags('B', b)
            cost_c = cost_for_bags('C', c)
            total_cost = cost_a + cost_b + cost_c
            
            if total_cost < min_cost:
                min_cost = total_cost
    
    return min_cost

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    for line in input_lines:
        a = int(line)
        if a == 0:
            break
        # Résoudre pour la quantité a
        answer = solve_for_amount(a)
        print(answer)

if __name__ == "__main__":
    main()