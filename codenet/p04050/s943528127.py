n,m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

breakFlag = False
for i in range(1,m-1):
    if a[i]%2==1:
        if a[0]%2==1:
            if a[len(a)-1]%2==1:
                print("Impossible")
                breakFlag = True
                break
            else:
                a[i],a[len(a)-1] = a[len(a)-1],a[i]
        else:
            a[i],a[0] = a[0],a[i]

if breakFlag==False:
    ans = ''.join([str(s)+" " for s in a])
    print(ans[:-1])
    if m==1:
        if a[0]>1:
            a[0]-=1
            a.append(1)
            print(m+1)
        else:
            print(m)
    else:
        if a[len(a)-1]==1:
            print(m-1)
            a.pop()
            a[0]+=1
        else:
            print(m)
            a[0]+=1
            a[len(a)-1] -= 1
    ans = ''.join([str(s)+" " for s in a])
    print(ans[:-1])