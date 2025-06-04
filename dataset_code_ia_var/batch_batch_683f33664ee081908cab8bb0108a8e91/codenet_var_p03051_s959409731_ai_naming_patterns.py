import sys
import math
import collections
import heapq
import itertools

input_stream = sys.stdin

def read_single_line_stripped():
    return input_stream.readline().strip("\n")

def read_line_split():
    return input_stream.readline().strip("\n").split()

def compute_gcd(val_a, val_b):
    val_a, val_b = max(val_a, val_b), min(val_a, val_b)
    while val_a % val_b > 0:
        val_a, val_b = val_b, val_a % val_b
    return val_b

MODULO = 7 + 10 ** 9

def process_solution():
    num_elements = int(read_single_line_stripped())
    input_values = [int(val) for val in read_line_split()]

    xor_dp = [[0, 1] for _ in range(2 ** 20)]
    memoization = [0] * (2 ** 20)
    acc_xor = 0
    zero_sequences = 0

    for idx in range(num_elements):
        acc_xor ^= input_values[idx]
        if acc_xor == 0:
            zero_sequences += 1
        else:
            xor_dp[acc_xor][1] += xor_dp[acc_xor][0] * (zero_sequences - memoization[acc_xor])
            xor_dp[acc_xor][1] %= MODULO
            xor_dp[acc_xor][0] += xor_dp[acc_xor][1]
            xor_dp[acc_xor][0] %= MODULO
            memoization[acc_xor] = zero_sequences

    if acc_xor > 0:
        print(xor_dp[acc_xor][1])
    else:
        result_answer = pow(2, zero_sequences - 1, MODULO)
        for idx in range(2 ** 20):
            result_answer += xor_dp[idx][0]
            result_answer %= MODULO
        print(result_answer)

    return 0

if __name__ == "__main__":
    process_solution()