import sys
input=sys.stdin.readline

while True:
    T,P,R=map(int,input().split())
    if T==0 and P==0 and R==0:
        break
    # Initialize data structures
    solved=[0]*(T+1)
    penalty=[0]*(T+1)
    wrong=[ [0]*(P+1) for _ in range(T+1)]
    solved_flag=[ [False]*(P+1) for _ in range(T+1)]

    for _ in range(R):
        t,p,time,msg=input().split()
        t=int(t)
        p=int(p)
        time=int(time)
        if msg=="CORRECT":
            if not solved_flag[t][p]:
                solved_flag[t][p]=True
                solved[t]+=1
                penalty[t]+= wrong[t][p]*1200+time
        else:
            if not solved_flag[t][p]:
                wrong[t][p]+=1

    teams = [( -solved[i], penalty[i], i) for i in range(1,T+1)]
    teams.sort()
    for sc,pn,i in teams:
        print(i, -sc, pn)