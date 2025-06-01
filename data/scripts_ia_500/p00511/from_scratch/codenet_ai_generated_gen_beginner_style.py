result = int(input())
while True:
    op = input()
    if op == "=":
        print(result)
        break
    num = int(input())
    if op == "+":
        result += num
    elif op == "-":
        result -= num
    elif op == "*":
        result *= num
    elif op == "/":
        if result < 0:
            result = -(-result // num)
        else:
            result = result // num