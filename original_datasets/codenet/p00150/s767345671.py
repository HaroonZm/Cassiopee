P = []
for n in range(10000):
    p = 3
    c = 0
    if n % 2 == 0:
        c += 1
    else:
        while p < int(n**0.5) + 1:
            if n % p != 0:
                p += 2
            else:
                c += 1
                break
    if c == 0:
        P.append(n)

P.reverse()

while 1:
        j = 0
        n = int(input())
        if n == 0:
            break
        else:
            for i in range(len(P)):
                if n >= P[i]:
                    j = i
                    break
            while 1:
                if P[j]-2 == P[j+1]:
                    print(P[j+1],P[j])
                    break
                else:
                    j += 1