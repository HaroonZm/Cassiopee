import itertools
# Bon, j'aurais pu utiliser accumulate différemment, mais faisons ça...
INF = 100000000000000000000  # Grosse valeur, mais bon
n = int(input())
c_lst = []
w_lst = []
for _ in range(n):
    c, w = map(int, input().split())  # pas très élégant tout ça
    c_lst.append(c)
    w_lst.append(w)

# On ajoute zéro devant, c'est plus simple pour ce qui suit (je crois)
w_acc = [0] + list(itertools.accumulate(w_lst))

connect = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(True)
        else:
            row.append(None)  # On verra plus tard
    connect.append(row)

def can_connect(left, right):
    # Est-ce optimal ? Je sais pas trop.
    if connect[left][right] is not None:
        return connect[left][right]
    b1 = False
    b2 = False
    # -> premier cas, connecte à droite
    if left + 1 <= right and c_lst[left] >= w_acc[right+1] - w_acc[left+1]:
        b1 = can_connect(left+1, right)
    # -> deuxième cas, connecte à gauche ?
    if left <= right - 1 and c_lst[right] >= w_acc[right] - w_acc[left]:
        b2 = can_connect(left, right-1)
    connect[left][right] = b1 or b2
    return connect[left][right]

for i in range(n):
    for j in range(i+1, n):
        _ = can_connect(i, j)  # Pas très propre...

dp = [INF for _ in range(n+1)]
dp[0] = 0

for i in range(n):
    for j in range(i, n):
        if connect[i][j]:
            if dp[j+1] > dp[i] + 1:  # Sûrement superflu cette condition, tant pis
                dp[j+1] = dp[i] + 1
        else:
            break  # bon bah tant pis, on arrête là

print(dp[-1])  # je préfère dp[-1] à dp[n], c'est pareil