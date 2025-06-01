w = {}
l = {}
for _ in range(int(input())):
    u, c, d = input().split() 
    if c == "lock":
        if u not in l:l[u] = set([d])
        else:l[u].add(d)
    else:
        if d not in w:w[d] = set([u])
        else:w[d].add(u)
f = 0
for k in l:
    a = [k]
    while True:
        b = set()
        for i in a:
            if i in l:b |= l[i]
        b = list(b)
        a = set()
        for i in b:
            if i in w:a |= w[i]
        a = list(a)
        if k in a:
            print(1)
            f = 1
            break
        elif a == []:break
    if f:break
else:print(0)