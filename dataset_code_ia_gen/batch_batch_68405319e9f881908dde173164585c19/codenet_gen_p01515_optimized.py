import sys
sys.setrecursionlimit(10**7)

class Parser:
    def __init__(self, s):
        self.s = s
        self.pos = 0
        self.len = len(s)

    def peek(self):
        if self.pos < self.len:
            return self.s[self.pos]
        return ''

    def consume(self, c):
        if self.s[self.pos:self.pos+len(c)] == c:
            self.pos += len(c)
            return True
        return False

    def parse_formula(self):
        c = self.peek()
        if c == 'T':
            self.pos += 1
            return ('T',)
        if c == 'F':
            self.pos += 1
            return ('F',)
        if c in 'abcdefghijk':
            self.pos += 1
            return ('var', c)
        if c == '-':
            self.pos += 1
            f = self.parse_formula()
            return ('not', f)
        if c == '(':
            self.pos += 1
            left = self.parse_formula()
            if self.consume('*'):
                op = '*'
            elif self.consume('+'):
                op = '+'
            elif self.consume("->"):
                op = '->'
            else:
                # invalid op, but problem states BNF is guaranteed
                op = ''
            right = self.parse_formula()
            if not self.consume(')'):
                pass
            return (op, left, right)
        return None

def eval_expr(expr, env):
    t = expr[0]
    if t == 'T':
        return True
    if t == 'F':
        return False
    if t == 'var':
        return env[expr[1]]
    if t == 'not':
        return not eval_expr(expr[1], env)
    if t == '*':
        return eval_expr(expr[1], env) and eval_expr(expr[2], env)
    if t == '+':
        return eval_expr(expr[1], env) or eval_expr(expr[2], env)
    if t == '->':
        return (not eval_expr(expr[1], env)) or eval_expr(expr[2], env)

def vars_in_expr(expr, s=None):
    if s is None:
        s = set()
    t = expr[0]
    if t == 'var':
        s.add(expr[1])
    elif t in ('not',):
        vars_in_expr(expr[1], s)
    elif t in ('*', '+', '->'):
        vars_in_expr(expr[1], s)
        vars_in_expr(expr[2], s)
    return s

for line in sys.stdin:
    line = line.strip()
    if line == '#':
        break
    eq_pos = line.find('=')
    left_s = line[:eq_pos]
    right_s = line[eq_pos+1:]
    p1 = Parser(left_s)
    p2 = Parser(right_s)
    left_expr = p1.parse_formula()
    right_expr = p2.parse_formula()
    vars_set = vars_in_expr(left_expr).union(vars_in_expr(right_expr))
    vars_list = sorted(vars_set)
    n = len(vars_list)
    is_id = True
    for mask in range(1<<n):
        env = {}
        for i,v in enumerate(vars_list):
            env[v] = (mask>>i)&1 == 1
        if eval_expr(left_expr, env) != eval_expr(right_expr, env):
            is_id = False
            break
    print("YES" if is_id else "NO")