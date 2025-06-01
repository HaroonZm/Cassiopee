while True:
    try:
        line = input()
        if not line:
            break
        a, b, n = map(int, line.split())
        remainder = a % b
        total = 0
        for i in range(n):
            remainder *= 10
            digit = remainder // b
            total += digit
            remainder = remainder % b
        print(total)
    except EOFError:
        break