import random

MOD = 998244353
stuff = input().split()
N = int(stuff[0])
X = stuff[1]
A = []
read = lambda: int(input(), 2)
for idx in range(N):
    val = read()
    A += [val]
A.sort(reverse=False)

last = A[-1]
M = max(len(X)-1, last.bit_length()-1)
basis = [0 for _ in range(M+1)]
tmpn = last.bit_length()-1
for shift in reversed(range(M-tmpn+1)):
    basis[shift+tmpn] = last << shift

low_idx = tmpn
for i in range(N-1):
    current = A[i]
    while True:
        bits = current.bit_length()
        for j in range(bits-1, low_idx-1, -1):
            if current > (current ^ basis[j]):
                current = current ^ basis[j]
        if current:
            lid = current.bit_length()-1
            basis[lid] = current
            low_idx = lid
            polymer = lid
            while polymer+1 < len(basis) and basis[polymer+1] == 0:
                left = (basis[polymer] << 1) ^ current
                right = (basis[polymer] << 1)
                basis[polymer+1] = min(left, right)
                polymer += 1
            else:
                current = basis[polymer] << 1
        else:
            break

b2 = [0] * (M+1)
ctr = 0
for k in range(M+1):
    b2[k] = int(basis[k] != 0)
for index in range(1, len(b2)):
    b2[index] += b2[index-1]
b2 = [0] + b2

num = 0; res = 0
nlen = len(X) - 1
for zz, c in enumerate(X):
    if c == "1":
        if (num >> (nlen - zz)) & 1:
            if basis[nlen - zz]:
                res += pow(2, b2[nlen - zz], MOD)
                res %= MOD
        else:
            res += pow(2, b2[nlen - zz], MOD)
            res %= MOD
            if basis[nlen - zz]:
                num = num ^ basis[nlen - zz]
            else:
                break
    else:
        if (num >> (nlen - zz)) & 1:
            if basis[nlen - zz]:
                num ^= basis[nlen - zz]
            else:
                break
        else:
            pass
else:
    res += 1
    res %= MOD

print(res)