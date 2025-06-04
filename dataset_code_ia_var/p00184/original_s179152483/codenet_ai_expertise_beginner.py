while True:
    n = int(input())
    if n == 0:
        break
    h = [0, 0, 0, 0, 0, 0, 0]
    for i in range(n):
        a = int(input())
        a = a // 10
        if a > 6:
            a = 6
        h[a] = h[a] + 1
    for i in range(7):
        print(h[i])