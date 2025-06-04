# Programme complet Python pour le problème d'analyse des connexions/déconnexions des PCs

import sys
import bisect

def merge_intervals(intervals):
    """
    Fusionne une liste d'intervalles (déjà triés par début) en un ensemble minimal d'intervalles
    sans chevauchement.
    """
    if not intervals:
        return []
    merged = []
    current_start, current_end = intervals[0]
    for start, end in intervals[1:]:
        if start <= current_end:
            # chevauchement, on étend la fin
            current_end = max(current_end, end)
        else:
            # pas de chevauchement, on stocke l'ancien intervalle et on démarre un nouveau
            merged.append((current_start, current_end))
            current_start, current_end = start, end
    merged.append((current_start, current_end))
    return merged

def interval_overlap(interval1, interval2):
    """
    Calcule la durée de recouvrement entre deux intervalles (start, end).
    Renvoie 0 si pas de recouvrement.
    """
    s1, e1 = interval1
    s2, e2 = interval2
    start = max(s1, s2)
    end = min(e1, e2)
    return max(0, end - start)

def usage_in_period(intervals, query_start, query_end):
    """
    Calcule la somme des durées des intervalles d'usage (sans chevauchement)
    recouvrant la période [query_start, query_end).
    Les intervals sont une liste triée d'intervalles (start, end).
    """
    total = 0
    # Parcourir les intervalles ordonnés qui peuvent chevaucher la période demandée
    # On peut utiliser bisect pour optimiser la recherche
    # Chercher la première intervalle qui peut commencer avant query_end
    i = bisect.bisect_left(intervals, (query_end, ))
    # On regarde les intervalles avant cet indice (car ils peuvent chevaucher)
    for interval in intervals[max(i-10,0):i+10]:
        if interval[1] < query_start:
            continue
        total += interval_overlap(interval, (query_start, query_end))
    return total

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        N_M = line.strip()
        if N_M == '':
            continue
        N, M = map(int, N_M.split())
        # Condition d'arrêt
        if N == 0 and M == 0:
            break

        r = int(input())  # nombre d'enregistrements
        # dictionnaire pour stocker les connexions en cours par PC
        # et aussi stocker les intervals par étudiant
        # pc_login : key = pc, value = (student, start_time)
        pc_login = {}
        # Pour chaque étudiant, une liste d'intervalles cumulés sur tous les PCs
        student_intervals = {m: [] for m in range(1, M+1)}

        for _ in range(r):
            t, n, m, s = map(int, input().split())
            if s == 1:
                # login
                pc_login[n] = (m, t)
            else:
                # logout
                # récupérer l'étudiant qui était connecté
                logged_student, start_time = pc_login.pop(n)
                # historique de cet étudiant : ajouter intervalle
                # s'assure que c'est bien le même étudiant selon l'énoncé
                assert logged_student == m
                student_intervals[m].append((start_time, t))

        # On fusionne les intervalles pour chaque étudiant afin de gérer le multi-PC
        for m in student_intervals:
            student_intervals[m] = merge_intervals(sorted(student_intervals[m]))

        q = int(input())  # nombre de queries
        for _ in range(q):
            ts, te, m = map(int, input().split())
            # Calculer le temps d'usage du student m entre ts et te
            ans = usage_in_period(student_intervals.get(m, []), ts, te)
            print(ans)


if __name__ == "__main__":
    main()