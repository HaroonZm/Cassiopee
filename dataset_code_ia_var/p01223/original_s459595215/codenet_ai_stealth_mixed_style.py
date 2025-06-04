n = int(input())
for _ in range(n):
    useless = input()
    n -= 1
    a = input().split()
    b = []
    for i in range(len(a)):
        b.append(int(a[i]))
    up = 0
    down = 0
    i = 1
    while i < len(b):
        diff = b[i] - b[i-1]
        if diff > 0:
            if diff > up: up = diff
        else:
            if -diff > down: down = -diff
        i = i + 1
    print('{} {}'.format(up, down))