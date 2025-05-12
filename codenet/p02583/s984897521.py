n = int(input())
l = [int(x) for x in input().split()]

if(n<3):
    print(0)
    exit()
l.sort(reverse=True)
ln = len(l)
cnt = 0
for i in range(ln):
    for j in range(i+1,ln):
        for k in range(j+1,ln):
            a,b,c = l[i],l[j],l[k]
            if(a==b or b==c or a==c):
                continue
            if(a<(b+c)):
                cnt += 1

print(cnt)