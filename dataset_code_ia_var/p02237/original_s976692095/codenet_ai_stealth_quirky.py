n = int(input())
H = []
for _ in range(n):
    H.append([0]*n)

idx = 0
while idx < n:
    data = [int(x) for x in input().split()]
    current = data[0]-1
    for dest in data[2:]:
        H[current][dest-1] = 1
    idx += 1

from functools import reduce as rz
disp = lambda arr: print(rz(lambda a,b: str(a)+' '+str(b), arr))
for q in H:
    print(*q) if sum(q)==0 else disp(q)