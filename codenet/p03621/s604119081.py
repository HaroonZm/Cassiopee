def ilog2(n):
    return 0 if n <= 0 else n.bit_length() - 1
def pack(pack, shamt):
    size = len(pack)
    while size > 1:
        npack = []
        for i in range(0, size - 1, 2):
            npack += [pack[i] | (pack[i+1] << shamt)]
        if size & 1:
            npack += [pack[-1]]
        pack, size, shamt = npack, (size + 1) >> 1, shamt << 1
    return pack[0]
def unpack(M, size, shamt):
    s, sizes = size, []
    while s > 1:
        sizes += [s]
        s = (s + 1) >> 1
    ret = [M]
    for size in sizes[::-1]:
        mask, nret = (1 << shamt) - 1, []
        for c in ret:
            nret += [c & mask, c >> shamt]
        ret, shamt = nret[:size], shamt >> 1
    return ret
def poly_mul_mod(f, g, mod):
    size = min(len(f), len(g))
    shift = ((mod - 1) ** 2 * size).bit_length()
    rsize = len(f) + len(g) - 1
    h = unpack(pack(f, shift) * pack(g, shift), rsize, shift * (1 << ilog2(rsize - 1)))
    return [int(x % mod) for x in h]
mod, N = 998244353, 10 ** 4 + 10
def inv(n): return pow(n, mod - 2, mod)
def poly_power_mod(f, n, mx):
	ret = [1]
	while n:
		if n & 1 : ret = poly_mul_mod(ret, f, mod)[:mx]
		f = poly_mul_mod(f, f, mod)[:mx]
		n >>= 1
	return ret	

fact, ifact, sm, poly = [1] * N, [1] * N, 1, [1] * N
for i in range(1, N): 
	fact[i], ifact[i] = (fact[i - 1] * i) % mod, (ifact[i - 1] * inv(i)) % mod
	poly[i - 1] = ifact[i]

A, B, n, m = raw_input(), raw_input(), 0, 0
for i in range(len(A)):
	if(A[i] == '1'):
		n += 1
		if(B[i] != '1'): m += 1		

ans, poly = 0, poly_power_mod(poly, m, n + 1)
for k in range(n - m + 1):
	term = fact[n - m - k] * fact[n - m - k] % mod
	if k < len(poly):
		term *= poly[k] * fact[m]
	else : term = 0	
	term *= fact[n - m] * fact[n] * ifact[n - m - k] * ifact[n - m - k]
	ans += term

print ans % mod