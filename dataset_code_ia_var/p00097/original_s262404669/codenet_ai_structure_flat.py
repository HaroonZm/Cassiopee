l = []
for i in range(10):
    l.append([0]*1001)
l[0][0] = 1
i = 0
while i < 101:
    j = 9
    while j > 0:
        k = i
        while k < 1000:
            l[j][k] += l[j-1][k-i]
            k += 1
        j -= 1
    i += 1
while True:
    try:
        n, k = map(int, raw_input().split())
    except EOFError:
        break
    if n == 0 and k == 0:
        break
    print l[n][k]