N = int(input())
a = list(int(input()) for _ in range(N))
cnt = 0
l = 1
for _ in range(N):
        l = a[l-1]
        cnt += 1
        if l == 2:
            print(cnt)
            break
else:
    print(-1)