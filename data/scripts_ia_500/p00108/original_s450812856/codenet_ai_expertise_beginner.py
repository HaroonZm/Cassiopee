def f(x):
    a = x
    c = 0
    while True:
        b = []
        for e in a:
            b.append(a.count(e))
        if a == b:
            return c, " ".join(str(num) for num in a)
        else:
            a = b
            c = c + 1

while True:
    val = input()
    if val == '0':
        break
    line = input()
    numbers = list(map(int, line.split()))
    c, s = f(numbers)
    print(c)
    print(s)