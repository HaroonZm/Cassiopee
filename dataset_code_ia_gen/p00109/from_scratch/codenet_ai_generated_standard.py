def calc(expr):
    def precedence(op):
        if op in ('+', '-'): return 1
        if op in ('*', '/'): return 2
        return 0

    def apply_op(a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return int(a / b)  # truncate toward zero

    values, ops = [], []
    i, n = 0, len(expr)
    while i < n:
        c = expr[i]
        if c.isdigit():
            val = 0
            while i < n and expr[i].isdigit():
                val = val * 10 + int(expr[i])
                i += 1
            values.append(val)
            continue
        elif c == '(':
            ops.append(c)
        elif c == ')':
            while ops and ops[-1] != '(':
                b, a = values.pop(), values.pop()
                values.append(apply_op(a, b, ops.pop()))
            ops.pop()
        elif c in "+-*/":
            while ops and precedence(ops[-1]) >= precedence(c):
                b, a = values.pop(), values.pop()
                values.append(apply_op(a, b, ops.pop()))
            ops.append(c)
        elif c == '=':
            while ops:
                b, a = values.pop(), values.pop()
                values.append(apply_op(a, b, ops.pop()))
            return values[0]
        i += 1

n = int(input())
for _ in range(n):
    print(calc(input()))