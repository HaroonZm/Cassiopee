import math
a = [int(input()) for i in range(5)]
b = sorted([math.ceil(a[1]/a[3]),math.ceil(a[2]/a[4])])
print(a[0]-b[-1])