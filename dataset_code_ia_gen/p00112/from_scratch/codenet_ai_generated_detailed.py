# Solution python complète avec commentaires détaillés

import sys

def main():
    input = sys.stdin.readline  # Utiliser readline pour une lecture efficace
    while True:
        n = int(input())
        if n == 0:  # Condition de fin : ligne contenant 0
            break

        times = [int(input()) for _ in range(n)]  # liste des temps par client

        # Objectif : minimiser la somme des temps d'attente cumulés
        # Approche classique : trier les temps de service par ordre croissant (SJF - Shortest Job First)
        times.sort()

        total_waiting_time = 0
        current_time = 0
        for t in times:
            # Pour chaque client, son temps d'attente est le temps cumulé avant son service
            total_waiting_time += current_time
            current_time += t

        print(total_waiting_time)

if __name__ == "__main__":
    main()