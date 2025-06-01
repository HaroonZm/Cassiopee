def f(e):
    a = sorted([list(map(int, input().split())) for _ in range(int(e))])
    b = sorted([list(map(int, input().split())) for _ in range(int(input()))])
    bx, by = b[0]
    for ux, uy in a:
        x, y = bx - ux, by - uy
        if all([ux + x, uy + y] in b for ux, uy in a):
            print(x, y)
            return

for e in iter(input, '0'):
    f(e)