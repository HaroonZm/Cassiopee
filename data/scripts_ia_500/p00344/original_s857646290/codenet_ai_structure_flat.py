n = int(input())
A = list(map(int, input().split()))
l = [0]*n
count = 0
for i in range(n):
    if l[i] == 0:
        s = set()
        p = i
        can = 1
        while p not in s:
            if l[p] == 1:
                can = 0
                break
            s.add(p)
            l[p] = 1
            p = (p + A[p]) % n
        if can:
            while l[p] == 1:
                l[p] = 2
                p = (p + A[p]) % n
for e in l:
    if e == 2:
        count += 1
print(count)