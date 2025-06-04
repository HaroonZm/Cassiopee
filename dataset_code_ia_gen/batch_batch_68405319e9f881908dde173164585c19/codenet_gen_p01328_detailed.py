import sys
import math

def main():
    input = sys.stdin.readline
    
    while True:
        # Lire N et M
        line = input()
        if not line:
            break
        N, M = map(int, line.split())
        # Condition d'arrêt
        if N == 0 and M == 0:
            break
        
        cats = []
        for _ in range(N):
            x, y, c = map(int, input().split())
            cats.append((x, y, c))
        
        feeders = []
        for _ in range(M):
            x = int(input())
            feeders.append(x)
        
        # On trie les emplacements des feeders par leur x pour gérer le tie break
        feeders.sort()
        
        # Pour chaque groupe de chats, on cherche le feeder le plus proche
        # En cas d'égalité de distance, on choisit celui avec abscisse la plus petite (déjà triés)
        # On attribue donc chaque groupe au feeder unique correspondant
        
        # Compteur du nombre de chats par feeder
        # clé : x du feeder, valeur : nombre de chats attribués
        cats_per_feeder = {x:0 for x in feeders}
        
        for (cx, cy, cc) in cats:
            min_dist = None
            chosen_feeder = None
            # calculer la distance au carré (pas besoin de racine carrée pour comparer)
            for fx in feeders:
                dist_sq = (fx - cx)**2 + (0 - cy)**2
                if min_dist is None or dist_sq < min_dist:
                    min_dist = dist_sq
                    chosen_feeder = fx
                elif dist_sq == min_dist:
                    # Tie break : on garde celui avec x plus petit
                    if fx < chosen_feeder:
                        chosen_feeder = fx
            cats_per_feeder[chosen_feeder] += cc
        
        # Chercher le maximum de chats sur un même feeder
        max_cats = max(cats_per_feeder.values()) if cats_per_feeder else 0
        
        print(max_cats)


if __name__ == "__main__":
    main()