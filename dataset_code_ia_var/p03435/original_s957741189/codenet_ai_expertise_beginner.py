c1 = input().split()
c1 = [int(x) for x in c1]
c2 = input().split()
c2 = [int(x) for x in c2]
c3 = input().split()
c3 = [int(x) for x in c3]

sw = 1

b1 = min(c1)
a0 = c1[0] - b1
a1 = c1[1] - b1
a2 = c1[2] - b1
a = [a0, a1, a2]

if (c2[0] - a0 != c2[1] - a1) or (c2[1] - a1 != c2[2] - a2):
    sw = 0
if (c3[0] - a0 != c3[1] - a1) or (c3[1] - a1 != c3[2] - a2):
    sw = 0

if sw == 1:
    print("Yes")
else:
    print("No")