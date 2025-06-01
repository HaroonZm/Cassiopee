def f(e):
    n = int(e)
    a = []
    for i in range(n):
        line = input().split()
        a.append([int(line[0]), int(line[1])])
    a.sort(key=lambda x: x[0])
    
    m = int(input())
    b = []
    for i in range(m):
        line = input().split()
        b.append([int(line[0]), int(line[1])])
    b.sort(key=lambda x: x[0])
    
    for s, t in b:
        u, v = a[0]
        x = s - u
        y = t - v
        
        match = True
        for u2, v2 in a:
            if [u2 + x, v2 + y] not in b:
                match = False
                break
        if match:
            print(x, y)
            return

while True:
    e = input()
    if e == '0':
        break
    f(e)