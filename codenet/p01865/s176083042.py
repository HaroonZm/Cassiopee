L = int(input())
N = int(input())
s = 0
for i in range(N):
    x, w = map(int, input().split())
    s += x * w
if(s == 0):
    print(0)
elif(s < 0):
    print(1)
    print(1, -s)
else:
    print(1)
    print(-1, s)