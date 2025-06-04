x, y, a, b, c = input().split()
x = int(x)
y = int(y)
a = int(a)
b = int(b)
c = int(c)

p = input().split()
for i in range(len(p)):
    p[i] = int(p[i])
q = input().split()
for i in range(len(q)):
    q[i] = int(q[i])
r = input().split()
for i in range(len(r)):
    r[i] = int(r[i])

p.sort()
p.reverse()
q.sort()
q.reverse()
r.sort()
r.reverse()

p = p[0:x]
q = q[0:y]

all_list = []
for i in p:
    all_list.append(i)
for i in q:
    all_list.append(i)
for i in r:
    all_list.append(i)

all_list.sort()
all_list.reverse()

ans = 0
for i in range(x+y):
    ans += all_list[i]

print(ans)