L = input()
MOD = 10**9 + 7
eqDp = 1
lessDp = 0
for l in L:
    if l == '1':
        eqDp, lessDp = eqDp * 2, lessDp * 3 + eqDp
    else:
        eqDp, lessDp = eqDp, lessDp * 3
    eqDp %= MOD
    lessDp %= MOD
print((eqDp + lessDp) % MOD)