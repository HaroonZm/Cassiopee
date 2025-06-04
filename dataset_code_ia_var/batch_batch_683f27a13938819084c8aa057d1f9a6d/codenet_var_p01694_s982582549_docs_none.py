while True:
    N = int(input())
    if N == 0:
        break
    b = input().split()
    x = 0
    for i in range(N // 2):
        if (b[2 * i], b[2 * i + 1]) in [('lu', 'ru'), ('ru', 'lu'), ('ld', 'rd'), ('rd', 'ld')]:
            x += 1
    print(x)