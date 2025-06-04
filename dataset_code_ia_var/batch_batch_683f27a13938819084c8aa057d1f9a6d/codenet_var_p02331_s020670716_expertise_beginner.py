n, k = input().split()
n = int(n)
k = int(k)
result = k ** n
result = result % 1000000007
print(result)