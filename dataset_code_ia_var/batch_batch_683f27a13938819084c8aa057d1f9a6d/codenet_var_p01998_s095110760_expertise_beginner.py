N = int(input())
P = []
for x in range(N + 3):
    P.append(True)

P[0] = False
P[1] = False

i = 2
while i * i <= N + 2:
    if P[i]:
        j = i * 2
        while j < N + 3:
            P[j] = False
            j += i
    i += 1

count = 0
q = 3
while q <= N:
    if P[q] and P[q + 2]:
        count = count + 2
    q = q + 1

print(count)