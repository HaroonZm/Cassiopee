# Solution Python complète pour le problème "沢山の種類の林檎 (Many Kinds of Apples)"

# Approche :
# - On initialise un tableau `capacities` pour stocker la capacité maximale de chaque boîte.
# - On initialise un tableau `apples` pour garder le nombre actuel de pommes dans chaque boîte (initialement 0).
# - On parcours ensuite chaque instruction :
#   * Si c'est une instruction de récolte (t=1), on essaye d'ajouter `d` pommes dans la boîte `x`.
#       - Si cela dépasse la capacité, c'est une instruction impossible, on renvoie `x`.
#   * Si c'est une instruction de livraison (t=2), on essaye d'enlever `d` pommes dans la boîte `x`.
#       - Si on n'a pas assez de pommes, c'est une instruction impossible, on renvoie `x`.
# - Si toutes les instructions sont possibles, on renvoie 0.

import sys
input = sys.stdin.readline

def main():
    # Lecture du nombre de boîtes / espèces
    N = int(input())
    # Lecture des capacités maximales des boîtes
    capacities = list(map(int, input().split()))
    # Initialisation du tableau de stockage actuel des pommes
    apples = [0] * N
    # Lecture du nombre d'instructions à traiter
    Q = int(input())
    
    for _ in range(Q):
        t, x, d = map(int, input().split())
        x -= 1  # indice zéro-based pour simplifier la gestion en tableau
        
        if t == 1:
            # Récolte d'apples dans la boîte x
            if apples[x] + d > capacities[x]:
                # Instruction impossible : dépassement de capacité
                print(x + 1)  # renvoi indice 1-based
                return
            apples[x] += d
        else:
            # Livraison d'apples depuis la boîte x
            if apples[x] < d:
                # Instruction impossible : pas assez d'apples à livrer
                print(x + 1)
                return
            apples[x] -= d
    
    # Si on arrive ici, toutes les instructions sont possibles
    print(0)

if __name__ == "__main__":
    main()