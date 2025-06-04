import sys

variables = ['a','b','c','d','e','f','g','h','i','j','k']

class Parser:
    def __init__(self, s):
        self.s = s
        self.pos = 0
        self.len = len(s)
    def peek(self):
        if self.pos < self.len:
            return self.s[self.pos]
        else:
            return ''
    def consume(self, c=None):
        if self.pos < self.len:
            ch = self.s[self.pos]
            if c is not None and ch != c:
                return None
            self.pos += 1
            return ch
        else:
            return None
    def parse_formula(self):
        ch = self.peek()
        if ch == 'T':
            self.consume('T')
            return ('const', True)
        if ch == 'F':
            self.consume('F')
            return ('const', False)
        if ch in variables:
            self.consume(ch)
            return ('var', ch)
        if ch == '-':
            self.consume('-')
            inner = self.parse_formula()
            return ('not', inner)
        if ch == '(':
            self.consume('(')
            left = self.parse_formula()
            op = None
            if self.s[self.pos:self.pos+2] == '->':
                op = 'imp'
                self.pos += 2
            else:
                op_ch = self.consume()
                if op_ch == '*':
                    op = 'and'
                elif op_ch == '+':
                    op = 'or'
            right = self.parse_formula()
            if self.consume(')') is None:
                pass
            return (op, left, right)
        return None

def eval_formula(ast, valuation):
    tp = ast[0]
    if tp == 'const':
        return ast[1]
    if tp == 'var':
        return valuation[ast[1]]
    if tp == 'not':
        val = eval_formula(ast[1], valuation)
        return not val
    if tp == 'and':
        left = eval_formula(ast[1], valuation)
        right = eval_formula(ast[2], valuation)
        return left and right
    if tp == 'or':
        left = eval_formula(ast[1], valuation)
        right = eval_formula(ast[2], valuation)
        return left or right
    if tp == 'imp':
        left = eval_formula(ast[1], valuation)
        right = eval_formula(ast[2], valuation)
        return (not left) or right

def find_vars(ast, vs):
    tp = ast[0]
    if tp == 'var':
        if ast[1] not in vs:
            vs.append(ast[1])
    elif tp == 'not':
        find_vars(ast[1], vs)
    elif tp in ('and','or','imp'):
        find_vars(ast[1], vs)
        find_vars(ast[2], vs)
    # const: do nothing

for line in sys.stdin:
    line = line.strip()
    if line == '#':
        break
    if '=' not in line:
        continue
    left_str, right_str = line.split('=', 1)
    pleft = Parser(left_str)
    pright = Parser(right_str)
    left_ast = pleft.parse_formula()
    right_ast = pright.parse_formula()
    vs = []
    find_vars(left_ast, vs)
    find_vars(right_ast, vs)
    ok = True
    n = len(vs)
    for state in range(1<<n):
        valuation = {}
        for i in range(n):
            valuation[vs[i]] = (state & (1<<i)) != 0
        lv = eval_formula(left_ast, valuation)
        rv = eval_formula(right_ast, valuation)
        if lv != rv:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")