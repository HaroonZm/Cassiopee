s=input()
N=len(s)
gcount=0
pcount=0

def janken(me,you):
    if (me=="g")and(you=="p"):
        return -1
    elif (me=="p")and(you=="g"):
        return 1
    else:
        return 0
score=0
for i in range(N):
    if gcount==pcount:
        score=score+janken("g",s[i])
        gcount=gcount+1
    else:
        score=score+janken("p",s[i])
        pcount=pcount+1
print(score)