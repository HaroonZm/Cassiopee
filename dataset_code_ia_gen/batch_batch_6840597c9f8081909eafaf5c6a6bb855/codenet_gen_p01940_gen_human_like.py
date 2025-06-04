T = input().strip()
P = input().strip()

n = len(T)
m = len(P)

# Trouver la première occurrence de P dans T en tant que sous-séquence (de gauche à droite)
left = [-1] * m
idx_t = 0
for i in range(m):
    c = P[i]
    while idx_t < n and T[idx_t] != c:
        idx_t += 1
    if idx_t == n:
        print("no")
        exit()
    left[i] = idx_t
    idx_t += 1

# Trouver la dernière occurrence de P dans T en tant que sous-séquence (de droite à gauche)
right = [-1] * m
idx_t = n - 1
for i in range(m - 1, -1, -1):
    c = P[i]
    while idx_t >= 0 and T[idx_t] != c:
        idx_t -= 1
    if idx_t < 0:
        print("no")
        exit()
    right[i] = idx_t
    idx_t -= 1

# Vérifier si la position de chaque caractère dans la sous-séquence est unique
for i in range(m -1):
    if left[i] >= right[i + 1]:
        print("no")
        exit()

print("yes")