m = set()
for _ in range(int(input())):
    a, b = map(int, input().split())
    i = 0
    while True:
        if a + b + i in m:
            m.remove(a + b + i)
            i += 1
        else:
            m.add(a + b + i)
            break
m = list(m)
m.sort()
for i in m:
    print("{} 0".format(i))