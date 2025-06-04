L = int(input())
N = int(input())
s = 0
for _ in range(N):
    x_w = input().split()
    x = int(x_w[0])
    w = int(x_w[1])
    s += x * w
if s == 0:
    print(0)
else:
    print(1)
    if s < 0:
        print(1, -s)
    else:
        print(-1, s)