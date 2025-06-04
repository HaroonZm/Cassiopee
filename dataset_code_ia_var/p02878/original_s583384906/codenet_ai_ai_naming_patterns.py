n_value, a_value, b_value = map(int, input().split())
modulus = 998244353
factorial_size = n_value + 1
factorial_current = 1
factorial_table = [1] * factorial_size
inverse_table = [1] * factorial_size
result_sum = 0
range_func = range

if b_value == 0:
    print(1)
    exit()

# Compute factorial table
for idx in range_func(1, factorial_size):
    factorial_table[idx] = factorial_current = factorial_current * idx % modulus

# Compute inverse factorial table
inverse_table[n_value] = inverse_current = pow(factorial_current, modulus - 2, modulus)
for idx in range_func(n_value, 1, -1):
    inverse_table[idx - 1] = inverse_current = inverse_current * idx % modulus

# Calculate sum following pattern
if n_value - b_value - a_value:
    k_limit = min(a_value + 1, n_value - b_value)
else:
    k_limit = a_value + 1

for k_idx in range_func(k_limit):
    q_value = n_value - b_value - k_idx - 1
    term = (b_value - k_idx) * factorial_table[b_value + k_idx - 1] * inverse_table[b_value] * inverse_table[k_idx]
    term = term * factorial_table[q_value + a_value - k_idx] * inverse_table[q_value] * inverse_table[a_value - k_idx]
    result_sum = (result_sum + term) % modulus

print(result_sum)