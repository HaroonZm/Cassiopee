import sys
sys.setrecursionlimit(10**7)

N, K = map(int, input().split())
parts = {}
for _ in range(K):
    line = input().split()
    name = line[0]
    h = int(line[1])
    g = [list(map(int, input().split())) for __ in range(h - 1)]
    # Build permutation of size N from this part
    perm = list(range(N))
    for row in range(h - 1):
        for c in range(N - 1):
            if g[row][c] == 1:
                perm[c], perm[c+1] = perm[c+1], perm[c]
    # Invert perm to get mapping from top to bottom
    # Actually we want: start from top i, follow perm to get bottom
    # Here perm[i] = position after this part for vertical line i (zero-based)
    # But the way we built perm is by swapping perm[c] and perm[c+1]
    # So it is final mapping from bottom to top? Actually perm is the bottom order.
    # To get the image of i, we just use perm[i].
    parts[name] = perm

E = int(input())
expressions = [input() for _ in range(E)]

# Parsing the expression language:
# expression := repetition | term + expression | term
# repetition := number ( expression )
# term := part_name | repetition
# number is integer >= 1
# part_name is a letter (A-Z)

# We parse and generate the overall permutation for each expression.

# Permutations are lists of length N, mapping line i (top) to line perm[i] (bottom).
# To combine permutations P and Q (concatenate parts P followed by Q), the resulting permutation R is R[i] = Q[P[i]]

class Parser:
    def __init__(self, s):
        self.s = s
        self.pos = 0
        self.len = len(s)

    def peek(self):
        if self.pos < self.len:
            return self.s[self.pos]
        return ''

    def eat(self, c):
        if self.peek() == c:
            self.pos += 1
            return True
        return False

    def parse_number(self):
        start = self.pos
        while self.peek().isdigit():
            self.pos += 1
        return int(self.s[start:self.pos])

    def parse_part(self):
        # parse either repetition: number(expr) or part_name
        if self.peek().isdigit():
            n = self.parse_number()
            assert self.eat('(')
            inner = self.parse_expr()
            assert self.eat(')')
            return self.repeat_permutation(inner, n)
        else:
            # part name is a single letter uppercase
            c = self.peek()
            assert 'A' <= c <= 'Z'
            self.pos += 1
            return parts[c]

    def parse_expr(self):
        # parse a sequence connected by '+'
        perm = self.parse_part()
        while self.eat('+'):
            right = self.parse_part()
            perm = self.combine(perm, right)
        return perm

    def combine(self, p1, p2):
        # compose two permutations: p1 followed by p2
        # i mapped by p1 then by p2: res[i] = p2[p1[i]]
        return [p2[p1[i]] for i in range(N)]

    def repeat_permutation(self, p, m):
        # exponentiate permutation p to power m
        # binary exponentiation
        res = list(range(N))
        base = p
        while m > 0:
            if m & 1:
                res = self.combine(res, base)
            base = self.combine(base, base)
            m >>= 1
        return res

for expr in expressions:
    parser = Parser(expr)
    perm = parser.parse_expr()
    print(*[x+1 for x in perm])