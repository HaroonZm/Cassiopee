n,m = [int(s) for s in input().split(" ")]
bibs = []
for i in range(n):
    bibs.append(int(input()))
k = 1
while k <= m:
    i = 0
    while i < n - 1:
        if bibs[i] % k > bibs[i + 1] % k:
            temp = bibs[i]
            bibs[i] = bibs[i + 1]
            bibs[i + 1] = temp
        i += 1
    k += 1
i = 0
while i < n:
    print(bibs[i])
    i += 1