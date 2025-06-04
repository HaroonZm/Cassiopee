import re
from typing import List, Dict, Tuple, Union

class Term:
    def __init__(self, coefficient: int, exponent: int):
        self.coefficient = coefficient
        self.exponent = exponent

    def __repr__(self):
        return f"Term({self.coefficient}, {self.exponent})"

class Polynomial:
    def __init__(self, terms: List[Term]):
        # Terms must be sorted by exponent descending,
        # but input guarantees order, let's be safe.
        self.terms = sorted(terms, key=lambda t: -t.exponent)
        self.degree = self.terms[0].exponent if self.terms else 0
        self.coeffs = self._to_coeff_dict()

    def _to_coeff_dict(self) -> Dict[int, int]:
        d = {}
        for t in self.terms:
            d[t.exponent] = t.coefficient
        # Fill missing powers with 0
        for deg in range(self.degree, -1, -1):
            if deg not in d:
                d[deg] = 0
        return d

    @classmethod
    def from_string(cls, s: str) -> 'Polynomial':
        # Parse polynomial string according to problem spec
        # The string is e.g. "x^5+15x^4+85x^3+225x^2+274x+120"
        # Terms separated by + or -
        # We'll handle signs, coefficients, exponents accordingly.
        # Pattern for terms:
        # optional sign, optional coeff, optional x, optional ^exponent or exponent=1 if x with no ^
        # or constant (no x)
        # We'll extract signs and terms carefully:
        # The input guarantees the leading term has coeff 1 and no sign (no leading - for max degree)
        # Let's split on + or - carefully preserving signs.

        # Adjust string to mark explicit signs for splitting: add '+' in front if none
        if not s.startswith('+') and not s.startswith('-'):
            s = '+' + s
        # Split while keeping signs
        tokens = re.findall(r'[+\-][^+\-]+', s)
        terms = []
        for token in tokens:
            sign = 1 if token[0] == '+' else -1
            body = token[1:]
            if 'x' not in body:
                # Constant term
                c = int(body)
                terms.append(Term(sign * c, 0))
            else:
                # Has x
                # Format: optional coeff, x, optional ^exponent
                m = re.fullmatch(r'(\d*)x(?:\^(\d+))?', body)
                if m is None:
                    # single x or x^exp ?
                    # but above regex matches these all
                    raise ValueError("Unexpected term format " + token)
                coeff_str, exp_str = m.groups()
                coeff = int(coeff_str) if coeff_str != '' else 1
                exponent = int(exp_str) if exp_str is not None else 1
                terms.append(Term(sign * coeff, exponent))
        return cls(terms)

    def coefficients_list(self) -> List[int]:
        # returns list from degree to 0
        return [self.coeffs[i] for i in range(self.degree, -1, -1)]

    def __repr__(self):
        return "Polynomial(" + ", ".join(repr(t) for t in self.terms) + ")"

class Factorizer:
    def __init__(self, polynomial: Polynomial):
        self.poly = polynomial
        self.degree = polynomial.degree
        self.coeffs = polynomial.coefficients_list()  # a_n ... a_0
        if self.coeffs[0] != 1:
            # By problem statement highest degree coeff is 1, no check needed generally.
            raise ValueError("Leading coefficient must be 1")
        self.factors: List[int] = []

    @staticmethod
    def divisors(n: int) -> List[int]:
        # Returns all positive and negative divisors of n sorted ascending by absolute then by value
        absn = abs(n)
        divs = []
        for i in range(1, int(absn**0.5) + 1):
            if absn % i == 0:
                divs.append(i)
                if i != absn // i:
                    divs.append(absn // i)
        divs += [-d for d in divs]
        divs = list(set(divs))
        divs.sort(key=lambda x: (abs(x), x))
        return divs

    def find_factors(self):
        # Based on Viete's formulas:
        # polynomial: x^n + a_{n-1} x^{n-1} + ... + a_0
        # factors: (x + r1)(x + r2)...(x + rn)
        # where r_i are the roots' additive inverses
        #
        # The constant term a_0 = r1 * r2 * ... * rn
        # Each r_i is a nonzero integer, distinct.
        #
        # We need to find the integer roots r_i satisfying those.
        #
        # Since degree max 5, manageable by trial.

        n = self.degree
        a_coeffs = self.coeffs  # [1, a_{n-1}, ..., a_0]
        # factors to find: r_i where polynomial = \prod (x + r_i)
        # a_0 = product(r_i)
        # a_{n-1} = sum(r_i)
        # ... symmetric sums of roots.

        # We'll use a backtracking approach generating candidates for r_i from divisors of a_0.

        constant = a_coeffs[-1]
        candidates = self.divisors(constant)

        # Symmetric sums are related to coefficients by Viète:
        # for k=1,...,n,
        # sum_{|I|=k} prod_{i in I} r_i = a_{n-k} * (-1)^k

        # Build list of coeffs needed for verification:
        # For k-th elementary symmetric sum of roots S_k:
        # S_k = sum of products of roots taken k at a time
        # S_k = (-1)^k * a_{n - k}
        target_sums = []
        for k in range(1, n+1):
            target = a_coeffs[n-k] * ((-1)**k)
            target_sums.append(target)

        # Generate candidate roots tuples of length n with distinct elements from candidates
        # obeying that product == constant (already implied), distinctness, and symmetric sums match.

        # Optimization: product of candidates must equal constant.
        # Backtracking with pruning.

        found_factors = []

        def sym_sums(roots: List[int]) -> List[int]:
            # Compute elementary symmetric sums S_k of roots
            # naive combinatorial approach since n <=5
            # use recursion or iterative
            n = len(roots)
            sums = [0]*n
            # k=1..n sums:
            # Use classical combinational formula via DP
            esums = [0]*(n+1)
            esums[0] = 1
            for r in roots:
                for k in range(n,0,-1):
                    esums[k] += esums[k-1]*r
            # esums[k] = sum of products of roots taken k at a time
            # We need from k=1 to n:
            return esums[1:]

        def backtrack(depth: int, chosen: List[int], used: set):
            if depth == n:
                # verify all symmetric sums
                sums = sym_sums(chosen)
                if sums == target_sums:
                    found_factors.append(list(chosen))
                return
            # Prune: partial product and sums are complicated to prune perfectly.
            for c in candidates:
                if c in used:
                    continue
                # If depth == n-1, check product will satisfy
                # product so far:
                if depth == 0:
                    product_so_far = 1
                else:
                    product_so_far = 1
                    for x in chosen:
                        product_so_far *= x
                # Remaining product:
                prod_after = product_so_far * c
                # If depth == n-1, prod_after must == constant
                if depth == n-1:
                    if prod_after != constant:
                        continue
                # Distinctness checked by used
                chosen.append(c)
                used.add(c)
                backtrack(depth+1, chosen, used)
                chosen.pop()
                used.remove(c)

        backtrack(0, [], set())

        if len(found_factors) == 0:
            raise ValueError("No factorization found. Contradicts guarantee.")

        # There can be multiple orderings: choose ordering by increasing constant term of each linear factor
        # But factors are (x + r_i), constants are r_i
        # Sort the solution by r_i ascending
        solution = sorted(found_factors[0])
        self.factors = solution

    def formatted_output(self) -> str:
        # Print factors (x + r_i) sorted by r_i ascending
        res = []
        for c in sorted(self.factors):
            if c < 0:
                res.append(f"(x{c})")
            else:
                res.append(f"(x+{c})")
        return "".join(res)

def main():
    import sys
    s = sys.stdin.readline().strip()
    poly = Polynomial.from_string(s)
    factorizer = Factorizer(poly)
    factorizer.find_factors()
    print(factorizer.formatted_output())

if __name__ == "__main__":
    main()