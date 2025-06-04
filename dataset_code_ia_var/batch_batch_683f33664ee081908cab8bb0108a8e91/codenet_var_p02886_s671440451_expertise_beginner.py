N = int(input())
d = input().split()
for i in range(len(d)):
    d[i] = int(d[i])
ans = 0
total = 0
for num in d:
    total = total + num
for i in range(len(d)):
    ans = ans + d[i] * (total - d[i])
print(ans // 2)