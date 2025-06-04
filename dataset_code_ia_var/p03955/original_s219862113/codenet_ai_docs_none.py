from sys import stdin
import sys

def bitadd(a, w, bit):
    x = a
    while x <= (len(bit)-1):
        bit[x] += w
        x += x & (-x)

def bitsum(a, bit):
    ret = 0
    x = a
    while x > 0:
        ret += bit[x]
        x -= x & (-x)
    return ret

N = int(stdin.readline())
a = []
for i in range(3):
    tmp = list(map(int, stdin.readline().split()))
    a.append(tmp)

lis = []
bi = []

for j in range(N):
    a[0][j] -= 1
    a[1][j] -= 1
    a[2][j] -= 1
    if a[0][j]//3 == a[1][j]//3 == a[2][j]//3 and a[0][j]//3 % 2 == j % 2:
        if a[0][j] > a[1][j] > a[2][j]:
            lis.append(a[0][j]//3)
            bi.append(-1)
        elif a[0][j] < a[1][j] < a[2][j]:
            lis.append(a[0][j]//3)
            bi.append(1)
        else:
            print("No")
            sys.exit()
    else:
        print("No")
        sys.exit()

evenall = 1
for i in range(0, N, 2):
    evenall *= bi[i]
oddall = 1
for i in range(1, N, 2):
    oddall *= bi[i]

a = lis

BIT = [0] * (N+2)
ans = 0
for i in range(0, N, 2):
    ans += i//2 - bitsum(a[i]+1, BIT)
    bitadd(a[i]+1, 1, BIT)

if (ans % 2 == 0 and oddall == -1) or (ans % 2 == 1 and oddall == 1):
    print("No")
    sys.exit()

BIT = [0] * (N+2)
ans = 0
for i in range(1, N, 2):
    ans += i//2 - bitsum(a[i]+1, BIT)
    bitadd(a[i]+1, 1, BIT)

if (ans % 2 == 0 and evenall == -1) or (ans % 2 == 1 and evenall == 1):
    print("No")
    sys.exit()

print("Yes")