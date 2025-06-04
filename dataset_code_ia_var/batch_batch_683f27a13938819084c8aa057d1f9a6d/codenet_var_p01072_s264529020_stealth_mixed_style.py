hi = {}
for a in range(51):
    for b in range(51):
        hi[(a,b)] = 0

params = input().split()
W = int(params[0])
H = int(params[1])
T = int(params[2])

P = int(input())
k = 0
while k < P:
    k += 1
    temp = input().split()
    x, y, t = int(temp[0]), int(temp[1]), int(temp[2])
    if (x, y) in hi:
        hi[(x, y)] = hi.get((x, y), 0) + 1
    else:
        hi[(x, y)] = 1

answer = 0
yindex = 0
while yindex < H:
    values = [*map(int, input().split())]
    xidx = 0
    for value in values:
        if value != 0:
            try:
                answer += hi[(xidx, yindex)]
            except:
                pass
        xidx += 1
    yindex += 1

print(answer)