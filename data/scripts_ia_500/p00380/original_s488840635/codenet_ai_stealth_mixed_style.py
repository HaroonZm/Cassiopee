n=int(input())
a_lst=list(map(int,input().split()))
queries=[]
for _ in range(int(input())):
    x,y=map(int,input().split())
    queries.append((x,y))

comp=sorted(a_lst)
diff=0
for i in range(n):
    if a_lst[i]!=comp[i]:
        diff+=1

def swap_and_update(diff,a_lst,comp,x,y):
    # Indices are 0-based
    diff -= (a_lst[x]==comp[y]) + (a_lst[y]==comp[x]) - (a_lst[x]==comp[x]) - (a_lst[y]==comp[y])
    a_lst[x],a_lst[y]=a_lst[y],a_lst[x]
    return diff

if diff==0:
    print(0)
else:
    i=0
    while i<len(queries):
        x,y=queries[i]
        x-=1
        y-=1
        diff=swap_and_update(diff,a_lst,comp,x,y)
        if diff==0:
            print(i+1)
            break
        i+=1
    else:
        print(-1)