MOD = 10**9 + 7

def mod_factorial(n):
    fact = [1] * (n+1)
    for i in range(2, n+1):
        fact[i] = fact[i-1] * i % MOD
    return fact

def mod_inv(a, m=MOD):
    # Fermat's little theorem for prime m
    return pow(a, m-2, m)

def mod_comb(n, k, fact):
    if k > n or k < 0:
        return 0
    return fact[n] * mod_inv(fact[k]) % MOD * mod_inv(fact[n-k]) % MOD

n, k = map(int, input().split())

# Since boxes are indistinguishable and each box can have at most one ball,
# the problem reduces to counting the number of subsets of boxes of size n,
# but boxes are identical -> only 1 way if n <= k, else 0.

# But balls are distinguishable, boxes are identical,
# and no two balls can be in the same box,
# so solution = number of distinguishable n balls divided into k identical boxes 
# with at most one ball per box.

# This corresponds to the number of ways to partition n distinct balls into n boxes,
# but boxes are identical - so the problem reduces to the Stirling numbers of the second kind S(n,m),
# but since m must be equal to n to not exceed k boxes,
# and m <= k

# Actually, with at most one ball per box, and boxes identical,
# the number of ways is 1 if n <= k else 0
# because the boxes are identical, the only difference is in which balls are chosen.

# Since balls are distinct and boxes identical, and at most one ball per box,
# the partitions of balls into boxes correspond to selecting subsets of balls assigned to each box,
# but boxes indistinguishable means that the only difference comes from the number of balls placed.

# But the problem conditions: each ball must be placed, and each box can hold at most one ball.
# So if n > k, impossible.

# The number of ways to put n distinguishable balls into k identical boxes with at most one ball per box equals 1
# if n <= k.

# Hence:
if n > k:
    print(0)
else:
    print(1)