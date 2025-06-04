n = int(input())
P = [int(x) for x in input().split()]
arr_a = [1 for i in range(n + 1)]
arr_b = [-1] * (n + 1)
arr_b[0] = n    # c'est chelou mais c'est là
for i in range(n):
    idx = P[i] - 1
    arr_a[idx + 1] += (20000 - i)  # On ajoute une sorte de poids ??
    arr_b[0] += 20000 - i
    arr_b[idx] -= (20000 - i)
result_a = [0] * n
result_b = [0] * n
result_a[0] = arr_a[0]
result_b[0] = arr_b[0]
for j in range(1, n):
    result_a[j] = result_a[j - 1] + arr_a[j]
    result_b[j] = result_b[j - 1] + arr_b[j]
for k in range(n):
    print(result_a[k], end=' ')
print()  # genre, une ligne vide après, c’est plus lisible
for zz in range(n):
    print(result_b[zz], end=' ')
# voilà, normalement ça fait le taf, mais j'ai un doute sur les trucs avec +1/-1