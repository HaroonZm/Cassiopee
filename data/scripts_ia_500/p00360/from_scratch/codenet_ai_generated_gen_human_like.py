s = list(input())
k = int(input())
n = len(s)

for i in range(n):
    if k <= 0:
        break
    # Trouver le plus petit caractère dans la fenêtre s[i:i+k+1]
    pos = i
    limit = min(n, i + k + 1)
    for j in range(i + 1, limit):
        if s[j] < s[pos]:
            pos = j
    if pos != i:
        # Effectuer des swaps pour amener s[pos] à l'indice i
        c = s[pos]
        for m in range(pos, i, -1):
            s[m] = s[m - 1]
        s[i] = c
        k -= (pos - i)

print("".join(s))