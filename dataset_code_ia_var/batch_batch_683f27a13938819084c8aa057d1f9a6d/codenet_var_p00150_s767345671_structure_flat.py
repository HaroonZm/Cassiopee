P = []
n = 0
while n < 10000:
    p = 3
    c = 0
    if n % 2 == 0:
        c += 1
    else:
        root = int(n ** 0.5) + 1
        while p < root:
            if n % p != 0:
                p += 2
            else:
                c += 1
                break
    if c == 0:
        P.append(n)
    n += 1

i = 0
j = len(P) - 1
while i < j:
    P[i], P[j] = P[j], P[i]
    i += 1
    j -= 1

while 1:
    j = 0
    n = int(input())
    if n == 0:
        break
    k = 0
    while k < len(P):
        if n >= P[k]:
            j = k
            break
        k += 1
    while 1:
        if P[j] - 2 == P[j+1]:
            print(P[j+1], P[j])
            break
        else:
            j += 1