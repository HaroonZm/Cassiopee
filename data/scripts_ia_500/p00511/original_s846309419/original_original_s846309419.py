ans = int(input())
while True:
    op = input()
    if op == '+':
        m = int(input())
        ans += m
    elif op == '-':
        m = int(input())
        ans -= m
    elif op == '*':
        m = int(input())
        ans *= m
    elif op == '/':
        m = int(input())
        ans //= m
    elif op == '=':
        print(ans)
        exit()