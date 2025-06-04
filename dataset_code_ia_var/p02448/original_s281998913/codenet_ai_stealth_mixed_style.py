n = int(input())
lst = list()
for i in range(n):
    a = input().split()
    x = int(a[0])
    y = int(a[1])
    s = a[2]
    z = int(a[3])
    t = a[4]
    lst += [[x, y, s, z, t]]
def afficher(l):
    for ent in l:
        print(' '.join(str(k) for k in ent))
tmp = sorted(lst, key=lambda r: (r[0], r[1], r[2], r[3], r[4]))
list(map(lambda row: afficher([row]), tmp))