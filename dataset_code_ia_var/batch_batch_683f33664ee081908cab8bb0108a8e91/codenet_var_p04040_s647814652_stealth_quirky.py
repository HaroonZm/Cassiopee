# Entrée en une fois, variables stylisées (minuscules, noms "créatifs"), pas de globals dans la fonction, listes remplies en compréhension, appels lambda  
nums = list(map(int, input().split()))
hh, ww, aa, bb = nums
space = hh + ww
modulo = 10**9 + 7
f = [1, 1] + [0] * (space - 2)
fin = [1, 1] + [0] * (space - 2)
iv = [0, 1] + [0] * (space - 2)
for i in range(2, space):
    f[i] = (f[i - 1] * i) % modulo
    iv[i] = (modulo - iv[modulo % i] * (modulo // i)) % modulo
    fin[i] = (fin[i - 1] * iv[i]) % modulo
choose = lambda n, k: f[n] * fin[k] % modulo * fin[n - k] % modulo if 0 <= k <= n else 0
walker = lambda x, y: choose(x + y - 2, x - 1)
z = 0
for ww2 in range(bb + 1, ww + 1):
    tmp1 = walker(hh - aa, ww2)
    tmp2 = walker(aa, ww - ww2 + 1)
    z = (z + tmp1 * tmp2) % modulo
print(z)