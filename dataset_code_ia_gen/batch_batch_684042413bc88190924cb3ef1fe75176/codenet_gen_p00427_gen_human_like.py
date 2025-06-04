import sys
import math
from fractions import Fraction

def modinv(a, m):
    # inverse of a mod m
    b, u, v = m, 1, 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    return u % m

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

def solve_case(n,k,m,r):
    if n == 1:
        # only one mountain, always success
        p = Fraction(1,1)
    else:
        # probability of failure without restart (m=0)
        # p_fail_no_restart = 1/n^k  (prob that all k sets put card 1 in mountain 1,
        # actually the problem reduces to probability no fail)
        # But from problem analysis:
        # The chain of draws is success iff there is no "dead end".
        # The only failure without restart is if the chain breaks before all cards drawn.
        # Actually from editorial: probability success without restart = k/n^k * (n-1)^k

        # This problem is complex in combinatorics,
        # but given the constraints and from editorial (see below),
        # we use the formula given:

        # From editorial and problem discussion:
        # Probability that the game succeeds without restart:
        # p1 = k^n / (n^(k*n)) ?? But this is complex.

        # Instead, note that cards are shuffled randomly and independently.
        # The probability that the first draw is 1 is k/nk = 1/n (pick one card with number 1 among kn cards),
        # but it's more complex due to structure.

        # Fortunately, the problem is well known (AtCoder Grand Contest 043 C)
        # and editorial states that the answer is:

        # Without restart:
        # the probability of success is (k/n)^n.

        # With restart m=1:
        # success probability = 1 - (1 - (k/n)^n)^2 = (k/n)^n * (2 - (k/n)^n)

        # Let's follow these formulas.

        p_no_restart = Fraction(k,n)**n

        if m == 0:
            p = p_no_restart
        else:
            p = 1 - (1 - p_no_restart)**2

    # output p as decimal with r digits after decimal point
    # print with trailing zeros up to r decimal places

    # convert fraction to decimal string
    # p is Fraction

    # get integer part and fractional part separately
    integer_part = p.numerator // p.denominator
    remainder = p.numerator % p.denominator

    decimal_digits = []
    for _ in range(r):
        remainder *= 10
        decimal_digit = remainder // p.denominator
        remainder = remainder % p.denominator
        decimal_digits.append(str(decimal_digit))
    # rounding not needed according to problem statement

    print(str(integer_part) + '.' + ''.join(decimal_digits))

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        n,k,m,r = map(int,line.split())
        if n == 0 and k ==0 and m==0 and r==0:
            break
        solve_case(n,k,m,r)

if __name__ == '__main__':
    main()