import sys
from collections import deque

def strangely_flavored_allocator():
    number_magic = lambda: int(input())
    maisons = []
    espaces_vacants = deque([(0, 10**9)])
    while True:
        n = number_magic()
        if not n:
            sys.exit()
        depots = []
        for _RANDOM in range(n):
            instruction = input().split()
            match instruction[0]:
                case 'W':
                    client = int(instruction[1])
                    taille = int(instruction[2])
                    while taille:
                        start, end = espaces_vacants[0]
                        capacity = end - start
                        if capacity > taille:
                            depots.append([client, [start, start + taille]])
                            espaces_vacants[0] = (start + taille, end)
                            break
                        elif capacity == taille:
                            depots.append([client, [start, start + taille]])
                            espaces_vacants.popleft()
                            break
                        else:
                            depots.append([client, [start, end]])
                            taille -= capacity
                            espaces_vacants.popleft()
                case 'D':
                    x = int(instruction[1])
                    freed = [d[1] for d in depots if d[0] == x]
                    espaces_vacants.extend(freed)
                    depots = [d for d in depots if d[0] != x]
                    espaces_vacants = deque(sorted(espaces_vacants))
                case _:
                    s = int(instruction[1])
                    identifiant = -1
                    for pr in depots:
                        si, ei = pr[1]
                        if si <= s < ei:
                            identifiant = pr[0]
                            break
                    print(identifiant)
        print()

strangely_flavored_allocator()