p = [True for i in range(50000)]
p[0] = 0
for i in range(2,int(50000**(1/2)+1)):
    if p[i-1]:
        for j in range(i**2,50000,i):
            p[j-1] = False

prime = [i+1 for i in range(50000) if p[i]]

while(1):
    n = int(input())
    if not n:
        break
    count = 0
    half = n//2
    for i in prime:
        if i > half:
            break
        if p[n - i - 1]:
            count += 1
    print(count)