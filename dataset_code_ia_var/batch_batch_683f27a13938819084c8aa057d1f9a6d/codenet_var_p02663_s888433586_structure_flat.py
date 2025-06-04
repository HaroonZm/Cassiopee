h1, m1, h2, m2, k = map(int, input().split())
if k >= 60:
    tmp1 = k // 60
    tmp2 = k % 60
else:
    tmp1 = 0
    tmp2 = k
h3 = h2 - tmp1
m3 = m2 - tmp2
if m3 < 0:
    h3 -= 1
    m3 += 60
a = 60 * h1 + m1
b = 60 * h3 + m3
print(b - a)