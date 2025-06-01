B,M,S=13,9,5
dx=[0,0,1,0,-1,1,1,-1,-1,0,2,0,-2]
dy=[0,-1,0,1,0,-1,1,1,-1,2,0,-2,0]
def isOnCloth(x,y):
    return 0<=x<10 and 0<=y<10
def soak(cloth,x,y,ink):
    for i in xrange(ink):
        cloth[y+dy[i]][x+dx[i]]-=1
def drop(cloth,x,y,ink):
    for i in xrange(ink):
        cloth[y+dy[i]][x+dx[i]]+=1
def canSoak(cloth,x,y,ink):
    return all([isOnCloth(x+dx[i],y+dy[i]) and cloth[y+dy[i]][x+dx[i]]>0 for i in xrange(ink)])
def DFS(cloth,ink_set,cur):
    if len(ink_set)==0:
        return []
    for i in xrange(cur,100):
        if not cloth[i/10][i%10]==0:
            break
        cur+=1
    for ink in set(ink_set):
        for i in xrange(ink):
            cx,cy=cur%10+dx[i],cur/10+dy[i]
            if isOnCloth(cx,cy) and cloth[cy][cx]>0:
                if canSoak(cloth,cx,cy,ink):
                    soak(cloth,cx,cy,ink)
                    ink_set.remove(ink)
                    result=DFS(cloth,ink_set,cur)
                    if not result==False:
                        result.append([cx,cy,ink])
                        return result
                    ink_set.append(ink)
                    drop(cloth,cx,cy,ink)
    return False
ink_set=[B,S]
clothA=[ [0,0,0,0,0,0,0,0,0,0],
         [0,0,1,0,0,0,0,0,0,0],
         [0,1,1,1,0,0,0,0,0,0],
         [1,1,1,1,1,0,0,0,0,0],
         [0,1,1,1,0,0,0,0,0,0],
         [0,0,1,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,1,0,0,0],
         [0,0,0,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,1,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],]
clothB=[ [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,1,0,0,0,0,0,0,0],
         [0,1,1,1,0,0,0,0,0,0],
         [0,0,1,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],]
import itertools
n=input()
cloth=[]
for u in xrange(10):
    cloth.append(map(int,raw_input().split(" ")))
su=sum([sum(cloth[i]) for i in xrange(10)])
ink_sets=[list(a) for a in itertools.combinations_with_replacement([0,13,9,5],n) if sum(a)==su]
for ink_set in ink_sets:
    result=DFS(cloth,ink_set,0)
    if not result==False:
        break
dic={B:3,M:2,S:1}
for r in result:
    print "{} {} {}".format(r[0],r[1],dic[r[2]])