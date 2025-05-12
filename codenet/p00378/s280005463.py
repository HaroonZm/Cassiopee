a, b, x = map(int, input().split())

if a // 2 < b:
    num_a = x // 1000
    if x % 1000 == 0:
        print(a * num_a)
    elif a < b:
        print(a * (num_a + 1))
    elif x % 1000 > 500:
        print(a * (num_a + 1))
    else:
        print(a * num_a + b)
else:
    num_b = x // 500
    if x % 500 == 0:
        print(b * num_b)
    else:
        print(b * (num_b + 1))