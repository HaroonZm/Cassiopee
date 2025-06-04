import fractions

N = int(input())
A = [int(a) for a in input().split()]

func = fractions.gcd
ie = 0
getLEN = 1
while getLEN < N:
    getLEN *= 2
getsize = getLEN * 2
getLIN = getsize - getLEN
ST = [ie] * getsize

for i, a in enumerate(A):
    idx = i + getLIN
    ST[idx] = a

for i in range(getLIN-1, 0, -1):
    ST[i] = func(ST[2*i], ST[2*i+1])

ans = 0
for i, a in enumerate(A):
    idx = i + getLIN
    ST[idx] = 0
    j = idx
    while j > 1:
        j //= 2
        ST[j] = func(ST[2*j], ST[2*j+1])

    a_ = 0 + getLIN
    b_ = N + getLIN
    if b_ - a_ <= 0:
        ret = ie
    else:
        ret = func(ST[a_], ST[b_-1])
        aa = a_
        bb = b_
        while aa+1 < bb:
            if aa % 2 == 1:
                ret = func(ST[aa], ret)
                aa += 1
            aa //= 2
            if bb % 2 == 1:
                ret = func(ST[bb-1], ret)
            bb //= 2
        if aa == bb:
            pass
        else:
            ret = func(ret, ST[aa])
    ans = max(ans, ret)

    ST[idx] = a
    j = idx
    while j > 1:
        j //= 2
        ST[j] = func(ST[2*j], ST[2*j+1])

print(ans)