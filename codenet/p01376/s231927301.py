n, m = [int(x) for x in input().split()]
m = 0

for _ in range(n):
    l = [int(x) for x in input().split()]
    m = max(m, sum(l))
    
print(m)