N = int(input())
dif = []
a = list(map(int,input().split()))
bef = a[0]
for i,j in enumerate(a):
    if i==0:
        bef = j
        sum = 1
    elif j==bef:
        sum += 1
    else:
        dif.append(sum)
        sum = 1
        bef = j
dif.append(sum)

res = 0
for i in dif:
    res += i//2
print(res)