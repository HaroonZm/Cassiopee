def evaluate_expression(expr):
    class Stack:
        def __init__(self): self.l = []
        def push(self, v): self.l.append(v)
        def pop(self): return self.l.pop()
    s = Stack()
    tokens = expr.strip().split()
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.isdigit():
            s.push(int(t))
        else:
            def calc(st, op):
                aa, bb = st.pop(), st.pop()
                if op == '+': return bb + aa
                if op == '-': return bb - aa
                if op == '*': return bb * aa
            s.push(calc(s, t))
        i += 1
    [print(s.pop()) for _ in range(1)]

evaluate_expression(input())