N = int(input())
flag = 1
i = 0
while i < N:
    txy = input().split()
    t = int(txy[0])
    x = int(txy[1])
    y = int(txy[2])
    if (x + y) % 2 != t % 2 or x + y > t:
        flag = 0
    i += 1
if flag:
    print("Yes")
else:
    print("No")