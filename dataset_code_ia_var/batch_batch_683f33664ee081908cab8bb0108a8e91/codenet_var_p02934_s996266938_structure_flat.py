n = int(input())
a = list(map(int, input().split()))
sum = 0
i = 0
while i < n:
    sum += 1 / a[i]
    i += 1
print(1 / sum)