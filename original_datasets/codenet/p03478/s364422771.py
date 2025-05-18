N, A, B = list(map(int, input().split()))

ans = 0
for i in range(N+1):
    if A <= sum(list(map(int, str(i)[::]))) <= B:
        ans += i

print(ans)