import sys
import math

def main():
    input = sys.stdin.readline
    while True:
        n = input()
        if not n:
            break
        n = n.strip()
        if n == '0':
            break
        n = int(n)
        L = []
        V = []
        for _ in range(n):
            d,v = map(int,input().split())
            L.append(d)
            V.append(v)
        times = [L[i]/V[i] for i in range(n)]
        # find lcm of fractions = lcm of numerators / gcd of denominators
        # represent fractions as times[i] = p_i / q_i
        # We want T = LCM(p_i)/GCD(q_i)
        # but fractions are float, transform to fractions of integers
        # Since all L[i], V[i] are integers, times[i] = L[i]/V[i] rational
        # numerator = L[i], denominator= V[i]

        # To find common time T so that T / times[i] = integer
        # => T / (Li/Vi) = T * Vi / Li integer
        # So T*(Vi)/Li integer for all i
        # Let T = X / Y in reduced form
        # Then X / Y * Vi / Li integer
        # => (X * Vi) / (Y * Li) integer
        # Set Y = 1 as any scaling factor
        # find T such that T * Vi / Li integer
        # Minimal T is lcm of fractions Li / Vi
        # Another method:
        # Let’s find LCM of all times: LCM of fractions = lcm of numerators / gcd of denominators
        # numerators = L[i], denominators = V[i]

        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        def lcm(a,b):
            return a*b//gcd(a,b)

        # first compute gcd of denominators (V)
        gcd_d = V[0]
        for v in V[1:]:
            gcd_d = gcd(gcd_d,v)
        # compute lcm of numerators (L)
        lcm_n = L[0]
        for l in L[1:]:
            lcm_n = lcm(lcm_n,l)
        # T = lcm_n / gcd_d

        # Now for each i, rounds = T / times[i] = (lcm_n / gcd_d) / (L[i]/V[i]) = (lcm_n / gcd_d) * (V[i]/L[i])
        # = (lcm_n * V[i]) / (gcd_d * L[i])

        # compute rounds: integer per constraint

        for i in range(n):
            res = (lcm_n * V[i]) // (gcd_d * L[i])
            print(res)

if __name__=="__main__":
    main()