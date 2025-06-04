N = int(input())
a = []
for _ in range(N):
    a.append(int(input()))
cnt = 0
l = 1
i = 0
while i < N:
    l = a[l-1]
    cnt += 1
    if l == 2:
        print(cnt)
        break
    i += 1
else:
    print(-1)