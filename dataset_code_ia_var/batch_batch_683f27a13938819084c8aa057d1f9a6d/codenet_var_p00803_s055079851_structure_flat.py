cube = []
tetrahedral = []
for i in range(0, 55):
    cube.append(i**3)
for i in range(0, 97):
    tetrahedral.append(i*(i+1)*(i+2)//6)
ans = []
while True:
    n = int(input())
    if n == 0:
        break
    min_val = 0
    diff_min = 10**6
    for x in cube:
        for y in tetrahedral:
            s = x + y
            d = n - s
            if d < diff_min and d >= 0:
                diff_min = d
                min_val = s
    ans.append(min_val)
for a in ans:
    print(a)