import sys
import re
from typing import List, Union, Optional, Tuple, Iterator, Dict, Any

class FiniteFieldElement:
    def __init__(self, value: int, prime: int):
        if not (2 <= prime <= 46000):
            raise ValueError("Prime out of bounds")
        self.p = prime
        self.v = value % prime

    def __add__(self, other: 'FiniteFieldElement') -> 'FiniteFieldElement':
        self._check_compatibility(other)
        return FiniteFieldElement((self.v + other.v) % self.p, self.p)

    def __sub__(self, other: 'FiniteFieldElement') -> 'FiniteFieldElement':
        self._check_compatibility(other)
        # Subtraction as addition of additive inverse
        inv = (-other.v) % self.p
        return FiniteFieldElement((self.v + inv) % self.p, self.p)

    def __mul__(self, other: 'FiniteFieldElement') -> 'FiniteFieldElement':
        self._check_compatibility(other)
        return FiniteFieldElement((self.v * other.v) % self.p, self.p)

    def __truediv__(self, other: 'FiniteFieldElement') -> 'FiniteFieldElement':
        self._check_compatibility(other)
        inverse = other.inverse()
        if inverse is None:
            raise ZeroDivisionError("Division by zero in finite field")
        return self * inverse

    def inverse(self) -> Optional['FiniteFieldElement']:
        # Using Fermat's Little Theorem: a^(p-2) mod p is inverse of a mod p (if a != 0)
        if self.v == 0:
            return None
        inv_val = pow(self.v, self.p - 2, self.p)
        return FiniteFieldElement(inv_val, self.p)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FiniteFieldElement):
            return False
        return self.p == other.p and self.v == other.v

    def __repr__(self) -> str:
        return f"FFE({self.v} mod {self.p})"

    def _check_compatibility(self, other: 'FiniteFieldElement'):
        if not isinstance(other, FiniteFieldElement) or self.p != other.p:
            raise TypeError("Operands must be FiniteFieldElement with the same prime")

    def __int__(self) -> int:
        return self.v

class Token:
    def __init__(self, typ: str, val: Any):
        self.type = typ  # 'num', 'op', 'lpar', 'rpar'
        self.val = val

    def __repr__(self):
        return f"Token({self.type}, {self.val})"

class Tokenizer:
    token_specification = [
        ('num',    r'\d+'),
        ('op',     r'[\+\-\*/]'),
        ('lpar',   r'\('),
        ('rpar',   r'\)'),
        ('skip',   r'[ \t]+'),
    ]
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    get_token = re.compile(tok_regex).match

    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.end = len(text)

    def __iter__(self) -> Iterator[Token]:
        mo = self.get_token(self.text)
        pos = 0
        while mo is not None:
            typ = mo.lastgroup
            if typ == 'skip':
                pass
            else:
                val = mo.group(typ)
                yield Token(typ, val)
            pos = mo.end()
            mo = self.get_token(self.text, pos)
        if pos != self.end:
            raise SyntaxError(f"Unexpected character {self.text[pos]} at pos {pos}")

class ExprNode:
    def evaluate(self, ff_prime: int) -> FiniteFieldElement:
        raise NotImplementedError()

    def to_compact_str(self) -> str:
        raise NotImplementedError()

class NumNode(ExprNode):
    def __init__(self, n: int):
        self.n = n

    def evaluate(self, ff_prime: int) -> FiniteFieldElement:
        return FiniteFieldElement(self.n, ff_prime)

    def to_compact_str(self) -> str:
        return str(self.n)

class BinOpNode(ExprNode):
    def __init__(self, left: ExprNode, op: str, right: ExprNode):
        self.left = left
        self.op = op
        self.right = right

    def evaluate(self, ff_prime: int) -> FiniteFieldElement:
        lval = self.left.evaluate(ff_prime)
        rval = self.right.evaluate(ff_prime)

        try:
            if self.op == '+':
                return lval + rval
            elif self.op == '-':
                return lval - rval
            elif self.op == '*':
                return lval * rval
            elif self.op == '/':
                return lval / rval
            else:
                raise RuntimeError(f"Unknown operator {self.op}")
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero")

    def to_compact_str(self) -> str:
        left_str = self.left.to_compact_str()
        right_str = self.right.to_compact_str()
        # According to problem, no spaces around + - * /
        # We do not add extra parentheses: just replicate the formatting as in input compactly
        # Parentheses should be preserved from input, but we do not store them,
        # so just omit them here and keep precedence by AST structure (no parentheses)
        # Instead, we always put operator directly between left and right
        # According to example outputs, parentheses inside expression are stripped when printing?
        # No: output does not contain parentheses, except those around "(mod p)"
        # So print without spaces and without parentheses.
        return f"{left_str}{self.op}{right_str}"

class Parser:
    def __init__(self, tokens: List[Token], p: int):
        self.tokens = tokens
        self.pos = 0
        self.p = p

    def peek(self) -> Optional[Token]:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expected_type: Optional[str] = None, expected_val: Optional[str] = None) -> Token:
        if self.pos >= len(self.tokens):
            raise SyntaxError("Unexpected end of input")
        tok = self.tokens[self.pos]
        if expected_type and tok.type != expected_type:
            raise SyntaxError(f"Expected token type {expected_type}, got {tok.type}")
        if expected_val and tok.val != expected_val:
            raise SyntaxError(f"Expected token value {expected_val}, got {tok.val}")
        self.pos += 1
        return tok

    def parse(self) -> ExprNode:
        return self.parse_expr()

    # expr -> term { (+|-) term }*
    def parse_expr(self) -> ExprNode:
        node = self.parse_term()
        while True:
            tok = self.peek()
            if tok is not None and tok.type == 'op' and tok.val in ('+', '-'):
                op = tok.val
                self.consume('op')
                right = self.parse_term()
                node = BinOpNode(node, op, right)
            else:
                break
        return node

    # term -> factor { (*|/) factor }*
    def parse_term(self) -> ExprNode:
        node = self.parse_factor()
        while True:
            tok = self.peek()
            if tok is not None and tok.type == 'op' and tok.val in ('*', '/'):
                op = tok.val
                self.consume('op')
                right = self.parse_factor()
                node = BinOpNode(node, op, right)
            else:
                break
        return node

    # factor -> num | '(' expr ')'
    def parse_factor(self) -> ExprNode:
        tok = self.peek()
        if tok is None:
            raise SyntaxError("Unexpected end of input in factor")
        if tok.type == 'num':
            self.consume('num')
            n = int(tok.val)
            if n < 0 or n >= self.p:
                # Numbers can only be from 0 to p-1 per problem statement
                # But input may have numbers larger than p-1, we must accept them?
                # Problem states numbers are 0..p-1, so invalid otherwise
                # If out of range, mod them on read? The problem states numbers ARE from 0 to p-1.
                # So no mod, input guaranteed.
                pass
            return NumNode(n)
        elif tok.type == 'lpar':
            self.consume('lpar')
            node = self.parse_expr()
            if self.peek() is None or self.peek().type != 'rpar':
                raise SyntaxError("Unmatched parenthesis")
            self.consume('rpar')
            return node
        else:
            raise SyntaxError(f"Unexpected token {tok.type} {tok.val} in factor")

class Calculator:
    def __init__(self):
        self.cache_primes: Dict[int, bool] = {}

    def is_prime(self, n: int) -> bool:
        if n in self.cache_primes:
            return self.cache_primes[n]
        if n < 2:
            self.cache_primes[n] = False
            return False
        if n in (2,3):
            self.cache_primes[n] = True
            return True
        if n % 2 == 0:
            self.cache_primes[n] = False
            return False
        r = int(n**0.5)
        for i in range(3, r+1, 2):
            if n % i == 0:
                self.cache_primes[n] = False
                return False
        self.cache_primes[n] = True
        return True

    def calculate(self, p: int, expression: str) -> Union[str, int]:
        if not self.is_prime(p):
            raise ValueError(f"{p} is not prime")
        # Tokenize
        tokenizer = Tokenizer(expression)
        try:
            tokens = list(tokenizer)
        except SyntaxError:
            return "NG"
        # Parse
        parser = Parser(tokens, p)
        try:
            tree = parser.parse()
            if parser.pos != len(tokens):
                # Not all tokens consumed
                return "NG"
        except (SyntaxError, ValueError):
            return "NG"
        # Evaluate
        try:
            result = tree.evaluate(p)
            return int(result)
        except ZeroDivisionError:
            return "NG"

    def format_output(self, p: int, expression: str, result: Union[int, str]) -> str:
        # Remove all whitespace around tokens for the expression output
        # But keep numbers and operators and parens glued together, no spaces at all
        # The problem states no spaces around operators/number/brackets in output expression
        tokens = list(Tokenizer(expression))
        parts = []
        for t in tokens:
            parts.append(t.val)
        compact_expr = ''.join(parts)
        if result == "NG":
            return "NG"
        else:
            return f"{compact_expr} = {result} (mod {p})"

def main():
    calc = Calculator()
    # Read lines until "0:" line found
    for line in sys.stdin:
        line = line.strip()
        if line == "0:":
            break
        # parse line of form p:exp
        m = re.match(r'^(\d+)\s*:(.*)$', line)
        if not m:
            # invalid input line
            print("NG")
            continue
        p_str, expr = m.group(1), m.group(2)
        p = int(p_str)
        expr = expr.strip()
        res = calc.calculate(p, expr)
        output = calc.format_output(p, expr, res)
        print(output)

if __name__ == "__main__":
    main()