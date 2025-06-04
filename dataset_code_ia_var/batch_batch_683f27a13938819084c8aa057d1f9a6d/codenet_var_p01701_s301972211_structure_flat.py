from fractions import Fraction
while True:
    s = input()
    if s == "#":
        break
    result = []
    for c in s:
        if c == 'n' or c == 'w':
            result.append(c)
    s = "".join(result)
    if s[-1] == 'n':
        x = 0
    else:
        x = 90
    i = 0
    length = len(s)
    while i < length - 1:
        char = s[length - 2 - i]
        if char == 'n':
            x -= Fraction(45, 1 << i)
        else:
            x += Fraction(45, 1 << i)
        i += 1
    print(x)