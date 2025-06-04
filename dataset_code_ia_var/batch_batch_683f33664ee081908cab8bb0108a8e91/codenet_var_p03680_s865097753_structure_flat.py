n = int(input())
An = [0 for i in range(n)]
for i in range(n):
    An[i] = int(input())
ret = 0
nxt = 1
found = False
while ret <= n+1:
    nxt = An[nxt-1]
    ret += 1
    if nxt == 2:
        print(ret)
        found = True
        break
if not found:
    print(-1)