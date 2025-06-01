def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

try:
    while True:
        line = input()
        if line == '':
            break
        parts = line.split()
        if len(parts) != 2:
            continue
        x = int(parts[0])
        y = int(parts[1])
        print(gcd(x, y))
except EOFError:
    pass