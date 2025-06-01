p = [True]*50000
p[0] = False
i = 2
while i*i <= 50000:
    if p[i-1]:
        j = i*i
        while j <= 50000:
            p[j-1] = False
            j += i
    i += 1
prime = []
for i in range(50000):
    if p[i]:
        prime.append(i+1)
while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    half = n//2
    for i in prime:
        if i > half:
            break
        if p[n - i - 1]:
            count += 1
    print(count)