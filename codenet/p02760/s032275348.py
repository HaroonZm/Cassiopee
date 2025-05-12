import sys
import math
import collections
#n = int(input())
a1, a2, a3 = map(int, input().split())
a4, a5, a6 = map(int, input().split())
a7, a8, a9 = map(int, input().split())
#s = input()
#x = list(map(int, input().split()))
a = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
c = [0 for k in range(9)]
n = int(input())
for i in range(n):
    b = int(input())
    for j in range(9):
        if a[j] == b:
            c[j] = 1

if c[0] + c[1] + c[2] == 3:
    print("Yes")
    sys.exit()
if c[4] + c[5] + c[3] == 3:
    print("Yes")
    sys.exit()
if c[7] + c[8] + c[6] == 3:
    print("Yes")
    sys.exit()
if c[0] + c[3] + c[6] == 3:
    print("Yes")
    sys.exit()
if c[1] + c[4] + c[7] == 3:
    print("Yes")
    sys.exit()
if c[2] + c[5] + c[8] == 3:
    print("Yes")
    sys.exit()
if c[0] + c[4] + c[8] == 3:
    print("Yes")
    sys.exit()
if c[2] + c[4] + c[6] == 3:
    print("Yes")
    sys.exit()

print("No")