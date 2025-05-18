n = list(map(int,input()))
cnt = 0
f = n[0]

for i in range(4):
    if cnt == 3:
        break
    if f == n[i]:
        cnt += 1
        f = n[i]
    else:
        cnt = 0
        f = n[i]
if f == n[i]:
    cnt += 1

if cnt >= 3:
    print("Yes")
else:
    print("No")