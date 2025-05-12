n = int(input())
k = int(input())
x = int(input())
y = int(input())

a = min(n,k)
b = max(n-k,0)
print(a*x+b*y)