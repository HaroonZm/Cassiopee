a, b, c = map(int, input().split())
k = int(input())
num = max(a, b, c)
for i in range(1, k + 1):
    num = num * 2
print(num+(a+b+c)-max(a,b,c))