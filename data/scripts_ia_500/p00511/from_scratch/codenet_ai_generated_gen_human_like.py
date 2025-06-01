result = int(input())
while True:
    op = input()
    if op == '=':
        print(result)
        break
    num = int(input())
    if op == '+':
        result += num
    elif op == '-':
        result -= num
    elif op == '*':
        result *= num
    elif op == '/':
        if result * num < 0 and result % num != 0:
            result = result // num + 1
        else:
            result = result // num