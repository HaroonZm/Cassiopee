# Lecture des entrées
N, M, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

from itertools import combinations
# On cherche la valeur maximale possible des pommes de terre récoltées après 1 an

max_potatoes = 0

# On teste toutes les combinaisons de K champs parmi les N
for fields in combinations(range(N), K):
    # fields contient les indices des champs sélectionnés, par exemple (0,2,4)
    
    # On va distribuer les M pommes de terre à planter dans ces champs
    # Chaque champ i peut recevoir au maximum b[i] pommes de terre
    
    # Initialisation d'un tableau dp :
    # dp[j] = nombre maximal de pommes de terre récoltées en ayant planté j pommes au total
    dp = [-1]*(M+1)
    dp[0] = 0  # Pas de pommes plantées = 0 récoltées
    
    for i in fields:
        # Pour le champ i, on crée un tableau temporaire pour mise à jour du dp
        ndp = [-1]*(M+1)
        max_plant = min(b[i], M)
        
        # On essaie toutes les quantités x possibles à planter sur ce champ i
        for j in range(M+1):
            if dp[j] < 0:
                continue
            for x in range(max_plant+1):
                if j + x > M:
                    break
                # pommes de terre récoltées = pommes déjà récoltées + x * a[i]
                val = dp[j] + x * a[i]
                if val > ndp[j+x]:
                    ndp[j+x] = val
        dp = ndp
    
    # Après avoir traité ces champs, on cherche le maximum total de pommes de terre récoltées,
    # et on ajoute les pommes de terre non plantées (M - total planté)
    for j in range(M+1):
        if dp[j] < 0:
            continue
        total = dp[j] + (M - j)  # Les pommes non plantées restent telles quelles
        if total > max_potatoes:
            max_potatoes = total

print(max_potatoes)