n = int(input())
alst = input().split()
wlst = input().split()
right = []
left = []
for i in range(n):
    a = int(alst[i])
    w = int(wlst[i])
    if a == 0:
        right.append(w)
    elif a == 1:
        left.append(w)
if len(right) > 0 and len(left) > 0:
    print(min(right) + min(left))
else:
    print(0)