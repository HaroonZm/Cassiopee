just_len = 60

import re
import collections

NUM     = r'(?P<NUM>\d+)'
PLUS    = r'(?P<PLUS>\+)'
MINUS   = r'(?P<MINUS>-)'
TIMES   = r'(?P<TIMES>\*)'
LPAREN  = r'(?P<LPAREN>\()'
RPAREN  = r'(?P<RPAREN>\))'
WS      = r'(?P<WS>\s+)'

master_pattern = re.compile('|'.join((NUM, PLUS, MINUS, TIMES, LPAREN, RPAREN, WS)))
Token = collections.namedtuple('Token', ['type', 'value'])

def generate_tokens(pattern, text):
    scanner = pattern.scanner(text)
    for m in iter(scanner.match, None):
        token = Token(m.lastgroup, m.group())

        if token.type != 'WS':
            yield token

def minus(x):
  if x==0: ans=2
  if x==1: ans=1
  if x==2: ans=0
  return ans

def mult(x,y):
  if x==0:
    a=0
  if x==1:
    if y==0: a=0
    if y==1: a=1
    if y==2: a=1
  if x==2:
    if y==0: a=0
    if y==1: a=1
    if y==2: a=2
  return a

def add(x,y):
  if x==0:
    if y==0: a=0
    if y==1: a=1
    if y==2: a=2
  if x==1:
    if y==0: a=1
    if y==1: a=1
    if y==2: a=2
  if x==2:
    a=2
  return a

class ExpressionEvaluator:
    def parse(self, text):
        self.tokens = generate_tokens(master_pattern, text)
        self.current_token = None
        self.next_token = None
        self._advance()

        # expr is the top level grammar. So we invoke that first.
        # it will invoke other function to consume tokens according to grammar rule.
        return self.expr()

    def _advance(self):
        self.current_token, self.next_token = self.next_token, next(self.tokens, None)

    def _accept(self, token_type):
        # if there is next token and token type matches
        if self.next_token and self.next_token.type == token_type:
            self._advance()
            return True
        else:
            return False

    def _expect(self, token_type):
        if not self._accept(token_type):
            raise SyntaxError('Expected ' + token_type)

    def expr(self):
        '''
        expression ::= term { ( +|-) term } *
        '''
        expr_value = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.current_token.type

            right = self.term()
            if op == 'PLUS':
                #expr_value += right
                expr_value = add(expr_value, right)
            elif op == 'MINUS':
                #expr_value -= right
                expr_value = add(expr_value, minus(right))
            else:
                raise SyntaxError('Should not arrive here ' + op)

        return expr_value

    def term(self):
        '''
        term    ::= factor { ('*') factor } *
        '''
        term_value = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.current_token.type

            if op == 'TIMES':
                #term_value *= self.factor()
                term_value = mult(term_value, self.factor())
            else:
                raise SyntaxError('Should not arrive here ' + op)

        return term_value

    def factor(self):
        '''
        factor  ::= NUM | (expr) | -(factor)

        '''

        # it can be a number
        if self._accept('NUM'):
            expr_value = int(self.current_token.value)
        # or (expr)
        elif self._accept('LPAREN'):
            expr_value = self.expr()
            self._expect('RPAREN')
        elif self._accept('MINUS'):
            expr_value = minus(self.factor())
        else:
            raise SyntaxError('Expect NUMBER or LPAREN')
        return expr_value

e = ExpressionEvaluator()
# print('parse 2'.ljust(just_len),
#       e.parse('2'))
#
# print('parse 2 + 3'.ljust(just_len),
#       e.parse('2 + 3'))
# print('parse 2 + 3 * 4'.ljust(just_len),
#       e.parse('2 + 3 * 4'))
#
# print('parse (2 + 3) * 4'.ljust(just_len),
#       e.parse('(2 + 3) * 4'))
while True:
  rS=input()
  if rS=='.': break

  ans=0
  for p in range(3):
    for q in range(3):
      for r in range(3):
        S = rS.replace('P',str(p))\
              .replace('Q',str(q))\
              .replace('R',str(r))
        if e.parse(S)==2: ans+=1
  print(ans)