x,y,a,b,c = list(map(int, input().split()))
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort()
q.sort()
p0 = p[-x:]
q0 = q[-y:]

all1 = p0 + q0 + r
all1.sort()

print(sum(all1[-(x+y):]))