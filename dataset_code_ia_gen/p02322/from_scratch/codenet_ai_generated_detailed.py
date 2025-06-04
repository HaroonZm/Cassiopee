# Solution complète en Python pour le problème "Knapsack Problem with Limitations II"
# Approche :
# Le problème est une variante du problème du sac à dos avec un nombre limité d'objets par item.
# Contraintes :
# - N ≤ 50
# - W jusqu’à 10^9 (très grand)
# - poids et nombre max d'items très grands aussi.

# La méthode classique en poids (dp sur poids) n’est pas faisable à cause du poids maximal.
# On remarque que la valeur max par item est petite (≤ 50) et que N est petit,
# ce qui suggère de travailler en DP sur la valeur totale, en minimisant le poids nécessaire pour atteindre cette valeur.
# Puis on cherche la valeur maximale dont le poids est ≤ W.

# On transforme les items en "items décomposés" par la technique de décomposition binaire du nombre m_i,
# pour gérer la limite d'items sans boucle excessive.

# DP:
# On crée dp[v] = poids minimum nécessaire pour atteindre exactement la valeur v.
# On initialise dp[0] = 0, les autres très grands.

# On met à jour dp pour chaque "item décomposé".

# Enfin, on parcour dp pour trouver la valeur maximale avec poids ≤ W.

import sys
input = sys.stdin.readline

def main():
    N, W = map(int, input().split())
    items = []
    max_total_value = 0

    for _ in range(N):
        v, w, m = map(int, input().split())
        # On décompose la quantité m en puissances de 2 pour gérer la limite
        # Cette décomposition permet de traiter chaque groupe comme un objet 0/1 classique
        k = 1
        while m > 0:
            cnt = min(k, m)
            m -= cnt
            items.append((v * cnt, w * cnt))  # valeur totale et poids total du groupe
            max_total_value += v * cnt
            k <<= 1

    # On initialise le dp avec un nombre très grand (inf) pour le poids
    INF = 10**18
    dp = [INF] * (max_total_value + 1)
    dp[0] = 0

    # Pour chaque groupe d’objets, on met à jour le dp
    for value_group, weight_group in items:
        # On fait une mise à jour du dp à partir de la valeur max vers la valeur_group pour éviter le recalcul multiple
        for val in range(max_total_value - value_group, -1, -1):
            if dp[val] != INF:
                new_val = val + value_group
                new_weight = dp[val] + weight_group
                if new_weight < dp[new_val]:
                    dp[new_val] = new_weight

    # On récupère la meilleure valeur possible pour un poids ≤ W
    answer = 0
    for val in range(max_total_value + 1):
        if dp[val] <= W:
            answer = val

    print(answer)

if __name__ == "__main__":
    main()