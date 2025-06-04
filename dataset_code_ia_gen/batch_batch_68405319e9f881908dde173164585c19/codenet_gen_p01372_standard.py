import sys
sys.setrecursionlimit(10**7)

def tokenize(s):
    tokens = []
    i = 0
    while i < len(s):
        c = s[i]
        if c.isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            tokens.append(('num', int(s[i:j])))
            i = j
        elif c in '+-*/()':
            tokens.append((c,))
            i += 1
        elif c == ' ':
            i += 1
        else:
            # invalid char, skip or error
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
    def consume(self, typ=None):
        cur = self.peek()
        if cur is None:
            return None
        if typ and cur[0] != typ:
            return None
        self.pos += 1
        return cur

def parse_expr(tokens):
    # parse full expr into tree based on grammar
    p = Parser(tokens)
    def expr():
        # parse factor, then recursively combine by operator
        # But grammar allows left recursion and multiple operators without precedence,
        # So we parse by consuming terms and ops in order: just parse until all consumed inside top level
        # Actually the grammar is ambiguous, we just parse as in grammar with parens and num leaves
        return parse_e()
    def parse_e():
        # parse a unit
        if p.peek() == ('(',):
            p.consume('(')
            node = parse_e()
            p.consume(')')
            return node
        elif p.peek() and p.peek()[0] == 'num':
            return ('num', p.consume('num')[1])
        else:
            # parse left op right, but expr can be just num or parens
            # we parse starting with num or parens, then op, then next expr
            left = None
            if p.peek() and p.peek()[0] == 'num':
                left = ('num', p.consume('num')[1])
            elif p.peek() == ('(',):
                p.consume('(')
                left = parse_e()
                p.consume(')')
            else:
                return None
            if p.peek() and p.peek()[0] in '+-*/':
                op = p.consume()[0]
                right = parse_e()
                return (op, left, right)
            else:
                return left
    # But above handles only one operator.
    # The input grammar is ambiguous and allows nested ops starting from expr.
    # We solve by hand: parse operator expressions in pairs recursively from left to right
    # or more simply, we parse fully by grammar since we only need to get tokens and then do all ways.
    # So better: parse as abstract syntax tree with full brackets
    # Here, because problem states input conforms to grammar, which is fully parenthesized or may not be?
    # The grammar is ambiguous; so just parse leftmost unit, then if operator, parse right recursively.
    # We must just parse tokens into AST properly.

    # Alternative approach:
    # Since the grammar is ambiguous and the problem is only about counting results from all *possible* parenthesizations,
    # the parser can just parse tokens into a flat list of "atomic" tokens: nums and operators, plus parens.
    # Then the dp will handle all ways of parenthesizing.

    # Therefore instead of a tree, just return token list without parens
    return tokens

def apply_op(a, b, op):
    if op == '+':
        return a + b, False
    elif op == '-':
        return a - b, False
    elif op == '*':
        return a * b, False
    elif op == '/':
        if b == 0:
            return None, True
        # Applyきたまさ君 rounding: after division, round towards the value with smaller abs, 
        # then floor fractional part, to int.
        # But since problem states: 
        # "割り算では常に絶対値の小さい方に丸め，小数部を切り捨てて整数にしてしまう．"
        # which means: 
        # For division a/b:
        # Calculate a/b (float)
        # Then we choose to round towards the operand with smaller absolute value
        # Then floor the decimal part (discard decimal part)
        # This is a bit ambiguous: but we interpret as:
        # - Rounded value is the integer nearer to the operand with smaller absolute value (among a and b)
        # - Then truncate decimal part (floor) after rounding to that value direction
        # But fractional part is discarded after rounding towards smaller abs operand.
        # Another interpretation:
        # - Compute exact a/b (float)
        # - Among operand a,b find the one with smaller abs
        # - Round a/b towards that value (so if a/b > that value, round down; else up), then floor (discard decimal)
        #
        # But that is complicated. The problem is oriented towards integer division modified.
        # Let's try simpler:
        # The problem example shows dividing int by int, rounding towards the operand with smaller abs, 
        # and then discard decimal to get int.
        # We interpret the division result d = a/b as float.
        # The "rounding towards smaller abs operand" means:
        # If d > min(abs(a), abs(b)), then round down to floor(d)
        # else round up to ceil(d)
        # Finally, discard decimal part: floor or ceil means integer value.
        #
        # But the sample outputs show the standard ambiguity too.
        #
        # Alternatively, since the problem states "割り算では常に絶対値の小さい方に丸め，小数部を切り捨てて整数にしてしまう．"
        #
        # I interpret it as:
        # 1) among a and b, find value with smaller absolute value, call it c (could be a or b)
        # 2) calculate d = a/b as real float
        # 3) round d towards c (that is, if d > c, truncate decimal part down; if d < c, truncate decimal part up)
        # "小数部を切り捨てて整数にしてしまう" means floor the decimal part (ignore), but sign depends on direction.
        #
        # So direction is towards c.
        #
        # Since "小数部を切り捨てて" means floor of decimal part
        # So this is a special rounding:
        # - If d >= c, floor(d)
        # - Else ceil(d)
        #
        # But c can be positive or negative, so exact:
        # If d >= c => round towards c means round down to floor(d)
        # else d < c => round up to ceil(d)
        #
        # Let's implement that.
        c = a if abs(a) <= abs(b) else b
        if d >= c:
            r = int(d // 1)  # floor
        else:
            r = int(-((-d) // 1))  # ceil
        return r, False
    return None, True

def calc_all_results(tokens):
    # Remove parentheses tokens because in DP we consider all parenthesizations anyway.
    filtered = [t for t in tokens if t[0] != '(' and t[0] != ')']

    n = len(filtered)
    # filtered tokens are num and operators alternatively starting and ending with num
    
    # Make list of values and ops
    values = []
    ops = []
    for i, t in enumerate(filtered):
        if i%2 == 0:
            # num
            values.append(t[1])
        else:
            ops.append(t[0])

    memo = {}

    def dfs(l, r):
        # calc all results from values[l:r+1]
        if (l, r) in memo:
            return memo[(l, r)]
        if l == r:
            memo[(l, r)] = set([values[l]])
            return memo[(l, r)]
        res = set()
        for i in range(l, r):
            lefts = dfs(l, i)
            rights = dfs(i+1, r)
            op = ops[i]
            for a in lefts:
                for b in rights:
                    val, err = apply_op(a, b, op)
                    if not err and abs(val) <= 10**9:
                        res.add(val)
        memo[(l, r)] = res
        return res

    return dfs(0, len(values)-1)

for line in sys.stdin:
    s = line.strip()
    if s == '#':
        break
    tokens = tokenize(s)
    results = calc_all_results(tokens)
    print(len(results))