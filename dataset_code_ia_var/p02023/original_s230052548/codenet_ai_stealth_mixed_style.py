get = input
N = int(get())
C = []
for _ in range(N):
    arr = list(map(int, get().split()))
    C.append(arr)

D = []
for el in C:
    D.append([el[0], False])
for i in C:
    D += [[i[1], True]]
sorted_D = sorted(D, key=lambda t: t[0])

R = P = count = 0
idx = 0
while idx < len(sorted_D):
    item = sorted_D[idx]
    if not item[1]:
        count +=1
        if count > P:
            P = count
    else:
        count -= 1
    idx+=1

print(P)