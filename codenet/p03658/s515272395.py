N, K = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort(reverse=True)
sum = 0
for i in range(0, K):
    sum += l[i]
print(sum)