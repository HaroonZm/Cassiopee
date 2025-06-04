x = []
for i in range(3):
    a = []
    for j in range(8):
        s = raw_input()
        a.append(s)
    b = sorted(a, key=lambda s: s.split()[1])
    for k in range(2):
        print b[k]
    x.append(b[2])
    x.append(b[3])
for i in range(len(x)):
    print x[i]