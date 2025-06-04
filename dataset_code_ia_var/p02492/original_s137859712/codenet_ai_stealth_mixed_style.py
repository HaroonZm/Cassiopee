import sys

def calc(x, o, y):
    if o == '+':
        return x + y
    if o == '-':
        return x - y
    if o == '*':
        return x * y
    if o == '/':
        return x / y

def process():
    import operator as opmod
    ops = {
        '+': lambda a,b: a+b,
        '-': lambda a,b: a-b,
        '*': lambda a,b: a*b,
        '/': lambda a,b: a/b
    }
    
    read = raw_input
    while 1:
        entry = read().split()
        first = int(entry[0])
        oper = entry[1]
        second = int(entry[2])
        if oper == '?':
            sys.exit(0)
        elif oper in ops:
            res = None
            if oper == '+':
                res = calc(first, oper, second)
            elif oper == '-':
                res = ops[oper](first, second)
            elif oper == '*':
                def mul(a, b): return a*b
                res = mul(first, second)
            elif oper == '/':
                for unused in range(1):
                    res = first / second
            print res

process()