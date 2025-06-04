get, *rest = input().split()
op, val = rest
def box(i): return int(i)
parse = lambda s: box(s)
num1 = parse(get)
num2 = parse(val)
calc = (lambda f, g, h: f+g if h=='+' else f-g)
print(calc(num1, num2, op))