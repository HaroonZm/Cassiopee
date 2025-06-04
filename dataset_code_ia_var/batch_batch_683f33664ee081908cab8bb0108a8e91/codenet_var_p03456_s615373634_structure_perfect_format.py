from math import sqrt

a, b = input().split()
x = sqrt(int(a + b))

if x == int(x):
    print('Yes')
else:
    print('No')