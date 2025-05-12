n = int(input())
k = int(input())
x = list(map(int, input().split()))
result = 0
for i in range(n):
    result += 2 * min(abs(0-x[i]), abs(k-x[i]))

print(result)