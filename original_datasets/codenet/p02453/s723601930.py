n=int(input())
a=list(map(int,input().split( )))
q=int(input())
k=[]
for i in range(q):
    k1=int(input())
    k.append([k1,i])

a.sort()
k.sort()

ans = [n]*q
i = 0 #k
j = 0 #a

while i<q and j<n:
    try:#j=nの処理
        while k[i][0] > a[j]:
            j += 1
    except:
        pass

    ans[k[i][1]] = j
    i+=1

for i in range(q):
    print(ans[i])