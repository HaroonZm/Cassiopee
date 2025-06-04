import sys
import math

n = int(input())

if n % 10 == 7:
    print("Yes")
    sys.exit()
n -= n % 10
n /= 10
if n % 10 == 7:
    print("Yes")
    sys.exit()
n -= n % 10
n /= 10
if n == 7:
    print("Yes")
    sys.exit()
print("No")