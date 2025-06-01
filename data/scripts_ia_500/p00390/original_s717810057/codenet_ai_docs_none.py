n = int(input())
alst = list(map(int, input().split()))
wlst = list(map(int, input().split()))
right = [w for a, w in zip(alst, wlst) if a == 0]
left = [w for a, w in zip(alst, wlst) if a == 1]
if right and left:
    print(min(right) + min(left))
else:
    print(0)