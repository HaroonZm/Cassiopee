n, k = map(int, input().split())
mod = 10**9 + 7
maxn = 1000

fct = [0 for _ in range(maxn + 1)]
inv = [0 for _ in range(maxn + 1)]
fct[0] = 1
inv[0] = 1
for i in range(maxn):
    fct[i + 1] = fct[i] * (i + 1) % mod
inv[maxn] = pow(fct[maxn], mod - 2, mod)
for i in range(maxn - 1, -1, -1):
    inv[i] = inv[i + 1] * (i + 1) % mod

stl = [[0 for j in range(maxn + 1)] for i in range(maxn + 1)]
bel = [[0 for j in range(maxn + 1)] for i in range(maxn + 1)]
prt = [[0 for j in range(maxn + 1)] for i in range(maxn + 1)]

stl[0][0] = 1
bel[0][0] = 1
for i in range(maxn):
    for j in range(maxn):
        stl[i + 1][j + 1] = (stl[i][j] + (j + 1) * stl[i][j + 1]) % mod
for i in range(maxn):
    for j in range(maxn):
        bel[i + 1][j + 1] = (bel[i + 1][j] + stl[i + 1][j + 1]) % mod
for j in range(maxn):
    prt[0][j] = 1
for i in range(maxn):
    for j in range(maxn):
        if i - j >= 0:
            prt[i + 1][j + 1] = (prt[i + 1][j] + prt[i - j][j + 1]) % mod
        else:
            prt[i + 1][j + 1] = prt[i + 1][j] % mod

# tw1 through tw12 as big if-elif-else
def solve(n, k, equate_element=False, equate_subset=True, less_than_1=False, more_than_1=False):
    a = equate_element
    b = equate_subset
    c = less_than_1
    d = more_than_1
    id = a * 3 + b * 6 + c + d * 2
    if id == 0: # tw1
        return pow(k, n, mod)
    elif id == 1: # tw2
        if k - n < 0: return 0
        return fct[k] * inv[k - n] % mod
    elif id == 2: # tw3
        return stl[n][k] * fct[k] % mod
    elif id == 3: # tw4
        if k == 0: return 0
        return fct[n + k - 1] * inv[n] * inv[k - 1] % mod
    elif id == 4: # tw5
        if k - n < 0: return 0
        return fct[k] * inv[n] * inv[k - n] % mod
    elif id == 5: # tw6
        if n - k < 0 or k == 0: return 0
        return fct[n - 1] * inv[k - 1] * inv[n - k] % mod
    elif id == 6: # tw7
        return bel[n][k]
    elif id == 7: # tw8
        if k - n < 0: return 0
        return 1
    elif id == 8: # tw9
        return stl[n][k]
    elif id == 9: # tw10
        return prt[n][k]
    elif id == 10: # tw11
        if k - n < 0: return 0
        return 1
    elif id == 11: # tw12
        if n - k < 0: return 0
        return prt[n - k][k]
    return 0

print(solve(n, k, 0, 1, 0, 0))