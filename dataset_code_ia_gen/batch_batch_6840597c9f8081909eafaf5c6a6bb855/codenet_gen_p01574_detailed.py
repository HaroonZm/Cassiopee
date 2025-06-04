# Solution explicative :
# Le problème demande s'il est possible, en appuyant exactement N fois sur des boutons,
# de faire en sorte que toutes les N positions autour d'un cadran soient allumées.
# 
# Chaque bouton déplace la "main" d'un nombre de positions Li.
# Le cadran est circulaire avec N positions (numérotées de 0 à N-1).
# 
# On commence avec tous les voyants éteints, la main pointant sur une position initiale (supposée 0).
# Après chaque pression, la main tourne Li positions dans le sens horaire, et la position pointée est allumée.
# Après N pressions, il faut que toutes les positions soient allumées.
#
# Or, si on note G = gcd(L1, L2, ..., LM, N), alors les positions atteignables par une somme de Li
# sont tous les multiples de G modulo N.
# Si G != 1, on ne peut jamais atteindre toutes les positions, car la main tourne toujours en sautant des positions.
#
# Par conséquent:
# - Calculer G = gcd(L1, L2, ..., LM, N)
# - Si G == 1, alors la réponse est "Yes"
# - Sinon, "No"
#
# Cette solution est efficace même pour des valeurs très grandes de N (jusqu'à 10^9)
# et un grand nombre de boutons (jusqu'à 10^5).

import sys
import math

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    gcd_all = N  # initialisation avec N
    
    for _ in range(M):
        Li = int(input())
        # Calculer le gcd cumulatif
        gcd_all = math.gcd(gcd_all, Li)
    
    # Si gcd_all == 1, on peut parcourir toute la circonférence
    if gcd_all == 1:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()