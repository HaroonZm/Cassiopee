N, L = map(int, input().split())
data = []
for i in range(N):
    data.append(input())
data.sort()
result = ""
for s in data:
    result += s
print(result)