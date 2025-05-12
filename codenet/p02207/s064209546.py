import sys
input = sys.stdin.readline

N=int(input())

E=[list(map(int,input().split())) for i in range(N)]

QU=int(input())

Q=[list(map(int,input().split())) for i in range(QU)]

TIMELIST=[]
for t,a in E:
    TIMELIST.append(t)

for l,r in Q:
    TIMELIST.append(l)
    TIMELIST.append(r)

compression_dict={a: ind for ind, a in enumerate(sorted(set(TIMELIST)))}

for i in range(N):
    E[i][0]=compression_dict[E[i][0]]

for i in range(QU):
    Q[i]=[compression_dict[Q[i][0]],compression_dict[Q[i][1]]]

    

def seg_function(x,y):# Segment treeで扱うfunction
    return x*y

seg_el=1<<(len(compression_dict).bit_length())# Segment treeの台の要素数
SEG=[1]*(2*seg_el)# 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化

for t,a in E:
    SEG[t+seg_el]=1-0.1*a

for i in range(seg_el-1,0,-1):# 親の部分もupdate
    SEG[i]=seg_function(SEG[i*2],SEG[i*2+1])

def update(n,x,seg_el):# A[n]をxへ更新（反映）
    i=n+seg_el
    SEG[i]=x
    i>>=1# 子ノードへ
    
    while i!=0:
        SEG[i]=seg_function(SEG[i*2],SEG[i*2+1])
        i>>=1
        
def getvalues(l,r):# 区間[l,r)に関するseg_functionを調べる
    L=l+seg_el
    R=r+seg_el
    ANS=1

    while L<R:
        if L & 1:
            ANS=ANS*SEG[L]
            L+=1

        if R & 1:
            R-=1
            ANS=ANS*SEG[R]
        L>>=1
        R>>=1

    return ANS

for l,r in Q:
    print(10**9*getvalues(l,r))