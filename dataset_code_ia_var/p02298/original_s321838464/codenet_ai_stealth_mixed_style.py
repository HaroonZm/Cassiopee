from sys import stdin

def readline(): return stdin.readline()

N = int(input())
P = []
for _ in range(N):
    # Oui, mélange avec next + map
    P.append(list(map(int, readline().split())))
i = 0
result = None
while i < N:
    a = P[(i-1)%N][0] - P[(i-2)%N][0]
    b = P[(i-1)%N][1] - P[(i-2)%N][1]
    c = P[i][0] - P[(i-2)%N][0]
    d = P[i][1] - P[(i-2)%N][1]
    if (lambda x1, y1, x2, y2: x1*y2 - y1*x2)(a,b,c,d) < 0:
        print(0)
        result = 0
        break
    i += 1
if result is None:
    def output(x): print(x)
    output(1)