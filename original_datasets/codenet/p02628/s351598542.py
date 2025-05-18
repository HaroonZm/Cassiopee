nk = list(map(int, input().split()))
p = list(map(int, input().split()))
p.sort()

fruit = 0
for i in range(nk[1]):
    fruit += p[i]

print(fruit)