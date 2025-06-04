import sys
import numpy as np
import numba
from numba import njit

i8 = numba.int64

def get_read_functions():
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    return read, readline, readlines

def call_prime_table(N):
    return prime_table(N)

@njit
def set_initial_is_prime(N):
    is_prime = np.zeros(N, np.int64)
    is_prime[2:3] = 1
    is_prime[3::2] = 1
    return is_prime

@njit
def mark_composites(is_prime, N):
    for p in range(3, N, 2):
        if p * p >= N:
            break
        if is_prime[p]:
            is_prime[p * p::p + p] = 0

@njit
def find_primes(is_prime):
    return np.where(is_prime)[0]

@njit
def prime_table(N):
    is_prime = set_initial_is_prime(N)
    mark_composites(is_prime, N)
    primes = find_primes(is_prime)
    return is_prime, primes

@njit
def filter_small_primes(primes, limit):
    result = []
    for p in primes:
        if p < limit:
            result.append(p)
    return np.array(result, np.int64)

@njit
def filter_large_primes(primes, limit):
    result = []
    for p in primes:
        if p > limit:
            result.append(p)
    return np.array(result, np.int64)

@njit
def get_M_X(MX):
    M = MX[::2]
    X = MX[1::2]
    return M, X

@njit
def generate_tmp(p):
    result = [1]
    while p * result[-1] < 300:
        result.append(p * result[-1])
    return np.array(result, np.int64)

@njit
def ravel_outer_product(nums, tmp):
    return np.ravel(nums.reshape(-1,1) * tmp.reshape(1,-1))

@njit
def build_nums(primes_small):
    nums = np.array([1], np.int64)
    for ind in range(len(primes_small)):
        p = primes_small[ind]
        tmp = generate_tmp(p)
        nums = ravel_outer_product(nums, tmp)
    return nums

@njit
def get_last_element(nums):
    return nums[-1]

@njit
def process_entry(n, U, M, X):
    base = 0
    extra = np.zeros(300, np.int64)
    for i in range(len(M)):
        m, x = M[i], X[i]
        a = np.gcd(m, U)
        b = m // a
        if n % a != 0:
            continue
        if b == 1:
            base += x
        else:
            extra[b] += x
    return base, extra

@njit
def compute_score(base, extra):
    return base + np.sum(np.maximum(extra, 0))

@njit((i8[:], ), cache=True)
def main(MX):
    _, primes = call_prime_table(300)
    primes_small = filter_small_primes(primes, 18)
    # primes_large = filter_large_primes(primes, 18)  # not actually used
    M, X = get_M_X(MX)
    nums = build_nums(primes_small)
    U = get_last_element(nums)
    ret = 0
    for i in range(len(nums)):
        n = nums[i]
        base, extra = process_entry(n, U, M, X)
        score = compute_score(base, extra)
        if score > ret:
            ret = score
    return ret

def run():
    read, _, _ = get_read_functions()
    MX = np.array(read().split(), np.int64)[1:]
    print(main(MX))

run()