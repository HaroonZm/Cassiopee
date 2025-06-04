from math import factorial as f
L, K = [int(x) for x in input().split()]
counter = 0
i = 1
while i <= ((L + 1)//2):
    for j in range(i+1):
        val = 2 * i - 1 + (j * (K - 1))
        if val > L: break
        def comb(n, r): return f(n) / f(r) / f(n - r)
        counter += comb(i, j)
    i += 1
print(int(counter))