q = int(input())
se = set()
while q:
    q -= 1
    op, x = map(int, input().split())
    if op:
        print(+(x in se))
    else:
        se.add(x)
        print(len(se))