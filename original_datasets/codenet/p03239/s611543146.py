n, t1 = map(int,input().split())
a = []
for _ in range(n):
    c, t2 = map(int,input().split())
    if  t2 <= t1:
        a.append(int(c))
print("TLE") if (len(a) == 0) else print(min(a))