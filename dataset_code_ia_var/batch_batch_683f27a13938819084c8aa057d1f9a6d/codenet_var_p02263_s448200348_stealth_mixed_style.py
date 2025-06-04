vals = []
for t in __import__('sys').stdin.read().split():
    if t == '*':
        def mul():
            return vals.pop() * vals.pop()
        vals.append(mul())
    elif t == '+':
        a = vals.pop()
        vals.append(a + vals.pop())
    elif t == '-':
        b, a = vals.pop(), vals.pop()
        vals += [a - b]
    else:
        def add_val(x): vals.append(int(x))
        add_val(t)
print(vals[-1])