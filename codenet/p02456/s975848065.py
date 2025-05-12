q = int(input())
se = set()
while q:
    q -= 1
    op, x = map(int, input().split())
    if op == 1:
        print(+(x in se))
    elif op == 0:
        se.add(x)
        print(len(se))
    else:
        se.discard(x)