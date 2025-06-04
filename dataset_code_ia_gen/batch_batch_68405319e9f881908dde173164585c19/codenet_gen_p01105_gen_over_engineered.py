from abc import ABC, abstractmethod
from functools import lru_cache
from itertools import product


class BoolExpr(ABC):
    """
    Abstract base class for all Boolean expressions.
    Anticipates extensions with visitor patterns or more operators.
    """

    @abstractmethod
    def evaluate(self, env: dict) -> bool:
        """
        Evaluate the expression for a given variable environment.
        env: dict mapping variable names ('a','b','c','d') to bool.
        """
        pass

    @abstractmethod
    def canonical_forms(self) -> set:
        """
        Return a set of canonical string representations of this expression,
        representing the same Boolean function.
        This abstraction anticipates future caching and normalization strategies.
        Each returned form is an expression string.
        """
        pass


class Const(BoolExpr):
    __slots__ = ('value',)

    def __init__(self, value: bool):
        self.value = value

    def evaluate(self, env: dict) -> bool:
        return self.value

    def canonical_forms(self) -> set:
        return { '1' if self.value else '0' }


class Var(BoolExpr):
    __slots__ = ('name',)

    def __init__(self, name: str):
        self.name = name

    def evaluate(self, env: dict) -> bool:
        return env[self.name]

    def canonical_forms(self) -> set:
        # single variable name as is
        return {self.name}


class Not(BoolExpr):
    __slots__ = ('expr',)

    def __init__(self, expr: BoolExpr):
        self.expr = expr

    def evaluate(self, env: dict) -> bool:
        return not self.expr.evaluate(env)

    def canonical_forms(self) -> set:
        # We produce minimal forms by prefixing '-' to child's minimal canonical forms
        forms = set()
        for f in self.expr.canonical_forms():
            # Avoid double negations in normalized form:
            if f.startswith('-'):
                # --x == x, so flatten
                forms.update({f[1:]})
            else:
                forms.add('-' + f)
        return forms


class BinOp(BoolExpr):
    __slots__ = ('left', 'right')

    def __init__(self, left: BoolExpr, right: BoolExpr):
        self.left = left
        self.right = right


class And(BinOp):
    def evaluate(self, env: dict) -> bool:
        return self.left.evaluate(env) and self.right.evaluate(env)

    def canonical_forms(self) -> set:
        # Generate all pairs of children canonical forms
        left_forms = self.left.canonical_forms()
        right_forms = self.right.canonical_forms()
        # Because AND is commutative, we impose order to avoid duplicates:
        forms = set()
        pairs = []
        for lf in left_forms:
            for rf in right_forms:
                pairs.append((lf, rf))
        # Sort pair lex to keep order
        for lf, rf in pairs:
            if lf < rf:
                expr_str = f'({lf}*{rf})'
            else:
                expr_str = f'({rf}*{lf})'
            forms.add(expr_str)
        return forms


class Xor(BinOp):
    def evaluate(self, env: dict) -> bool:
        return self.left.evaluate(env) != self.right.evaluate(env)

    def canonical_forms(self) -> set:
        # XOR is commutative and associative but grammar uses binary parentheses.
        # We impose left<right order lexicographically to get canonical forms.
        left_forms = self.left.canonical_forms()
        right_forms = self.right.canonical_forms()
        forms = set()
        pairs = []
        for lf in left_forms:
            for rf in right_forms:
                pairs.append((lf, rf))
        for lf, rf in pairs:
            if lf < rf:
                expr_str = f'({lf}^{rf})'
            else:
                expr_str = f'({rf}^{lf})'
            forms.add(expr_str)
        return forms


class Parser:
    """
    Recursive descent parser using the grammar:
    <E> ::= 0 | 1 | a | b | c | d | -<E> | (<E> ^ <E>) | (<E> * <E>)
    """

    def __init__(self, s: str):
        self.s = s
        self.pos = 0
        self.length = len(s)

    def parse(self) -> BoolExpr:
        expr = self.parse_expr()
        if self.pos != self.length:
            raise ValueError(f"Unexpected chars at pos {self.pos}")
        return expr

    def parse_expr(self) -> BoolExpr:
        if self.pos >= self.length:
            raise ValueError("Unexpected end of input")

        c = self.s[self.pos]

        # Terminal 0 or 1
        if c == '0':
            self.pos += 1
            return Const(False)
        if c == '1':
            self.pos += 1
            return Const(True)

        # Terminal variable
        if c in ('a', 'b', 'c', 'd'):
            self.pos += 1
            return Var(c)

        # Negation
        if c == '-':
            self.pos += 1
            sub = self.parse_expr()
            return Not(sub)

        # Paren construct: (<E> op <E>)
        if c == '(':
            self.pos += 1
            left = self.parse_expr()
            if self.pos >= self.length:
                raise ValueError("Expected operator but got end of input")
            op = self.s[self.pos]
            if op not in ('^', '*'):
                raise ValueError(f"Expected operator ^ or *, got {op} at pos {self.pos}")
            self.pos += 1
            right = self.parse_expr()
            if self.pos >= self.length or self.s[self.pos] != ')':
                raise ValueError(f"Expected ')' at pos {self.pos}")
            self.pos += 1
            if op == '*':
                return And(left, right)
            else:
                return Xor(left, right)

        raise ValueError(f"Unexpected char {c} at pos {self.pos}")


class TruthTable:
    """
    Abstraction to compute and represent truth tables of Boolean expressions with 4 vars.
    Encapsulates mapping env->val and comparison.
    """

    VARS = ['a', 'b', 'c', 'd']
    ALL_ENVS = list(product([False, True], repeat=4))

    def __init__(self, expr: BoolExpr):
        # We store 16 bits corrsponding to the 16 envs in VARS order
        bits = 0
        for i, env_values in enumerate(self.ALL_ENVS):
            env = dict(zip(self.VARS, env_values))
            val = expr.evaluate(env)
            if val:
                bits |= (1 << i)
        self.bits = bits

    def __eq__(self, other) -> bool:
        return isinstance(other, TruthTable) and self.bits == other.bits

    def __hash__(self):
        return hash(self.bits)


class Compressor:
    """
    This class organizes a bottom-up cache of minimal length expressions for each Boolean function.
    Extremely sophisticated structure to precompute minimal lengths leveraging the grammar and truth tables.
    Suitable for future extensions like multiple operators, arbitrary variables counts etc.
    """

    def __init__(self):
        # Maps TruthTable.bits -> minimal length expression strings with that function
        self.cache = dict()
        # We use the set of vars as primitives
        self.primitives = [
            (TruthTable(Var(v)).bits, v) for v in TruthTable.VARS
        ] + [
            (TruthTable(Const(False)).bits, '0'),
            (TruthTable(Const(True)).bits, '1')
        ]
        # Negations cache: truth bits -> minimal form length (and their forms, but forms only strings)
        self.neg_cache = dict()

        # Initialize cache with primitives
        for bits, expr_str in self.primitives:
            self.cache[bits] = {expr_str}

        # For negations of primitives
        self._build_negations()

        # We precompute minimal expressions iteratively to cover all needed functions.
        # The number of Boolean functions of 4 vars is 2^(16) which is huge,
        # so instead of all, we build cache only incrementally per input expression.

    def _build_negations(self):
        # For each cached function, cache negation minimal forms
        # We do this once to bootstrap negations of primitives.
        new_entries = dict()
        for bits, forms in self.cache.items():
            neg = bits ^ 0xFFFF  # 16 bits all ones
            neg_forms = set()
            for f in forms:
                # Only add negation form if it respects grammar as minimal form candidates
                # We add '-' + f unless f is already a negation, then strip double negations
                if f.startswith('-') and len(f) >= 2:
                    # --x == x
                    nf = f[1:]
                else:
                    nf = '-' + f
                neg_forms.add(nf)
            if neg not in self.cache:
                new_entries[neg] = neg_forms
            else:
                # Merge and keep minimal length forms
                current = self.cache[neg]
                merged = current | neg_forms
                # Keep only minimal length forms
                min_len = min(len(x) for x in merged)
                minimal = {x for x in merged if len(x) == min_len}
                new_entries[neg] = minimal
        # Add negations to cache
        for k, v in new_entries.items():
            if k in self.cache:
                self.cache[k].update(v)
            else:
                self.cache[k] = v

    def minimize(self, expr: BoolExpr) -> int:
        """
        Given an expr, find minimal length of an expression string equivalent to expr.
        The minimal string must be valid under grammar and evaluate identically over all environments.
        """
        # We compute its truth table:
        tt = TruthTable(expr)

        # We use a memoized bottom-up construction of minimal forms to avoid recomputations:

        @lru_cache(None)
        def dfs(bits: int):
            """
            Return a set of minimal length expression strings representing bits.
            """
            # If bits in cache, return cached forms directly:
            if bits in self.cache:
                # prune to minimal length
                forms = self.cache[bits]
                min_len = min(len(x) for x in forms)
                return {x for x in forms if len(x) == min_len}

            results = set()

            # Try negation of known bits if we have them cached:
            neg_bits = bits ^ 0xFFFF
            if neg_bits in self.cache:
                neg_forms = self.cache[neg_bits]
                min_len = min(len(x) for x in neg_forms)
                candidates = {'-' + x if not x.startswith('-') else x[1:] for x in neg_forms if len(x) == min_len}
                min_cand_len = min(len(x) for x in candidates)
                candidates = {x for x in candidates if len(x) == min_cand_len}
                results.update(candidates)

            # Try binary ops:
            # Because the grammar requires parentheses around binary ops, length always at least 5
            # Enumerate all partitions of bits into left and right operands that could be combined by AND or XOR

            # We will try all pairs from cache, but that is impossible since 2^16 huge.
            # Instead, recursively try combinations built from smaller bits.
            # But we do not know which functions compose bits.
            # So we memoize feasible from primitives and inputs from top.

            # To avoid infinite recursion, we forbid direct recursion by depth limit or caching.
            # Instead, use a memo and do a iterative discovery starting from primitives.

            # This is complicated, so we do a heuristic top-down approach to guess minimal expressions.

            # To attempt operations, we try all pairs (l, r) with lbits ^ rbits == bits if op is XOR,
            # and lbits & rbits == bits if op is AND, but that's complicated.
            # We'll do a loop over cached keys and try AND and XOR:

            # We trust the current cache to contain some expressions.
            for lbits in list(self.cache.keys()):
                for rbits in list(self.cache.keys()):
                    # Try AND
                    and_bits = lbits & rbits
                    if and_bits == bits:
                        # Compose forms from left and right minimal:
                        for lf in dfs(lbits):
                            for rf in dfs(rbits):
                                # produce normalized form (order lex for commutative)
                                a, b = sorted([lf, rf])
                                cand = '(' + a + '*' + b + ')'
                                results.add(cand)

                    # Try XOR
                    xor_bits = lbits ^ rbits
                    if xor_bits == bits:
                        for lf in dfs(lbits):
                            for rf in dfs(rbits):
                                a, b = sorted([lf, rf])
                                cand = '(' + a + '^' + b + ')'
                                results.add(cand)

            # Also try not to forget look up primitives
            if bits in self.cache:
                results.update(self.cache[bits])

            # Choose minimal length expressions
            if not results:
                # Should never happen if primitives are included
                return set()

            min_len = min(len(x) for x in results)
            minimal = {x for x in results if len(x) == min_len}

            # Cache this minimal set
            self.cache[bits] = minimal

            # For negation cache:
            neg_bits = bits ^ 0xFFFF
            if neg_bits not in self.cache:
                self.cache[neg_bits] = {('-' + x if not x.startswith('-') else x[1:]) for x in minimal}

            return minimal

        # Just call dfs on this expr's bits and return minimal length of any form
        minimal_forms = dfs(tt.bits)
        return min(len(f) for f in minimal_forms)


def main():
    compressor = Compressor()
    while True:
        line = input()
        if line == '.':
            break
        parser = Parser(line)
        expr = parser.parse()
        result = compressor.minimize(expr)
        print(result)


if __name__ == "__main__":
    main()