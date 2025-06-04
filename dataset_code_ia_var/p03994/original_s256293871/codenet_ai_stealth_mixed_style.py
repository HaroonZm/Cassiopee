def alpha2num(c):
    return ord(c) - 96

def num2alpha(n):
    return chr(n + 96)

import sys

def input_chars():
    return [alpha2num(ch) for ch in sys.stdin.readline().strip()]

def str_from_nums(nums):
    s = ''
    idx = 0
    while idx < len(nums):
        s += num2alpha(nums[idx])
        idx += 1
    return s

S = input_chars()
try:
    K = int(input())
except:
    K = 0

i = 0
while K and i < len(S):
    match S[i]:
        case 1:
            pass
        case _:
            cost = (27 - S[i])
            if cost <= K:
                K -= cost
                S[i] = 1
    i += 1

if K:
    last = len(S) - 1
    S[last] += K
    S[last] %= 26
    if S[last] == 0:
        S[last] = 26

print(''.join(map(lambda x: chr(x+96), S)))