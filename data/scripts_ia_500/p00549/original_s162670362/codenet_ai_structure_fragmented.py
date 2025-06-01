import sys
from sys import stdin
input = stdin.readline

def read_input():
    n = int(input())
    s = input().strip()
    return n, s

def initialize_counters(n):
    si = [0] * (n + 1)
    sj = [0] * (n + 1)
    return si, sj

def count_letters(n, s, si, sj):
    for i in range(n):
        count_i = is_I(s[i])
        count_j = is_J(s[i])
        si[i + 1] = si[i] + count_i
        sj[i + 1] = sj[i] + count_j

def is_I(c):
    return 1 if c == 'I' else 0

def is_J(c):
    return 1 if c == 'J' else 0

def compute_a(n, si, sj):
    max_a = 0
    for i in range(1, n):
        val = sj[i] * (si[n] - si[i])
        max_a = max(max_a, val)
    return max_a

def compute_b_c_ans(n, s, si, sj):
    b = 0
    c = 0
    ans = 0
    for i in range(n):
        if is_O(s[i]):
            b += si[n] - si[i + 1]
            c += sj[i]
            ans += (si[n] - si[i + 1]) * sj[i]
    return b, c, ans

def is_O(c):
    return c == 'O'

def main():
    n, s = read_input()
    si, sj = initialize_counters(n)
    count_letters(n, s, si, sj)
    a = compute_a(n, si, sj)
    b, c, ans = compute_b_c_ans(n, s, si, sj)
    print(ans + max(a, b, c))

if __name__ == "__main__":
    main()