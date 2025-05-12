n=int(input())
adj=[]
for i in range(n):
      adj.append(list(map(int, input().split())))

edge=[[0 for i2 in range(n)]for i1 in range(n)]

#??£??\???????????????

for i in range(n):
    for j in range(adj[i][1]):
        edge[i][adj[i][j+2]-1]=1

time=1
discover=[0 for i in range(n)]
final=[0 for i in range(n)]
stack=[]

def dfs(id,time):
    for i in range(n):
        c=0
        if edge[id][i]==1 and discover[i]==0:
            stack.append(id)
            discover[i]=time
            c+=1
            #print(discover,final,i,stack)
            dfs(i,time+1)
        else:
            pass
    if c==0:
        if len(stack)>0:
            if final[id]==0:
                final[id] = time
                #print("back",discover,final,id,stack)
                dfs(stack.pop(), time + 1)
            else:
                #print("back", discover, final, id, stack)
                dfs(stack.pop(),time)

discover[0]=time
stack.append(0)
dfs(0,time+1)

for i in range(n):
    if discover[i]==0:
        discover[i]=final[0]+1
        stack.append(i)
        dfs(i,final[0]+2)
        break

for i in range(n):
    print(i+1,discover[i],final[i])