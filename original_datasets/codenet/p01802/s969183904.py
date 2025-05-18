while 1:
    d,e = map(int,input().split())
    if d == 0: break
    a = []
    for i in range(d):
        a.append(abs((i**2+(d-i)**2)**0.5-e))
    print(min(a))