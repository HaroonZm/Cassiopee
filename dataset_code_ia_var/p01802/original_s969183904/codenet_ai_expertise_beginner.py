while True:
    d, e = input().split()
    d = int(d)
    e = int(e)
    if d == 0:
        break
    a = []
    for i in range(d):
        value = (i ** 2 + (d - i) ** 2) ** 0.5
        diff = abs(value - e)
        a.append(diff)
    print(min(a))