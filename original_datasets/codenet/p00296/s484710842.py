n = list(map(int, input().split()))[0]
s = [i for i in range(n)]
a = tuple(map(int, input().split()))
b = 0
for i in a:
    if i % 2:
        b = (b - i) % len(s)
        s.pop(b)
    else:
        b = (b + i) % len(s)
        s.pop(b)
r = tuple(map(int, input().split()))
for i in r:
    print(1 if i in s else 0)