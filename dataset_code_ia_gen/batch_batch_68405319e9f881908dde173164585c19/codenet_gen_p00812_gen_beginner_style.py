import sys

def tokenize(s):
    tokens = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == ' ':
            i += 1
            continue
        if c in '+-()^':
            tokens.append(c)
            i += 1
        elif c.isdigit():
            num = c
            i += 1
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            tokens.append(num)
        elif c.isalpha():
            tokens.append(c)
            i += 1
        else:
            # Unknown char, skip safely
            i += 1
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def get(self):
        t = self.peek()
        if t is not None:
            self.pos += 1
        return t

    def parse_expr(self):
        # expr = term { (+|-) term }*
        val = self.parse_term()
        while True:
            op = self.peek()
            if op == '+' or op == '-':
                self.get()
                right = self.parse_term()
                if op == '+':
                    val = poly_add(val, right)
                else:
                    val = poly_add(val, poly_neg(right))
            else:
                break
        return val

    def parse_term(self):
        # term = factor { factor }*
        val = self.parse_factor()
        while True:
            nextt = self.peek()
            # next factor can begin with digit, letter or '('
            if nextt is None:
                break
            if nextt.isdigit() or nextt.isalpha() or nextt == '(':
                right = self.parse_factor()
                val = poly_mul(val, right)
            else:
                break
        return val

    def parse_factor(self):
        # factor = integer | variable [^digit] | '(' expr ')'
        t = self.peek()
        if t == '(':
            self.get()
            val = self.parse_expr()
            if self.get() != ')':
                pass # assume valid input, no error handling
            return val
        elif t.isdigit():
            n = int(self.get())
            return {(): n}  # constant polynomial
        elif t.isalpha():
            var = self.get()
            power = 1
            if self.peek() == '^':
                self.get()
                p = self.get()
                power = int(p)
            return {(var, power): 1}  # monomial variable^power coeff 1
        else:
            # Not expected, return empty poly
            self.get()
            return {}

def poly_add(p1, p2):
    res = dict(p1)
    for k,v in p2.items():
        if k in res:
            res[k] += v
        else:
            res[k] = v
    # remove zeros
    res2 = {k:v for k,v in res.items() if v != 0}
    return res2

def poly_neg(p):
    return {k:-v for k,v in p.items()}

def poly_mul(p1, p2):
    res = {}
    for k1,v1 in p1.items():
        for k2,v2 in p2.items():
            k_new = merge_keys(k1,k2)
            if k_new in res:
                res[k_new] += v1*v2
            else:
                res[k_new] = v1*v2
    res2 = {k:v for k,v in res.items() if v != 0}
    return res2

def merge_keys(k1, k2):
    # k1 and k2 are tuples like (var1,pow1),(var2,pow2), etc. But here keys are tuples, we need to combine powers by variable
    # Actually, in this implementation keys are tuples like (var, pow), no because multiply of variables powers are merged?
    # Wait, our keys are just one variable and power, but what about multiple variables?
    # Actually, above I made mistake: keys must be tuple of pairs (var, pow), to represent monomials with multiple variables.

    # Fix: keys should be tuple sorted of (var,pow), pow>0
    # So change all keys to consistent format: tuple of (var,power), sorted by var

    # Let's convert k1,k2 to dict var->power
    d = {}
    for var,powr in k1:
        d[var] = d.get(var,0)+powr
    for var,powr in k2:
        d[var] = d.get(var,0)+powr
    # remove zero powers
    d = {var:powr for var,powr in d.items() if powr != 0}
    # sort keys
    lst = list(d.items())
    lst.sort()
    return tuple(lst)

def standardize_key(k):
    # from a monomial key of form (var, power), or tuple of such, make sure it is a tuple of (var,power) sorted by var
    # if key is empty tuple (), means constant
    if not isinstance(k, tuple):
        return ()
    # if key is like ('a',2)
    if len(k)>0 and isinstance(k[0], str):
        # maybe it is ('a',2)
        return tuple(sorted([k]))
    # if key is tuple of tuples
    s = []
    for item in k:
        if isinstance(item, tuple) and len(item)==2:
            s.append(item)
        else:
            # unknown format
            pass
    s = [x for x in s if x[1] !=0]
    s.sort()
    return tuple(s)

def parse_expression(s):
    # remove spaces before digits if needed (problem says spaces only occur before digits but after digits of ^)
    # sample input is handled by tokenizer: spaces are removed
    tokens = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == ' ':
            i += 1
            continue
        if c in '+-()^':
            tokens.append(c)
            i += 1
        elif c.isdigit():
            num = c
            i += 1
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            tokens.append(num)
        elif c.isalpha():
            tokens.append(c)
            i += 1
        else:
            i += 1
    p = Parser(tokens)
    val = p.parse_expr()
    # convert keys to standardized keys:
    val2 = {}
    for k,v in val.items():
        kstd = standardize_key(k)
        if kstd in val2:
            val2[kstd] += v
        else:
            val2[kstd] = v
    val3 = {k:v for k,v in val2.items() if v != 0}
    return val3

def polynomials_equal(p1,p2):
    # compare dictionary of monomials with integer coefficients
    keys = set(p1.keys()) | set(p2.keys())
    for k in keys:
        if p1.get(k,0) != p2.get(k,0):
            return False
    return True

answers = []
lines = sys.stdin.read().splitlines()
idx = 0
while True:
    if idx>=len(lines):
        break
    first = lines[idx].strip()
    idx += 1
    if first == '.':
        break
    correct = parse_expression(first)
    while True:
        if idx>=len(lines):
            break
        line = lines[idx].strip()
        idx += 1
        if line == '.':
            print('.')
            break
        stu = parse_expression(line)
        if polynomials_equal(correct,stu):
            print('yes')
        else:
            print('no')