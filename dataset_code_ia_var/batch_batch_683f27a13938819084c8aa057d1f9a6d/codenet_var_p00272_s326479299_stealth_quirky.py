V = dict(enumerate((0, 6000, 4000, 3000, 2000)))
i = 1
while i <= 4:
    s = input()
    l = s.split()
    t = int(l[0])
    n = int(l[1])
    res = V.get(t, 0)*n
    print('%d' % res)
    i += 1