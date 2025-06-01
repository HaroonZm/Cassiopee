n, m = map(int, input().split())
rane = [[] for _ in range(n)]

from collections import deque
rane = [deque() for _ in range(n)]

def get_rane():
    # Retourne l'indice du rane avec la file de voitures la plus courte,
    # ou le premier avec une file vide si possible
    return min(range(n), key=lambda i: len(rane[i]))

for _ in range(m):
    c, num = map(int, input().split())
    if c == 0:
        num -= 1
        print(rane[num].popleft())
    else:
        rane[get_rane()].append(num)