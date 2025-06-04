import sys
sys.setrecursionlimit(10**7)
M = int(sys.stdin.readline())
C = sys.stdin.readline().rstrip()
MOD = 10**9+7
n = len(C)

# D = digits d0 d1 ... d_{n-1}
# C = c0 c1 ... c_{n-1}
# There is a permutation p of digits 0-9 such that for all i, c_i = p(d_i)
# p is bijection on digits appeared in D <-> digits appeared in C

# We want to find D (no leading zero) s.t. D mod MOD = M and p(d_i) = c_i


# First, let set Ds = digits in D, Cs = digits in C (unknown),
# we know mapping p: D_digit -> C_digit is bijection for digits appearing.
# So count distinct digits in C => len(set(C))

# We'll try to find digits d_i such that p(d_i) = c_i.

# p is bijection: so digits in D map one-to-one to digits in C (both sets same size)

# For each digit in C, we assign a digit in D uniquely.

# We try to reconstruct D from C and M:
# We guess the mapping from digits in C to digits in D.

# Since p(d) = c, so p^{-1}(c) = d
# So digits in C map to digits in D uniquely.

# Let's collect distinct digits in C:

digits_c = []
pos = {}
for i,ch in enumerate(C):
    if ch not in pos:
        pos[ch] = len(pos)
for i in range(len(C)):
    if C[i] not in digits_c:
        digits_c.append(C[i])
k = len(digits_c)

# We need to assign digits in D to these digits_c, such that different digits_c have different digits in D.
# So mapping c_digit -> d_digit is bijection.

# So we will assign each digit in C a digit in D: mapping c_digit -> d_digit, where digits are 0-9

# D constructed by mapping each c_i via c_digit->d_digit: d_i = mapping[c_i]

# D has no leading zero: so d_0 != 0

# We must have D mod MOD = M

# Let's try all permutations of digits 0-9 taken k with bijection from digits_c digits to digits d digits.

# But k upto 10 max, but maybe length(C) up to 1e5.

# We cannot try all permutations: too large.

# Alternative:

# Let's represent the D number as:
# D = sum_{i=0 to n-1} d_i * 10^{n-1-i}
#      = sum_{digit in D} (digit) * (sum of 10^{pos} where that digit occurs)

# Similarly, since the digits_c are in C, mapping c_digit->d_digit, and C known.

# So for each c_digit, we can compute coef_c_digit = sum of 10^{n-1-i} over all i where C[i]==c_digit

# Then: D = sum_{c_digit} d_digit * coef_c_digit

# D mod MOD = M

# So unknowns = d_digit for c_digits in digits_c

# Restrictions:
# All d_digits distinct in [0..9]
# No leading zero in D => d_digit of C[0] != 0

# Solve:

# sum_{c_digits} d_digit * coef_c_digit ≡ M mod MOD under these constraints.

# Now, we can brute force only digits of length <= 10 (max unique digits in C)

# digits_c at most 10 digits

# So we assign digits to c digits: permutations of digits 0..9 choosing k digits.

# Additionally, d_digit of c_digit corresponding to C[0] must != 0

# Let's build coef array for c_digits: coef[i] = sum of 10^{n-1-j} mod MOD for all j where C[j] = digits_c[i]

# efficient power calculation:

pow10 = [1]*(n+1)
for i in range(n-1,-1,-1):
    pow10[i] = (pow10[i+1]*10)%MOD

coef = [0]*k
for i,ch in enumerate(C):
    coef[pos[ch]] = (coef[pos[ch]] + pow10[i])%MOD

from itertools import permutations

digits_range = list(range(10))
idx_first = pos[C[0]]

# Try permutations over digits_range pick k digits, assign to coef order

for perm in permutations(digits_range, k):
    if perm[idx_first] == 0:
        continue
    res = 0
    for i in range(k):
        res = (res + perm[i]*coef[i])%MOD
    if res == M:
        # Build D string:
        d_digits_map = {}
        for d_c, d_v in zip(digits_c, perm):
            d_digits_map[d_c] = str(d_v)
        D = ''.join(d_digits_map[ch] for ch in C)
        print(D)
        break
else:
    print(-1)