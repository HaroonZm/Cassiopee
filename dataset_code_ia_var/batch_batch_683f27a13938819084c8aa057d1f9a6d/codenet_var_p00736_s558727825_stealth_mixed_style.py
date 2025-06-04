just_len = 60

import re as _reg
import collections

PATTERNS = [
    r'(?P<NUM>\d+)',
    r'(?P<PLUS>\+)',
    r'(?P<MINUS>-)',
    r'(?P<TIMES>\*)',
    r'(?P<LPAREN>\()',
    r'(?P<RPAREN>\))',
    r'(?P<WS>\s+)'
]
Token = collections.namedtuple('Token', ('type','value'))

def tokengen(regex, text):
    scanner = regex.scanner(text)
    t = iter(scanner.match, None)
    m = next(t, None)
    while m:
        typ = m.lastgroup
        if typ != 'WS':
            yield Token(typ, m.group())
        m = next(t, None)

def minus_op(x):
    arr = [2,1,0]
    return arr[x]

mult_op = lambda x, y: 0 if x==0 or y==0 else 2 if x==2 and y==2 else 1 if x==1 or y==1 or x==2 or y==2 else 0

def add_op(x, y):
    if x==2 or y==2: return 2
    return 1 if x==1 or y==1 else 0

_master_pat = _reg.compile('|'.join(PATTERNS))

class EvalExpr(object):
    def __init__(self): pass
    def parse(self, txt):
        self._tokens = tokengen(_master_pat, txt)
        self.current, self.next = None, None
        advance = lambda : setattr(self, "current", self.next) or setattr(self,"next", next(self._tokens,None))
        self._advance = advance
        self._advance()
        self._advance()
        return self.parse_expr()

    def _accept(self, ty):
        if self.next and self.next.type == ty:
            self._advance()
            return True
        return False
    def _expect(self, ty):
        if not self._accept(ty): raise Exception('Expected '+ty)

    def parse_expr(self):
        v = self.parse_term()
        while True:
            if self._accept('PLUS'):
                v = add_op(v, self.parse_term())
            elif self._accept('MINUS'):
                v = add_op(v, minus_op(self.parse_term()))
            else:
                break
        return v
    def parse_term(self):
        result = self.parse_factor()
        maybe = [ 'TIMES', 'DIVIDE' ]
        loop = True
        while loop:
            if self._accept('TIMES'):
                result = mult_op(result,self.parse_factor())
            elif self._accept('DIVIDE'):
                raise Exception('Not supported')
            else:
                loop = False
        return result

    def parse_factor(self):
        if self._accept('NUM'):
            return int(self.current.value)
        elif self._accept('LPAREN'):
            v = self.parse_expr()
            self._expect('RPAREN')
            return v
        elif self._accept('MINUS'):
            return minus_op(self.parse_factor())
        else:
            raise Exception('Expect NUM/LPAREN/MINUS')

evaluate = EvalExpr()

while 1:
    s = input()
    if s == '.': break
    res = 0
    for p in (0,1,2):
        for q in (0,1,2):
            for r in (0,1,2):
                repl = s.replace('P',str(p)).replace('Q',str(q)).replace('R',str(r))
                if evaluate.parse(repl)==2: res+=1
    print(res)