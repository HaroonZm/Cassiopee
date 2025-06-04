import sys
input = sys.stdin.readline

w, h = map(int, input().split())
pq = [None] * (w + h)
for i in range(w + h):
    if i < w:
        pq[i] = (int(input()), 'x')
    else:
        pq[i] = (int(input()), 'y')

x_count = w + 1
y_count = h + 1
ans = 0
pq.sort()
for i in range(w + h):
    cost, flag = pq[i]
    if flag == 'x':
        ans += cost * y_count
        x_count -= 1
    else:
        ans += cost * x_count
        y_count -= 1
print(ans)