n = int(input())
cats = list(map(int, input().split()))

hole = []
p = "OK"

for i in range(n):
    if cats[i] < 0:
        if len(hole)==0 or cats[i] != -1*hole[-1]:
            p = str(i+1)
            break
        else:
            hole.pop()
    else:
        if cats[i] in hole:
            p = str(i+1)
            break
        else:
            hole.append(cats[i])

print(p)