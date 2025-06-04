T = input()
P = input()

n = len(T)
m = len(P)

# Trouver la première occurrence de P dans T en tant que sous-séquence
pos = -1
index_p = 0
positions = []
for i in range(n):
    if index_p < m and T[i] == P[index_p]:
        positions.append(i)
        index_p += 1
if index_p != m:
    print("no")
    exit()

# Trouver la dernière occurrence de P dans T en tant que sous-séquence (en partant de la fin)
index_p = m - 1
last_positions = []
for i in range(n-1, -1, -1):
    if index_p >= 0 and T[i] == P[index_p]:
        last_positions.append(i)
        index_p -= 1
if index_p != -1:
    print("no")
    exit()
last_positions.reverse()

# Vérifier si la première occurrence et la dernière occurrence sont identiques
if positions == last_positions:
    print("yes")
else:
    print("no")