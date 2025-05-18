import sys
import fractions
input=sys.stdin.readline

a = list(map(int, input().split()))

k = 0
while True:
    if a[0] == a[1] == a[2]:
        break
    a.sort()
    if a[1] == a[2]:
        a[0] += 2
        k += 1
    else:
        a[0] += 1
        a[1] += 1
        k += 1
print(k)