c = []
for i in range(6):
    line = input()
    parts = line.split()
    a = int(parts[0])
    b = int(parts[1])
    if a > b:
        a, b = b, a
    c.append([a, b])

c.sort()

i = 0
ok = True
while i < 6:
    if c[i] != c[i+1]:
        print('no')
        ok = False
        break
    i += 2

if ok:
    if c[0][0] == c[2][0] and c[0][1] == c[4][0] and c[2][1] == c[4][1]:
        print('yes')
    else:
        print('no')