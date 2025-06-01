def mod_inverse(x, p):
    return pow(x, p - 2, p)

def calc_mod_expr(expr, p):
    tokens = []
    i = 0
    length = len(expr)
    while i < length:
        c = expr[i]
        if c == ' ':
            i += 1
            continue
        elif c in '+-*/()':
            tokens.append(c)
            i += 1
        elif c.isdigit():
            num = 0
            while i < length and expr[i].isdigit():
                num = num * 10 + int(expr[i])
                i += 1
            tokens.append(num)
        else:
            # unexpected char, skip
            i += 1

    # operator precedence
    precedence = {'+':1, '-':1, '*':2, '/':2}

    def to_rpn(tokens):
        output = []
        op_stack = []
        for t in tokens:
            if isinstance(t,int):
                output.append(t)
            elif t == '(':
                op_stack.append(t)
            elif t == ')':
                while op_stack and op_stack[-1] != '(':
                    output.append(op_stack.pop())
                if op_stack and op_stack[-1] == '(':
                    op_stack.pop()
                else:
                    # unbalanced parenthesis
                    return []
            else:
                while op_stack and op_stack[-1] != '(' and precedence[op_stack[-1]] >= precedence[t]:
                    output.append(op_stack.pop())
                op_stack.append(t)
        while op_stack:
            if op_stack[-1] in '()':
                return []
            output.append(op_stack.pop())
        return output

    rpn = to_rpn(tokens)
    if not rpn:
        return None, True

    stack = []
    for t in rpn:
        if isinstance(t,int):
            stack.append(t % p)
        else:
            if len(stack) < 2:
                return None, True
            b = stack.pop()
            a = stack.pop()
            if t == '+':
                stack.append((a + b) % p)
            elif t == '-':
                stack.append((a - b) % p)
            elif t == '*':
                stack.append((a * b) % p)
            elif t == '/':
                if b == 0:
                    return None, True
                inv = mod_inverse(b, p)
                stack.append((a * inv) % p)
            else:
                return None, True
    if len(stack) != 1:
        return None, True
    return stack[0], False

while True:
    line = input()
    if line == '0:':
        break
    if ':' not in line:
        continue
    p_str, expr = line.split(':', 1)
    p = int(p_str.strip())
    expr_orig = expr.strip()
    val, error = calc_mod_expr(expr_orig, p)
    out_expr = expr_orig.replace(' ','')
    if error:
        print("NG")
    else:
        print(f"{out_expr} = {val} (mod {p})")