def precompute_factorials(max_n, mod):
    factorial = [1] * (max_n + 1)
    for idx in range(2, max_n + 1):
        factorial[idx] = factorial[idx - 1] * idx % mod
    return factorial

def precompute_inverse_factorials(factorial, mod):
    max_idx = len(factorial) - 1
    inv_factorial = list(factorial)
    inv_factorial[max_idx] = pow(factorial[max_idx], mod - 2, mod)
    for idx in range(max_idx - 1, -1, -1):
        inv_factorial[idx] = inv_factorial[idx + 1] * (idx + 1) % mod
    return inv_factorial

def compute_binomial_coefficient(factorial, inv_factorial, n_val, r_val, mod):
    return factorial[n_val] * inv_factorial[r_val] % mod * inv_factorial[n_val - r_val] % mod

input_n, input_a, input_b, input_k = map(int, input().split())
mod_const = 998244353
factorial_arr = precompute_factorials(input_n, mod_const)
inv_factorial_arr = precompute_inverse_factorials(factorial_arr, mod_const)
result_counter = 0
for trial_a in range(min(input_n + 1, input_k // input_a + 1)):
    total_a = input_a * trial_a
    if total_a > input_k:
        continue
    remainder_b = input_k - total_a
    if remainder_b % input_b != 0:
        continue
    trial_b = remainder_b // input_b
    if trial_b > input_n:
        continue
    combinations_a = compute_binomial_coefficient(factorial_arr, inv_factorial_arr, input_n, trial_a, mod_const)
    combinations_b = compute_binomial_coefficient(factorial_arr, inv_factorial_arr, input_n, trial_b, mod_const)
    result_counter = (result_counter + combinations_a * combinations_b) % mod_const
print(result_counter)