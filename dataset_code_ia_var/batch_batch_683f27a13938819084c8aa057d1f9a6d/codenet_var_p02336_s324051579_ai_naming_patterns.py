from functools import lru_cache
import sys

MOD_CONST = 1000000007

input_n, input_k = [int(value) for value in input().split(" ")]

factorial_list = [1 for _ in range(input_n + input_k + 1)]

for idx in range(1, input_n + input_k + 1):
    factorial_list[idx] = idx * factorial_list[idx - 1]

@lru_cache()
def compute_combination(param_i, param_j):
    return factorial_list[param_i] // (factorial_list[param_j] * factorial_list[param_i - param_j])

if input_n < input_k:
    print(0)
    sys.exit()

print(compute_combination(input_n - 1, input_k - 1) % MOD_CONST)