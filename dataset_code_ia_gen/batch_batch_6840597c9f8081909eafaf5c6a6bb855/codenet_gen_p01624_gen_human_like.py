import sys
sys.setrecursionlimit(10**7)

ops = ['*', '+', '-', '&', '^', '|']
precedence = {'*':0, '+':1, '-':1, '&':2, '^':3, '|':4}

def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c in '()*+ -&^|':
            # remove spaces if any
            if c == ' ':
                i += 1
                continue
            tokens.append(c)
            i += 1
        elif c.isdigit():
            j = i
            while j < len(expr) and expr[j].isdigit():
                j += 1
            tokens.append(expr[i:j])
            i = j
        else:
            # Should not happen due to constraints
            i += 1
    return tokens

def parse_expr(expr):
    # Parse expression into a syntax tree
    # Use shunting yard algorithm to parse into RPN, then build tree
    tokens = tokenize(expr)
    output = []
    stack = []
    for t in tokens:
        if t.isdigit():
            output.append(('num', int(t)))
        elif t == '(':
            stack.append(t)
        elif t == ')':
            while stack and stack[-1] != '(':
                op = stack.pop()
                output.append(('op', op))
            stack.pop()
        elif t in ops:
            while stack and stack[-1] in ops and \
                (precedence[stack[-1]] < precedence[t] or (precedence[stack[-1]] == precedence[t])):
                # left associative and equal precedence pop
                output.append(('op', stack.pop()))
            stack.append(t)
    while stack:
        output.append(('op', stack.pop()))
    # Build tree from RPN
    st = []
    for t in output:
        if t[0] == 'num':
            st.append(('num', t[1]))
        else:
            r = st.pop()
            l = st.pop()
            st.append(('op', t[1], l, r))
    return st[0]

def eval_tree(t):
    if t[0] == 'num':
        return t[1]
    op = t[1]
    a = eval_tree(t[2])
    b = eval_tree(t[3])
    if op == '*':
        return a*b
    elif op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '&':
        return a&b
    elif op == '^':
        return a^b
    elif op == '|':
        return a|b
    else:
        raise ValueError('Invalid operator')

def serialize(t):
    if t[0] == 'num':
        return str(t[1])
    op = t[1]
    left = serialize(t[2])
    right = serialize(t[3])
    # add parentheses for non-nums
    # but for simplicity just always put parentheses around op
    return '(' + left + op + right + ')'

def all_edits(expr):
    # generate all expressions by adding or removing one char
    # only produce valid expressions (according to problem)
    # chars allowed:
    ALPHABET = ['(', ')', '*', '+', '-', '&', '^', '|'] + [str(i) for i in range(10)]
    result = []
    n = len(expr)
    # deletion
    for i in range(n):
        newe = expr[:i] + expr[i+1:]
        if is_valid_expression(newe):
            result.append(newe)
    # insertion
    for i in range(n+1):
        for c in ALPHABET:
            newe = expr[:i] + c + expr[i:]
            if len(newe) <= 7 and is_valid_expression(newe):
                result.append(newe)
    return result

cache_valid = {}
def is_valid_expression(expr):
    # Given constraints, the expression was always valid input and we must check validity for the edits
    # So implement validator according to rules.
    if expr in cache_valid:
        return cache_valid[expr]
    # empty or too long
    if len(expr) == 0 or len(expr) > 7:
        cache_valid[expr] = False
        return False
    # check chars
    for c in expr:
        if c not in '()*+ -&^|0123456789':
            cache_valid[expr] = False
            return False
    # check grammar:
    # parse expression by same parser above, if parse fail return False
    try:
        # Also check leading zeros for numbers and parentheses balanced
        # Use a custom parser that validates according to the problem

        def parse_expr_valid(s):
            # We'll do a recursive descent parser according to grammar
            # to distinguish terms and operators.
            pos = 0
            length = len(s)
            def skip_ws():
                nonlocal pos
                while pos < length and s[pos] == ' ':
                    pos += 1
            def parse_factor():
                nonlocal pos
                skip_ws()
                # factor can be:
                # (expr) or positive integer no leading zero
                if pos >= length:
                    return None
                if s[pos] == '(':
                    pos += 1
                    node = parse_expr_inner()
                    if node is None:
                        return None
                    skip_ws()
                    if pos >= length or s[pos] != ')':
                        return None
                    pos += 1
                    return node
                else:
                    # number
                    start = pos
                    if pos < length and s[pos].isdigit():
                        # Check no leading zero unless single zero is invalid because 0 is invalid positive integer
                        if s[pos] == '0':
                            # 0 is not valid positive integer per problem; must be >0 and no leading zero
                            # so '0' or '01' invalid
                            # So returning failure
                            # 0 invalid, so reject 0 as positive integer
                            return None
                        while pos < length and s[pos].isdigit():
                            pos += 1
                        num_str = s[start:pos]
                        if len(num_str) == 0:
                            return None
                        # leading zero?
                        if num_str[0] == '0':
                            return None
                        return ('num', num_str)
                    return None

            def parse_term_level(level):
                nonlocal pos
                # If level == 5 (lowest precedence), parse factor
                # Level: 0:*, 1:+,-, 2:&, 3:^, 4:|
                if level == 5:
                    return parse_factor()
                node = parse_term_level(level+1)
                if node is None:
                    return None
                while True:
                    skip_ws()
                    if pos >= length:
                        break
                    c = s[pos]
                    # Check if operator at this level
                    target_ops = []
                    if level == 0: target_ops = ['*']
                    elif level == 1: target_ops = ['+', '-']
                    elif level == 2: target_ops = ['&']
                    elif level == 3: target_ops = ['^']
                    elif level == 4: target_ops = ['|']
                    if c in target_ops:
                        pos += 1
                        right = parse_term_level(level+1)
                        if right is None:
                            return None
                        node = ('op', c, node, right)
                    else:
                        break
                return node

            def parse_expr_inner():
                return parse_term_level(0)

            node = parse_expr_inner()
            skip_ws()
            if node is None or pos != length:
                return None
            return node

        tree = parse_expr_valid(expr)
        if tree is None:
            cache_valid[expr] = False
            return False
        # check leading zeros (already done)
        cache_valid[expr] = True
        return True
    except:
        cache_valid[expr] = False
        return False

from functools import lru_cache

@lru_cache(None)
def game(expr, edits_left, is_takumi_turn):
    # return optimal result of expr after edits_left left
    # is_takumi_turn: True if Takumi (maximize), False if Komachi (minimize)
    if edits_left == 0:
        tree = parse_expr(expr)
        val = eval_tree(tree)
        return val
    candidates = [expr]
    n = len(expr)
    ALPHABET = ['(', ')', '*', '+', '-', '&', '^', '|'] + [str(i) for i in range(10)]
    # all deletion
    for i in range(n):
        newe = expr[:i] + expr[i+1:]
        if len(newe) > 0 and len(newe) <= 7 and is_valid_expression(newe):
            candidates.append(newe)
    # all insertion
    for i in range(n+1):
        for c in ALPHABET:
            newe = expr[:i] + c + expr[i:]
            if len(newe) <= 7 and is_valid_expression(newe):
                candidates.append(newe)
    if is_takumi_turn:
        res = -1 << 60
        for c in candidates:
            val = game(c, edits_left-1, False)
            if val > res:
                res = val
        return res
    else:
        res = 1 << 60
        for c in candidates:
            val = game(c, edits_left-1, True)
            if val < res:
                res = val
        return res

def main():
    for line in sys.stdin:
        line=line.strip()
        if line == '0 #':
            break
        parts = line.split()
        if len(parts) >= 2:
            N = int(parts[0])
            expr = parts[1]
        else:
            N = int(line)
            expr = sys.stdin.readline().strip()
        ans = game(expr, N, True)
        print(ans)

if __name__=='__main__':
    main()