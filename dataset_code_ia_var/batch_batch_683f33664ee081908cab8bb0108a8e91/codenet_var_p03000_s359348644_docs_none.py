nx = input().split()
l = input().split()
nx = [int(x) for x in nx]
l = [int(n) for n in l]
buf = 0
count = 1
for i in range(nx[0]):
    buf = buf + l[i]
    if nx[1] >= buf:
        count += 1
print(count)