N = int(input())

flag = 1

for i in range(N):
    t, x, y = map(int, input().split())
    if (x+y)%2!=t%2 or x+y>t:
        flag = 0

if flag:
    print("Yes")
else:
    print("No")