def partitions(n, max_part):
    if n == 0:
        yield []
        return
    for i in range(min(n, max_part), 0, -1):
        for tail in partitions(n - i, i):
            yield [i] + tail

while True:
    n = int(input())
    if n == 0:
        break
    for p in partitions(n, n):
        print(*p)