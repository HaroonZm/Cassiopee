from __future__ import annotations
from typing import Dict, Tuple, Optional, List
from abc import ABC, abstractmethod


class Expr(ABC):
    """
    Expression base class. Expressions can be:
    - Sum of variables with positive integer coefficients
    """
    @abstractmethod
    def serialize(self) -> str:
        """
        Serialize expression to minimal length string representation,
        favoring use of multiplication and parentheses if shorter.
        """
        pass

    @abstractmethod
    def length(self) -> int:
        """
        Return length of the minimal string representation.
        """
        pass


class Polynomial(Expr):
    """
    Polynomial represented as dict variable => coefficient.
    Coefficients integer >= 1.
    No zero coefficients stored.
    """

    __slots__ = ('terms',)

    def __init__(self, terms: Optional[Dict[str, int]] = None):
        """
        terms: dict of var -> coefficient >=1
        """
        self.terms: Dict[str, int] = terms if terms else {}

    @staticmethod
    def from_variable(var: str) -> Polynomial:
        return Polynomial({var: 1})

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Polynomial):
            return False
        return self.terms == other.terms

    def __hash__(self) -> int:
        # hash by frozenset of terms items
        return hash(frozenset(self.terms.items()))

    def add(self, other: Polynomial) -> Polynomial:
        """
        Polynomial addition (self + other)
        """
        result_terms = self.terms.copy()
        for k, v in other.terms.items():
            result_terms[k] = result_terms.get(k, 0) + v
        return Polynomial(result_terms)

    def mul_const(self, c: int) -> Polynomial:
        """
        Multiply polynomial by positive integer c
        """
        return Polynomial({k: v * c for k, v in self.terms.items()})

    def degree(self) -> int:
        """
        Number of distinct variables
        """
        return len(self.terms)

    def is_single_var(self) -> bool:
        """
        True if represents a single variable (power 1)
        """
        return len(self.terms) == 1 and all(v == 1 for v in self.terms.values())

    def same_vars(self, other: Polynomial) -> bool:
        """
        Check if other polynomial has exactly the same variables (keys), ignoring coefficients.
        """
        return set(self.terms.keys()) == set(other.terms.keys())

    def serialize(self) -> str:
        """
        Minimal length serialization, considering:
        - For a single variable with coefficient 1, just the variable.
        - For single variable with coeff>1: var*c
        - For multiple variables (poly), fallback serialization is sum of var with coeff ones: "a+b+c"
          But we want minimal string using multiplications.
        We do not handle parentheses here because this is atomic polynomial factors.
        """
        # If single variable with coefficient 1
        if self.is_single_var():
            var = next(iter(self.terms.keys()))
            return var
        # If single variable with coeff >1
        if self.degree() == 1:
            var, coeff = next(iter(self.terms.items()))
            if coeff > 1:
                return f"{var}*{coeff}"
            else:
                return var  # coeff=1
        # If multiple variables with coefficient 1, must serialize summed as 'a+b+c'
        # variables are all single coefficients
        # problem input guarantees all coeffs >=1 but possibly >1? No adding to multi-coeff in input, so if >1, separated.
        # But multivariable poly with coeffs >1 is only from multiplication, no nested inside parentheses.
        # So serialization fallback is sum of var names
        # But here, we favor a+b+c notation for Polynomial that is 'sum of vars with coefficients'.
        # We just serialize as sum of 'v' repeated coeff times.
        parts = []
        for var in sorted(self.terms.keys()):
            c = self.terms[var]
            parts.append('+'.join([var]*c))
        # Join all parts with '+'
        return '+'.join(parts)

    def length(self) -> int:
        """
        Length of fallback serialization a+a+b+b -> counts '+' too
        """
        term_lengths = [(len(var)*c + (c - 1)) for var, c in self.terms.items()]
        # total pluses: sum of (c-1) for all vars + pluses between vars
        total_pluses = sum((c -1) for c in self.terms.values()) + max(0, self.degree() -1)
        # But above counted pluses inside each term (e.g. a+a means 1 plus)
        # Actually, fallback is flatten to a sequence: e.g. a+a+b = a + a + b = 2 pluses total
        # The correct count = total variables -1

        total_vars = sum(self.terms.values())
        return total_vars + (total_vars -1)  # vars + pluses between them


class ExpressionFactory:
    """
    Factory to build and manipulate expressions from substrings.
    Contains memoization and factoring logic for minimal length expression.
    """

    def __init__(self, S: str):
        self.S = S
        self.n = len(S)
        self.vars = self.extract_vars(S)
        # Parse expression from string S into list of variables in order, separated by '+'
        self.var_list = self.parse_vars(S)
        # Memo dict for intervals: memo[l][r] = Expression object minimal length
        self.memo: List[List[Optional[Expr]]] = [[None]*(self.n) for _ in range(self.n)]

    @staticmethod
    def extract_vars(S: str) -> set[str]:
        return set(ch for ch in S if 'a' <= ch <= 'z')

    @staticmethod
    def parse_vars(S: str) -> List[str]:
        # S guaranteed to be var+(var)+... pattern, length odd
        # vars at even positions 0,2,.. only
        return [S[i] for i in range(0, len(S), 2)]

    def build_polynomial(self, l: int, r: int) -> Polynomial:
        """
        Build polynomial from substring var_list[l:r+1]
        Sum variables with coeff counts.
        """
        freq: Dict[str, int] = {}
        for i in range(l, r+1):
            var = self.var_list[i]
            freq[var] = freq.get(var, 0) + 1
        return Polynomial(freq)

    def compute(self, l: int, r: int) -> Expr:
        """
        Compute minimal length expression for substring var_list[l:r+1].
        Dynamic programming with memoization.
        Attempts:
        - Just summing variables
        - Factoring constants out (e.g. a+a+a => a*3)
        - Factoring sums (e.g. (a+b)*3)
        """
        if self.memo[l][r] is not None:
            return self.memo[l][r]

        poly = self.build_polynomial(l, r)
        # Base candidate: expression as sum of variables with + only (情太くん style)
        base_expr = BasicExpression(poly)

        # Minimal expression candidate currently
        candidates: List[Expr] = [base_expr]

        # Try factoring single variable out (var * coeff)
        # Only possible if polynomial has one variable with coeff >1
        if poly.degree() == 1:
            var, coeff = next(iter(poly.terms.items()))
            if coeff > 1:
                candidates.append(MulExpression(BasicExpression(Polynomial.from_variable(var)), ConstExpression(coeff)))

        # Try full factoring: (expr) * k
        # For that we must find k >=2 s.t. poly = sub_poly * k
        # where sub_poly is polynomial over variables appearing in substring.
        length = r - l + 1

        for k in range(2, length + 1):
            if length % k != 0:
                continue
            size = length // k

            # Candidate sub-expression polynomials segments to repeat k times:
            # Check if substring var_list[l:l+size-1] repeated k times equals current substring

            # We must check if the whole substring can be presented as (sub_expr)*k
            # To do so, partition into k segments of size 'size', compare polynomials to see if all equal

            # Build base polynomial once
            base_poly = self.build_polynomial(l, l + size - 1)
            # Check each segment starting at l + j * size
            can_factor = True
            for seg_index in range(k):
                seg_poly = self.build_polynomial(l + seg_index * size, l + (seg_index + 1) * size - 1)
                if seg_poly != base_poly:
                    can_factor = False
                    break
            if not can_factor:
                continue

            # Now base_poly is arr of sum over size variables, repeated k times
            # Construct minimal expression for base_poly (recursive)
            sub_expr = self.compute(l, l + size - 1)

            # factored expression is MulExpression(sub_expr with parentheses if needed, and const k)
            # Parentheses needed if sub_expr is BasicExpression with multiple terms
            # or if sub_expr is SumExpression (actually, base_expr is BasicExpression representing sum)
            # We can check if sub_expr is BasicExpression with polynomial degree > 1 then parentheses

            use_paren = sub_expr.need_parentheses()

            candidates.append(MulExpression(sub_expr, ConstExpression(k), paren_subexpr=use_paren))

        # Also try plus partition to sum up expressions l..m and m+1..r
        # but only if it reduces length by grouping, and to detect fully sum reassembly (no factoring)
        for mid in range(l, r):
            lhs = self.compute(l, mid)
            rhs = self.compute(mid + 1, r)
            candidates.append(SumExpression(lhs, rhs))

        # Choose minimal length candidate
        min_expr = min(candidates, key=lambda e: e.length())
        self.memo[l][r] = min_expr
        return min_expr

    def minimal_length(self) -> int:
        expr = self.compute(0, len(self.var_list) - 1)
        return expr.length()


class ConstExpression(Expr):
    """
    Expression representing a constant integer (1..9)
    """

    __slots__ = ('value',)

    def __init__(self, value: int):
        self.value = value

    def serialize(self) -> str:
        return str(self.value)

    def length(self) -> int:
        return len(str(self.value))

    def need_parentheses(self) -> bool:
        return False


class BasicExpression(Expr):
    """
    Expression corresponding exactly to a polynomial sum of variables with positive coefficients.
    Does not use multiplication.
    """

    __slots__ = ('poly',)

    def __init__(self, poly: Polynomial):
        self.poly = poly

    def serialize(self) -> str:
        return self.poly.serialize()

    def length(self) -> int:
        # fallback length = sum of variables + plus signs = 2*n-1
        # but calc exactly pluses + variables count
        total_vars = sum(self.poly.terms.values())
        # total_vars chars for variables plus total_vars-1 for plus signs
        return total_vars + (total_vars - 1) if total_vars > 0 else 0

    def need_parentheses(self) -> bool:
        # If poly degree >= 2, parentheses required when multiplied
        return self.poly.degree() >= 2


class SumExpression(Expr):
    """
    Expression representing sum of two expressions with '+'
    """

    __slots__ = ('lhs', 'rhs')

    def __init__(self, lhs: Expr, rhs: Expr):
        self.lhs = lhs
        self.rhs = rhs

    def serialize(self) -> str:
        return f"{self.lhs.serialize()}+{self.rhs.serialize()}"

    def length(self) -> int:
        # length(lhs) + length(rhs) + 1 for '+'
        return self.lhs.length() + self.rhs.length() + 1

    def need_parentheses(self) -> bool:
        # Sums at top-level do not need parentheses for multiplication factors outside.
        return True


class MulExpression(Expr):
    """
    Expression representing multiplication of subexpression by constant integer.
    """
    __slots__ = ('subexpr', 'const', 'paren_subexpr')

    def __init__(self, subexpr: Expr, const: ConstExpression, paren_subexpr: bool = False):
        self.subexpr = subexpr
        self.const = const
        self.paren_subexpr = paren_subexpr

    def serialize(self) -> str:
        if self.paren_subexpr:
            return f"({self.subexpr.serialize()})*{self.const.serialize()}"
        else:
            return f"{self.subexpr.serialize()}*{self.const.serialize()}"

    def length(self) -> int:
        # subexpr length + length '*' + length(const)
        # plus 2 if parens
        l = self.subexpr.length() + self.const.length() + 1
        if self.paren_subexpr:
            l += 2
        return l

    def need_parentheses(self) -> bool:
        # Multiplication expression itself does not need parentheses for external multiplication
        return False


def main():
    import sys
    sys.setrecursionlimit(10**7)
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()

    factory = ExpressionFactory(S)
    print(factory.minimal_length())


if __name__ == "__main__":
    main()