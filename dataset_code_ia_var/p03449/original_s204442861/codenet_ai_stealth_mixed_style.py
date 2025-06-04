n = int(input())
a1 = []
for x in input().split():
    a1.append(int(x))
a2 = [int(i) for i in input().split()]

S1, S2 = sum(a1), sum(a2)
m = min(sum(a1[1:]), sum(a2[:-1]))

def calc(idx):
    s = 0
    for j in range(idx, n):
        s += a1[j]
    t = 0
    k = 0
    while k < idx-1:
        t = t + a2[k]
        k += 1
    return s + t

i = 2
while i < n:
    temp = calc(i)
    if temp < m:
        m = temp
    i += 1
print((S1 + S2) - m)