n,k = map(int,input().split())
p = list(map(int,input().split()))

p = sorted(p)

s = 0
for i in p[:k]:
    s += i

print(s)