import sys,math
range = xrange
input = raw_input

inp = [int(x) for x in sys.stdin.read().split()]; ii = 0

n = inp[ii]; ii += 1
k = inp[ii]; ii += 1

X = inp[ii + 0: ii + 3 * n: 3]
Y = inp[ii + 1: ii + 3 * n: 3]
C = inp[ii + 2: ii + 3 * n: 3]
ii += 3 * n

def dist(i,j):
    return math.sqrt((X[i] - X[j])**2 + (Y[i] - Y[j])**2)

l = 0.0
r = 100.0 * 1e18
while r - l >= 1e-9:
    t = (l + r) / 2

    R = [t/C[i] for i in range(n)]

    cand = [(X[i], Y[i]) for i in range(n)]

    for i in range(n):
        r0 = R[i]
        x0 = X[i]
        y0 = Y[i]
        for j in range(i):
            r1 = R[j]
            x1 = X[j]
            y1 = Y[j]

            d = dist(i,j)
            if d == 0.0:
                continue
            a = (r0**2 - r1**2 + d**2)/(2*d)
            if 0.0 < d <= r0 + r1 and r0**2 - a**2 >= 0.0:
                h = math.sqrt(r0**2 - a**2)

                x2 = x0 + a * (x1 - x0)/d
                y2 = y0 + a * (y1 - y0)/d
                #cand.append((x2,y2))

                x3 = x2 + h * (y1 - y0)/d
                y3 = y2 - h * (x1 - x0)/d
                cand.append((x3,y3))
                
                x3 = x2 + h * (y1 - y0)/d
                y3 = y2 - h * (x1 - x0)/d
                cand.append((x3,y3))

    for x,y in cand:
        count = 0
        for i in range(n):
            if math.sqrt((X[i] - x)**2 + (Y[i] - y)**2) <= R[i] + 1e-9:
                count += 1

        if count >= k:
            r = t
            break
    else:
        l = t
print (l + r)/2