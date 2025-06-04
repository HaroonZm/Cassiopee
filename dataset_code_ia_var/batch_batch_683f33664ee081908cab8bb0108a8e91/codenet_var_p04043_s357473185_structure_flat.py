l = list(map(int, input().split()))
c5 = 0
c7 = 0
for x in l:
    if x == 5:
        c5 += 1
    if x == 7:
        c7 += 1
if c5 == 2 and c7 == 1:
    print("YES")
else:
    print("NO")