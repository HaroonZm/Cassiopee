n, d = map(int, raw_input().split())
D = map(int, raw_input().split())
A = [0] * (n + 1)
P = [0] * (n + 1)
P[0] = d
pos = d
stop = False
for idx in range(n):
    if D[idx] <= 2 * pos:
        pos = abs(D[idx] - pos)
    P[idx + 1] = pos
    if pos == 0 and not stop:
        stop = True
break_idx = idx + 1 if stop else None

i = n - 1
while i >= 0:
    if D[i] <= 2 * A[i + 1] + 1:
        A[i] = A[i + 1] + D[i]
    else:
        A[i] = A[i + 1]
    i -= 1

q = input()
Q = map(int, raw_input().split())
for idx in range(q):
    i = Q[idx]
    if P[i - 1] <= A[i] and pos == 0:
        print "NO"
    else:
        print "YES"