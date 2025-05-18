V,E = list(map(int,input().split()))

#訪問済の頂点を保持
visit=[]
no_visit=list(range(V))

#各頂点の入次数
enter=[0]*V

#隣接リスト
ad_list=[[] for _ in range(V)]

for e in range(E):
    start,end=list(map(int,input().split()))
    ad_list[start].append(end)
    enter[end]+=1
    
enter , ad_list

while True:
    if len(visit)==V:
        break
        
    for n_v_idx,n_v in enumerate(no_visit):
        e=enter[n_v]
        if e == 0:
            v=no_visit.pop(n_v_idx)
            visit.append(v)
            for a in ad_list[n_v]:
                enter[a]=enter[a]-1
for v in visit:
    print(v)