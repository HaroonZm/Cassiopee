N = int(input())
D = []
i = 0
while i < N:
    D.append(int(input()))
    i += 1
A = []
if len(D) > 0:
    A.append(D[0])
for d in D:
    found = False
    for a in A:
        if d == a:
            found = True
            break
    if not found:
        A.append(d)
print(len(A))