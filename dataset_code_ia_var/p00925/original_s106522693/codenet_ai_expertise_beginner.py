def left2right(formula):
    result = int(formula[0])
    i = 1
    while i < len(formula):
        op = formula[i]
        num = int(formula[i+1])
        if op == '+':
            result = result + num
        elif op == '-':
            result = result - num
        elif op == '*':
            result = result * num
        elif op == '/':
            result = result / num
        i = i + 2
    return result

formula = input()
val = int(input())

if left2right(formula) == val:
    if eval(formula) == val:
        print('U')
    else:
        print('L')
else:
    if eval(formula) == val:
        print('M')
    else:
        print('I')