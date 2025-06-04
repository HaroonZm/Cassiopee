import sys
import math
import bisect
import random
from collections import defaultdict, deque
from heapq import heappush, heappop

def read_int_list(): return [int(x) for x in sys.stdin.readline().split()]
def read_int(): return int(sys.stdin.readline())
def read_str_list(): return [list(x) for x in sys.stdin.readline().split()]
def read_str_line():
    line = list(sys.stdin.readline())
    if line and line[-1] == "\n":
        return line[:-1]
    return line
def read_ints_n(n): return [read_int() for _ in range(n)]
def read_int_lists_n(n): return [read_int_list() for _ in range(n)]
def read_str_lines_n(n): return [read_str_line() for _ in range(n)]
def read_str_lists_n(n): return [read_str_list() for _ in range(n)]

sys.setrecursionlimit(1000000)
MOD = 10**9+7

def main_logic():
    base_digits = [int(d) for d in input()]
    query_list = list(input())
    query_length = len(query_list)
    for idx in range(query_length):
        if query_list[idx].isdecimal():
            query_list[idx] = int(query_list[idx])
    dp_state = [[[0]*2 for _ in range(2)] for _ in range(query_length+1)]
    dp_state[0][0] = [1, 0]
    power_ten_mod = [pow(10, i, MOD) for i in range(query_length)]
    for pos in range(query_length):
        next_pos = pos + 1
        for carry_state in range(2):
            if query_list[pos] == "?":
                max_digit = 9 if carry_state else base_digits[pos]
                for cur_digit in range(max_digit+1):
                    new_carry = carry_state | (cur_digit < base_digits[pos])
                    dp_state[next_pos][new_carry][0] += dp_state[pos][carry_state][0]
                    dp_state[next_pos][new_carry][1] += dp_state[pos][carry_state][0]*cur_digit + 10*dp_state[pos][carry_state][1]
                    dp_state[next_pos][new_carry][0] %= MOD
                    dp_state[next_pos][new_carry][1] %= MOD
            else:
                cur_digit = query_list[pos]
                new_carry = carry_state | (cur_digit < base_digits[pos])
                if cur_digit <= base_digits[pos]:
                    dp_state[next_pos][new_carry][0] += dp_state[pos][carry_state][0]
                    dp_state[next_pos][new_carry][1] += dp_state[pos][carry_state][0]*cur_digit + 10*dp_state[pos][carry_state][1]
                    dp_state[next_pos][new_carry][0] %= MOD
                    dp_state[next_pos][new_carry][1] %= MOD
                else:
                    if new_carry:
                        dp_state[next_pos][new_carry][0] += dp_state[pos][carry_state][0]
                        dp_state[next_pos][new_carry][1] += dp_state[pos][carry_state][0]*cur_digit + 10*dp_state[pos][carry_state][1]
                        dp_state[next_pos][new_carry][0] %= MOD
                        dp_state[next_pos][new_carry][1] %= MOD
    print((dp_state[-1][0][1] + dp_state[-1][1][1]) % MOD)
    return

if __name__ == "__main__":
    main_logic()