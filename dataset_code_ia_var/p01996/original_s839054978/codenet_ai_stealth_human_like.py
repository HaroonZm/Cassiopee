# Je suis sur mobile donc code rapide !
n, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = list(filter(lambda x: x <= m, a))   # Pourquoi pas une boucle ?
ans = m - len(b)
print(ans)
# ça devrait marcher je crois