import sys
import numpy as np
import numba
from numba import njit

INT64 = numba.int64

MOD_CONST = 1_000_000_007

input_buffer = sys.stdin.buffer.read
input_line = sys.stdin.buffer.readline
input_lines = sys.stdin.buffer.readlines

@njit((INT64, INT64), cache=True)
def compute_result(param_n, param_k):
    array_power = np.zeros(param_n + 10, np.int64)
    array_power[0] = 1
    for idx_power in range(1, param_n + 10):
        array_power[idx_power] = array_power[idx_power - 1] * (param_k + 1) % MOD_CONST
    result_value = param_k * (param_k + 1) // 2 * param_n * array_power[param_n - 1] % MOD_CONST

    array_dp = np.array([1], np.int64)
    array_dp[0] = 1
    for idx_n in range(param_n, 0, -1):
        next_dp_length = len(array_dp) * (idx_n + 1) // idx_n + 1
        array_dp_new = np.zeros(next_dp_length, np.int64)
        for idx_k in range(param_k + 1):
            for idx_t in range(len(array_dp)):
                is_k_greater = idx_k > idx_n
                int_x = 0 if is_k_greater else (idx_k + idx_t) // idx_n
                result_value -= int_x * array_dp[idx_t] % MOD_CONST * array_power[idx_n - 1] % MOD_CONST
                array_dp_new[idx_t + int_x] += array_dp[idx_t]
        array_dp = array_dp_new % MOD_CONST
    return result_value % MOD_CONST

input_n, input_k = map(int, input_buffer().split())

print(compute_result(input_n, input_k))