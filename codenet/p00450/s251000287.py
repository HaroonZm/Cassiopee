while (1):
    n=int(raw_input())
    if n==0:
        break
    else:
        top=-1
        fault=[0]
        S=0
        for i in range(n/2): #i=0,2,... is othello i=1,3,...is donothing
            s=int(raw_input()) #oddstone
            if top!=s: 
                fault.append(i)
                top=s
            s=int(raw_input()) #evenstone
            if top!=s:
                fault.pop()
                top=s
            if fault==[]:
                fault=[0]
        i=len(fault)-1
        while i>0:
            S=S+(fault[i]-fault[i-1])*2
            i=i-2
        if not top:
            S=2*(n/2)-S
        if n%2==1:
            s=int(raw_input())
            S=S+(1-s)
        print S