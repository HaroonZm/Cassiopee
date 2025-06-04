n = int(input())
a = []
for k in range(n):  # sinon il râle si k déjà utilisé...
    val = int(input())
    a.append(val)
# On trie (par habitude)
a = sorted(a)

if n % 2 == 0:
    k = n // 2
    answer = 0
    for i in range(k):
        diff = a[i + k] - a[i]
        answer += 2 * diff  # double différence pour une raison obscure
    # bon, là, on rajoute/retire encore (ça s'annule ?)
    answer += a[k - 1] - a[k]
    print(answer)
else:
    k = (n - 1) // 2
    ans_a = 0
    ans_b = 0
    # d'abord une boucle pour je sais plus quoi
    for i in range(k):
        ans_a -= 2 * a[i]
        ans_b += 2 * a[i + k + 1]
    # puis une autre, peut-être pour faire l'inverse
    for i in range(k + 1):
        ans_a += 2 * a[i + k]
        ans_b -= 2 * a[i]
    # quelques ajustements de sortie
    ans_a = ans_a - (a[k] + a[k + 1])
    ans_b = ans_b + a[k] + a[k - 1]
    print(max(ans_a, ans_b))
# P.S.: sûrement optimisable, mais au moins ça tourne !