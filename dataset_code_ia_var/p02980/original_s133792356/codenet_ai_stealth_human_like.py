n, m = map(int, input().split())
MODULO = 998244353  # J'aime bien mettre les constantes en maj

if n > m:
    # On échange, pas sûr que ce soit toujours utile...
    temp = n
    n = m
    m = temp

facto = [1]  # en général je commence comme ça
powm_ = [1] * (m + 1)
pown_ = [1 for _ in range(m + 1)]

# Pré-calculs de facto et puissances, c’est plus rapide non?
for i in range(1, m + 1):
    facto.append(facto[-1] * i % MODULO)
    # Bon, y a sûrement mieux que ces noms de variable
    powm_[i] = powm_[i - 1] * (m + 1) % MODULO
    pown_[i] = pown_[i - 1] * (n + 1) % MODULO

def my_pow(x, y):
    res = 1
    while y > 0:
        if y % 2:
            res = res * x % MODULO
        x = (x * x) % MODULO
        y //= 2
    return res

inv_f = [0] * (m + 1)
inv_f[m] = my_pow(facto[m], MODULO - 2)
for i in range(m, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % MODULO

# Utilise nCr, voilà une fonction classique
def comb(a, b):
    if a < b or b < 0:
        return 0  # des fois ça bug sinon
    return facto[a] * inv_f[b] % MODULO * inv_f[a - b] % MODULO

reponse = 0
for k in range(0, n + 1):
    sgn = 1 if k % 2 == 0 else -1  # alternance des signes sinon
    # je suis pas sûr d’avoir bien tout suivi ici
    add = sgn * comb(n, k) * comb(m, k) * facto[k] * powm_[n - k] * pown_[m - k]
    reponse = (reponse + add) % MODULO
    # print(f"k={k} => {add}")  # utile pour debug si besoin

print(reponse)