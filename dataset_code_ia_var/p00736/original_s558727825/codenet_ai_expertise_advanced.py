from functools import lru_cache, partial
import re

JUST_LEN = 60

# Define token patterns with comprehension and automatic group assignment
TOKENS = [
    ('NUM',    r'\d+'),
    ('PLUS',   r'\+'),
    ('MINUS',  r'-'),
    ('TIMES',  r'\*'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('WS',     r'\s+'),
]
token_regex = '|'.join(f'(?P<{name}>{pat})' for name, pat in TOKENS)
master_pattern = re.compile(token_regex)

from typing import NamedTuple, Iterator

class Token(NamedTuple):
    type: str
    value: str

def generate_tokens(pattern: re.Pattern, text: str) -> Iterator[Token]:
    for m in pattern.finditer(text):
        if m.lastgroup != 'WS':
            yield Token(m.lastgroup, m.group())

# Logic functions, optimized using tuple indexing and lru_cache
@lru_cache(maxsize=None)
def minus(x):     # Not operation in ternary logic
    return (2, 1, 0)[x]

@lru_cache(maxsize=None)
def mult(x, y):   # And operation in ternary logic
    tbl = (
        (0, 0, 0),
        (0, 1, 1),
        (0, 1, 2),
    )
    return tbl[x][y]

@lru_cache(maxsize=None)
def add(x, y):    # Or operation in ternary logic
    tbl = (
        (0, 1, 2),
        (1, 1, 2),
        (2, 2, 2),
    )
    return tbl[x][y]

class ExpressionEvaluator:
    def parse(self, text: str) -> int:
        self.tokens = iter(generate_tokens(master_pattern, text))
        self.current_token = None
        self._advance()
        return self.expr()

    def _advance(self):
        self.current_token = next(self.tokens, None)

    def _accept(self, token_type):
        if self.current_token and self.current_token.type == token_type:
            return True
        return False

    def _expect(self, token_type):
        if not self._accept(token_type):
            raise SyntaxError(f'Expected {token_type}')

    def expr(self):
        val = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.current_token.type
            self._advance()
            rhs = self.term()
            if op == 'PLUS':
                val = add(val, rhs)
            else:
                val = add(val, minus(rhs))
        return val

    def term(self):
        val = self.factor()
        while self._accept('TIMES'):
            self._advance()
            rhs = self.factor()
            val = mult(val, rhs)
        return val

    def factor(self):
        if self._accept('NUM'):
            val = int(self.current_token.value)
            self._advance()
            return val
        elif self._accept('LPAREN'):
            self._advance()
            val = self.expr()
            self._expect('RPAREN')
            self._advance()
            return val
        elif self._accept('MINUS'):
            self._advance()
            return minus(self.factor())
        else:
            raise SyntaxError('Expected NUMBER or LPAREN or MINUS')

e = ExpressionEvaluator()

try:
    while True:
        rS = input()
        if rS == '.': break
        ans = sum(
            e.parse(rS.replace('P', str(p)).replace('Q', str(q)).replace('R', str(r))) == 2
            for p in range(3) for q in range(3) for r in range(3)
        )
        print(ans)
except EOFError:
    pass