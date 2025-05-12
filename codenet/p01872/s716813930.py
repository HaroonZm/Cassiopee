#!/usr/bin/env python3

import array

def is_valid_number(sequence):
    q = lambda n: (n + 1) if 1 <= n <= 6 else (n - 5)
    sum_pq = 0
    for index in range(1, 12):
        sum_pq += sequence[index] * q(index)
    rem_pq = sum_pq % 11
    check_digit = 0 if rem_pq <= 1 else (11 - rem_pq)
    return sequence[0] == check_digit

def string2array(st):
    return array.array("B", map(int, st[::-1]))

def solve(s):
    candidates = set()
    for r in range(0, 10):
        sequence = string2array(s.replace("?", str(r)))
        if is_valid_number(sequence):
            candidates.add(r)
    if len(candidates) == 1:
        return candidates.pop()
    else:
        return -1

def main():
    answer = solve(input())
    print("MULTIPLE" if answer == -1 else answer)

if __name__ == '__main__':
    main()