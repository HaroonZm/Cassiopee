class ModuloFunction:
    def __init__(self, base: int):
        if base < 2:
            raise ValueError("Base must be at least 2.")
        self.N = base

    def f(self, a: int) -> int:
        # Compute a^N mod N
        return pow(a, self.N, self.N)

class FunctionalIteration:
    def __init__(self, func: ModuloFunction):
        self.func = func
        self.N = func.N

    def F_k(self, a: int, k: int) -> int:
        # Recursively apply f k times to a; optimized with iteration
        val = a
        for _ in range(k):
            val = self.func.f(val)
        return val

class GroupTheoryHelper:
    def __init__(self, N: int):
        self.N = N

    def prime_factors(self, n: int) -> dict:
        factors = {}
        x = n
        d = 2
        while d * d <= x:
            while x % d == 0:
                factors[d] = factors.get(d, 0) + 1
                x //= d
            d += 1 if d==2 else 2
        if x > 1:
            factors[x] = factors.get(x, 0) + 1
        return factors

    def compute_totient(self, n: int) -> int:
        # Euler's totient function φ(n)
        factors = self.prime_factors(n)
        result = n
        for p in factors:
            result -= result // p
        return result

    def divisors(self, n: int) -> list:
        # Efficient enumeration of divisors from prime factorization
        factors = self.prime_factors(n)
        divisors_list = [1]
        for p, exp in factors.items():
            new_divs = []
            for d in divisors_list:
                x = 1
                for _ in range(exp):
                    x *= p
                    new_divs.append(d * x)
            divisors_list += new_divs
        return sorted(divisors_list)

    def lcm(self, a: int, b: int) -> int:
        from math import gcd
        return a // gcd(a,b) * b

class IdentityFunctionSolver:
    def __init__(self, N: int):
        self.N = N
        self.func = ModuloFunction(N)
        self.iterator = FunctionalIteration(self.func)
        self.gt_helper = GroupTheoryHelper(N)

    def solve(self) -> int:
        # The function F_k(a) = a means that after k iterations of f, a is fixed.
        # Since f(a) = a^N mod N, and F_k+1(a) = F_k(f(a)),
        # We want the minimal k > 0 such that for every 1 <= a < N:
        # F_k(a) = a

        # If there exists an a such that the orbit under f doesn't cycle back to a at iteration k,
        # no such k.

        # Note that fixed points under f are values a such that a^N ≡ a (mod N).

        # The problem is equivalent to: find minimal k > 0 such that 
        # f^{k}(a) = a for all a in [1,N-1].

        # We will analyze the structure modulo the prime powers dividing N.

        # Step 1: Factorize N
        prime_factors = self.gt_helper.prime_factors(self.N)

        # Step 2: For each prime power dividing N, analyze the cycle lengths of f restricted mod p^e.
        # The function f reduces modulo p^e to a -> a^N mod p^e.
        # Let M = N.
        # We want minimal k such that for all a mod p^e,
        # (a^M)^(M^(k-1)) ≡ a mod p^e.
        # i.e. a^(M^{k}) ≡ a (mod p^e) for all a coprime to p.

        # This is simpler if we consider units mod p^e, i.e. (Z/(p^e)Z)^*

        # For any prime power q = p^e:
        # The group of units modulo q has order phi(q).
        # For unit a, a^{order of group} = 1 mod q.
        # The function f acts by raising to power N.
        # Then F_k acts by raising to power N^k
        # So for units, F_k(a) = a^{N^{k}} ≡ a mod q
        # This means a^{N^{k} - 1} ≡ 1 mod q for every unit a.
        # So N^{k} ≡ 1 mod order_of_group
        # We want the minimal k such that N^{k} ≡ 1 (mod order_of_group).
        # i.e. order_of_N modulo order_of_group

        # Additionally, for elements not coprime to q, (i.e. zero divisors)
        # we have to check that a^{N^{k}} ≡ a mod q holds.
        # Usually zero divisors won't be fixed typically, 
        # but because the problem statement requires all a in [1,N-1], 
        # including non-units, we must verify.

        # However, if q is prime, all nonzero a mod q are units.
        # For prime powers > 1, zero divisors can exist.

        # Step 3: So for each q = p^e dividing N:
        # - Let order = phi(q), compute order
        # - Find order of N modulo order
        # -- i.e. minimal k such that N^k ≡ 1 mod order
        # -- if no such k, return -1

        # - For zero divisors, check if fixed.

        # Step 4: Combine all k from all prime powers by computing their lcm.

        from math import gcd

        # Helper to compute modular multiplicative order:
        def mod_order(a: int, m: int) -> int or None:
            if gcd(a, m) != 1:
                return None
            # Find divisors of m
            divs = self.gt_helper.divisors(m)
            for d in divs:
                if pow(a, d, m) == 1:
                    return d
            return None

        # Extended prime power phi
        def phi_prime_power(p, e):
            if p == 2 and e >= 3:
                return 2 ** (e - 1)
            else:
                return (p - 1) * (p ** (e -1))

        ks = []

        for p, e in prime_factors.items():
            q = p ** e
            order = phi_prime_power(p,e)

            # order of N modulo order is the minimal k s.t N^k ≡ 1 (mod order)
            mo = mod_order(self.N % order, order)
            if mo is None:
                # no such order, no solution
                return -1

            # Now check zero divisors for that prime power:

            # For zero divisors a (multiples of p), verify if (a^{N^{k}}) mod q == a

            # For a = m*p (m < p^{e-1}), check:
            # (a^{N^{k}}) mod q ?= a

            # We only need to check if for these zero divisors,
            # (a^{N^{k}} - a) mod q == 0

            # a^{N^{k}} - a = a(a^{N^{k} - 1} - 1)

            # But if p divides a, and q=p^e, then a is divisible by p,
            # so a^{N^{k}} ≡ 0 mod p^(e) or not?
            # Large powers of multiples of p are divisible by higher powers usually.

            # Test the simplest case: a = p

            # We can test whether p^{N^{k}} ≡ p mod p^e

            # Since p^{N^{k}} ≡ p mod p^e means p^{N^{k}} - p ≡ 0 mod p^e

            # Or p * (p^{N^{k}-1} - 1) ≡ 0 mod p^e

            # Since p divides left, p^{N^{k}-1} -1 ≡ ? mod p^{e-1}

            # This implies (p^{N^{k}-1} ≡ 1 mod p^{e-1})

            # But p^{N^{k} -1} mod p^{e-1} is 0 if e-1>0

            # p^{anything>0} divisible by p^{e-1}? Not if exponent is 0

            # But note that p prime base power raised to power > 0 is always divisible by p

            # So p^{N^{k}-1} mod p^{e-1} = 0 if N^{k} -1 > 0

            # So then p^{N^{k} -1} - 1 ≡ -1 mod p^{e-1}

            # -1 mod p^{e-1} != 0 so the difference isn't zero mod p^{e-1}

            # So for e>1 zero divisors typically are not fixed by f^k unless k=0

            # We check a few values minimal:

            # If e=1 (prime), there are no zero divisors except zero which we exclude

            # So if e>1, the zero divisors prevent equality unless the zero divisors get fixed.

            # The problem sample 4 => N=4 = 2^2 outputs -1 (no such k)

            # So if prime power exponent e>1, then return -1 immediately

            if e > 1:
                return -1

            ks.append(mo)

        # Now lcm all found ks
        from math import gcd
        def lcm(a, b):
            return a // gcd(a,b) * b
        from functools import reduce

        return reduce(lcm, ks)

def main():
    import sys
    N = int(sys.stdin.readline())
    solver = IdentityFunctionSolver(N)
    print(solver.solve())

if __name__ == "__main__":
    main()