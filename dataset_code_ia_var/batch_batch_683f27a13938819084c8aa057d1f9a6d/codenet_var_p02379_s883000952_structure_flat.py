import math
a_b_c_d = input().split()
a = float(a_b_c_d[0])
b = float(a_b_c_d[1])
c = float(a_b_c_d[2])
d = float(a_b_c_d[3])
l = math.sqrt((a - c) * (a - c) + (b - d) * (b - d))
print('{:.08f}'.format(l))