import math
A_B_H_M = input().split()
A = int(A_B_H_M[0])
B = int(A_B_H_M[1])
H = int(A_B_H_M[2])
M = int(A_B_H_M[3])
s = 0.5 * (H * 60 + M)
l = 6 * M
if s > l:
    c = s - l
else:
    c = l - s
radians_c = math.radians(c)
cos_c = math.cos(radians_c)
ans = math.sqrt(A * A + B * B - 2 * A * B * cos_c)
print(ans)