while True:
    n = input()
    if n[0] == '0':
        break
    total = 0
    for digit in n:
        total = total + int(digit)
    print(total)