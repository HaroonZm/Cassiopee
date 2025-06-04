import sys
import bisect

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    # Lecture des données d'entrée
    N, K = map(int, input().split())
    T = int(input())
    # On récupère chaque tâche effectuée : intervalle [l,r] et ID x
    tasks_done = [tuple(map(int, input().split())) for _ in range(T)]

    # Pour chaque décoration x (1..K), on stocke les intervalles où cette tâche x a été appliquée
    # sous forme de liste de tuples (l,r)
    interval_by_task = [[] for _ in range(K+1)]

    for l, r, x in tasks_done:
        interval_by_task[x].append((l, r))

    # Cette fonction fusionne une liste d'intervalles qui peuvent se chevaucher
    # pour obtenir une liste d'intervalles disjoints et triés
    def merge_intervals(intervals):
        if not intervals:
            return []
        # trier par borne gauche
        intervals.sort()
        merged = []
        curr_l, curr_r = intervals[0]
        for l, r in intervals[1:]:
            if l <= curr_r + 1:
                # chevauchement ou continuité, on étend la borne droite
                if r > curr_r:
                    curr_r = r
            else:
                # pas de chevauchement, on ajoute l'intervalle courant puis passe au suivant
                merged.append((curr_l, curr_r))
                curr_l, curr_r = l, r
        merged.append((curr_l, curr_r))
        return merged

    # Pour chaque tâche entre 1 et K, on fusionne ses intervalles de tâches effectuées
    for x in range(1, K+1):
        interval_by_task[x] = merge_intervals(interval_by_task[x])

    # Maintenant on doit trouver les donuts qui ont été décorés dans l'ordre 1..K avec un intervalle consécutif pour chaque tâche
    # On va progresser tâche par tâche pour restreindre les positions possibles des donuts pour que la séquence soit respectée

    # current_intervals représente les positions des donuts décorés jusqu'à la tâche k-1 (intervalles fusionnés, disjoints)
    # Au départ, avant la 1ère tâche, tous les donuts peuvent être candidats (tout l'intervalle)
    current_intervals = [(1, N)]

    # Pour chaque tâche dans l'ordre 1..K, on fait l'intersection des intervalles courants avec les intervalles où cette tâche a été appliquée
    # Cela car, pour qu'un donut soit correctement décoré dans l'ordre, il doit être dans un intervalle où la tâche k a été appliquée,
    # et aussi dans current_intervals correspondant aux tâches précédentes.
    def intersect_intervals(A, B):
        # Intersection entre deux listes d'intervalles triés et disjoints A et B
        res = []
        i = j = 0
        while i < len(A) and j < len(B):
            a_l, a_r = A[i]
            b_l, b_r = B[j]
            # On calcule la borne gauche de la tranche d'intersection potentielle
            left = max(a_l, b_l)
            right = min(a_r, b_r)
            if left <= right:
                res.append((left, right))
            # On avance dans la liste qui a l'intervalle qui se termine le plus tôt
            if a_r < b_r:
                i += 1
            else:
                j += 1
        return res

    # On itère en imposant la contrainte de la tâche suivante
    for x in range(1, K+1):
        current_intervals = intersect_intervals(current_intervals, interval_by_task[x])
        if not current_intervals:
            # Aucun donut satisfait les contraintes, on peut arrêter
            print(0)
            return

    # A la fin, current_intervals contient les positions des donuts qui ont été décorés dans l'ordre complet 1..K
    # On calcule la somme des tailles des intervalles pour donner le nombre total de donuts valides
    result = 0
    for l, r in current_intervals:
        result += r - l + 1

    print(result)

if __name__ == "__main__":
    main()