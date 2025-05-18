n = int(input())
line = input().split()
a = int(line[0])
b = int(line[1])
line = input().split()
p = []
for i in range(n):
    p.append(int(line[i]))

c1 = 0
c2 = 0
c3 = 0

for i in p:
    if (i <= a):
        c1 += 1
    elif ((i >= a + 1) and (i <= b)):
        c2 += 1
    elif (i >= b +1):
        c3 += 1

print(min(c1,c2,c3))