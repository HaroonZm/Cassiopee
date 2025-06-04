def calc(o): return int(o[0]), o[1], int(o[2])

keep_going = 1

while keep_going:
    entry = input() if hasattr(__builtins__, "input") else raw_input()
    stuff = entry.split()
    a, op, c = calc(stuff)
    if op in ['+', '-', '*', '/']:
        if op == '+':
            res = a + c
            print(res)
        elif op == '-':
            print(a - c)
        else:
            match op:
                case '*':
                    print(a * c)
                case '/':
                    print(a / c)
    else:
        keep_going = False