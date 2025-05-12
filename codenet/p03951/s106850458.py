N = int(input())
s = input()
t = input()

ans = 2 * N
for i in range(N):
    if s[-1 - i : ] == t[0 : i + 1]:
        ans = 2 * N - i - 1
print(ans)