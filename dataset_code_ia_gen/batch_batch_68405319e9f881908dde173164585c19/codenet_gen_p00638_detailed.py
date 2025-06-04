# Solution au problème Old Bridges
# 
# Résumé du problème :
# On a n îles avec des trésors et une île vide avec laquelle on accède à toutes les autres par des ponts. 
# Le voleur commence sur l’île vide, veut visiter toutes les îles pour récolter tous les trésors, 
# et revenir à l’île vide. Le pont entre l’île vide et chaque île a une capacité maximale de trésors 
# que l’on peut transporter pour traverser ce pont. Le voleur peut transporter tous les trésors qu’il possède, 
# mais si le total de trésors dépasse la capacité du pont utilisé, le pont casse.
# 
# La question est : existe-t-il un ordre de visite des îles tel que le voleur puisse ramener tous les trésors et retourner à l’île vide 
# en respectant les contraintes de capacité des ponts à chaque passage ?
#
# Approche :
# - On note n le nombre d’îles avec trésors.
# - On connaît chaque île avec deux valeurs : sa quantité de trésors (T_i) et la capacité maximale du pont (C_i) pour y accéder.
# - Le voleur se déplace uniquement entre l’île vide (de trésors 0) et une île avec trésors.
# - Le voleur doit visiter toutes les îles exactement une fois (visiter = ramasser les trésors).
# 
# Observations importantes :
# - Quand on traverse un pont vers une île i, on ne transporte pas encore les trésors de cette île, 
#   donc la charge est la somme des trésors déjà collectés, sans T_i.
# - Quand on fait demi-tour (retour vers l’île vide depuis i), on transporte la totalité des trésors en poche, y compris T_i.
# - La capacité du pont i (C_i) s’applique aux deux traversées : 
#    - à l’aller, on doit transporter la somme des trésors déjà collectés (sans T_i), qui doit être ≤ C_i
#    - au retour, on transporte la totalité des trésors (avec T_i), qui doit être ≤ C_i
#
# Stratégie pour vérifier une séquence d'îles:
# Pour une séquence d'îles [i1, i2, ..., in]:
#     charge avant de traverser pont i_k = somme des T_j pour j avant k dans la séquence
#         Doit être ≤ C_{i_k}
#     charge au retour du pont i_k = somme des T_j pour toutes les îles (car on a tout collecté)
#         Doit être ≤ C_{i_k}
#
# Donc on peut faire un DFS/backtracking pour vérifier si :
# - Il existe une permutation des îles 1..n (indice depuis 0)
#   telle que pour chaque île visitée à l'étape k, 
#   la somme des trésors déjà récoltés ≤ C_i (pour l’aller)
#   et la somme totale des trésors ≤ C_i (pour le retour)
#
# Si une permutation valide existe, on affiche "Yes" sinon "No".
#
# Comme n ≤ 25, un backtracking naïf est trop coûteux (25! permutations).
# On peut optimiser :
# - Les contraintes sur le retour ne dépendent que de la capacité de pont (C_i) et de la somme totale S des trésors.
# - Pour qu’il existe une solution, la capacité max des ponts doit au moins pouvoir contenir S.
# - On peut faire un backtracking avec mémo en utilisant un masque bit (les îles visitées)
#   et garder la somme des trésors récoltés (pour vérifier la capacité à l’aller).
# - A chaque étape, on essaie d’ajouter une île non visitée i si la somme des trésors déjà récoltés est ≤ C_i
#   et si le total S ≤ C_i (pour le retour).
#
# Complexity: 2^n * n, réalisable pour n=25 avec pruning et mémorisation.
#
# Implémentation:
# - Mémoisation par dict avec clé = état (bitmask)
# - Fonction dfs(mask, current_sum) qui essaye les îles restantes.
# - current_sum = somme des trésors déjà collectés.
# - Pour la première traversée à une île i, check current_sum ≤ C_i et total ≤ C_i.
# - Quand toutes les îles sont visitées, on a trouvé une solution.


import sys
sys.setrecursionlimit(10**7)

def solve():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        treasures = []
        capacities = []
        for _ in range(n):
            t, c = map(int, input().split())
            treasures.append(t)
            capacities.append(c)

        total_treasures = sum(treasures)

        # Condition nécessaire rapide : 
        # chaque capacité doit supporter le total_treasures (retour)
        # sinon impossible
        possible_to_return = all(cap >= total_treasures for cap in capacities)
        if not possible_to_return:
            print("No")
            continue

        from functools import lru_cache

        @lru_cache(None)
        def dfs(visited_mask, current_sum):
            # Si toutes les îles visitées, succès
            if visited_mask == (1 << n) -1:
                return True
            # Essayer d'ajouter une île non visitée
            for i in range(n):
                if not (visited_mask & (1 << i)):
                    # Aller vers île i : charge = current_sum (sans trésor de i)
                    # Doit être <= capacité du pont i
                    if current_sum <= capacities[i]:
                        # retour du pont i : total_treasures <= capacities[i], 
                        # vérifié avant l'appel global
                        if dfs(visited_mask | (1 << i), current_sum + treasures[i]):
                            return True
            return False

        if dfs(0, 0):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    solve()