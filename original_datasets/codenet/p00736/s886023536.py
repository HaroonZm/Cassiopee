import itertools

def parse(expr):
    if expr == "P":
        return lambda p, q, r: p
    if expr == "Q":
        return lambda p, q, r: q
    if expr == "R":
        return lambda p, q, r: r
    if expr == "0":
        return lambda p, q, r: 0
    if expr == "1":
        return lambda p, q, r: 1
    if expr == "2":
        return lambda p, q, r: 2
    if expr[0] == "-":
        t = parse(expr[1:])
        return lambda p, q, r: 2 - t(p, q, r)
    if expr[0] != "(" or expr[-1] != ")":
        raise SyntaxError("invalid syntax")
    depth = 0
    i = 1
    l = len(expr) - 1
    op_pos = -1
    while i < l:
        c = expr[i]
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
        elif depth == 0 and c in ("+", "*"):
            if op_pos != -1:
                raise SyntaxError("invalid syntax")
            op_pos = i
        i += 1
    if depth != 0 or op_pos == -1:
        raise SyntaxError("invalid syntax")
    op = {
        "+": lambda x, y: max(x, y),
        "*": lambda x, y: min(x, y)
    }[expr[op_pos]]
    lhs = parse(expr[1:op_pos])
    rhs = parse(expr[op_pos + 1:-1])
    return lambda p, q, r: op(lhs(p, q, r), rhs(p, q, r))

# first part
while True:
    line = raw_input()
    if line == ".":
        break
    ans = 0

    f = parse(line)
    for p, q, r in itertools.product((0, 1, 2), repeat=3):
        if f(p, q, r) == 2:
            ans += 1

    print ans