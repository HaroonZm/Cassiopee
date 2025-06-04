from functools import lru_cache
s = input()
n = len(s)
digits = list(map(int, s))

# Precompute prefix sums of digits
sum_s = sum(digits)

# Compute prod_s modulo nothing (we need exact big int)
prod_s = 1
for d in digits:
    prod_s *= (d+1)

# Convert s to integer
int_s = int(s)

# max sum is 9 * n
max_sum = 9 * n

# For sums and products, we store dp states:
# dp_sum[count][sum] = number of sequences of length count with sum of digits = sum
# We need to count sequences less than s, in order defined:
# sequences less than s = sequences with sum < sum_s
# + sequences with sum==sum_s and prod < prod_s
# + sequences with sum==sum_s and prod==prod_s and int < int_s

# The main challenge is dealing with large product space.
# But product can be up to (10)^n which is huge.
# We will note that the (d_i +1) are in [1..10]

# Let's factorize product in prime factors 2,3,5,7
# since 10=2*5, digits+1 in 1..10
# primes = [2,3,5,7]
# we encode product by exponents of these primes

primes = [2,3,5,7]
def prime_factors(x):
    res = [0]*4
    for i,p in enumerate(primes):
        while x % p == 0:
            res[i]+=1
            x//=p
    return tuple(res)

prod_factors = tuple(0 if d==0 else prime_factors(d+1) for d in digits)

# Since prod_s = product of digits+1
# We can combine factors by summing tuple components

def add_factors(a,b):
    return tuple(x+y for x,y in zip(a,b))

def less_factor(a,b):
    # return True if a < b in lex order
    # but here factors are exponents, compare as integers
    # Since factorization represents product,
    # compare by cross multiply is complicated, but 
    # since we compare products, compare tuple lex order
    # but actually we want numeric comparison:
    # We can compare by log(product)
    # log_p = sum of exponents * log(prime)
    log_primes = [0.6931471805599453, 1.0986122886681098, 1.6094379124341003, 1.9459101490553132]
    la = sum(a[i]*log_primes[i] for i in range(4))
    lb = sum(b[i]*log_primes[i] for i in range(4))
    return la < lb

# Compute prod_s factors:
prod_s_factor = (0,0,0,0)
for d in digits:
    prod_s_factor = add_factors(prod_s_factor, prime_factors(d+1))

@lru_cache(None)
def dp_sum_prod(pos, sumd, prodf):
    # return number of sequences of length pos with sum sumd and prod factors prodf
    if pos==0:
        return 1 if sumd==0 else 0
    total = 0
    for dig in range(10):
        if sumd - dig < 0:
            break
        pf = prime_factors(dig+1)
        newf = add_factors(prodf,pf)
        total += dp_sum_prod(pos-1, sumd-dig, newf)
    return total

# We will iterate sum from 0 to sum_s-1 and sum==sum_s separately

# count sequences with sum < sum_s
ans = 0
memo_sp = {}
def dfs_sum_prod(pos, sumd, prodf):
    key = (pos,sumd,prodf)
    if key in memo_sp:
        return memo_sp[key]
    if pos==n:
        return 1 if sumd==0 else 0
    if sumd<0:
        return 0
    res=0
    for dig in range(10):
        if sumd - dig <0:
            break
        pf = prime_factors(dig+1)
        newf = add_factors(prodf,pf)
        res += dfs_sum_prod(pos+1, sumd-dig, newf)
    memo_sp[key]=res
    return res

# sum < sum_s
for sm in range(sum_s):
    ans += dfs_sum_prod(0, sm, (0,0,0,0))

# Now sequences with sum == sum_s and product < prod_s_factor
# Another DP with prod factor state for sum_s

@lru_cache(None)
def dfs_sum_eq_prod_less(pos, prodf, less_flag):
    # less_flag: whether product factor already less than prod_s_factor, so no constraint
    if pos == n:
        return 1
    total = 0
    for dig in range(10):
        pf = prime_factors(dig+1)
        newf = add_factors(prodf, pf)
        if less_flag:
            total += dfs_sum_eq_prod_less(pos+1, newf, True)
        else:
            # check if newf < prod_s_factor prefix
            # We do lex compare factor by factor
            # But primes=4, so compare as tuple
            # If newf < prod_s_factor => less_flag=True
            # If newf == prod_s_factor => less_flag=False
            # else break
            # But we need to check sum digits as well

            # We must ensure the total digits sum is sum_s, so only generate digits that sum up to sum_s
            # So prune by sum digits: handled outside
            # So here we just compare products incrementally

            # Since product factors can only increase, if newf > prod_s_factor, skip
            # Compare newf and prod_s_factor lex order

            # Check if newf[i] > prod_s_factor[i]
            for i in range(4):
                if newf[i] > prod_s_factor[i]:
                    break
                if newf[i] < prod_s_factor[i]:
                    total += dfs_sum_eq_prod_less(pos+1, newf, True)
                    break
            else:
                # equal so far, less_flag remains False
                total += dfs_sum_eq_prod_less(pos+1, newf, False)
    return total

# The above ignores sum constraint, need to track sum digits

# So redesign:

@lru_cache(None)
def dfs_sum_eq_prod_less_sum(pos, sumd, prodf, less_flag):
    if pos == n:
        return 1 if sumd == 0 else 0
    res = 0
    for dig in range(10):
        if sumd - dig < 0:
            break
        pf = prime_factors(dig+1)
        newf = add_factors(prodf, pf)
        if less_flag:
            res += dfs_sum_eq_prod_less_sum(pos+1, sumd - dig, newf, True)
        else:
            # Check if newf > prod_s_factor, skip
            # compare newf and prod_s_factor
            # If newf > prod_s_factor, skip
            for i in range(4):
                if newf[i] > prod_s_factor[i]:
                    break
                if newf[i] < prod_s_factor[i]:
                    res += dfs_sum_eq_prod_less_sum(pos+1, sumd - dig, newf, True)
                    break
            else:
                # equal so far, less_flag stays False
                res += dfs_sum_eq_prod_less_sum(pos+1, sumd - dig, newf, False)
    return res

ans += dfs_sum_eq_prod_less_sum(0, sum_s, (0,0,0,0), False)

# Now sequences with sum==sum_s and prod==prod_s_factor and int < int_s
# To count that, we enumerate sequences digit by digit with those constraints

# We basically count sequences s' with same sum, prod and s' < s in decimal lex order

@lru_cache(None)
def dfs_final(pos, sumd, prodf, less_flag):
    if pos == n:
        return 1 if sumd == 0 else 0
    res = 0
    limit = digits[pos] if not less_flag else 9
    for dig in range(limit+1):
        if sumd - dig <0:
            break
        pf = prime_factors(dig+1)
        newf = add_factors(prodf, pf)
        if newf > prod_s_factor:
            continue
        if newf < prod_s_factor:
            continue
        new_less_flag = less_flag or (dig < digits[pos])
        res += dfs_final(pos+1, sumd - dig, newf, new_less_flag)
    return res

# The above counts sequences <= s, but we want < s, so subtract 1 if applicable
# but dfs_final counts sequences with prod == prod_s_factor, sum == sum_s

count_eq_prod_sum_less_int = dfs_final(0, sum_s, (0,0,0,0), False) - 1

ans += count_eq_prod_sum_less_int

print(ans)