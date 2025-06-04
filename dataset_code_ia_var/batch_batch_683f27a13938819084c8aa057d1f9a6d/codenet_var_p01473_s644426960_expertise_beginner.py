def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

S = raw_input()
lS = len(S)
unique_letters = list(set(list(S)))
ls = len(unique_letters)
d = []
for i in unique_letters:
    d.append(S.count(i))

odd_counts = 0
for i in range(ls):
    if d[i] % 2 != 0:
        odd_counts += 1

if (lS % 2 == 0 and odd_counts != 0) or (lS % 2 == 1 and odd_counts != 1):
    print 0
else:
    denomi = 1
    for i in range(ls):
        denomi *= fact(d[i] / 2)
    print fact(lS / 2) / denomi