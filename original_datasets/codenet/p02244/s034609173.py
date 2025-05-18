import itertools
queen=[-1]*8
N=int(input())
de=[]
for i in range(N):
    x,y =list(map(int,input().split()))
    de.append(x)
    queen[x]=y
def check(n):#nはクイーンの個数
    for y in range(n):
        if crshu(queen[y],y):return False
    return True
def crshu(x,y):
    for y1 in range(y):
        x1=queen[y1]
        if x1-y1==x-y or x1+y1==x+y:return True
    return False
def board():
    king=[]
    for i in range(8):
        king.append([i,queen[i]])
    for i in range(8):
        for j in range(8):
            if [i,j] in king:
                print("Q",end="")
            else:
                print(".",end="")
        print()
    exit()

def search(n,y):
    if n==y:
        if check(8):
            board()
    else:
        if y in de:
            search(n,y+1)
        else:
            for i in range(n):
                if i not in queen :
                    queen[y]=i
                    search(n,y+1)
                    for l in range(y+1,8):
                        if l not in de:
                            queen[l]=-1
search(8,0)