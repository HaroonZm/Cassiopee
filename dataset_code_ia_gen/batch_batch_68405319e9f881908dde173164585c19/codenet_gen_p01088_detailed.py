# Problème détaillé : Collecter le maximum de pièces de 500-yen en achetant au plus un souvenir dans chaque magasin,
# dans l'ordre, avec la contrainte d'utiliser des billets de 1000-yen en nombre illimité, et les pièces reçues comme monnaie.
# On veut maximiser le nombre de pièces de 500-yen obtenues, puis minimiser la dépense totale pour ce maximum.

# Approche proposée :
# On utilise une approche de programmation dynamique (DP).
# États DP : à l'étape i (magasin i),
# on mémorise pour chaque nombre de pièces 500-yen en sa possession et les pièces (1,5,10,50,100) détenues,
# la dépense minimale pour arriver à cet état.
#
# Difficulté : 
# Les pièces 1,5,10,50,100 peuvent être en quantité variable, mais neutrement gérables car les montants max = 5000,
# donc les pièces max sont limitées.
#
# Simplification :
# Pour gérer efficacement l'état, on soupçonne que pour éviter explosion d'états,
# on ne mémorise que la quantité de pièces 500-yen possédées + la "configuration" des pièces (1,5,10,50,100).
# Seulement 500-yen et pièces faciales inférieures.
#
# Comme on ne peut pas avoir plus de 10 pièces de chaque sorte (car montant max 5000 yen),
# on limite les nombres max de pièces dans l'état.
#
# Implémentation principale :
# - Pour chaque magasin,
#   on tente 2 options :
#     - ne pas acheter (état inchangé, despense inchangée)
#     - acheter une pièce :
#       - On essaie tous les montants à verser possibles, concoctant la monnaie versée (bill+pièces)
#         telle que montant donné - prix = monnaie rendue contenant une ou plusieurs pièces 500-yen.
#       - On simule la transaction de pièces (enlever les pièces données, ajouter celles reçues).
#       - On met à jour le DP avec le nombre de pièces 500-yen total et la dépense.
#
# Optimisations possibles :
# - On "compresse" l'état des pièces en un tuple, on évite doublons.
# - On réduit la recherche des montants donnés en utilisant la nature des pièces et billets.
# - On limite la taille des états gardés pour éviter explosion.

import sys
import collections

# Pièces en circulation (autres que 500, 1000)
COIN_TYPES = [1, 5, 10, 50, 100]
MAX_COINS = [4, 4, 4, 4, 10]  # max pièces estimées raisonnables par type pour limiter les états

def make_change_min_coins(amount):
    # Retourne la distribution pour rendre le montant donné (change) avec le moins de pièces/billets
    # possible, en utilisant les pièces/billets : 1000, 500, 100, 50, 10, 5, 1
    # Sera utilisée pour calculer la monnaie rendue avec la devise japonaise
    res = {1000:0, 500:0, 100:0, 50:0, 10:0, 5:0, 1:0}
    for coin in [1000, 500, 100, 50, 10, 5, 1]:
        res[coin], amount = divmod(amount, coin)
    return res

def coins_to_list(coins_dict):
    # Retourne une liste du nombre de pièces dans l'ordre de COIN_TYPES
    return [coins_dict.get(c,0) for c in COIN_TYPES]

def list_to_coins(lst):
    # Transforme une liste [n1,n5,n10,n50,n100] en dictionnaire {valeur: nombre}
    return {c:n for c,n in zip(COIN_TYPES,lst)}

def coins_add(a, b):
    # Additionne 2 listes de pièces
    return [x+y for x,y in zip(a,b)]

def coins_sub(a,b):
    # Soustrait b de a pour des listes de pièces, renvoie None si b> a en quelconque pièce
    res = []
    for x,y in zip(a,b):
        if y > x:
            return None
        res.append(x-y)
    return res

def coins_count_500(coins_dict):
    # Nombre de pièces 500 dans un dictionnaire, sinon 0
    return coins_dict.get(500,0)

def coins_dict_to_tuple(coins_dict):
    # Retourne un tuple (c1,c5,c10,c50,c100) pour état
    return tuple(coins_to_list(coins_dict))

def coins_tuple_to_dict(tpl):
    return {c:n for c,n in zip(COIN_TYPES,tpl)}

def add_coins_dict(a,b):
    # addition deux dict de pièces
    res = a.copy()
    for k,v in b.items():
        res[k] = res.get(k,0)+v
    return res

def sub_coins_dict(a,b):
    # soustrait b de a dict, None si impossible
    res = a.copy()
    for k,v in b.items():
        if res.get(k,0) < v:
            return None
        res[k] = res.get(k,0) - v
    # Nettoyage clés à 0
    keys_to_del = [k for k,v in res.items() if v==0]
    for k in keys_to_del:
        del res[k]
    return res

def coins_tuple_is_valid(tpl):
    # Vérifie que les pièces dans tpl ne dépassent pas le max raisonnable pour éviter explosion d'états
    for i, n in enumerate(tpl):
        if n > MAX_COINS[i]:
            return False
    return True

def num_500_in_coins(coins_dict):
    return coins_dict.get(500, 0)

def dp_solution(prices):
    n = len(prices)

    # Etat DP : dictionnaire {(nombre pieces 500, pieces tuple (c1,c5,c10,c50,c100)) : dépense minimale}
    # Initial : 0 pieces 500, pas de pièces, dépense 0
    from collections import defaultdict
    dp = defaultdict(lambda: float('inf'))
    dp[(0, (0,0,0,0,0))] = 0

    for idx, price in enumerate(prices, start=1):
        ndp = defaultdict(lambda: float('inf'))
        # Pour chaque état actuel
        for (num_500, coins_tpl), expense in dp.items():
            # Option 1 : ne pas acheter dans ce magasin -> état inchangé
            if ndp[(num_500, coins_tpl)] > expense:
                ndp[(num_500, coins_tpl)] = expense

            # Option 2 : acheter à ce magasin
            # On doit envisager tous sommes à payer >= prix
            # montant donné = x, x >= price
            # x - price = change à recevoir
            #
            # Pour réduire l'espace de recherche :
            # Il doit y avoir au moins 1 pièce 500 dans la monnaie rendue (change),
            # sinon pas intérêt d'acheter dans ce magasin.
            # De plus, on essaie plusieurs montants donnés x, en minimisant le paiement total par magasin
            #
            # On utilise les pièces disponibles (coins_tpl) + billets illimités (1000 yens)
            # pour composer le montant donné.

            # Convert coin tuple en dict
            coins_dict = coins_tuple_to_dict(coins_tpl)

            # max montant donné considéré : price + 1000 (paiement par 1 billet 1000 + pas trop énorme)
            # On peut aller jusqu'à price + 1000 (car changer plus n'a aucun sens)
            # Par ailleurs, on peut tester les montants donnés avec 1000 yens multiples:
            # On testera x = price ... price + 1000

            for pay in range(price, price + 1001):
                change = pay - price
                # Obtenir le rendu minimal de monnaie pour change
                change_coins = make_change_min_coins(change)
                # Si pas de pièces 500 retournées -> pas intéressant
                if change_coins[500] == 0:
                    continue

                # On veut retirer les pièces données pour payer pay
                # montants payés peuvent utiliser:
                # - autant de billets 1000 qu'on veut
                # - et les pièces (1,5,10,50,100) en possession

                # Montant à payer : pay
                # Calcul nombre billets 1000 nécessaires :
                num_1000_needed = pay // 1000
                rest_pay = pay % 1000

                # Pour payer rest_pay, on doit utiliser des pièces en main
                # On doit trouver si on peut composer rest_pay avec les pièces en main

                # Problème : on peut utiliser un nombre quelconque de pièces qu'on détient
                # On doit vérifier si l'on peut composer rest_pay avec pièces en main
                # On essaye de prendre pièces pour la partie rest_pay

                # Solution pour vérifier composition :
                # On fait un recherche de pièces possible pour rest_pay
                # Double contrainte sur nombre de pièces max : denotes qu'on utilise pas trop pièces
                # mais ici on cherche juste composabilité.

                # On fait un simple backtrack / DP pour vérifier si rest_pay peut être payé avec les pièces en main

                # Convert coins_dict à simple liste (index coef)
                avail_coins = []
                for c in COIN_TYPES:
                    avail_coins.append(coins_dict.get(c, 0))

                # DP pour composabilité rest_pay en utilisant les pièces disponibles
                # pièce unité et quantités limitées

                can_pay = False
                def can_make_money(i, amount):
                    # i : pièce index dans COIN_TYPES
                    # amount : montant à réaliser

                    # DP mémorisation (on la fera iterative)
                    memo = {}
                    stack = [(i, amount)]
                    while stack:
                        i, amount = stack.pop()
                        key = (i, amount)
                        if key in memo:
                            continue
                        if amount == 0:
                            memo[key] = True
                            continue
                        if i == len(COIN_TYPES):
                            memo[key] = False
                            continue
                        max_use = min(avail_coins[i], amount // COIN_TYPES[i])
                        # On essaiera d'utiliser 0..max_use pièces
                        possible = False
                        for use in range(max_use+1):
                            next_key = (i+1, amount - COIN_TYPES[i]*use)
                            if next_key in memo:
                                if memo[next_key]:
                                    possible = True
                                    break
                            else:
                                stack.append(next_key)
                        memo[key] = possible
                    return memo.get((0, rest_pay), False)

                # Pour éviter coût important, on utilise un simple DP bottom-up :

                dp_can = [False]*(rest_pay+1)
                dp_can[0] = True
                for ci, cval in enumerate(COIN_TYPES):
                    maxcount = avail_coins[ci]
                    for _ in range(maxcount):
                        for v in range(rest_pay - cval, -1, -1):
                            if dp_can[v]:
                                dp_can[v+cval] = True
                can_pay = dp_can[rest_pay]

                if not can_pay:
                    continue

                # Si on peut payer pay :
                # On enlève les pièces utilisées pour payer rest_pay (exact)
                # On ajoute les pièces de la monnaie rendue (change_coins)

                # Pour enlever pièces utilisées :
                # On doit trouver une combinaison d'utilisation des pièces pour rest_pay.
                # On récupère une combination avec technique DP arrière.

                # On refait DP avec trace :

                dp_track = [None]*(rest_pay+1)
                dp_track[0] = [0]*len(COIN_TYPES)
                for ci, cval in enumerate(COIN_TYPES):
                    maxcount = avail_coins[ci]
                    for _ in range(maxcount):
                        for v in range(rest_pay - cval, -1, -1):
                            if dp_track[v] is not None:
                                if dp_track[v + cval] is None:
                                    dp_track[v + cval] = dp_track[v][:]  # copie
                                    dp_track[v + cval][ci] +=1

                used_coins = dp_track[rest_pay]
                if used_coins is None:
                    continue  # impossible mais déjà testé

                # On calcule les nouvelles pièces après paiement et rendu monnaie
                new_coins_list = []
                # Pieces en main - utilisés + rendu monnaie (sauf pièces 500 yen rendues! Car 500 yen revient en pièce importante)
                # Ici, la monnaie rendue contient pièces 500 yen, qu'on doit ajouter à notre compte.

                for i,count in enumerate(avail_coins):
                    new_coins_list.append(count - used_coins[i])
                # Ajout pièces rendues (1,5,10,50,100) + pièces 500 yen (nombre)
                # moedas rendue en dict change_coins

                for i, c in enumerate(COIN_TYPES):
                    new_coins_list[i] += change_coins.get(c, 0)
                new_500_count = num_500 + change_coins.get(500, 0)

                # On vérifie validité de l'état (pas trop de pièces pour empêcher explosion)
                new_coins_tpl = tuple(new_coins_list)
                if not coins_tuple_is_valid(new_coins_tpl):
                    continue

                # Calcul de la dépense totale = expense + pay
                new_expense = expense + pay

                key = (new_500_count, new_coins_tpl)
                if ndp[key] > new_expense:
                    ndp[key] = new_expense

        # Nouvel état
        dp = ndp

    # Après tous magasins
    # Trouver max nombre pièces 500, puis la dépense minimale associée
    max_500 = max(k[0] for k in dp.keys())
    min_expense = min(v for (c500, _), v in dp.items() if c500 == max_500)
    return max_500, min_expense

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        prices = []
        for _ in range(n):
            prices.append(int(input()))
        c, s = dp_solution(prices)
        print(c, s)

if __name__ == "__main__":
    main()