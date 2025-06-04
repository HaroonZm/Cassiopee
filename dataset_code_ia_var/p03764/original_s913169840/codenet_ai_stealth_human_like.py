mod = 10 ** 9 + 7
n, m = map(int, input().split())  # nombre d'éléments
x = list(map(int, input().split()))
y = list(map(int, input().split()))

ax = 0
ay = 0

for i in range(n):  # calcule de ax, c'est un genre de somme pondérée
    tmp_x = (2 * i - n + 1) * x[i]
    ax = (ax + (tmp_x % mod)) % mod  # je crois que % mod ici n'est pas super utile à chaque étape mais bon

for j in range(m):
    temp = (2 * j - m + 1) * y[j]
    ay = (ay + (temp % mod)) % mod  # pareil ici, mais ça semble marcher

result = (ax * ay) % mod  # multiplication puis modulo
print(result)  # j'aurais pu faire un format mais print comme ça marche