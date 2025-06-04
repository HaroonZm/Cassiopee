def smallest_number_with_n_divisors(N):
    # For N=1 to 12, we can precompute primes for factorization: use first few primes
    primes = [2,3,5,7,11,13,17,19,23,29,31,37]
    # We'll use backtracking to generate numbers whose number of divisors == N
    # Number of divisors for n = product of (exponent_i +1)
    # We want minimal n with product of (exponent_i +1) = N

    ans = float('inf')

    def backtrack(i, current_num, current_divisors, limit_exp):
        nonlocal ans
        if current_divisors == N:
            if current_num < ans:
                ans = current_num
            return
        if current_divisors > N or i >= len(primes):
            return
        exp = 1
        while True:
            new_divisors = current_divisors * (exp + 1)
            if new_divisors > N:
                break
            new_num = current_num * (primes[i] ** exp)
            if new_num >= ans:
                break
            backtrack(i+1, new_num, new_divisors, exp)
            exp += 1

    if N == 1:
        return 1

    backtrack(0, 1, 1, 64)
    return ans

N = int(input())
print(smallest_number_with_n_divisors(N))