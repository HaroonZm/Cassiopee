n = int(input())
a = list(map(int, input().split()))
color = [0] * 8
cnt = 0
for val in a:
    for i in range(8):
        if 400 * i <= val < 400 * (i + 1):
            color[i] = 1
    if val >= 3200:
        cnt += 1
all_c_zero = True
for c in color:
    if c != 0:
        all_c_zero = False
        break
if all_c_zero:
    s = 1
else:
    s = 0
    for v in color:
        s += v
l = 0
for v in color:
    l += v
l += cnt
print(s, l)