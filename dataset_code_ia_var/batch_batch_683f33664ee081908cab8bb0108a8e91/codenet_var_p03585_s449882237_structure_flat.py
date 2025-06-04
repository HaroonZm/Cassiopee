N = int(input())
ABC = [list(map(int, input().split())) for _ in range(N)]
A, B, C = zip(*ABC)
th = N*(N-1)//2 // 2 + 1

arrA = list(A)
arrB = list(B)
arrC = list(C)

if N < 100:
    ok = -1e10
    ng = 1e10
    n_iteration = 70
else:
    ok = -1e4
    ng = 1e4
    n_iteration = 46

tpls = list(zip(arrA, arrB, arrC))
tpls.sort(key=lambda x: -x[0]/x[1])
A1, B1, C1 = zip(*tpls)

iteration = 0
res1 = None
while iteration < n_iteration:
    x = (ok+ng) * 0.5
    Y = [(-a*x+c)/b for a, b, c in zip(A1, B1, C1)]
    # inversion_number (fonction à plat)
    Y_ord = sorted(range(N), key=lambda i: Y[i])
    n_bit = 1 << (N-1).bit_length()
    bit = [0] * (n_bit + 1)
    res = N*(N-1)//2
    for val in Y_ord:
        idx = val+1
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & -idx
        res -= s
        idx = val+1
        while idx <= n_bit:
            bit[idx] += 1
            idx += idx & -idx
    inv_num = res
    if inv_num >= th:
        ok = x
    else:
        ng = x
    iteration += 1
res1 = ok

if N < 100:
    ok = -1e10
    ng = 1e10
    n_iteration = 70
else:
    ok = -1e4
    ng = 1e4
    n_iteration = 46

tpls = list(zip(arrB, arrA, arrC))
tpls.sort(key=lambda x: -x[0]/x[1])
B2, A2, C2 = zip(*tpls)

iteration = 0
res2 = None
while iteration < n_iteration:
    x = (ok+ng) * 0.5
    Y = [(-a*x+c)/b for a, b, c in zip(B2, A2, C2)]
    Y_ord = sorted(range(N), key=lambda i: Y[i])
    n_bit = 1 << (N-1).bit_length()
    bit = [0] * (n_bit + 1)
    res = N*(N-1)//2
    for val in Y_ord:
        idx = val+1
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & -idx
        res -= s
        idx = val+1
        while idx <= n_bit:
            bit[idx] += 1
            idx += idx & -idx
    inv_num = res
    if inv_num >= th:
        ok = x
    else:
        ng = x
    iteration += 1
res2 = ok

print(res1, res2)