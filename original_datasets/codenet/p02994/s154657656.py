N, L = map(int, input().split())
apple = []
for i in range(N):
    apple.append(L+i)
apple.sort(key = abs)
apple = apple[1:]
ans = sum(apple)
print(ans)