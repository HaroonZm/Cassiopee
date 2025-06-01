import itertools as ite
import math

def read_initial_values():
    return map(int, raw_input().split())

def read_and_adjust_values(M, p, N):
    values = []
    for _ in range(M):
        raw_val = input()
        adjusted_val = (raw_val - p) % N
        values.append(adjusted_val)
    return values

def sort_values(values):
    return sorted(values)

def find_min_endpoints(ls, N):
    return min(ls[-1], N - ls[0])

def calculate_minimum_distance(ls, N):
    ans = find_min_endpoints(ls, N)
    for i in range(len(ls) - 1):
        len1 = ls[i]
        len2 = N - ls[i + 1]
        ans = min(ans, len1 * 2 + len2, len2 * 2 + len1)
    return ans

def main():
    N, M, p = read_initial_values()
    ls = read_and_adjust_values(M, p, N)
    ls = sort_values(ls)
    ans = calculate_minimum_distance(ls, N)
    print ans * 100

main()