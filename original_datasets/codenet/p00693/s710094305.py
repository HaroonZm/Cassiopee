def ipmatch(ip,iprule):
    ret=1
    for i in range(8):
        if iprule[i]!='?':
            ret*=ip[i]==iprule[i]
    return ret

def rulematch(sip,dip,rule):
    rulesip=rule[1]
    ruledip=rule[2]
    return ipmatch(sip,rulesip) and ipmatch(dip,ruledip)

while(1):
    [n,m]=[int(x) for x in raw_input().split()]
    if n==0 and m==0:
        break
    else:
        anssum=0
        ansmes=[]
        rules=[]
        for i in range(n):
            rulei=raw_input().split()
            rules.append(rulei)
        for i in range(m):
            message=raw_input().split()
            sip=message[0]
            dip=message[1]
            for j in range(-1,-n-1,-1):
                if rules[j][0]=='deny':
                    if rulematch(sip,dip,rules[j]):
                        break
                else:
                    if rulematch(sip,dip,rules[j]):
                        anssum+=1
                        ansmes+=[[sip,dip,message[2]]]
                        break
        print anssum
        for mm in ansmes:
            print mm[0],mm[1],mm[2]