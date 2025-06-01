while True:
    p = int(input())
    if p == 0:
        break
    a = 0
    c = 1000 - p
    for i in [500, 100, 50, 10, 5, 1]:
        a += c // i
        c = c % i
    print(a)