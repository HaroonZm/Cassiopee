n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
result = 0
for i in range(n):
    score = v[i] - c[i]
    if score > 0:
        result += score
print(result)