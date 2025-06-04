def partitions(n, max_part, prefix):
    if n == 0:
        print(' '.join(map(str, prefix)))
        return
    for i in range(min(max_part, n), 0, -1):
        partitions(n - i, i, prefix + [i])

while True:
    n = int(input())
    if n == 0:
        break
    partitions(n, n, [])