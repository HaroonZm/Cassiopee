import sys
import os

def main():
    n, m = read_ints()
    a = read_ints()
    b = []
    for _ in range(m):
        b.append(read_ints())
    result = solve(n, m, a, b)
    print(result)

def solve(n, m, a, b):
    b.sort()
    dp = [0] * (n + 1)
    range_counter = []
    range_starts = []
    range_number = {}
    end_ranges = {}

    b_index = 0
    curr_range = 0

    for i in range(1, n + 1):
        # Read start of new ranges
        while b_index < len(b) and b[b_index][0] == i:
            l, r = b[b_index]
            if l not in range_number:
                range_number[l] = len(range_counter)
                range_counter.append(0)
                range_starts.append(l)
            range_counter[range_number[l]] += 1
            if r not in end_ranges:
                end_ranges[r] = []
            end_ranges[r].append(range_number[l])
            b_index += 1

        prev_index = i - 1
        if curr_range < len(range_counter):
            prev_index = range_starts[curr_range] - 1
        dp[i] = max(dp[i-1], dp[prev_index] + a[i-1])

        # Remove ended ranges
        if i in end_ranges:
            for rn in end_ranges[i]:
                range_counter[rn] -= 1
        while curr_range < len(range_counter) and range_counter[curr_range] == 0:
            curr_range += 1

    return dp[n]

def inp():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(inp())

def read_ints():
    return [int(x) for x in inp().split()]

if __name__ == '__main__':
    main()