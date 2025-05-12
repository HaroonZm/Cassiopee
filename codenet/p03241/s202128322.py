N, M = list(map(int, input().split()))
s, r = divmod(M, N)
ans = 1
for i in range(s, 0, -1):
    if M % i == 0:
        print(i)
        break