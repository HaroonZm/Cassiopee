n,w = map(int,input().split(" "))
pack = []

for _ in range(n):
    x,y = map(int,input().split(" "))
    pack.append([x/y,x,y])

pack.sort()
pp = pack[::-1]

sum = 0
for ele in pp:
    if w-ele[2] > 0:
        sum += ele[1]
        w = w - ele[2]
    else:
        sum += ele[0]*w
        break

print(sum)