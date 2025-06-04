height, width, row_start, col_start = map(int, input().split())
combinatorial_cache = {}
modulus = 10**9 + 7
modulus_inverse = modulus - 2
for index in range(height + width - 1):
    if combinatorial_cache.get(index - 1):
        factorial = (index * combinatorial_cache[index - 1][0]) % modulus
    else:
        factorial = 1
    inverse_factorial = pow(factorial, modulus_inverse, modulus)
    combinatorial_cache[index] = (factorial, inverse_factorial)

def binomial_coefficient(n_val, k_val):
    return combinatorial_cache[n_val][0] * combinatorial_cache[k_val][1] * combinatorial_cache[n_val - k_val][1]

total_paths = 0
for column_index in range(col_start, width):
    path_count_1 = binomial_coefficient(column_index + height - row_start - 1, column_index)
    path_count_2 = binomial_coefficient(width - 1 - column_index + row_start - 1, width - 1 - column_index)
    total_paths += path_count_1 * path_count_2

print(total_paths % modulus)