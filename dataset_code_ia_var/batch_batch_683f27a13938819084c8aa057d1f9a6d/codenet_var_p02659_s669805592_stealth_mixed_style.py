from functools import reduce

def calc():
    a_b = input().split()
    a = int(a_b[0])
    c, d = a_b[1].split('.')
    d = reduce(lambda acc, x: acc*10 + int(x), d, 0)
    if c.isdigit():
        mul = a * int(c)
    else:
        mul = 0
    result = mul + (a * d // 100)
    print(result)

calc()