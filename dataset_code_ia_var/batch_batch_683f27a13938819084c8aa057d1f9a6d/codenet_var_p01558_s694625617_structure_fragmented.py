from collections import deque
import itertools as it
import sys
import math

def set_large_recursion_limit():
    sys.setrecursionlimit(1000000)

def get_modulo():
    return 10 ** 30 + 7

def read_input():
    N, M = map(int, raw_input().split())
    s = raw_input()
    return N, M, s

def initialize_p27(limit, MOD):
    p27 = [1 for _ in range(limit)]
    for i in range(1, limit):
        p27[i] = (p27[i - 1] * 27) % MOD
    return p27

def get_initial_hash(s):
    return ord(s[0]) - ord('a') + 1

def remove_left_char(P, s, l, r, p27, MOD):
    value = ord(s[l]) - ord('a') + 1
    P -= value * p27[r - l]
    P %= MOD
    l += 1
    return P, l

def add_left_char(P, s, l, r, p27, MOD):
    l -= 1
    value = ord(s[l]) - ord('a') + 1
    P += value * p27[r - l]
    P %= MOD
    return P, l

def add_right_char(P, s, r, MOD):
    r += 1
    value = ord(s[r]) - ord('a') + 1
    P = (P * 27 + value) % MOD
    return P, r

def remove_right_char(P, s, r, MOD):
    value = ord(s[r]) - ord('a') + 1
    P -= value
    P %= MOD
    P = adjust_hash_after_right_removal(P, MOD)
    r -= 1
    return P, r

def adjust_hash_after_right_removal(P, MOD):
    for i in range(27):
        candidate = (P + MOD * i)
        if candidate % 27 == 0:
            P = candidate / 27
            break
    return P

def process_operation(S, P, l, r, s, p27, MOD):
    if S == 'L++':
        P, l = remove_left_char(P, s, l, r, p27, MOD)
    elif S == 'L--':
        P, l = add_left_char(P, s, l, r, p27, MOD)
    elif S == 'R++':
        P, r = add_right_char(P, s, r, MOD)
    elif S == 'R--':
        P, r = remove_right_char(P, s, r, MOD)
    return P, l, r

def handle_operations(M, s, p27, MOD):
    m = {}
    P = get_initial_hash(s)
    l = 0
    r = 0
    for _ in range(M):
        S = raw_input()
        P, l, r = process_operation(S, P, l, r, s, p27, MOD)
        m[P] = 1
    return m

def main():
    set_large_recursion_limit()
    MOD = get_modulo()
    N, M, s = read_input()
    p27 = initialize_p27(500000, MOD)
    m = handle_operations(M, s, p27, MOD)
    print len(m)

main()