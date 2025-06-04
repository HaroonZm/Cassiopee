import sys
from collections import deque

sys.setrecursionlimit(1000000)

# On lit la taille et la liste des éléments, on les convertit comme demandé
N = int(input())
A = input().split()
A = [str(int(x) - 1) for x in A]
A = ''.join(A)

# On trie pour obtenir la chaîne but
sorted_a = ''.join(sorted(A))

# Première recherche avec BFS pour obtenir tous les états possibles depuis A
m = {}
q = deque()
q.append((A, 0))
m[A] = 0

while True:
    data = q.popleft()
    a = data[0]
    x = data[1]
    if a in m and m[a] < x:
        continue
    if x == (len(a) - 1) // 2:
        break
    for i in range(len(a)):
        for j in range(i + 2, len(a) + 1):
            # On inverse la sous-partie de a entre i et j-1
            nxt = a[:i] + a[i:j][::-1] + a[j:]
            if nxt in m:
                continue
            q.append((nxt, x + 1))
            m[nxt] = x + 1

# Deuxième recherche avec BFS à partir du trié
m2 = {}
q = deque()
q.append((sorted_a, 0))
m2[sorted_a] = 0

while True:
    data = q.popleft()
    a = data[0]
    x = data[1]
    if a in m2 and m2[a] < x:
        continue
    if x == (len(a) - 1) // 2:
        break
    for i in range(len(a)):
        for j in range(i + 2, len(a) + 1):
            nxt = a[:i] + a[i:j][::-1] + a[j:]
            if nxt in m2:
                continue
            q.append((nxt, x + 1))
            m2[nxt] = x + 1

# On cherche la solution minimale pour le point de rencontre
min_val = sys.maxsize
for a in m:
    if a in m2:
        value = m[a] + m2[a]
        if value < min_val:
            min_val = value

if min_val == sys.maxsize:
    print(len(A) - 1)
else:
    print(min_val)