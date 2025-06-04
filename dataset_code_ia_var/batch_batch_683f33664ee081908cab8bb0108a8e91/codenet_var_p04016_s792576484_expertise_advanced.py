from math import isqrt

def find_base(n, s):
    r = isqrt(n)
    for b in range(2, r + 2):
        m, t = n, 0
        while m:
            t, m = t + m % b, m // b
        if t == s:
            return b

    for p in range(r - 1, 0, -1):
        if (n - s) % p == 0:
            b = (n - s) // p + 1
            q = s - p
            if 1 <= p < b and 0 <= q < b:
                return b

    if n == s:
        return n + 1
    return -1

if __name__ == "__main__":
    n, s = int(input()), int(input())
    print(find_base(n, s))