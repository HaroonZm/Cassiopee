n, m = map(int, input().split())
c = []
for i in range(m):#h:高さ
    c.append([int(m) for m in input().split()])
c.sort(key=lambda x:(x[0], x[1]))
p = []
q = []
for i in range(n):
    p.append(0)
    q.append(0)
j = 0
count = 0
for i in range(m):
    if i == 0:
        p[j] = c[i][0]
        q[j] = c[i][1] - 1
    elif i != 0:
        if c[i][0] != c[i - 1][0]:
            j += 1
            p[j] = c[i][0]
            q[j] = c[i][1] - 1
            if q[j - 1] < p[j]:
                count += 1
            else:
                if p[j] < p[j - 1]:
                    p[j] = p[j - 1]
                if q[j] > q[j - 1]:
                    q[j] = q[j - 1]
count += 1
print(count)