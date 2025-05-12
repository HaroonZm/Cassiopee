# Your code here!

n,m = map(int,input().split())

#こっからunion-find

#各ノードの親を格納するリスト
par = [i for i in range(n+1)]
#各木の根に対するrankを格納するリスト
rank = [0 for i in range(n+1)]

#xの根を発見する
#発見するだけでなくxと通過したノードを根の直下に配置する
def find(x):
    #自分の親が自分なら根
    if x==par[x]:
        return x
    else:
        #違う場合は親の根を自分の親にする
        par[x]=find(par[x])
        return par[x]

#xとyが含まれる木を合併する
def unite(x,y):
    #xの根,yの根をrx,ryとする
    rx=find(x)
    ry=find(y)
    
    #根が同じならもともと同じ木なのでok
    if rx==ry:
        return
    
    #根が異なる場合はrankが大きい木に小さい木をくっつける（rankを増やさないため）
    if rank[rx]<rank[ry]:
        par[rx]=ry
    else:
        par[ry]=rx
    #rankが等しい気を合併した時のみrankが増える
    if rank[rx]==rank[ry]:
        rank[rx]+=1

#x,yが同じ木に含まれるかの判定
def some(x,y):
    return find(x)==find(y)

#union-find終わり

#入力x,yを同じグループに
for i in range(m):
    x,y,z=map(int,input().split())
    unite(x,y)

#すべてのノードを根の直下に配置
for i in range(1,n+1):
    find(i)

#木の数を数える(根の種類を数える)
ans=len(set(par))-1

print(ans)