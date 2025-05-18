n = int(input())
a = list(map(int, input().split()))

sums = 0
for x in a:
    sums ^= x

blu = set()
remain = set(range(n))

for i in range(61)[::-1]:
    if (sums >> i) & 1 == 0:
        di = -1
        for j in remain:
            if (a[j] >> i) & 1 == 1:
                di = j
                break
        if di != -1:
            blu.add(di)
            remain.remove(di)
            for j in range(n):
                if j != di and (a[j] >> i) & 1 == 1:
                    a[j] = a[j] ^ a[di]
bsum = 0
for i in blu:
    bsum = bsum ^ a[i]
print(bsum + (sums ^ bsum))