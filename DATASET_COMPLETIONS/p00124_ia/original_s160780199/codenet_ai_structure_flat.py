n = int(input())
while True:
    lines = []
    for _ in range(n):
        s, a, b, c = input().split()
        lines.append((s, int(a)*3 + int(c)))
    lines.sort(key=lambda x: -x[1])
    for s, p in lines:
        print('{},{}'.format(s, p))
    n = int(input())
    if n == 0:
        break
    print()