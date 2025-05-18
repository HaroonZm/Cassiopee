import copy ; import sys ;input = sys.stdin.readline; sys.setrecursionlimit(11451419);from collections  import deque 
n=int(input())
G=[[] for i in range(n)]
for i in range(n):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
seen=[0 for i in range(n)]

hist=deque([]) #頂点の訪問履歴
pos=-1  #サイクルの1成分 -1はサイクル未発見

def dfs(x,p):  #pはxの親
    global pos #global!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    seen[x]=1
    hist.append(x)  #訪れたらhistにappend
    for to in G[x]:
        if to==p:continue  #親なら無視
        if seen[to]==1:
            pos=to
            return    #サイクルを発見したら、即すべてのdfsを終える
        #残りはseen[x]=0のみ
        dfs(to,x)
        if pos != -1:return  #帰りがけ、サイクルが検出済みなら何もしない
    hist.pop()  #stackの末尾を消す
    #ループなく平和に終わったらpopできる
    return  #まあなくてもいいけどreturnは終了であることを強調

dfs(0,-1)

#この状態だと、サイクルに入る前に通った枝葉がhistに入ってる。
#枝葉が終わったら、posからループの順番に頂点番号が入ってる。
cycle=set([])
while hist:
    qwe=hist.pop()
    cycle.add(qwe)
    if qwe==pos:break
    #そっかこっちの方が速いよね～～～～～indexだとちょっとアレだよね～～～～～～～～～～～～～～～～～～～～～～はい
    
m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    if a-1 in cycle  and  b-1 in cycle:
        print(2)
    else:
        print(1)