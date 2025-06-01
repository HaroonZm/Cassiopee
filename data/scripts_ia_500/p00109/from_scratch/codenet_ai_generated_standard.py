def calc(expr):
    def precedence(op):
        return 2 if op in ('*', '/') else 1

    def apply_op(a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return int(a / b)

    tokens = []
    num = 0
    num_building = False
    for c in expr:
        if c.isdigit():
            num = num * 10 + int(c)
            num_building = True
        else:
            if num_building:
                tokens.append(num)
                num = 0
                num_building = False
            if c in '+-*/()':
                tokens.append(c)
            elif c == '=':
                break

    ops = []
    values = []

    def apply_stack_op():
        op = ops.pop()
        b = values.pop()
        a = values.pop()
        values.append(apply_op(a, b, op))

    i = 0
    while i < len(tokens):
        t = tokens[i]
        if isinstance(t, int):
            values.append(t)
        elif t == '(':
            ops.append(t)
        elif t == ')':
            while ops and ops[-1] != '(':
                apply_stack_op()
            ops.pop()
        else:
            while ops and ops[-1] != '(' and precedence(ops[-1]) >= precedence(t):
                apply_stack_op()
            ops.append(t)
        i += 1

    while ops:
        apply_stack_op()

    return values[0]

n = int(input())
for _ in range(n):
    print(calc(input()))