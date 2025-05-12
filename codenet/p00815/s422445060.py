#1236
q=int(input())
for _ in range(q):
    data=[]
    while 1:
        data+=list(map(int,input().split()))
        if data[-1]==0:
            break
    rooms=[(-1,1,[])]
    now=0
    i=0
    st=[]
    counter=[-1 for i in range(1000)]
    while data[i]!=0:
        while rooms[now][1]<=len(rooms[now][2]):
            now=st.pop()
        if data[i]>0:
            rooms.append((rooms[now][0]+1,data[i]+(1 if i==0 else 0),[]))
            counter[rooms[now][0]+1]=len(rooms)-1
            rooms[now][2].append(len(rooms)-1)
            rooms[len(rooms)-1][2].append(now)
            if len(rooms[now][2])<rooms[now][1]:
                st.append(now)
            now=len(rooms)-1
        elif data[i]<0:
            nxt=counter[rooms[now][0]+data[i]]
            rooms[nxt][2].append(now)
            rooms[now][2].append(nxt)
        i+=1
    for i in range(1,len(rooms)):
        print(i,end='')
        for e in sorted(rooms[i][2]):
            if e==0:
                continue
            print('',e,end='')
        print()