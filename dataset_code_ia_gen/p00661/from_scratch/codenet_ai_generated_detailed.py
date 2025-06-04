import sys
import math

def input():
    return sys.stdin.readline()

def count_multiples(n, p_list):
    # Inclusion-Exclusion to count numbers from 1 to n divisible by any p_i in p_list
    # p_list elements are guaranteed to divide n
    m = len(p_list)
    res = 0
    # There are at most 20 p_i’s, so subsets up to size 20 (2^20=1,048,576, feasible)
    # Use bitmask enumeration for subsets
    for mask in range(1, 1 << m):
        lcm = 1
        bits_count = 0
        for i in range(m):
            if mask & (1 << i):
                bits_count += 1
                # Compute lcm with p_list[i]
                # Since p_i divides n, lcm won't exceed n
                p = p_list[i]
                lcm = lcm * p // math.gcd(lcm, p)
                if lcm > n:  # no multiples if lcm > n
                    break
        else:
            count = n // lcm
            if bits_count % 2 == 1:
                res += count
            else:
                res -= count
    return res

def main():
    # For each test case, read n, m, then p_list, then compute expected revenue
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return
        n_m = line.strip().split()
        if len(n_m) < 2:
            n_m += sys.stdin.readline().strip().split()
        n, m = map(int, n_m)
        if n == 0 and m == 0:
            break
        p_line = ''
        p_list = []
        # Read possibly multiple lines until we have m integers
        while len(p_list) < m:
            p_line += ' ' + sys.stdin.readline()
            p_list = list(map(int, p_line.strip().split()))
        # Total numbers from 1..n = n
        # Count numbers divisible by any p_i in p_list
        divisible_count = count_multiples(n, p_list)
        allowed_count = n - divisible_count
        if allowed_count == 0:
            # No year left for order, expected income = 0
            print('0.0000000000')
            continue
        # Sum of all allowed years = sum(1..n) - sum of all multiples of forbidden p_i’s
        total_sum = n * (n + 1) // 2

        # Inclusion-Exclusion for sum of multiples
        def sum_multiples(n, p_list):
            m = len(p_list)
            res = 0
            for mask in range(1, 1 << m):
                lcm = 1
                bits_count = 0
                for i in range(m):
                    if mask & (1 << i):
                        bits_count += 1
                        p = p_list[i]
                        lcm = lcm * p // math.gcd(lcm, p)
                        if lcm > n:
                            break
                else:
                    max_k = n // lcm
                    # sum of multiples of lcm up to n: lcm * sum(1..max_k)
                    s = lcm * max_k * (max_k + 1) // 2
                    if bits_count % 2 == 1:
                        res += s
                    else:
                        res -= s
            return res

        forbidden_sum = sum_multiples(n, p_list)
        allowed_sum = total_sum - forbidden_sum

        # Expected value = allowed_sum / allowed_count
        expected = allowed_sum / allowed_count
        print(f'{expected:.10f}')

if __name__ == '__main__':
    main()