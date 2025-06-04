from typing import List, Tuple, Dict, Union
import sys
import re
from abc import ABC, abstractmethod

class ParseError(Exception):
    pass

# Abstract Syntax Tree Nodes
class Expr(ABC):
    @abstractmethod
    def expand(self) -> 'Polynomial':
        pass

# Polynomial representation: map from monomials to integer coefficients
# A monomial is a tuple of (var:str, power:int), sorted lex
# The polynomial is a dict: monomial_key -> coefficient
# monomial_key is a tuple of (var, power), sorted by var, powers > 0 only.
class Polynomial:
    def __init__(self, terms: Dict[Tuple[Tuple[str,int], ...], int] = None):
        self.terms: Dict[Tuple[Tuple[str,int], ...], int] = terms if terms else {}

    @staticmethod
    def from_constant(c: int) -> 'Polynomial':
        return Polynomial({tuple(): c}) if c != 0 else Polynomial()

    @staticmethod
    def from_monomial(var: str, power: int) -> 'Polynomial':
        if power == 0:
            return Polynomial.from_constant(1)
        key = ((var, power),)
        return Polynomial({key: 1})

    def __add__(self, other: 'Polynomial') -> 'Polynomial':
        result = Polynomial(self.terms.copy())
        for m, c in other.terms.items():
            result.terms[m] = result.terms.get(m,0) + c
            if result.terms[m] == 0:
                del result.terms[m]
        return result

    def __neg__(self) -> 'Polynomial':
        return Polynomial({m: -c for m, c in self.terms.items()})

    def __sub__(self, other: 'Polynomial') -> 'Polynomial':
        return self + (-other)

    def __mul__(self, other: 'Polynomial') -> 'Polynomial':
        result_terms: Dict[Tuple[Tuple[str,int], ...], int] = {}
        for m1, c1 in self.terms.items():
            for m2, c2 in other.terms.items():
                merged = Polynomial.merge_monomials(m1, m2)
                result_terms[merged] = result_terms.get(merged, 0) + c1 * c2
        # Remove zero coefficients
        result_terms = {m: c for m, c in result_terms.items() if c != 0}
        return Polynomial(result_terms)

    @staticmethod
    def merge_monomials(m1: Tuple[Tuple[str,int], ...], m2: Tuple[Tuple[str,int], ...]) -> Tuple[Tuple[str,int], ...]:
        # merge two sorted lists of (var, power) summing powers of same var
        merged = []
        i, j = 0, 0
        while i < len(m1) and j < len(m2):
            if m1[i][0] == m2[j][0]:
                p = m1[i][1] + m2[j][1]
                if p != 0:
                    merged.append((m1[i][0], p))
                i += 1
                j += 1
            elif m1[i][0] < m2[j][0]:
                merged.append(m1[i])
                i += 1
            else:
                merged.append(m2[j])
                j += 1
        while i < len(m1):
            merged.append(m1[i])
            i += 1
        while j < len(m2):
            merged.append(m2[j])
            j += 1
        return tuple(merged)

    def __eq__(self, other) -> bool:
        # Equality by comparing normalized terms
        return self.terms == other.terms

# Expression subclasses:
class ConstExpr(Expr):
    def __init__(self, value: int):
        self.value = value

    def expand(self) -> Polynomial:
        return Polynomial.from_constant(self.value)

class VarExpr(Expr):
    def __init__(self, var: str, power: int = 1):
        self.var = var
        self.power = power

    def expand(self) -> Polynomial:
        return Polynomial.from_monomial(self.var, self.power)

class AddExpr(Expr):
    def __init__(self, terms: List[Expr]):
        self.terms = terms  # list of Expr

    def expand(self) -> Polynomial:
        result = Polynomial()
        for t in self.terms:
            result = result + t.expand()
        return result

class SubExpr(Expr):
    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

    def expand(self) -> Polynomial:
        return self.left.expand() - self.right.expand()

class MulExpr(Expr):
    def __init__(self, factors: List[Expr]):
        self.factors = factors  # list of Expr

    def expand(self) -> Polynomial:
        result = Polynomial.from_constant(1)
        for f in self.factors:
            result = result * f.expand()
        return result

class Parser:
    def __init__(self, s: str):
        # Remove all spaces for easier parsing except where needed for coefficients
        self.s = s
        self.pos = 0
        self.len = len(s)

    def peek(self) -> str:
        if self.pos < self.len:
            return self.s[self.pos]
        return ''

    def consume(self, c: str) -> bool:
        if self.peek() == c:
            self.pos += 1
            return True
        return False

    def expect(self, c: str):
        if not self.consume(c):
            raise ParseError(f"Expected '{c}' at pos {self.pos}")

    def eof(self) -> bool:
        return self.pos >= self.len

    # Parsing helpers: skip spaces except those important for integers following integers or digits after ^
    # The problem states no spaces between digits of an integer, so safe to strip all spaces for parsing,
    # but to keep tokens correct, implement carefully.
    def parse_expression(self) -> Expr:
        # Parse an expression -> sequence of terms separated by '+' or '-'
        # Note: '+' and '-' are always binary, no unary

        # It's easier to tokenize upfront and parse tokens, because spaces can be arbitrary.
        tokens = self.tokenize(self.s)
        # Now parse from tokens:
        parser = TokensParser(tokens)
        expr = parser.parse_expression()
        if parser.pos != len(tokens):
            raise ParseError("Extra tokens after expression end")
        return expr

    def tokenize(self, s: str) -> List[str]:
        # Tokenize input s into:
        # integers (non-negative), variables (a-z), '^', '+', '-', '(', ')'
        # Spaces handled: remove spaces except where integer digits separated by spaces after integer or after ^ digit,
        # but per problem statement spaces won't be inside integers digits, so safe to remove all spaces.
        s_no_spaces = ''.join(s.split())

        tokens = []
        i = 0
        while i < len(s_no_spaces):
            c = s_no_spaces[i]
            if c in '+-^()':
                tokens.append(c)
                i += 1
            elif '0' <= c <= '9':
                j = i + 1
                while j < len(s_no_spaces) and '0' <= s_no_spaces[j] <= '9':
                    j += 1
                tokens.append(s_no_spaces[i:j])
                i = j
            elif 'a' <= c <= 'z':
                tokens.append(c)
                i += 1
            else:
                raise ParseError(f"Invalid character '{c}' in input")
        return tokens

class TokensParser:
    def __init__(self, tokens: List[str]):
        self.tokens = tokens
        self.pos = 0
        self.len = len(tokens)

    def peek(self) -> str:
        if self.pos < self.len:
            return self.tokens[self.pos]
        return ''

    def consume(self, expected: str = None) -> str:
        if self.pos >= self.len:
            raise ParseError("Unexpected end of tokens")
        token = self.tokens[self.pos]
        if expected is not None and token != expected:
            raise ParseError(f"Expected token {expected} but got {token}")
        self.pos += 1
        return token

    def eof(self) -> bool:
        return self.pos >= self.len

    # Expression := Term {('+'|'-') Term}*
    def parse_expression(self) -> Expr:
        left = self.parse_term()
        while not self.eof() and self.peek() in ('+', '-'):
            op = self.consume()
            right = self.parse_term()
            if op == '+':
                # combine left + right = AddExpr
                if isinstance(left, AddExpr):
                    left.terms.append(right)
                else:
                    left = AddExpr([left,right])
            else:
                # left - right = SubExpr
                left = SubExpr(left, right)
        return left

    # Term := Factor { Factor }*
    def parse_term(self) -> Expr:
        factors = []
        while True:
            if self.eof():
                break
            # Factor can start with number, variable, '('
            # But '+' or '-' token means end of term
            if self.peek() in ('+', '-', ')'):
                break
            factors.append(self.parse_factor())
        if not factors:
            raise ParseError("Empty term")
        if len(factors) == 1:
            return factors[0]
        else:
            return MulExpr(factors)

    # Factor := integer | variable [ '^' digit ] | '(' Expression ')'
    def parse_factor(self) -> Expr:
        token = self.peek()
        if token.isdigit():
            # ConstExpr
            num = int(self.consume())
            return ConstExpr(num)
        elif len(token) == 1 and 'a' <= token <= 'z':
            var = self.consume()
            power = 1
            if not self.eof() and self.peek() == '^':
                self.consume('^')
                if self.eof():
                    raise ParseError("Expected digit after '^'")
                power_token = self.consume()
                if not power_token.isdigit() or power_token == '0':
                    raise ParseError(f"Invalid power '{power_token}', must be non-zero digit")
                power = int(power_token)
            return VarExpr(var, power)
        elif token == '(':
            self.consume('(')
            expr = self.parse_expression()
            self.consume(')')
            return expr
        else:
            raise ParseError(f"Invalid factor token '{token}'")

class ExpressionComparator:
    @staticmethod
    def equivalent(e1: Expr, e2: Expr) -> bool:
        p1 = e1.expand()
        p2 = e2.expand()
        return p1 == p2

def process_block(lines: List[str]) -> List[str]:
    # first line is Mr. Simpson's answer
    simpson_expr_line = lines[0]
    parser = Parser(simpson_expr_line)
    try:
        simpson_expr = parser.parse_expression()
    except ParseError:
        # If parsing error, no answer is equivalent
        outputs = []
        for _ in lines[1:]:
            outputs.append('no')
        outputs.append('.')
        return outputs

    outputs = []
    for student_line in lines[1:]:
        if student_line == '.':
            continue
        try:
            parser_stu = Parser(student_line)
            stu_expr = parser_stu.parse_expression()
            equ = ExpressionComparator.equivalent(simpson_expr, stu_expr)
            outputs.append('yes' if equ else 'no')
        except ParseError:
            outputs.append('no')
    outputs.append('.')
    return outputs

def main():
    blocks = []
    current_block = []
    for line in sys.stdin:
        line = line.strip()
        if line == '.':
            if current_block:
                blocks.append(current_block)
                current_block = []
            else:
                # line '.' with empty current_block: end of input
                break
        else:
            current_block.append(line)
    # There might be a block without trailing '.'? Per spec no, so safe.

    for block in blocks:
        results = process_block(block)
        for r in results:
            print(r)

if __name__ == '__main__':
    main()