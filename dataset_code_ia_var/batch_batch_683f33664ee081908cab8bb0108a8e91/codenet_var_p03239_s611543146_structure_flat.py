n_t1 = input().split()
n = int(n_t1[0])
t1 = int(n_t1[1])
a = []
for _ in range(n):
    c_t2 = input().split()
    c = int(c_t2[0])
    t2 = int(c_t2[1])
    if t2 <= t1:
        a.append(c)
if len(a) == 0:
    print("TLE")
else:
    print(min(a))