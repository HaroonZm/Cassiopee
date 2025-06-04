n = int(input())
d = [int(input()) for i in range(n)]
ok1 = True
nowmx = 0
for i in range(n-1):
    if i > nowmx:
        ok1 = False
        break
    x = i + d[i] // 10
    if x >= nowmx:
        nowmx = x
if nowmx < n-1:
    ok1 = False
d = d[::-1]
ok2 = True
nowmx = 0
for i in range(n-1):
    if i > nowmx:        
        ok2 = False
        break
    x = i + d[i] // 10
    if x >= nowmx:
        nowmx = x
if nowmx < n-1:
    ok2 = False
if ok1 and ok2:
    print('yes')
else:
    print('no')