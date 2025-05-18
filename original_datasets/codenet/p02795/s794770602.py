import math

def int_input():
    return int(input())

H = int_input()
W = int_input()
N = int_input()

max_len = max(H, W)

print(math.ceil(N/max_len))