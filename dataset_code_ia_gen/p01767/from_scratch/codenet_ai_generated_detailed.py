# Solution Python complète avec commentaires détaillés

import sys
import bisect

def main():
    input = sys.stdin.readline

    # Lecture du nombre de problèmes
    N = int(input())
    # Lecture des points de chaque problème
    a = list(map(int, input().split()))
    # Lecture du nombre de participants
    M = int(input())
    # Lecture des niveaux d'habileté des participants
    b = list(map(int, input().split()))
    # Lecture des scores cibles des participants
    c = list(map(int, input().split()))

    # Étape 1 : trier la liste des points des problèmes pour permettre une recherche efficace
    a.sort()

    # Étape 2 : construire un tableau de sommes prefixées sur les points triés
    # prefix_sum[i] = somme des a[0] à a[i-1]
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i+1] = prefix_sum[i] + a[i]

    # Étape 3 : Pour chaque participant j,
    # on veut calculer la somme des points des problèmes i tels que a_i <= b_j
    # Puis vérifier si cette somme >= c_j

    for j in range(M):
        # Utiliser bisect_right pour trouver l'indice d'insertion de b[j] dans a trié
        # Cela donne le nombre de problèmes que le participant peut résoudre
        idx = bisect.bisect_right(a, b[j])
        total_score = prefix_sum[idx]  # somme des points des problèmes pouvant être résolus

        # Vérifier si total_score >= cible c[j]
        if total_score >= c[j]:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()