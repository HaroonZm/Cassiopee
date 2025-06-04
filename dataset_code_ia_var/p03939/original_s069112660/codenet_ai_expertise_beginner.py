N_d1_xx = raw_input().split()
N = int(N_d1_xx[0])
d1 = int(N_d1_xx[1])
xx = int(N_d1_xx[2])

d = float(d1)
x = float(xx)

res = 0.0

while N > 1:
    res = res + (2 * d + (2 * N - 1) * x) / 2
    d = d * (1.0 + 1.0 / N)
    d = d + x * 5.0 / (2 * N)
    x = x * (1.0 + 2.0 / N)
    N = N - 1

result = res + d + x / 2
print "%.12f" % result