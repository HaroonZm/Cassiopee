n = int(input())
for _ in range(n):
    numbers = input().split()
    x = int(numbers[0])
    y = int(numbers[1])
    b = int(numbers[2])
    p = int(numbers[3])
    s = x * b + y * p
    t = int((x * 5 + y * 2) * 0.8)
    u = s
    if s <= t:
        print(s)
    else:
        if 5 - b > 0:
            u = u + (5 - b) * x
        if 2 - p > 0:
            u = u + (2 - p) * y
        val = int(u * 0.8)
        if s < val:
            print(s)
        else:
            print(val)