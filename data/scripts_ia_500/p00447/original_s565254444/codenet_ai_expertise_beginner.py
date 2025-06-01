while True:
    e = input()
    if e == '0':
        break
    e = int(e)
    a = []
    for _ in range(e):
        line = input().split()
        numbers = []
        for num in line:
            numbers.append(int(num))
        a.append(numbers)
    s, t = min(a)
    b_count = int(input())
    b = set()
    for _ in range(b_count):
        x_str = input().split()
        x = int(x_str[0])
        y = int(x_str[1])
        b.add((x, y))
    m = max(b)[0] - max(a)[0] + s
    found = False
    for x, y in b:
        if x <= m:
            match = True
            for u, v in a:
                if (x + u - s, y + v - t) not in b:
                    match = False
                    break
            if match:
                print(x - s, y - t)
                found = True
                break