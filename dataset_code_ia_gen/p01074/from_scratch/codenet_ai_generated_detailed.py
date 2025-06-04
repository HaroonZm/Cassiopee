# On modélise les horaires comme un ensemble de créneaux 5 jours * N cours/jour = 5*N maximum 40.
# Chaque cours occupe plusieurs créneaux consécutifs dans un jour donné.
# Le problème est une sélection de cours (max L) sans chevauchement de créneaux, maximisant la somme des bonheur t_i.

# On code une solution avec programmation dynamique par masque d'occupation des créneaux.
# Chaque cours est représenté par un masque binaire indiquant les créneaux occupés.
# On trie les cours, puis on fait DP sur (masque occupation, nombre de cours pris),
# on essaie d'ajouter un cours qui ne chevauche pas et met à jour le max bonheur.

# Cette solution est possible car au maximum on a 5*8=40 créneaux,
# L max <= min(5*N, M) donc au pire 40 ou 300,
# les états sont donc gérables avec stockage intelligent.

import sys
input = sys.stdin.readline

def main():
    N, M, L = map(int, input().split())

    classes = []
    for _ in range(M):
        d, a, k, t = map(int, input().split())
        # Créneaux couvrerts : du (d*N + (a-1)) au (d*N + (a-1)+(k-1))
        mask = 0
        start = d * N + (a - 1)
        for x in range(k):
            mask |= 1 << (start + x)
        classes.append((mask, t))

    # DP: dict clé = (masque_occupation_cours), valeur = bonheur maximum atteint avec certains cours
    # on limitera à selectionner au plus L cours.
    # Comme on doit aussi limiter le nombre de cours, on gardera un tableau dp[l][mask] = max bonheur
    # où l = nombre de cours pris, mask = occupation

    from collections import defaultdict

    dp = [defaultdict(lambda: -1) for _ in range(L+1)]
    dp[0][0] = 0  # sans cours, pas d'occupation, bonheur 0

    for mask_class, t in classes:
        # on itère en arrière sur le nombre de cours pour éviter doubles comptes
        for l in range(L-1, -1, -1):
            for occ_mask, val in dp[l].items():
                if val == -1:
                    continue
                if (occ_mask & mask_class) == 0:
                    # pas de chevauchement, on peut ajouter ce cours
                    new_mask = occ_mask | mask_class
                    if dp[l+1][new_mask] < val + t:
                        dp[l+1][new_mask] = val + t

    # La réponse est le max dp[l][mask] avec l <= L pour tout mask
    ans = 0
    for l in range(L+1):
        if dp[l]:
            ans = max(ans, max(dp[l].values()))

    print(ans)

if __name__ == "__main__":
    main()