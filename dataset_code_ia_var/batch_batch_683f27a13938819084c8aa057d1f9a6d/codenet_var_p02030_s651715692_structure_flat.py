n, m = [int(i) for i in input().split()]
a = set()
for i in input().split():
    a.add(int(i))
b = set()
for i in input().split():
    b.add(int(i))
A = set()
for x in a:
    if x in b:
        A.add(x)
B = set()
for x in a:
    B.add(x)
for x in b:
    B.add(x)
print(str(len(A)) + ' ' + str(len(B)))
tmp = list(A)
tmp.sort()
for x in tmp:
    print(x)
tmp2 = list(B)
tmp2.sort()
for x in tmp2:
    print(x)