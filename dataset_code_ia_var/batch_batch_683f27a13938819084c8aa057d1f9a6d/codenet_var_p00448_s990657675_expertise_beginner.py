e = input()
while e != '0 0':
    r = int(e.split()[0])
    lignes = []
    for i in range(r):
        ligne = input().split()
        lignes.append(ligne)
    d = []
    for col in zip(*lignes):
        bits = ''.join(col)
        d.append(int(bits, 2))
    a = 0
    b = 1 << r
    f = [1] * b
    for m in range(b):
        if f[m]:
            f[~m] = 0
            t = 0
            for s in d:
                c = bin(m ^ s).count('1')
                if c > r // 2:
                    t += c
                else:
                    t += r - c
            if t > a:
                a = t
    print(a)
    e = input()