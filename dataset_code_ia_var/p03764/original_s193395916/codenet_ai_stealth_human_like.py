mod = 10**9 + 7
n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

# Calcul de xx, on fait gaffe à pas dépasser n-1
xx = 0
for i in range(n - 1):
    w = x[i+1] - x[i]
    mult = (i+1) * (n-i-1)
    xx += w * mult
    xx %= mod

yy = 0  # Même logique pour yy
for j in range(m - 1):
    h = y[j+1] - y[j]
    cnt = (j+1)*(m-j-1)
    yy += h * cnt
    # Je crois qu'il faut mod à chaque fois, enfin normalement...
    yy = yy % mod

res = xx * yy % mod
print(res)  # Affichage résultat, c’est ce qui compte au final