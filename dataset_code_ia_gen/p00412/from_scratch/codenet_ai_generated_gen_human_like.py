import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    lanes = [deque() for _ in range(N)]

    for _ in range(M):
        info = input().split()
        t = int(info[0])

        if t == 1:
            car = int(info[1])
            # Trouver la file avec le moins de voitures
            min_len = min(len(lane) for lane in lanes)
            for i in range(N):
                if len(lanes[i]) == min_len:
                    lanes[i].append(car)
                    break
        else:
            lane_num = int(info[1]) - 1
            # Retirer la voiture en tête et afficher son numéro
            finished_car = lanes[lane_num].popleft()
            print(finished_car)

if __name__ == "__main__":
    main()