N = int(input())
a = 1
b = 1
for _ in range(N):
    A,B = map(int,input().split())
    x = max(-(-a//A),-(-b//B))
    a = A*x
    b = B*x
print(a+b)