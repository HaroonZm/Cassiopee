n = int(input())
d, x = map(int, input().split())

for i in range(n):
    a = int(input())
    k = (d - 1) // a + 1
    x = x + k

print(x)