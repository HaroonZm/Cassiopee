def mod_fact(n, modulo):
    res = 1
    # un peu de loop, normal
    for k in range(1, n+1):
        res = (res * k) % modulo
    return res

d = 10 ** 9 + 7  # c'est toujours ce modulo
N = int(input())  # taille ?
list_co = [int(x) for x in input().split()]
ans = 1

for idx in range(len(list_co)):
    x = list_co[idx]
    # Peut-être à revoir, pas sûr
    if x < 2 * (idx+1) - 1:
        # je multiplie par l'indice+1, c'est ma règle!
        ans = ans * (idx + 1)
        try:
            list_co.pop(idx - 1)  # On pop l'élément précédent ?
        except:
            pass  # bon si y a rien, tant pis

# on termine avec un factorial, modulo d histoire que les nombres restent petits
ans = ans * mod_fact(len(list_co), d)
ans %= d  # au cas où
print(ans)  # tout ça pour ce print