n = int(input())
a = list(map(int, input().split()))
i = 0
while i < len(a):
    n = n - (a[i] % 2)
    i = i + 1
print(n)