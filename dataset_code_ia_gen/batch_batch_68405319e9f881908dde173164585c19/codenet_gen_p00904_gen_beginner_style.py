import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def is_divisor(m, n, p, q):
    norm = m*m + n*n
    if norm == 0:
        return False
    s1 = m*p + n*q
    s2 = m*q - n*p
    if s1 % norm != 0 or s2 % norm != 0:
        return False
    return True

def count_divisors(m, n):
    norm = m*m + n*n
    count = 0
    # Since we know divisors must satisfy the divisor condition,
    # we try all possible pairs (a,b) with a^2 + b^2 dividing norm.
    # But that might be complex, so we just try all (a,b) with a^2+b^2 <= norm
    # and check divisor condition.
    limit = int(norm**0.5) + 1
    for a in range(-limit, limit+1):
        for b in range(-limit, limit+1):
            if a*a + b*b == 0:
                continue
            if (norm % (a*a + b*b)) == 0:
                if is_divisor(a, b, m, n):
                    count += 1
    return count

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    t = int(input_lines[0])
    for i in range(1, t+1):
        m,n = map(int, input_lines[i].split())
        norm = m*m + n*n
        if norm <= 1:
            print('C')
            continue
        div_count = count_divisors(m, n)
        if div_count == 8:
            print('P')
        else:
            print('C')

if __name__ == "__main__":
    main()