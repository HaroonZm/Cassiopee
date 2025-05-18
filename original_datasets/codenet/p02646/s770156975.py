# B

A, V = list(map(int, input().split()))
B, W = list(map(int, input().split()))
T = int(input())

vel_diff = V - W
loc_diff = abs(A - B)

if loc_diff - vel_diff * T <= 0:
    print('YES')
else:
    print('NO')