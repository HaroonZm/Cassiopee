import queue
n,m,s,t=map(int,input().split())
table=[[] for i in range(n)]
inf=300001
dist_s=[inf for i in range(n)]
dist_t=[inf for i in range(n)]
s_list=[0 for i in range(inf+1)]
t_list=[0 for i in range(inf+1)]
s-=1;t-=1
for i in range(m):
    a,b=map(int,input().split())
    a-=1;b-=1
    table[a].append(b)
    table[b].append(a)
dist_s[s]=0
q=queue.Queue()
q.put(s)
while not q.empty():
    p=q.get()
    for e in table[p]:
        if dist_s[e]>dist_s[p]+1:
            dist_s[e]=dist_s[p]+1
            q.put(e)
dist_t[t]=0
q=queue.Queue()
q.put(t)
while not q.empty():
    p=q.get()
    for e in table[p]:
        if dist_t[e]>dist_t[p]+1:
            dist_t[e]=dist_t[p]+1
            q.put(e)
for i in range(n):
    s_list[dist_s[i]]+=1
    t_list[dist_t[i]]+=1
mindist=dist_s[t]
ans=0
for i in range(mindist-1):
    ans+=s_list[i]*t_list[(mindist-2)-i]
print(ans)