from math import ceil

def min_cost(n, a, b, c, d):
    cost1 = -(-n // a) * b   # Optimized ceil division using integer math
    cost2 = -(-n // c) * d
    return min(cost1, cost2)

print(min_cost(*map(int, input().split())))